from PermSynCreator import PermSynCreator


class PermSynCreatorPR_TURK(PermSynCreator):

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
            for feat in [x+y for y in self.NUMBERS for x in self.PERSONS]:
                res_dict[feat + " c " + tense] = cont_dict[tense][feat]

        return res_dict



class PermSynCreatorPR_TURK_T(PermSynCreatorPR_TURK):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_TURK_T"

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

class PermSynCreatorPR_TURK_Th(PermSynCreatorPR_TURK):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_TURK_Th"

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v", "3", "2h"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


class PermSynCreatorPR_TURK_P(PermSynCreatorPR_TURK):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_TURK_P"

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC","INSTR","ALLA","EQUA","SIMI","COM"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

class PermSynCreatorPR_TURK_A(PermSynCreatorPR_TURK):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_TURK_A"

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC","INSTR"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

class PermSynCreatorPR_TURK_Ah(PermSynCreatorPR_TURK):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_ROM_TURK_Ah"

        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v", "3", "2h"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC","INSTR"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40




class PermSynCreatorPR_TUNG(PermSynCreator):

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

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in [x+y for y in self.NUMBERS for x in self.PERSONS] + ["12p"]:
                res_dict[feat + " c " + tense] = cont_dict[tense][feat]

        return res_dict

class PermSynCreatorPR_TUNG_M(PermSynCreatorPR_TUNG):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)



        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"] #"12"
        #
        self.TENSES_CASES = ["NOM","AKK","GEN","DAT","ABL"]


        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]\
                        + ["12p " + g + " " + t for t in self.TENSES_CASES for g in self.GENDERS]
        print("BBB")
        print(self.COMBINED)

        self.shuffle_length = 40




class PermSynCreatorPR_TUNG_U(PermSynCreatorPR_TUNG):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)



        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2", "3"] #"12"
        #
        self.TENSES_CASES = ["NOM","AKK","GEN","DAT","ABL","LOC","INSTR","PROL","DIR"]


        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]\
                        + ["12p " + g + " " + t for t in self.TENSES_CASES for g in self.GENDERS]
        print("BBB")
        print(self.COMBINED)

        self.shuffle_length = 40


class PermSynCreatorPR_MONG(PermSynCreatorPR_TUNG):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)



        self.GENDERS = ["c"]
        self.NUMBERS = ["s", "p"]
        self.PERSONS = ["1", "2v", "3", "2h"] #"12"
        #
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","ABL","LOC","INSTR","COM","DIR"]


        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]\
                        + ["12p " + g + " " + t for t in self.TENSES_CASES for g in self.GENDERS]
        print("BBB")
        print(self.COMBINED)

        self.shuffle_length = 40
