import sys

import torch
import torch.nn as nn
import torch.optim as optim

from torchtext.data import Field, TabularDataset, BucketIterator

import numpy as np

import random
import math
import time
from collections import Counter
import os

from seq2seq_model import DecoderRNN, EncoderRNN, Seq2Seq
from PermFileResults import PermResults
from create_frequencies import read_weights_from_file
from util_directories import LOSSES_DIR, PERM_DIR, FREQ_FILES
from util_featurecombinations import COMBINED

SEED = 1234
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.backends.cudnn.deterministic = True



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
BATCH_SIZE = 1
CLIP = 1





class ModelRunner:
    @staticmethod
    def epoch_time(start_time, end_time):
        elapsed_time = end_time - start_time
        elapsed_mins = int(elapsed_time / 60)
        elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
        return elapsed_mins, elapsed_secs

    @staticmethod
    def tokenize_input(text):
        # 3p f
        # 1d
        text = text.replace(" ", "")
        features = list(text)
        return features[::-1]

    @staticmethod
    def tokenize_output_soundbased(text):
        # ta-…-ii
        # na-…
        text = text.replace("-", "")
        tokens = list(text)
        return tokens

    def __init__(self, number_of_epochs, weights_dict):
        self.number_of_epochs = number_of_epochs
        self.weights_dict = weights_dict
        print("Weights-Dict (init):"+str(self.weights_dict))

        # Field for the input (person, number, gender)
        self.SRC = Field(tokenize=self.tokenize_input,
                         init_token='<sos>',
                         eos_token='<eos>',
                         lower=True)

        # Field for input
        self.TRG = Field(tokenize=self.tokenize_output_soundbased,
                         init_token='<sos>',
                         eos_token='<eos>',
                         lower=True)


    def create_model(self, training_filename, training_directory):
        print(training_filename)
        self.name = ".".join(training_filename.split(".")[:-1])

        # read in tsv file
        self.enumerated_features_dict = dict()
        self.features_counter = Counter()
        with open(training_directory+training_filename) as f:
            data = f.read().strip().split("\n")
            i = 0
            for line in data:
                feat_str = line.split("\t")[0]
                self.enumerated_features_dict[i] = feat_str
                self.features_counter.update([feat_str])
                i += 1

        train_data, valid_data, test_data = TabularDataset.splits(
            path=training_directory,
            train=training_filename,
            validation=training_filename,
            test=training_filename,
            format='tsv',
            fields=[('text', self.SRC), ('labels', self.TRG)])

        self.SRC.build_vocab(train_data)
        self.TRG.build_vocab(train_data)

        pad_token_index = self.TRG.vocab.stoi[self.TRG.pad_token]
        self.criterion = nn.CrossEntropyLoss(ignore_index=pad_token_index)


        self.train_iterator, valid_iterator, test_iterator = BucketIterator.splits(
            (train_data, valid_data, test_data),
            batch_size=BATCH_SIZE,
            device=device)

        ####TRAINING MODEL
        INPUT_DIM = len(self.SRC.vocab)
        OUTPUT_DIM = len(self.TRG.vocab)
        ENC_EMB_DIM = 256
        DEC_EMB_DIM = 256
        HID_DIM = 512
        N_LAYERS = 2
        ENC_DROPOUT = 0.5
        DEC_DROPOUT = 0.5

        # create model
        enc = EncoderRNN(INPUT_DIM, ENC_EMB_DIM, HID_DIM, N_LAYERS, ENC_DROPOUT)
        dec = DecoderRNN(OUTPUT_DIM, DEC_EMB_DIM, HID_DIM, N_LAYERS, DEC_DROPOUT)
        self.model = Seq2Seq(enc, dec, device).to(device)


        #self.model.apply(init_weights)
        self._init_weights()

        print(f'The model has {self.count_parameters():,} trainable parameters')

        self.optimizer = optim.Adam(self.model.parameters())  # stochastic optimization

        print(self.weights_dict)

    def _init_weights(self):
        #initializes weights (uniform distribution between -0.08 and +0.08)
        for name, param in self.model.named_parameters():
            nn.init.uniform_(param.data, -0.08, 0.08)

    def count_parameters(self):
        # calculate the number of trainable parameters
        return sum(p.numel() for p in self.model.parameters() if p.requires_grad)

    def run_epoch(self):
        """
        runs one epoch
        :return:
        :rtype tuple (float, dict)
               (average_epoch_loss, averaged_epoch_loss_dict)
               average_epoch_loss: average of losses of all items
               averaged_epoch_loss_dict: average of losses for all items of specific feature
        """
        #set module to training mode
        self.model.train()

        epoch_loss = 0

        #saves losses per epoch and per feature
        epoch_loss_dict = {feat:0 for feat in COMBINED_TENSES+["total"]}

        for i, batch in enumerate(self.train_iterator):
            #get source and target text
            src = batch.text #note: has to be the same name as the Fields
            trg = batch.labels #note: has to be the same name as the Fields

            #Gradient auf null zurücksetzen
            self.optimizer.zero_grad()

            #feed current example into the model
            output = self.model(src, trg)

            #note: this seems to be something technical
            output_dim = output.shape[-1]

            output = output[1:].view(-1, output_dim)
            trg = trg[1:].view(-1)

            loss = self.criterion(output, trg)

            #calculate gradients
            loss.backward()

            #clip gradient to prevent from exploding
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), CLIP)

            #update parameters with the optimizer
            self.optimizer.step()

            #add calculated loss of the example to overall loss
            item_loss = loss.item() * self.weights_dict[self.enumerated_features_dict[i]]
            epoch_loss += item_loss

            #add to dict
            epoch_loss_dict[self.enumerated_features_dict[i]] += item_loss
            epoch_loss_dict["total"] += item_loss

        #average losses
        average_epoch_loss = epoch_loss / len(self.train_iterator)
        #add to dict
        averaged_epoch_loss_dict = dict()
        for feat, loss in epoch_loss_dict.items():
            if feat == "total":
                averaged_epoch_loss_dict[feat] = loss / len(self.train_iterator)
            else:
                averaged_epoch_loss_dict[feat] = loss / self.features_counter[feat]

        return average_epoch_loss, averaged_epoch_loss_dict


    def run_training(self):
        # list containing the losses for each training epoch
        loss_list = []
        # dictionary containing the losses (by feature set) for each training epoch
        loss_dict = {feat:list() for feat in COMBINED_TENSES+["total"]}

        for epoch in range(self.number_of_epochs):

            start_time = time.time()

            train_loss, train_loss_dict = self.run_epoch()

            #add losses to loss_list and loss_dict
            loss_list.append(train_loss)
            for feat, value in train_loss_dict.items():
                loss_dict[feat].append(value)

            end_time = time.time()
            epoch_mins, epoch_secs = self.epoch_time(start_time, end_time)

            print(f'Epoch: {epoch + 1:02} | Time: {epoch_mins}m {epoch_secs}s')
            print(f'\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}')
        return loss_list, loss_dict


