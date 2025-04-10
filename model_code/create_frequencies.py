from util_directories import PROJ_FOLDER, FREQ_DIR

from util_featurecombinations import COMBINED

class WeightsCreator:

    def __init__(self, default_freq=True):
        self.count_dict = dict()

        self.count_gender_dict = {"m": 0, "f": 0}
        self.count_aspect_dict = {"V": 0, "G": 0}
        self.count_number_dict = {"s": 0, "d": 0, "p": 0}
        self.count_person_dict = {"1": 0, "2": 0, "3": 0}
        self.count_gender_by_number = {"s": {"m": 0, "f": 0}, "d": {"m": 0, "f": 0}, "p": {"m": 0, "f": 0}}

        self.perc_gender_dict = dict()
        self.perc_aspect_dict = dict()
        self.perc_number_dict = dict()
        self.perc_person_dict = dict()
        self.perc_gender_by_number = {"s": dict(), "d": dict(), "p": dict()}

        self.weights_dict = dict()

        if default_freq:
            self.weights_dict = {item: 1 for item in COMBINED["VERB_SEM"]}

    def _create_key(self, feature_dict):
        asp = "G" if feature_dict["Aspect"] == "Imp" else "V"
        gen = feature_dict["Gender"][0].lower()
        num = feature_dict["Number"][0].lower()
        pers = feature_dict["Person"]

        count_features = pers + num + " " + gen + " " + asp

        return count_features, (pers, num, gen, asp)

    def _add_to_count_dicts(self, feature_dict):
        # add to full dict
        item, (pers, num, gen, asp) = self._create_key(feature_dict)
        if item in self.count_dict:
            # count up for old items
            self.count_dict[item] += 1
        else:
            # add new item
            self.count_dict[item] = 1

        # add to seperate dicts:
        self.count_person_dict[pers] += 1
        self.count_number_dict[num] += 1
        self.count_gender_dict[gen] += 1
        self.count_aspect_dict[asp] += 1
        self.count_gender_by_number[num][gen] += 1


    def read_in_file(self, *files):
        for filename in files:
            with open(filename) as f:
                text = f.read()
                sentence_list = text.split("\n\n")
                for sentence in sentence_list:
                    word_list = sentence.split("\n")
                    for word in word_list:
                        # skip comments
                        if word.startswith("#"):
                            continue

                        word_list = word.split("\t")
                        if word_list[3] == "VERB":
                            # only get conjugated verbs
                            if word_list[4].startswith("IV") or word_list[4].startswith("PV"):  # or word_list[4].startswith("CV")
                                word_features = word_list[5]
                                word_feature_list = word_features.split("|")
                                feature_dict = dict()
                                for feature in word_feature_list:
                                    feat = feature.split("=")
                                    feature_dict[feat[0]] = feat[1]
                                # add some missing (but implied features)
                                # if unclear skip the word
                                if "Aspect" not in feature_dict:
                                    if "Mood" in feature_dict:
                                        if feature_dict["Mood"] == "Jus" or feature_dict["Mood"] == "Sub":
                                            feature_dict["Aspect"] = "Imp"
                                        else:
                                            continue
                                    else:
                                        continue

                                self._add_to_count_dicts(feature_dict)

    def calculate_percentage_dicts(self):

        num_of_items = 0
        for value in self.count_dict.values():
            num_of_items += value

        for key, val in self.count_number_dict.items():
            percentage = round((val / num_of_items) * 100, ndigits=2)
            self.perc_number_dict[key] = percentage
            print(str(key) + ":" + str(val) + " --> " + str(percentage) + "%")

        for key, val in self.count_aspect_dict.items():
            percentage = round((val / num_of_items) * 100, ndigits=2)
            self.perc_aspect_dict[key] = percentage
            print(str(key) + ":" + str(val) + " --> " + str(percentage) + "%")

        for key, val in self.count_gender_dict.items():
            percentage = round((val / num_of_items) * 100, ndigits=2)
            self.perc_gender_dict[key] = percentage
            print(str(key) + ":" + str(val) + " --> " + str(percentage) + "%")

        for key, val in self.count_person_dict.items():
            percentage = round((val / num_of_items) * 100, ndigits=2)
            self.perc_person_dict[key] = percentage
            print(str(key) + ":" + str(val) + " --> " + str(percentage) + "%")

        for num, d in self.count_gender_by_number.items():
            # get total number of occurences of current number
            num_of_items_for_curr_num = self.count_number_dict[num]

            for gen, val in d.items():
                percentage = round((val / num_of_items_for_curr_num) * 100, ndigits=2)
                self.perc_gender_by_number[num][gen] = percentage
                print(str(num) + " " + str(gen) + ":" + str(val) + " --> " + str(percentage) + "%")

    def calculate_weights(self):
        #Note: the numbers are not percentages

        # old values (Noga&Mora: Figure 3)
        s1 = 23.71
        s2 = 15.96
        s3 = 37.86

        p1 = 05.22
        p2 = 07.84
        p3 = 07.58

        # calculate new values

        # d1 m = (p1[zaslavsky] * perc_of_dual / (perc_of_dual + perc_of_plural))  *  perc_of_masc

        _d1 = p1 * (self.perc_number_dict["d"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))
        _p1 = p1 * (self.perc_number_dict["p"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))
        _d2 = p2 * (self.perc_number_dict["d"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))
        _p2 = p2 * (self.perc_number_dict["p"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))
        _d3 = p3 * (self.perc_number_dict["d"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))
        _p3 = p3 * (self.perc_number_dict["p"] / (self.perc_number_dict["d"] + self.perc_number_dict["p"]))

        for T in ["V", "G"]:
            for G in ["m", "f"]:
                self.weights_dict["1s " + G + " " + T] = round(s1 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["2s " + G + " " + T] = round(s2 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["3s " + G + " " + T] = round(s3 * (self.perc_gender_dict[G] / 100), ndigits=2)

                self.weights_dict["1d " + G + " " + T] = round(_d1 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["2d " + G + " " + T] = round(_d2 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["3d " + G + " " + T] = round(_d3 * (self.perc_gender_dict[G] / 100), ndigits=2)

                self.weights_dict["1p " + G + " " + T] = round(_p1 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["2p " + G + " " + T] = round(_p2 * (self.perc_gender_dict[G] / 100), ndigits=2)
                self.weights_dict["3p " + G + " " + T] = round(_p3 * (self.perc_gender_dict[G] / 100), ndigits=2)

        full_perc = 0
        for key, val in self.weights_dict.items():
            print(str(key) + ": " + str(val))
            full_perc += val
        print(full_perc)

        return self.weights_dict

    def write_weights_to_file(self, writefile):
        res_str = ""
        for feat, value in self.weights_dict.items():
            res_str += feat + "\t" + str(value) + "\n"
        res_str.strip()

        with open(writefile, "w") as g:
            g.write(res_str)


def read_weights_from_file(freq_file):
    """
    reads in the weights from a file and creates a dictionary of weights
    :param freq_file: file containing the weights
    :return: dict: feature -> weights
    """
    weights_dict = dict()
    with open(freq_file) as f:
        data = f.read()
        data = data.strip()
        data = data.split("\n")
        for item in data:
            item = item.split("\t")
            feat = item[0]
            weight = float(item[1])
            weights_dict[feat] = weight
    print(weights_dict)
    return weights_dict



def run_frequency_calculation():
    """
    calculates the frequencies,
    and creates the weights files for weighted and default weights
    :return: (weighted_weights:dict, default_weights:dict)
    """
    #NOTE: download files from https://github.com/UniversalDependencies/UD_Arabic-NYUAD/blob/master
    file1 = PROJ_FOLDER+"_data_util/ar_nyuad-ud-dev.conllu"
    file2 = PROJ_FOLDER+"_data_util/ar_nyuad-ud-test.conllu"
    file3 = PROJ_FOLDER+"_data_util/ar_nyuad-ud-train.conllu"

    freq_counter = WeightsCreator()
    freq_counter.read_in_file(file1, file2, file3)

    for key, value in reversed(sorted(freq_counter.count_dict.items(), key=lambda item: item[1])):
        print(str(key) + ": " + str(value))

    freq_counter.calculate_percentage_dicts()
    freq_counter.calculate_weights()

    freq_counter.write_weights_to_file(FREQ_DIR+"calculated_weights.tsv")


    return freq_counter.weights_dict


if __name__ == "__main__":
    #run this to create the frequency/weights files
    run_frequency_calculation()

    w1 = read_weights_from_file(FREQ_DIR+"calculated_weights.tsv")
