from PermSynCreator import PermSynCreator

class PermSynCreatorPR_KAUK(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["c"]


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
                    cont_dict[tense][line[0] + " c"] = line[count]

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict


class PermSynCreatorPR_KAUK_A(PermSynCreatorPR_KAUK):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]

        self.TENSES_CASES = ["NOM","AKK","INSTR","DAT","ABL","GEN","LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


class PermSynCreatorPR_KAUK_G(PermSynCreatorPR_KAUK):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]

        self.TENSES_CASES = ["NOM","ERG","INSTR","DAT","ADV","GEN"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



class PermSynCreatorPR_KAUK_K(PermSynCreatorPR_KAUK):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]

        self.TENSES_CASES = ["NOM","OBL"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40



class PermSynCreatorPR_KAUK_C(PermSynCreatorPR_KAUK):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3e","3x","3w"]

        self.TENSES_CASES = ["NOM","ERG","INSTR","ADV"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40