def run_model(num_epochs):
    # run training
    res = PermResults()
    for filename in os.listdir(PERM_DIR):
        if filename.endswith(".tsv"):
            print("Reading in file: " + str(filename) + " (" + str(PERM_DIR) + ")")

            weights_dict = read_weights_from_file(FREQ_FILE)
            print("Weights-Dict:"+ str(weights_dict))

            model_runner = ModelRunner(number_of_epochs=num_epochs, weights_dict=weights_dict)
            model_runner.create_model(training_filename=filename, training_directory=PERM_DIR)

            loss_list, loss_dict = model_runner.run_training()

            res.add_file(filename, loss_list, loss_dict, weights_dict, COMBINED_TENSES)

    res.write_to_file(LOSSES_DIR)


if __name__ == "__main__":
    #NOTE: command line arguments:
    #      PERM_DIR: directory where the permutation files are
    #      N_EPOCHS: number of epochs
    #      LANG_TYPE: type of language (VERB_SEM, VERB_GER, PR_SLAV etc.)

    PERM_DIR = sys.argv[1]
    N_EPOCHS = int(sys.argv[2])
    LANG_TYPE = sys.argv[3]

    FREQ_FILE = FREQ_FILES[LANG_TYPE]
    COMBINED_TENSES = COMBINED[LANG_TYPE]

    run_model(num_epochs=N_EPOCHS)