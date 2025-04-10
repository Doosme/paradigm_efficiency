from PermSynCreator import PermSynCreator


class PermSynCreatorPR_INDIRA_PROX(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]\
                       +["h","j"]\
                       +["x","w"]

        self.TENSES_CASES = []

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                feat = line[0].strip()
                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][feat] = line[count]

        help_iter = list(iter(cont_dict["NOM"].keys()))
        for feat in help_iter:
            gender_contained = False
            for g in self.GENDERS:
                if g in feat:
                    gender_contained = True
            if gender_contained == False:
                for tense in self.TENSES_CASES:
                    for g in self.GENDERS:
                        cont_dict[tense][feat + " " + g] = cont_dict[tense][feat]
                    del cont_dict[tense][feat]

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict



class PermSynCreatorPR_INDIRA_PROX_U(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v","2h","2j", "3e","3x","3w"]

        self.TENSES_CASES = ["NOM","INDIR","ERG","GEN","DAT"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                feat = line[0].strip()
                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][feat] = line[count]

        help_iter = list(iter(cont_dict["NOM"].keys()))
        for feat in help_iter:
            gender_contained = False
            for g in self.GENDERS:
                if g in feat:
                    gender_contained = True
            if gender_contained == False:
                for tense in self.TENSES_CASES:
                    for g in self.GENDERS:
                        cont_dict[tense][feat + " " + g] = cont_dict[tense][feat]
                    del cont_dict[tense][feat]


        for g in self.GENDERS:
            for n in self.NUMBERS:
                for tense in self.TENSES_CASES:
                    if "2"+n+" "+g in cont_dict[tense].keys():
                        cont_dict[tense]["2v"+n+" "+g] = cont_dict[tense]["2"+n+" "+g]
                        cont_dict[tense]["2h"+n+" "+g] = cont_dict[tense]["2"+n+" "+g]
                        cont_dict[tense]["2j"+n+" "+g] = cont_dict[tense]["2"+n+" "+g]
                        del cont_dict[tense]["2"+n+" "+g]

                    if "3"+n+" "+g in cont_dict[tense].keys():
                        cont_dict[tense]["3e"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        cont_dict[tense]["3x"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        cont_dict[tense]["3w"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        del cont_dict[tense]["3"+n+" "+g]

                    if "2h"+n+" "+g not in cont_dict[tense].keys():#polite form 1
                        cont_dict[tense]["2h"+n+" "+g] = cont_dict[tense]["2v"+n+" "+g]
                    if "2j"+n+" "+g not in cont_dict[tense].keys():#polite form 2
                        cont_dict[tense]["2j"+n+" "+g] = cont_dict[tense]["2hf"+n+" "+g]
                    if "3x"+n+" "+g not in cont_dict[tense].keys():#remote form 1
                        cont_dict[tense]["3x"+n+" "+g] = cont_dict[tense]["3e"+n+" "+g]
                    if "3w"+n+" "+g not in cont_dict[tense].keys():#remote form 2
                        cont_dict[tense]["3w"+n+" "+g] = cont_dict[tense]["3x"+n+" "+g]


        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict


class PermSynCreatorPR_INDIRA_PROX_P(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m", "f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v","2h", "3e","3x","3w"]

        self.TENSES_CASES = ["NOM","OBJ"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            #dual_exists = list()
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                feat = line[0].strip()
                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][feat] = line[count]

        #add gender!
        help_iter = list(iter(cont_dict["NOM"].keys()))
        for feat in help_iter:
            gender_contained = False
            for g in self.GENDERS:
                if g in feat:
                    gender_contained = True
            if gender_contained == False:
                for tense in self.TENSES_CASES:
                    for g in self.GENDERS:
                        cont_dict[tense][feat + " " + g] = cont_dict[tense][feat]
                    del cont_dict[tense][feat]


        for g in self.GENDERS:
            for n in self.NUMBERS:
                for tense in self.TENSES_CASES:
                    if "2"+n+" "+g in cont_dict[tense].keys():
                        cont_dict[tense]["2v"+n+" "+g] = cont_dict[tense]["2"+n+" "+g]
                        cont_dict[tense]["2h"+n+" "+g] = cont_dict[tense]["2"+n+" "+g]
                        del cont_dict[tense]["2"+n+" "+g]

                    if "3"+n+" "+g in cont_dict[tense].keys():
                        cont_dict[tense]["3e"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        cont_dict[tense]["3x"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        cont_dict[tense]["3w"+n+" "+g] = cont_dict[tense]["3"+n+" "+g]
                        del cont_dict[tense]["3"+n+" "+g]

                    if "2h"+n+" "+g not in cont_dict[tense].keys():#polite form 1
                        cont_dict[tense]["2h"+n+" "+g] = cont_dict[tense]["2v"+n+" "+g]
                    if "3x"+n+" "+g not in cont_dict[tense].keys():#remote form 1
                        cont_dict[tense]["3x"+n+" "+g] = cont_dict[tense]["3e"+n+" "+g]
                    if "3w"+n+" "+g not in cont_dict[tense].keys():#remote form 2
                        cont_dict[tense]["3w"+n+" "+g] = cont_dict[tense]["3x"+n+" "+g]


        print(cont_dict["NOM"].keys())

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict



class PermSynCreatorPR_INDIRA_PROX_A(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1","2v","2h","2j","3ev","3ej","3eh","3xv","3xj","3xh"]
        #
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40





class PermSynCreatorPR_INDIRA_PROX_B(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)



        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v", "2h","2j","3ev","3ej","3xv","3xj","3wv","3wj"]

        self.TENSES_CASES = ["NOM","OBJ","GEN"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



class PermSynCreatorPR_INDIRA_PROX_G(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)



        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2"]\
                       +["3ev","3eh", "3xv","3xh","rv","rh"]#"12"
        #
        self.TENSES_CASES = ["NOM","ERG","DAT","GEN"]


        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]\
                        + ["12p " + g + " " + t for t in self.TENSES_CASES for g in self.GENDERS]

        self.shuffle_length = 40





class PermSynCreatorPR_INDIRA_PROX_I(PermSynCreatorPR_INDIRA_PROX):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m","f"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2"]\
                       +["3e","3x","3w"]

        self.TENSES_CASES = ["NOM","OBL","GEN"]



        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40
