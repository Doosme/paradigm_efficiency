from PermSynCreator import PermSynCreator


class PermSynCreatorPR_ROM(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            #dual_exists = list()
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][line[0]] = line[count]

        #add reflexiv:
        res_dict = dict()
        for tense in self.TENSES_CASES:
            feat_list = [x+y for y in self.NUMBERS for x in self.PERSONS]

            #print(feat_list)

            print(feat_list)
            for feat in feat_list:
                keys_list = cont_dict[tense].keys()
                if feat in keys_list:  # e.g. 1s
                    for g in self.GENDERS:
                        res_dict[feat + " "+g+" " + tense] = cont_dict[tense][feat]

                else:
                    if feat + " m" in keys_list:
                        res_dict[feat + " m " + tense] = cont_dict[tense][feat + " m"]
                    if feat + " f" in keys_list:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " f"]
                    if feat + " n" in keys_list:
                        res_dict[feat + " n " + tense] = cont_dict[tense][feat + " n"]

                    if feat + " f" not in keys_list:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " m"]
                    if "n" in self.GENDERS:
                        if feat + " n" not in keys_list:
                            res_dict[feat + " n " + tense] = cont_dict[tense][feat + " m"]

        return res_dict

class PermSynCreatorPR_ROM_F(PermSynCreatorPR_ROM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_F"

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3", "r"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "DISJ","CON"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



class PermSynCreatorPR_ROM_D(PermSynCreatorPR_ROM):
    #Dalamatian, Romantsch
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_D"

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3", "r"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


class PermSynCreatorPR_ROM_R(PermSynCreatorPR_ROM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_R"

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN", "AKKl", "DATl"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



class PermSynCreatorPR_ROM_L(PermSynCreatorPR_ROM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_L"

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3", "r"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN", "DISJ", "CON"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


class PermSynCreatorPR_ROM_S(PermSynCreatorPR_ROM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_S"

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v", "3", "r", "2h"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN", "DISJ", "CON"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40




    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            # dual_exists = list()
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][line[0]] = line[count]

        print("A")
        print(cont_dict["NOM"].keys())

        help_iter = list(iter(cont_dict["NOM"].keys()))
        for elem in help_iter:
            gender_contained = False
            for g in self.GENDERS:
                if g in elem: gender_contained = True
            if gender_contained == False:
                for tense in self.TENSES_CASES:
                    for g in self.GENDERS:
                        cont_dict[tense][elem + " " + g] = cont_dict[tense][elem]
                    del cont_dict[tense][elem]


        print(cont_dict["NOM"].keys())


        # add reflexiv:
        for g in self.GENDERS:
            if "2hs "+g in cont_dict["NOM"].keys():
                if "2hp "+g not in cont_dict["NOM"].keys():
                    for tense in self.TENSES_CASES:
                        cont_dict[tense]["2hp "+g] = cont_dict[tense]["2hs "+g]
            else:
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["2hs "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2hp "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2vs "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2vp "+g] = cont_dict[tense]["2s "+g]
                    del cont_dict[tense]["2s "+g]

        print(cont_dict["NOM"].keys())

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict