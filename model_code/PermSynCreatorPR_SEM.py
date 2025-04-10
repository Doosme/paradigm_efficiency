from PermSynCreator import PermSynCreator
from PermSynCreatorVERB import PermSynCreatorSEM


class PermSynCreatorPR_SEM(PermSynCreatorSEM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_SEM"


class PermSynCreatorPR_SEM_h(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_SEM_h"

        self.PERSONS = ["1", "2v", "2h", "3"]
        self.TENSES_CASES = ["NOM", "SUFF"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]



    def read_in_conjugation_table(self, input_filename):
        """reads in a conjugation table with several columns for tenses"""
        cont_dict = {t: dict() for t in self.TENSES_CASES}

        with open(input_filename) as f:
            # dual_exists = list()
            d_list = list()
            p_list = list()
            for line in f:
                line = line.strip()
                line = line.split("\t")
                if line[0] == "NOM": continue

                if "d" in line[0]:
                    d_list.append(line[0])
                elif "p" in line[0]:
                    p_list.append(line[0])

                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][line[0]] = line[count]

        print(cont_dict)
        # add dual
        add_list_p = list()
        if d_list == list():
            for elem in cont_dict["NOM"].keys():
                if "p" in elem:
                    add_list_p.append(elem)
        for elem in add_list_p:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem.replace("p", "d")] = cont_dict[tense][elem]

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
                if "2hd "+g not in cont_dict["NOM"].keys():
                    for tense in self.TENSES_CASES:
                        cont_dict[tense]["2hd "+g] = cont_dict[tense]["2hs "+g]
            else:
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["2hs "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2hd "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2hp "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2vs "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2vd "+g] = cont_dict[tense]["2s "+g]
                    cont_dict[tense]["2vp "+g] = cont_dict[tense]["2s "+g]
                    del cont_dict[tense]["2s "+g]


        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict