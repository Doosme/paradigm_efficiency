class FileResults:
    """represents the results of one file"""
    def __init__(self, name, COMBINED):
        """
        :param name: should be only the name of the file not with file-ending
        """
        self.total_losses_per_epoch = list()
        self.loss_dict = {feat:list() for feat in COMBINED+["total"]}
        self.averaged_loss_dict = {feat:list() for feat in COMBINED+["total"]}
        self.freq_dict = {feat:1 for feat in COMBINED}
        self.name = name
        self.num_of_epochs = 0

    def read_in_from_file(self, loss_file, freq_file, step_size=1):
        self._read_losses_from_file(loss_file)
        self._read_freqs_from_file(freq_file)
        self._calculate_averaged_losses(step_size)

    def create_from_object(self, loss_list, loss_dict, freq_dict, step_size=1):
        self.num_of_epochs = len(loss_list)
        self.total_losses_per_epoch = loss_list
        self.loss_dict = loss_dict
        self.freq_dict = freq_dict

        self._calculate_averaged_losses(step_size)

    def _read_losses_from_file(self, loss_file):
        with open(loss_file) as f:
            data = f.read()
            data = data.strip()
            data = data.split("\n")
            for line in data:
                line_lst = line.split("\t")
                loss_list_str = line_lst[1:]
                loss_list = [float(loss) for loss in loss_list_str]
                self.loss_dict[line_lst[0]] = loss_list
        self.num_of_epochs = len(self.loss_dict["total"])
        self.total_losses_per_epoch = self.loss_dict["total"]

    def _read_freqs_from_file(self, freq_file):
        self.freq_dict = dict()
        with open(freq_file) as f:
            data = f.read().strip().split("\n")
            for line in data:
                line_str = line.split("\t")
                feat = line_str[0]
                loss = float(line_str[1])
                self.freq_dict[feat] = loss

    def _calculate_averaged_losses(self, step_size):
        for feat, loss in self.loss_dict.items():
            loss_lst = []
            for i in range(0, self.num_of_epochs,step_size):
                summed_step_loss = 0
                for j in range(step_size):
                    summed_step_loss += loss[i+j]

                averaged_step_loss = (summed_step_loss)/step_size
                loss_lst.append(averaged_step_loss)

            self.averaged_loss_dict[feat] = loss_lst

    def write_to_file(self, write_dir):
        res_table = ""
        for feat, loss_list in self.loss_dict.items():
            res_table += feat + "\t" + "\t".join(map(str, loss_list)) + "\n"
        res_table.strip()

        with open(write_dir+self.name+"_losses"+".tsv", "w") as g:
            g.write(res_table)

class PermResults:
    def __init__(self):
        #list containing all the FileResults items for all the permutations and the baseline
        self.file_results_list = list()

    def read_from_file(self, loss_dir, freq_file, file_ending, file_name_list, COMBINED, step_size=1):
        for filename in file_name_list:
            print("processing:" + str(filename))
            loss_file = loss_dir + filename + file_ending
            file_res = FileResults(name=filename, COMBINED=COMBINED)
            file_res.read_in_from_file(loss_file=loss_file, freq_file=freq_file, step_size=step_size)
            self.file_results_list.append(file_res)

    def write_to_file(self, write_dir):
        for item in self.file_results_list:
            item.write_to_file(write_dir)

    def add_file(self, filename, loss_list, loss_dict, freq_dict, COMBINED):
        name = ".".join(filename.split("/")[-1].split(".")[:-1])
        item = FileResults(name, COMBINED=COMBINED)
        item.create_from_object(loss_list=loss_list, loss_dict=loss_dict, freq_dict=freq_dict)

        self.file_results_list.append(item)

        print(filename)
        print(name)


