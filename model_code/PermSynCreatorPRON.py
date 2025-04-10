from PermSynCreator import PermSynCreator

import itertools


class PermSynCreatorPRON(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PRON"

        self.TENSES_CASES = [" "]
        self.PERSONS = ["1","2","3"]
        self.NUMBERS = ["s","p"]
        self.COMBINED = [p+n for n in self.NUMBERS for p in self.PERSONS] + ["12p"]

    def _create_variations(self):
        # permutations:
        self._create_permutation_PERS_files()
        self._create_permutation_NUM_files()
        self._create_permutation_XROSS_files()
        # shuffled permutations:
        self._create_SHUF_files()

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

                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][line[0]] = line[count]

        # add m f
        # and tense
        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat, conj in cont_dict[tense].items():
                res_dict[feat] = conj

        return res_dict

    @staticmethod
    def _swap_4(perm_dict, f1, f2, f3, f4, n1, n2, n3, n4):
        perm_dict[f1], perm_dict[f2], perm_dict[f3], perm_dict[f4] \
            = perm_dict[n1], perm_dict[n2], perm_dict[n3], perm_dict[n4]

    @staticmethod
    def _swap_7(perm_dict, n1, n2, n3, n4, n5, n6, n7):
        perm_dict["1s"], perm_dict["2s"], perm_dict["3s"], perm_dict["1p"],perm_dict["2p"], perm_dict["3p"], perm_dict["12p"] \
            = perm_dict[n1], perm_dict[n2], perm_dict[n3], perm_dict[n4], perm_dict[n5], perm_dict[n6], perm_dict[n7]

    @staticmethod
    def _rotate_4_right(perm_dict, f1, f2, f3, f4):
        # 1 -> 2 -> 3 -> 4
        perm_dict[f1], perm_dict[f2], perm_dict[f3], perm_dict[f4] = perm_dict[f4], perm_dict[f1], perm_dict[f2], perm_dict[f2]

    @staticmethod
    def _rotate_4_left(perm_dict, f1, f2, f3, f4):
        # 1 <- 2 <- 3 <- 4
        perm_dict[f1], perm_dict[f2], perm_dict[f3], perm_dict[f4] = perm_dict[f2], perm_dict[f3], perm_dict[f4], perm_dict[f1]

    @staticmethod
    def _rotate_4_double(perm_dict, f1, f2, f3, f4):
        # 1 <- 2 <- 3 <- 4
        perm_dict[f1], perm_dict[f2], perm_dict[f3], perm_dict[f4] = perm_dict[f3], perm_dict[f4], perm_dict[f1], perm_dict[f2]


    def _create_permutation_PERS_files(self):
        """
        creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
        """
        # 1s <-> 2s
        self.add_pers_perm_variation([("1s","2s")])

        # 1s <-> 3s
        self.add_pers_perm_variation([("1s","3s")])

        # 2s <-> 3s
        self.add_pers_perm_variation([("2s","3s")])

        # 12p <-> 3p, 3s <-> 2s
        self.add_pers_perm_variation([("12p","3p"),("3s","2s")])

        # 12p <-> 3p, 3s <-> 1s
        self.add_pers_perm_variation([("12p","3p"),("3s","1s")])

        # 12p <-> 3p, 2s <-> 1s
        self.add_pers_perm_variation([("12p","3p"),("2s","1s")])

        #rotate
        self.add_pers_perm_variation(rotate_right_list=[("1p","2p","3p")])
        self.add_pers_perm_variation(rotate_left_list=[("1p","2p","3p")])
        self.add_pers_perm_variation(rotate_right_list=[("1s","2s","3s")])
        self.add_pers_perm_variation(rotate_left_list=[("1s","2s","3s")])


        #combination 12

        # 12p <-> 1p, 2p <-> 3p, 1s <-> 2s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "3p"),("1s", "2s")])

        # 12p <-> 1p, 2p <-> 3p, 1s <-> 3s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "3p"),("1s", "3s")])

        # 12p <-> 1p, 2p <-> 3p, 2s <-> 3s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "3p"),("2s", "3s")])

        # 12p <-> 2p, 1p <-> 3p, 2s <-> 1s
        self.add_pers_perm_variation([("12p", "1p"),("1p", "3p"),("2s", "1s")])

        # 12p <-> 2p, 1p <-> 3p, 2s <-> 3s
        self.add_pers_perm_variation([("12p", "1p"),("1p", "3p"),("2s", "3s")])

        # 12p <-> 2p, 1p <-> 3p, 1s <-> 3s
        self.add_pers_perm_variation([("12p", "1p"),("1p", "3p"),("1s", "3s")])

        # 12p <-> 3p, 2p <-> 1p, 3s <-> 2s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "1p"),("3s", "2s")])

        # 12p <-> 3p, 2p <-> 1p, 3s <-> 1s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "1p"),("3s", "1s")])

        # 12p <-> 3p, 2p <-> 1p, 2s <-> 1s
        self.add_pers_perm_variation([("12p", "1p"),("2p", "1p"),("2s", "1s")])



        # 12p <-> 1p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "1p")],rotate_left_list=[("1s", "2s", "3s")])




        # 12p <-> 1p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "1p")],rotate_right_list=[("1s", "2s", "3s")])

        # 12p <-> 2p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "2p")],rotate_left_list=[("1s", "2s", "3s")])

        # 12p <-> 2p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "2p")],rotate_right_list=[("1s", "2s", "3s")])

        # 12p <-> 3p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "3p")],rotate_left_list=[("1s", "2s", "3s")])

        # 12p <-> 3p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "3p")],rotate_right_list=[("1s", "2s", "3s")])


        # 12p <-> 1p, 2p <-> 3p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("2p", "3p")],rotate_left_list=[("1s", "2s", "3s")])

        # 12p <-> 1p, 2p <-> 3p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("2p", "3p")],rotate_right_list=[("1s", "2s", "3s")])

        # 12p <-> 2p, 1p <-> 3p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("1p", "3p")],rotate_left_list=[("1s", "2s", "3s")])

        # 12p <-> 2p, 1p <-> 3p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("1p", "3p")],rotate_right_list=[("1s", "2s", "3s")])

        # 12p <-> 3p, 2p <-> 1p, rotate s (left)
        self.add_pers_perm_variation(swap_list=[("12p", "3p"),("2p", "1p")],rotate_left_list=[("1s", "2s", "3s")])

        # 12p <-> 3p, 2p <-> 1p, rotate s (right)
        self.add_pers_perm_variation(swap_list=[("12p", "3p"),("2p", "1p")],rotate_right_list=[("1s", "2s", "3s")])



        #12p <-> 1p, 2p <-> 3p
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("2p", "3p")])

        #12p <-> 2p, 1p <-> 3p
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("1p", "3p")])

        #12p <-> 3p, 2p <-> 1p
        self.add_pers_perm_variation(swap_list=[("12p", "3p"),("2p", "1p")])

        # 12p <-> 1p, 1s <-> 2s
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("2s", "2s")])

        # 12p <-> 1p, 1s <-> 3s
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("1s", "3s")])

        # 12p <-> 1p, 2s <-> 3s
        self.add_pers_perm_variation(swap_list=[("12p", "1p"),("2s", "3s")])

        # 12p <-> 2p, 2s <-> 1s
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("2s", "1s")])

        # 12p <-> 2p, 2s <-> 3s
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("2s", "3s")])

        # 12p <-> 2p, 1s <-> 3s
        self.add_pers_perm_variation(swap_list=[("12p", "2p"),("1s", "3s")])


        # 1 - 2 - 3 - 4
        permutations = list(itertools.permutations(["1p", "12p", "2p", "3p"]))
        #i = 41
        for f_lst in permutations[1:]:
            self.add_pers_perm_variation(swap_4p_list=[(f_lst[0], f_lst[1], f_lst[2], f_lst[3])])


            #curr_perm = copy.deepcopy(self.org_conj_dict)
            #self._swap_4(curr_perm, "1p", "2p", "3p", "12p", )
            #self._add_var("PERM_PERS" + str(i), curr_perm)
            #i += 1
            #23 stück

    def _create_permutation_NUM_files(self):
        """
        creates all permutation files where NUM-features are swapped (s <-> p)
        """
        # 1s <-> 1p
        self.add_num_perm_variation([("1s","1p")])

        # 2s <-> 2p
        self.add_num_perm_variation([("2s","2p")])

        # 3s <-> 3p
        self.add_num_perm_variation([("3s","3p")])

        # 1s <-> 1p, 2s <-> 2p
        self.add_num_perm_variation([("1s","1p"),("2s","2p")])

        # 1s <-> 1p, 3s <-> 3p
        self.add_num_perm_variation([("1s","1p"),("3s","3p")])

        # 2s <-> 2p, 3s <-> 3p
        self.add_num_perm_variation([("2s","2p"),("3s","3p")])

    def _create_permutation_XROSS_files(self):
        """
        creates all permutation files where XROSS-features are swapped (1 <-> 2 <-> 3)
        """
        # 1s <-> 2p
        self.add_xross_perm_variation([("1s","2p")])

        # 1s <-> 3p
        self.add_xross_perm_variation([("1s","3p")])

        # 2s <-> 1p
        self.add_xross_perm_variation([("2s","1p")])

        # 2s <-> 3p
        self.add_xross_perm_variation([("2s","3p")])

        # 3s <-> 1p
        self.add_xross_perm_variation([("3s","1p")])

        # 3s <-> 2p
        self.add_xross_perm_variation([("3s","2p")])

        # 1s <-> 12p
        self.add_xross_perm_variation([("1s","12p")])


        # 2s <-> 12p
        self.add_xross_perm_variation([("2s","12p")])


        # 3s <-> 12p
        self.add_xross_perm_variation([("3s","12p")])


        #cross two
        # 1s <-> 2p; 2s <-> 3p
        self.add_xross_perm_variation([("1s","2p"),("2s","3p")])

        # 1s <-> 2p; 2s <-> 1p
        self.add_xross_perm_variation([("1s","2p"),("2s","1p")])

        # 1s <-> 2p; 3s <-> 2p
        self.add_xross_perm_variation([("1s","2p"),("3s","2p")])

        # 1s <-> 2p; 3s <-> 1p
        self.add_xross_perm_variation([("1s","2p"),("3s","1p")])

        # 1s <-> 3p; 2s <-> 1p
        self.add_xross_perm_variation([("1s","3p"),("2s","1p")])

        # 1s <-> 3p; 2s <-> 3p
        self.add_xross_perm_variation([("1s","3p"),("2s","3p")])

        # 1s <-> 3p; 3s <-> 1p
        self.add_xross_perm_variation([("1s","3p"),("3s","1p")])

        # 1s <-> 3p; 3s <-> 2p
        self.add_xross_perm_variation([("1s","3p"),("3s","2p")])

        ### 1 <-> 2
        # 2s <-> 1p; 3s <-> 1p
        self.add_xross_perm_variation([("2s","1p"),("3s","1p")])

        # 2s <-> 1p; 3s <-> 2p
        self.add_xross_perm_variation([("2s","1p"),("3s","2p")])

        # 2s <-> 3p; 3s <-> 2p
        self.add_xross_perm_variation([("2s","3p"),("3s","2p")])

        # 2s <-> 3p; 3s <-> 1p
        self.add_xross_perm_variation([("2s","3p"),("3s","1p")])

        ### 1 <-> 3
        # 3s <-> 2p; 2s <-> 1p
        self.add_xross_perm_variation([("3s","2p"),("2s","1p")])

        # 3s <-> 2p; 2s <-> 3p
        self.add_xross_perm_variation([("3s","2p"),("2s","3p")])

        # 3s <-> 1p; 2s <-> 3p
        self.add_xross_perm_variation([("3s","1p"),("2s","3p")])

        # 3s <-> 1p; 2s <-> 1p
        self.add_xross_perm_variation([("3s","1p"),("2s","1p")])


        #keep one, cross other
        # 1s <-> 1p; 2s <-> 3p
        self.add_xross_perm_variation([("1s","1p"),("2s","3p")])

        # 1s <-> 1p; 3s <-> 2p
        self.add_xross_perm_variation([("1s","1p"),("3s","2p")])

        # 1s <-> 1p; 2s <-> 3p, 3s <-> 2p
        self.add_xross_perm_variation([("1s","1p"),("2s","3p"),("3s","2p")])

        # 2s <-> 2p; 1s <-> 3p
        self.add_xross_perm_variation([("2s","2p"),("1s","3p")])

        # 2s <-> 2p; 3s <-> 1p
        self.add_xross_perm_variation([("2s","2p"),("3s","1p")])

        # 2s <-> 2p; 1s <-> 3p,  3s <-> 1p
        self.add_xross_perm_variation([("2s","2p"),("1s","3p"),("3s","1p")])

        # 3s <-> 3p; 2s <-> 1p
        self.add_xross_perm_variation([("3s","3p"),("2s","1p")])

        # 3s <-> 3p; 1s <-> 2p
        self.add_xross_perm_variation([("3s","3p"),("1s","2p")])

        # 3s <-> 3p; 2s <-> 1p, 1s <-> 2p
        self.add_xross_perm_variation([("3s","3p"),("2s","1p"),("1s","2p")])


        #12p <-> 1s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","1s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 1s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","1s")],rotate_right_list=[("1p","2p","3p")])

        #12p <-> 2s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","2s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 2s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","2s")],rotate_right_list=[("1p","2p","3p")])

        #12p <-> 3s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","3s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 3s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","3s")],rotate_right_list=[("1p","2p","3p")])




        #12p <-> 1s, 2s <-> 3s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 1s, 2s <-> 3s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s")],rotate_right_list=[("1p","2p","3p")])

        #12p <-> 2s, 1s <-> 3s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 2s, 1s <-> 3s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s")],rotate_right_list=[("1p","2p","3p")])

        #12p <-> 3s, 2s <-> 1s, rotate p (left)
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s")],rotate_left_list=[("1p","2p","3p")])

        #12p <-> 3s, 2s <-> 1s, rotate p (right)
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s")],rotate_right_list=[("1p","2p","3p")])





        #12p <-> 1s, 2s <-> 3s
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s")])

        #12p <-> 2s, 1s <-> 3s
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s")])

        #12p <-> 3s, 2s <-> 1s
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s")])



        #12p <-> 1s, 2s <-> 3s, 1p <-> 2p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s"),("1p","2p")])

        #12p <-> 1s, 2s <-> 3s, 1p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s"),("1p","3p")])

        #12p <-> 1s, 2s <-> 3s, 2p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2s","3s"),("2p","3p")])

        #12p <-> 2s, 1s <-> 3s, 2p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s"),("2p","1p")])

        #12p <-> 2s, 1s <-> 3s, 2p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s"),("2p","3p")])

        #12p <-> 2s, 1s <-> 3s, 1p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1s","3s"),("1p","3p")])

        #12p <-> 3s, 2s <-> 1s, 3p <-> 2p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s"),("3p","2p")])

        #12p <-> 3s, 2s <-> 1s, 3p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s"),("3p","1p")])

        #12p <-> 3s, 2s <-> 1s, 2p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2s","1s"),("2p","1p")])






        #12p <-> 1s, 1p <-> 2p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("1p","2p")])

        #12p <-> 1s, 1p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("1p","3p")])

        #12p <-> 1s, 2p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","1s"),("2p","3p")])

        #12p <-> 2s, 2p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("2p","1p")])

        #12p <-> 2s, 2p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("2p","3p")])

        #12p <-> 2s, 1p <-> 3p
        self.add_xross_perm_variation(swap_list=[("12p","2s"),("1p","3p")])

        #12p <-> 3s, 3p <-> 2p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("3p","2p")])

        #12p <-> 3s, 3p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("3p","1p")])

        #12p <-> 3s, 2p <-> 1p
        self.add_xross_perm_variation(swap_list=[("12p","3s"),("2p","1p")])


        #full-perm
        self.add_xross_perm_variation(swap_list=[("1s","12p"),("2s","3p"),("3s","2p")])
        self.add_xross_perm_variation(swap_list=[("1s","1p"),("2s","2p"),("3s","12p")])
        self.add_xross_perm_variation(swap_list=[("1s","2p"),("2s","1p"),("3p","12p")])
        self.add_xross_perm_variation(swap_list=[("1s","3p"),("2s","1p"),("3s","12p")])
        self.add_xross_perm_variation(swap_list=[("1s","2p"),("2s","3p"),("3s","12p")])
        self.add_xross_perm_variation(swap_list=[("1s","2p"),("2s","1p"),("3s","12p")])

        self.add_xross_perm_variation(full_swap7_list=[("1p", "1s", "12p", "2s", "3s", "3p", "2p")])
        self.add_xross_perm_variation(full_swap7_list=[("2p", "3s", "1s", "12p", "3p", "2s", "1p")])
        self.add_xross_perm_variation(full_swap7_list=[("12p", "2p", "3s", "2s", "1s", "3p", "1p")])
        self.add_xross_perm_variation(full_swap7_list=[("2p", "3s", "2s","12p", "1s", "3p", "1p")])
        self.add_xross_perm_variation(full_swap7_list=[("2p", "1s", "3s", "12p", "3p", "1p", "2s")])
        self.add_xross_perm_variation(full_swap7_list=[("2s", "1s", "12p", "2p", "3s", "3p", "1p")])
        self.add_xross_perm_variation(full_swap7_list=[("3s", "1p", "2p", "3p", "2s", "12p", "1s")])
        self.add_xross_perm_variation(full_swap7_list=[("12p", "2p", "1p", "2s", "3p", "1s", "3s")])
