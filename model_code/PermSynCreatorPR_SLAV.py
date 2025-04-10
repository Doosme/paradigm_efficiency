from PermSynCreator import PermSynCreator


class PermSynCreatorPR_SLAV(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

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

        #add dual
        add_list_p = list()
        if d_list == list():
            for elem in cont_dict["NOM"].keys():
                if "p" in elem:
                    add_list_p.append(elem)
        for elem in add_list_p:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem.replace("p","d")] = cont_dict[tense][elem]

        # add reflexiv:
        if "rs" in cont_dict["NOM"].keys():
            if "rp" not in cont_dict["NOM"].keys():
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["rp"] = cont_dict[tense]["rs"]
            if "rd" not in cont_dict["NOM"].keys():
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["rd"] = cont_dict[tense]["rs"]

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in [x+y for y in self.NUMBERS for x in self.PERSONS]:
                keys_list = cont_dict[tense].keys()
                if feat in keys_list:  # e.g. 1s
                    res_dict[feat + " m " + tense] = cont_dict[tense][feat]
                    res_dict[feat + " f " + tense] = cont_dict[tense][feat]
                    res_dict[feat + " n " + tense] = cont_dict[tense][feat]
                else:
                    if feat + " m" in keys_list:
                        res_dict[feat + " m " + tense] = cont_dict[tense][feat + " m"]

                    if feat + " f" in keys_list:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " f"]
                    else:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " m"]

                    if feat + " n" in keys_list:
                        res_dict[feat + " n " + tense] = cont_dict[tense][feat + " n"]
                    else:
                        res_dict[feat + " n " + tense] = cont_dict[tense][feat + " m"]

        return res_dict


class PermSynCreatorPR_SLAV_E(PermSynCreatorPR_SLAV):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_SLAV_E"

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "d", "p"]
        self.PERSONS = ["1", "2", "3", "r"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN", "INSTR", "LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

    def _create_variations(self):
        # randoms:
        self._create_random_PERM_files()
        self._create_random_SYN_files()
        self._create_random_PERM_dims_files()
        self._create_random_SYN_dims_files()
        # permutations:
        self._create_permutation_PERS_files()
        self._create_permutation_NUM_files()
        self._create_permutation_GEN_files()
        self._create_permutation_TENSE_files()
        self._create_permutation_X_files()
        # syncretic variants:
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_GEN_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

    def _create_permutation_PERS_files(self):
        # 3s
        # print("HERE")
        # for i, j in self.org_conj_dict.items():
        #    print(i,j)

        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g LOC", "1a g LOC")])


        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g LOC", "1a g LOC"),
             ("2a g DAT", "1a g DAT"),
             ("2a g INSTR", "1a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g LOC", "2a g LOC"),
             ("3a g DAT", "1a g DAT"),
             ("3a g INSTR", "1a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g INSTR", "2a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g LOC", "2a g LOC"),
             ("1a g DAT", "2a g DAT"),
             ("1a g INSTR", "2a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("1a g LOC", "2a g LOC"),
             ("1a g DAT", "2a g DAT"),
             ("1a g INSTR", "3a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3s g AKK", "1s g AKK"),
             ("3s g GEN", "1s g GEN")])

        self.add_pers_perm_variation(
            [("3s g AKK", "1s g AKK")])

        self.add_pers_perm_variation(
            [("3s g DAT", "2s g DAT"),
             ("3s g INSTR", "2s g INSTR")])

        self.add_pers_perm_variation(
            [("3s g GEN", "2s g GEN")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g LOC", "2s g LOC"),
             ("1s g GEN", "2s g GEN")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g INSTR", "2s g INSTR")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("2s g AKK", "3s g AKK"),
             ("1s g GEN", "3s g GEN")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f LOC", "2s f LOC"),
             ("1s f GEN", "2s f GEN")])

        self.add_pers_perm_variation(
            [("1s g AKK", "2s g AKK"),
             ("1s g GEN", "2s g GEN"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2p g LOC", "1p g LOC"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN"),
             ("2d g LOC", "1d g LOC")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2p g LOC", "1p g LOC")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f INSTR", "2s f INSTR")])

        self.add_pers_perm_variation(
            [("1s m DAT", "2s m DAT"),
             ("2s n AKK", "3s n AKK"),
             ("1s f GEN", "3s f GEN")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("2s g AKK", "3s g AKK"),
             ("1s g GEN", "3s g GEN")])

        self.add_pers_perm_variation(
            [("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT")])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK")])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK"),
             ("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT"),
             ("1p g GEN", "2p g GEN"),
             ("1d g GEN", "2d g GEN")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "2p g INSTR"),
             ("1d g INSTR", "2d g INSTR"),
             ("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT"),
             ("3p g GEN", "2p g GEN"),
             ("3d g GEN", "2d g GEN")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "3p g INSTR"),
             ("1d g INSTR", "3d g INSTR"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "3p g INSTR"),
             ("3p g DAT", "2p g DAT")
             ])

        self.add_pers_perm_variation(
            [("3p g AKK", "2p g AKK"),
             ("3d g DAT", "1d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g NOM", "2p g NOM"),
             ("1d g NOM", "2d g NOM"),
             ("1p g INSTR", "2p g INSTR"),
             ("1d g INSTR", "2d g INSTR"),
             ("1p g LOC", "2p g LOC"),
             ("1d g LOC", "2d g LOC")
             ])

        self.add_pers_perm_variation([
            ("1s g INSTR", "2s g INSTR")
        ])

        self.add_pers_perm_variation([
            ("2s g INSTR", "3s g INSTR")
        ])

        self.add_pers_perm_variation([
            ("2s g INSTR", "3s g INSTR"),
            ("2s g LOC", "3s g LOC")
        ])

        self.add_pers_perm_variation(
            [("1p m NOM", "2p m NOM"),
             ("1d f NOM", "2d f NOM"),
             ("1p n INSTR", "2p n INSTR"),
             ("1d n INSTR", "2d n INSTR"),
             ("1p f LOC", "2p f LOC"),
             ("1d m LOC", "2d m LOC")
             ])

        self.add_pers_perm_variation(
            [("1p m NOM", "2p m NOM"),
             ("1d m NOM", "2d m NOM"),
             ("1p n INSTR", "2p n INSTR"),
             ("1d n INSTR", "2d n INSTR"),
             ("1p f LOC", "2p f LOC"),
             ("1d f LOC", "2d f LOC")
             ])

        self.add_pers_perm_variation(
            rotate_right_list=
            [("1p g GEN", "2p g GEN", "3p g GEN")]
        )

        # print(self.pers_perm_count)

    def _create_permutation_NUM_files(self):
        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM")])

        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK")])

        for c in ["DAT", "INSTR", "LOC", "GEN"]:
            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("1d g " + c, "1p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("3d g " + c, "3p g " + c)])

            self.add_num_perm_variation(
                [("1d g " + c, "1p g " + c),
                 ("3d g " + c, "3p g " + c)])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("2d g INSTR", "2p g INSTR")])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g INSTR", "3p g INSTR")])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g INSTR", "3p g INSTR"),
             ("1d g LOC", "1p g LOC")])

        self.add_num_perm_variation(
            [("2d m DAT", "2p m DAT"),
             ("3d f DAT", "2p f DAT"),
             ("3d n INSTR", "3p n INSTR"),
             ("1d m INSTR", "1p m INSTR"),
             ("1d f LOC", "1p f LOC"),
             ("2d n LOC", "2p n LOC")
             ])

        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM"),
             ("2s g AKK", "2p g AKK"),
             ("1s g DAT", "1d g DAT"),
             ("2s g GEN", "2d g GEN")])

        self.add_num_perm_variation(
            [("3s m NOM", "3p m NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3d n DAT")])

        self.add_num_perm_variation(
            [("3s m NOM", "3d m NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3s f NOM", "3d f NOM"),
             ("3s m LOC", "3p m LOC"),
             ("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p f NOM", "3d f NOM"),
             ("3s f LOC", "3p f LOC"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p m NOM", "3d m NOM"),
             ("3s m LOC", "3p m LOC"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p m NOM", "3d m NOM"),
             ("3s m LOC", "3p m LOC"),
             ("3s n INSTR", "3p n INSTR"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(rotate_left_list=
                                    [("3s m NOM", "3d m NOM", "3p m NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")],
            rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s m GEN", "3d m GEN", "3p m GEN"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s m GEN", "3d m GEN", "3p m GEN"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ],
            rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM"),
                               ("3s f AKK", "3d f AKK", "3p f AKK")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("3s m GEN", "3d m GEN", "3p m GEN"),
             ("1s n DAT", "1d n DAT", "1p n DAT")
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m DAT", "3d m DAT", "3p m DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("2s m AKK", "2d m AKK", "2p m AKK"),
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m DAT", "3d m DAT", "3p m DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT")],
            rotate_right_list=[
                ("2s n AKK", "2d n AKK", "2p n AKK"),
                ("2s m AKK", "2d m AKK", "2p m AKK")
            ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("2s g DAT", "2d g DAT", "2p g DAT"),
             ("3s f DAT", "3d f DAT", "3p f DAT")],
            rotate_right_list=[
                ("1s g AKK", "1d g AKK", "1p g AKK"),
                ("3s f AKK", "3d f AKK", "3p f AKK")
            ])

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GEN", "1p g GEN"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GEN", "2d g GEN"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GEN", "3p g GEN"),
                ("2p g LOC", "2d g LOC"), ("1s g INSTR", "1d g INSTR"),
                ("1p g LOC", "1d g LOC"), ("2s g INSTR", "2d g INSTR"),
                ("3p g LOC", "3d g LOC"), ("3s g INSTR", "3d g INSTR")
            ]
        )

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GEN", "1p g GEN"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GEN", "2d g GEN"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GEN", "3p g GEN"),
                ("2p g LOC", "2d g LOC"), ("1s g INSTR", "1d g INSTR"),
                ("1p g LOC", "1d g LOC"), ("2s g INSTR", "2d g INSTR"),
                ("3p g LOC", "3d g LOC"), ("3s g INSTR", "3d g INSTR")
            ]
        )
        self.add_num_perm_variation(
            rotate_left_list=[
                ("1s g GEN", "1d g GEN", "1p g GEN"),
                ("2s g AKK", "2d g AKK", "2p g AKK"),
                ("3s n INSTR", "3d n INSTR", "3p n INSTR"),
            ],
            rotate_right_list=[
                ("2s g GEN", "2d g GEN", "2p g GEN"),
                ("1s g DAT", "1d g DAT", "1p g DAT"),
                ("3s m INSTR", "3d m INSTR", "3p m INSTR"),
            ]
        )

    def _create_permutation_GEN_files(self):

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m GEN", "3s f GEN", "3s n GEN")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m INSTR", "3s f INSTR", "3s n INSTR")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m INSTR", "3s f INSTR", "3s n INSTR")],
            rotate_left_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK"),
                ("3s m LOC", "3s f LOC", "3s n LOC")],
        )

        ###

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m LOC", "3s f LOC", "3s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m LOC", "3s f LOC", "3s n LOC")],
            rotate_left_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT")],
        )

        self.add_gen_perm_variation(
            [("3s m DAT", "3s f DAT"),
             ("3s m LOC", "3s f LOC")
             ])

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK"),
                ("3s m GEN", "3s f GEN", "3s n GEN"),
                ("3s m LOC", "3s f LOC", "3s n LOC"), ],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK")],
            rotate_left_list=
            [
                ("3s m GEN", "3s f GEN", "3s n GEN"),
                ("3s m LOC", "3s f LOC", "3s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("2s m DAT", "2s f DAT", "2s n DAT"),
                ("2s m LOC", "2s f LOC", "2s n LOC")],
            rotate_left_list=
            [
                ("1s m GEN", "1s f GEN", "1s n GEN"),
                ("1s m LOC", "1s f LOC", "1s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m LOC", "3s f LOC", "3s n LOC")],
            rotate_left_list=
            [
                ("3s m GEN", "3s f GEN", "3s n GEN"),
                ("3s m AKK", "3s f AKK", "3s n AKK")],
        )

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3s m GEN", "3s f GEN"),
             ("3s m LOC", "3s f LOC")
             ])

        for g in ["m", "n"]:
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " INSTR", "3s f INSTR")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " LOC", "3s f LOC")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " LOC", "3s f LOC"),
                 ("3s " + g + " DAT", "3s f DAT"),
                 ("3s " + g + " INSTR", "3s f INSTR")])
            self.add_gen_perm_variation(
                [("3s " + g + " NOM", "3s f NOM")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GEN", "3s f GEN")])

            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GEN", "3s f GEN")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s m NOM", "2s f NOM"),
             ("1s m AKK", "1s f AKK"),
             ("3s m INSTR", "3s f INSTR"),
             ("1s m AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s f LOC"),
             ("3p m INSTR", "3p f INSTR"),
             ("3s n NOM", "3s m NOM"),
             ("3d m GEN", "3d f GEN")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s n NOM", "2s f NOM"),
             ("1s m GEN", "1s f GEN"),
             ("3s m INSTR", "3s n INSTR"),
             ("1s m AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s n LOC"),
             ("3p m INSTR", "3p f INSTR"),
             ("3s n NOM", "3s m NOM"),
             ("3d m GEN", "3d f GEN"),
             ("2s m AKK", "2s f AKK"),
             ("2d n DAT", "2d f DAT"),
             ("2s n LOC", "2s f LOC"),
             ("1p m INSTR", "1p f INSTR"),
             ("1s n NOM", "1s m NOM"),
             ("1d m GEN", "1d f GEN")
             ])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s n LOC"),
             ("3p m INSTR", "3p f INSTR"),
             ("3s n NOM", "3s m NOM"),
             ("3d m GEN", "3d f GEN"),
             ("2s f AKK", "2s n AKK"),
             ("2d n DAT", "2d m DAT"),
             ("2s n LOC", "2s m LOC"),
             ("1p n INSTR", "1p f INSTR"),
             ("1s f NOM", "1s m NOM"),
             ("1d m GEN", "1d f GEN")
             ])

        self.add_gen_perm_variation(
            [
                ("2s f AKK", "2s n AKK"),
                ("2d n DAT", "2d m DAT"),
                ("2p n LOC", "2p m LOC"),
                ("1p n INSTR", "1p f INSTR"),
                ("1s f NOM", "1s m NOM"),
                ("1d m GEN", "1d f GEN"),
                ("2s f DAT", "2s n DAT"),
                ("2d n GEN", "2d m GEN"),
                ("2p n NOM", "2p m NOM"),
                ("1p n GEN", "1p f GEN"),
                ("1s f LOC", "1s m LOC"),
                ("1d m NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d n INSTR", "2d m INSTR"),
                ("2p n GEN", "2p m GEN"),
                ("1p n AKK", "1p f AKK"),
                ("1s f GEN", "1s m GEN"),
                ("1d m INSTR", "1d f INSTR")
            ])

        self.add_gen_perm_variation(
            [
                ("2s f LOC", "2s n LOC"),
                ("2d n AKK", "2d m AKK"),
                ("2p n LOC", "2p m LOC"),
                ("1p n INSTR", "1p f INSTR"),
                ("1s f NOM", "1s m NOM"),
                ("1d m GEN", "1d f GEN"),
                ("2s f INSTR", "2s n INSTR"),
                ("2d n GEN", "2d f GEN"),
                ("2p n NOM", "2p f NOM"),
                ("1p n GEN", "1p f GEN"),
                ("1s f LOC", "1s n LOC"),
                ("1d n NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d f INSTR", "2d m INSTR"),
                ("2p f GEN", "2p m GEN"),
                ("1p n AKK", "1p f AKK"),
                ("1s n GEN", "1s m GEN"),
                ("1d m INSTR", "1d f INSTR")
            ])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s f AKK", "2s n AKK"), ("2d m AKK", "2d n AKK"), ("2p f AKK", "2p m AKK"),
             ("2s m DAT", "2s n DAT"), ("1d f DAT", "1d n DAT"), ("1s f DAT", "1s m DAT"),
             ("1d m INSTR", "1d n INSTR"), ("3d m INSTR", "3d f INSTR"), ("2p m INSTR", "2p f INSTR"),
             ("2s m LOC", "2s n LOC"), ("1d f LOC", "1d n LOC"), ("1s f LOC", "1s m LOC")])

        self.add_gen_perm_variation(
            rotate_right_list=
            [("3p m AKK", "3p f AKK", "3p n AKK"),
             ("3s m DAT", "3s f DAT", "3s n DAT")],
            rotate_left_list=
            [("3d m NOM", "3d f NOM", "3d n NOM"),
             ("3s m INSTR", "3s f INSTR", "3s n INSTR")]
        )

    def _create_permutation_TENSE_files(self):
        self.add_ten_perm_variation(
            [("za g NOM", "za g INSTR")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g INSTR"),
             ("za g DAT", "za g GEN")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g INSTR"),
             ("za g DAT", "za g GEN"),
             ("za g LOC", "za g NOM")])

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g GEN", "1p g LOC"),
                ("1d g AKK", "1d g GEN", "1d g LOC")],
            rotate_right_list=[
                ("2d g AKK", "2d g GEN", "2d g LOC"),
                ("2d g AKK", "2d g GEN", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g AKK", "1p g GEN"),
                ("1d g AKK", "1d g GEN"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g GEN", "1p g LOC"),
                ("1d g GEN", "1d g LOC"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC"),
                ("1s g AKK", "1s g GEN")
            ])

        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m GEN"),
                ("1d g AKK", "1d g GEN"),
                ("1p g AKK", "1p g GEN"),
                ("2s g AKK", "2s g GEN")
            ])
        ###

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g INSTR", "1p g LOC"),
                ("1d g AKK", "1d g INSTR", "1d g LOC")],
            rotate_right_list=[
                ("2d g AKK", "2d g GEN", "2d g INSTR"),
                ("2d g AKK", "2d g GEN", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g GEN"),
                ("1d g NOM", "1d g GEN"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g LOC"),
                ("1d g NOM", "1d g LOC"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR"),
                ("1s g AKK", "1s g NOM")
            ])

        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m INSTR"),
                ("1d g AKK", "1d g INSTR"),
                ("1p g AKK", "1p g INSTR"),
                ("2s g AKK", "2s g INSTR")
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m LOC"),
                ("1s g DAT", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m LOC"),
                ("3s n DAT", "3s n LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g LOC"),
                ("2s g DAT", "2s g LOC"),
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s m GEN", "3s m LOC"),
                ("1s g GEN", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m LOC"),
                ("1s g AKK", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m LOC", "3s m AKK"),
                ("3s n LOC", "3s n AKK"),
            ])
        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m AKK"),
                ("3s n DAT", "3s n AKK"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g INSTR"),
                ("2s g DAT", "2s g INSTR"),
            ])

        ###

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g INSTR"),
             ("zp g AKK", "zp g INSTR"),
             ("zs g DAT", "zs g GEN"),
             ("zs g LOC", "zs g NOM")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR")])

        self.add_ten_perm_variation(
            [("3p g DAT", "3p g INSTR"),
             ("3d g DAT", "3d g INSTR")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g DAT"),
             ("2p g GEN", "2p g INSTR")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR"),
             ("1p g GEN", "1p g DAT")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g DAT"),
             ("2p g GEN", "2p g INSTR"),
             ("3d g GEN", "3d g DAT"),
             ("2d g GEN", "2d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR"),
             ("1p g GEN", "1p g DAT"),
             ("3d g GEN", "3d g INSTR"),
             ("1d g GEN", "1d g DAT")
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("3s f INSTR", "3s f LOC"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("1d g DAT", "1d g GEN"),
             ("2p g INSTR", "2p g LOC"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("1d g DAT", "1d g GEN"),
             ("2p g INSTR", "2p g LOC"),
             ("3d g LOC", "3d g GEN"),
             ("3p g DAT", "3p g INSTR"),
             ])

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g LOC"),
             ("zp g AKK", "zp g LOC"),
             ("zs g DAT", "zs g INSTR")])

        self.add_ten_perm_variation(
            [("zd m AKK", "zd m LOC"),
             ("zp f AKK", "zp f LOC"),
             ("zs n DAT", "zs n INSTR")])

        self.add_ten_perm_variation(
            [("1a g NOM", "1a g INSTR")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g INSTR")])

        self.add_ten_perm_variation(
            [("1a g AKK", "1a g DAT")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g GEN")])

        self.add_ten_perm_variation(
            [("1a g NOM", "1a g DAT"),
             ("3a g NOM", "3a g AKK"),
             ("1a g NOM", "1a g GEN")])

        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g NOM", "1a g AKK"),
             ("2a g NOM", "2a g GEN")])

        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g LOC", "1a g AKK"),
             ("3a g NOM", "3a g GEN")])

        self.add_ten_perm_variation(
            [("2a g INSTR", "2a g DAT"),
             ("1a g LOC", "1a g AKK"),
             ("3a f NOM", "3a f GEN")])

        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])

        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT"),
             ("1s g LOC", "1s g INSTR")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("2p g LOC", "2p g INSTR"),
             ("2d g LOC", "2d g INSTR")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2s g LOC", "2s g INSTR"),
             ("1p g LOC", "1p g INSTR"),
             ("1d g LOC", "1d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2p g LOC", "2p g INSTR"),
             ("2d g LOC", "2d g INSTR"),
             ("1p g LOC", "1p g INSTR"),
             ("1d g LOC", "1d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("1s g DAT", "1s g INSTR")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g INSTR")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g INSTR"),
             ("1s g AKK", "1s g LOC")])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC")])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC"),
             ("2p g NOM", "2p g GEN"),
             ("2d g AKK", "2d g LOC")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC"),
             ("2p m NOM", "2p m GEN"),
             ("2d n AKK", "2d n LOC")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2p m NOM", "2p m GEN"),
             ("2d n AKK", "2d n DAT")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2p g NOM", "2p g GEN"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g INSTR"),
             ("2p g NOM", "2p g LOC")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g DAT"),
             ("2p g NOM", "2p g AKK")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m INSTR"),
             ("3p f DAT", "3p f INSTR"),
             ("3d n AKK", "3d n LOC"),
             ("2d m AKK", "2d m DAT"),
             ("1d f NOM", "1d f DAT"),
             ("2p n NOM", "2p n AKK")
             ])

        self.add_ten_perm_variation(
            [("1s m NOM", "3s m INSTR"),
             ("2p f NOM", "3p f LOC"),
             ("2d n NOM", "3d n GEN"),
             ("2d m NOM", "2d m DAT"),
             ("1d f NOM", "1d f AKK"),
             ])

        self.add_ten_perm_variation(
            [("3a g AKK", "3a g GEN")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g GEN")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g GEN"),
             ("1a g AKK", "1a g GEN")])

        self.add_ten_perm_variation(
            [("zs g AKK", "zs g GEN")])

        self.add_ten_perm_variation(
            [("zp g AKK", "zp g GEN"),
             ("zd g AKK", "zd g GEN")])

        self.add_ten_perm_variation(
            rotate_left_list=
            [("1p g AKK", "1p g GEN", "1p g DAT")],
            rotate_right_list=
            [("2p g AKK", "2p g GEN", "2p g DAT")]
        )

        self.add_ten_perm_variation(
            rotate_left_list=
            [("1p g AKK", "1p g GEN", "1p g DAT"),
             ("3p m LOC", "3p m NOM", "3p m INSTR")],
            rotate_right_list=
            [("2p g AKK", "2p g GEN", "2p g DAT"),
             ("3p n LOC", "3p n NOM", "3p n INSTR")]
        )

    def _create_permutation_X_files(self):
        self.add_xross_perm_variation(
            [("3p g LOC", "2s g LOC")])

        self.add_xross_perm_variation(
            [("3s m INSTR", "3s n GEN"),
             ("2s m DAT", "3s n LOC")])

        self.add_xross_perm_variation(
            [("3p f NOM", "3p n AKK")])

        self.add_xross_perm_variation(
            [("3d f AKK", "3s n NOM"),
             ("3d n AKK", "3s f NOM")])

        self.add_xross_perm_variation(
            [("3s n AKK", "3p f NOM"),("2d g AKK", "1s g NOM")])


        self.add_xross_perm_variation(
            [("3s m INSTR", "3s m GEN"),
             ("2s n DAT", "3s n LOC")])

        self.add_xross_perm_variation(
            rotate_right_list=
            [("1p g GEN", "2p g GEN", "3p g GEN"),
             ("3s m GEN", "3s f GEN", "3s n GEN")],
        )

        self.add_xross_perm_variation(
            [("1p g DAT", "2p g GEN")]
        )

        self.add_xross_perm_variation(
            [("3s n AKK", "3s n LOC"),
             ("3s n AKK", "3s n INSTR")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g INSTR"),
             ("2s g NOM", "2p g LOC")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g INSTR")])

        self.add_xross_perm_variation(
            [("rs g GEN", "rp g INSTR")])

        self.add_xross_perm_variation(
            [("rd g GEN", "rp g INSTR")])

        self.add_xross_perm_variation(
            [("rs m GEN", "3p m LOC"),
             ("rp f GEN", "3p f LOC"),
             ("rd n GEN", "3p n LOC")])

        self.add_xross_perm_variation(
            [("rs m GEN", "3p m LOC"),
             ("rp f GEN", "3p f LOC"),
             ("rd n GEN", "3p n LOC"),

             ("rs m INSTR", "3d m DAT"),
             ("rp f INSTR", "3d f DAT"),
             ("rd n INSTR", "3d n DAT")
             ])

        self.add_xross_perm_variation(
            [("rs m GEN", "3p m LOC"),
             ("rp f GEN", "3p f LOC"),
             ("rd n GEN", "3p n LOC"),

             ("rs m INSTR", "3d m DAT"),
             ("rp f INSTR", "3d f DAT"),
             ("rd n INSTR", "3d n DAT"),

             ("rs m DAT", "3p m INSTR"),
             ("rp f DAT", "3p f INSTR"),
             ("rd n DAT", "3p n INSTR"),

             ("rs m LOC", "3d m GEN"),
             ("rp f LOC", "3d f GEN"),
             ("rd n LOC", "3d n GEN")
             ])

        self.add_xross_perm_variation(
            [("1s g DAT", "1s g INSTR"),
             ("3s f DAT", "3s m DAT"),
             ("3s f INSTR", "3s m INSTR")])

        self.add_xross_perm_variation(
            [("3s g NOM", "2p g INSTR"),
             ("3s m GEN", "2p f DAT"),
             ("3s n GEN", "1s f NOM"),
             ("3s f DAT", "1p f NOM")])

        self.add_xross_perm_variation(
            [("1s g NOM", "2p g INSTR"),
             ("2s g DAT", "2s g LOC"),
             ("2s g AKK", "1p g INSTR"),
             ("1p g GEN", "1s g LOC"),
             ("2p g DAT", "2s g INSTR"),
             ("3p g NOM", "1d g INSTR"),
             ("1d g AKK", "3d g LOC"),
             ("2d g GEN", "3p g INSTR"),
             ("3d g NOM", "1d g LOC")])

        self.add_xross_perm_variation(
            [("1p g AKK", "2p g LOC"),
             ("1d g AKK", "2d g LOC"),
             ("1s g DAT", "2s g INSTR"),
             ("3s m AKK", "3s n DAT"),
             ("3s m NOM", "3s n INSTR")])

        self.add_xross_perm_variation(
            [
                ("1s f NOM", "2s n NOM"), ("2s m GEN", "1s m DAT"), ("2s n DAT", "1s m AKK"),
                ("1s n GEN", "1s f DAT"), ("1p f GEN", "1p m GEN"), ("2s n GEN", "2s f GEN"),
                ("1p f DAT", "1p m DAT"), ("1s m GEN", "1s n DAT"), ("2p f AKK", "2s m AKK"),
                ("2s f DAT", "2p m AKK"), ("1p n DAT", "2p n GEN"), ("1s n NOM", "1s m NOM"),
                ("2s f NOM", "1p n NOM"), ("1s f AKK", "1p m AKK"), ("1p f NOM", "1p m NOM"),
                ("1p f AKK", "2s m NOM"), ("2s n AKK", "2s f AKK"), ("1p n AKK", "1s n AKK"),
                ("1p n GEN", "1s f GEN"), ("2p f NOM", "2s m DAT"), ("2p f DAT", "2p n DAT"),
                ("2p n NOM", "2p m DAT"), ("2p m GEN", "2p m NOM"), ("2p f GEN", "2p n AKK")
            ])

        self.add_xross_perm_variation(
            [
                ("1s m AKK", "2p m NOM"), ("1s f GEN", "1s f NOM"), ("1s m GEN", "2p m DAT"),
                ("1s n DAT", "2p m AKK"), ("2s f AKK", "1s n GEN"), ("1p m DAT", "1p n DAT"),
                ("2s m AKK", "1s f DAT"), ("2s n GEN", "1s m NOM"), ("1p m NOM", "1p f NOM"),
                ("2s m NOM", "2s m DAT"), ("2s m GEN", "1p m GEN"), ("2p m GEN", "2p f GEN"),
                ("2s f DAT", "2s n NOM"), ("2s n AKK", "2p f AKK"), ("1p n GEN", "2s n DAT"),
                ("2p n AKK", "2s f NOM"), ("1s f AKK", "1s n NOM"), ("1s m DAT", "1s n AKK"),
                ("1p n NOM", "2p n NOM"), ("1p f AKK", "2s f GEN"), ("1p f DAT", "1p f GEN"),
                ("2p n GEN", "1p m AKK"), ("2p f DAT", "2p n DAT"), ("2p f NOM", "1p n AKK"),
            ])

        self.add_xross_perm_variation(
            [
                ("1s m AKK", "1s f AKK"), ("1p f DAT", "1p n DAT"), ("1p n GEN", "2p n AKK"),
                ("1s m NOM", "2s m AKK"), ("2p f AKK", "1p f NOM"), ("1s f GEN", "1s n GEN"),
                ("1p n AKK", "2s n NOM"), ("2s f NOM", "1p f AKK"), ("2p f GEN", "2p n GEN"),
                ("1p m NOM", "1s f DAT"), ("1s n DAT", "2p m AKK"), ("2p f NOM", "2p n NOM"),
                ("1s n NOM", "1s m DAT"), ("1p n NOM", "2s f DAT"), ("2s n DAT", "1s f NOM"),
                ("2s m DAT", "2p m NOM"), ("1s m GEN", "1p m DAT"), ("1s n AKK", "2p m GEN"),
                ("1p f GEN", "2p f DAT"), ("2s m NOM", "2p m DAT"), ("2s f AKK", "2s n AKK"),
                ("2s m GEN", "2p n DAT"), ("1p m GEN", "2s f GEN"), ("2s n GEN", "1p m AKK")
            ])

        self.add_xross_perm_variation(
            [("1p n GEN", "3s n NOM"), ("3p m AKK", "1p n AKK"), ("3s n GEN", "2s n DAT"),
             ("2s m DAT", "2s f DAT"), ("2p f DAT", "1s n AKK"), ("1p m AKK", "2p n AKK"),
             ("1s f NOM", "1s n DAT"), ("3s n AKK", "2s f NOM"), ("3p n NOM", "2s f GEN"),
             ("2p n DAT", "2p m NOM"), ("3s m NOM", "2s n AKK"), ("2p n GEN", "1p m GEN"),
             ("1s m AKK", "3p n GEN"), ("1p f NOM", "2s n GEN"), ("1s f DAT", "3s f DAT"),
             ("2s m GEN", "1p f AKK"), ("1s m DAT", "2s n NOM"), ("2p m DAT", "2s m NOM"),
             ("2p m AKK", "2p f AKK"), ("1p n NOM", "3p f GEN"), ("1p m DAT", "3p n DAT"),
             ])

        self.add_xross_perm_variation(
            [
                ("1s n LOC", "1s m INSTR"), ("2s m INSTR", "1s m NOM"), ("3s f INSTR", "3s f LOC"),
                ("1s m AKK", "1s n DAT"), ("1p n GEN", "2s m GEN"), ("3s m LOC", "1s f AKK"),
                ("2s f INSTR", "3s m NOM"), ("2s f GEN", "3s n NOM"), ("1s f NOM", "2p m INSTR"),
                ("2p n DAT", "2s n INSTR"), ("2p n GEN", "2s m NOM"), ("1s n NOM", "2p f DAT"),
                ("1p f DAT", "1p m DAT"), ("3s n GEN", "3p n DAT"), ("1p n DAT", "2s f NOM"),
                ("2s n GEN", "2p m GEN"), ("2p f GEN", "2s n NOM"), ("3s f NOM", "3s n LOC"),
                ("3p n GEN", "3p n AKK"), ("1p m GEN", "3p f INSTR"), ("1p f LOC", "3p f NOM"),
                ("3s m DAT", "3s n INSTR"), ("1p n AKK", "3p m NOM"), ("3p n NOM", "1p n NOM"),
                ("3s f GEN", "1p f GEN"), ("1p m AKK", "3p m INSTR"), ("1p m NOM", "1p f NOM"),
                ("1s f INSTR", "3s m GEN"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("2p g AKK", "2p g GEN"), ("1p g AKK", "2p g NOM"),
                ("1p g DAT", "2p g DAT"), ("1p g GEN", "1p g NOM"),
                ("3s f DAT", "3p f AKK"), ("3p m AKK", "3p f DAT"), ("3s m DAT", "3p n AKK"),
                ("3s n AKK", "3p n NOM"), ("3s n GEN", "3p n GEN"), ("3s f DAT", "3s n DAT")
            ])

        self.add_xross_perm_variation(
            [
                ("3s m GEN", "3p f DAT"), ("3p n DAT", "3s f GEN"), ("3s f DAT", "3s f AKK"),
                ("3s n NOM", "3s m DAT"), ("3s m AKK", "3p m DAT"), ("3s f NOM", "3p m NOM"),
                ("3p m GEN", "3p f GEN"), ("3p f NOM", "3p n AKK"), ("3s n AKK", "3s m NOM"),
                ("3p m AKK", "3p n GEN"), ("3p f AKK", "3p n NOM"), ("3s n DAT", "3s n GEN")
            ]
        )

        self.add_xross_perm_variation(
            [
                ("3s g GEN", "2s g NOM"), ("2s g GEN", "1p g GEN"), ("3s g DAT", "1s g AKK"),
                ("2s g DAT", "2p g GEN"), ("3s g NOM", "1p g DAT"), ("2s g AKK", "2p g AKK"),
                ("2p g NOM", "2p g DAT"), ("3p g NOM", "1s g GEN"), ("1p g AKK", "1p g NOM"),
                ("1s g DAT", "3p g DAT"), ("3p g GEN", "1s g NOM"), ("3p g AKK", "3s g AKK"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("3a g GEN", "2a g NOM"),
                ("2a g AKK", "1a g DAT"),
                ("1a g DAT", "2a g NOM"),
                ("3a g DAT", "3a g GEN"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("zd g GEN", "zs g NOM"),
                ("zd g LOC", "zp g GEN"),
                ("zp g INSTR", "zs g NOM"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("1s g LOC", "1s g DAT"),
                ("2d g LOC", "2s g NOM"),
                ("3p g LOC", "3s g GEN"),
                ("1p g INSTR", "2s g DAT"),
                ("2d g INSTR", "1s g NOM"),
                ("3p g INSTR", "3s g AKK"),
            ]
        )


    def _create_syncretic_PERS_files(self):
        self.add_pers_sync_variation([("1a g AKK", "2a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g DAT", "2a g DAT"), ("1a g GEN", "2a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g DAT", "3a g DAT"), ("2a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g DAT", "1a g DAT"), ("2a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g DAT", "3a g DAT"), ("1a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g DAT", "1a g DAT"), ("3a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g DAT", "2a g DAT"), ("3a g GEN", "2a g GEN")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g GEN", "2a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g GEN", "2a g GEN")])


        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g INSTR", "2a g INSTR")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g INSTR", "3a g INSTR")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g INSTR", "1a g INSTR")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g INSTR", "3a g INSTR")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g INSTR", "1a g INSTR")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g INSTR", "2a g INSTR")])

        self.add_pers_sync_variation([("1s g AKK", "2s g AKK"),
                                      ("1p g DAT", "2p g DAT"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("3s g GEN", "rs g GEN")])


        self.add_pers_sync_variation([("1s g AKK", "3s g AKK"),
                                      ("2d g DAT", "3d g DAT"),
                                      ("1p g GEN", "2p g GEN")])


        self.add_pers_sync_variation([("1s m AKK", "3s m AKK"),
                                      ("2d f DAT", "3d f DAT")])


        self.add_pers_sync_variation([("1p g AKK", "2p g AKK"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("1s g GEN", "2s g GEN")])


        self.add_pers_sync_variation([("1p g INSTR", "2p g INSTR"),
                                      ("1d g LOC", "2d g LOC")])


        self.add_pers_sync_variation([("2p g INSTR", "3p g INSTR"),
                                      ("2p g LOC", "3p g LOC")])

    def _create_syncretic_NUM_files(self):

        for p in ["1","2","3"]:
            self.add_num_sync_variation([(p+"s g INSTR", p+"p g INSTR")])
            self.add_num_sync_variation([(p+"s g LOC", p+"p g LOC")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g LOC", p+"p g LOC")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g LOC", p+"p g LOC"),
                                         (p + "s g AKK", p + "p g AKK"),
                                         (p + "s g INSTR", p + "p g INSTR")
                                         ])


            self.add_num_sync_variation([(p+"s g INSTR", p+"p m INSTR"),
                                        (p+"s g LOC", p+"p m LOC")])

            self.add_num_sync_variation([(p+"s g INSTR", p+"d m INSTR"),
                                        (p+"s g LOC", p+"d m LOC")])

            self.add_num_sync_variation([(p+"s g t", p+"p g t")])

        self.add_num_sync_variation([("zs g t", "zp g t")])
        self.add_num_sync_variation([("zd g t", "zp g t")])
        self.add_num_sync_variation([("1s g t", "1p g t"),
                                     ("2s g t", "2p g t")])


    def _create_syncretic_GEN_files(self):
        #self.add_gen_sync_variation([("za g t", "za g t")])

        self.add_gen_sync_variation([("za f t", "za m t")])
        self.add_gen_sync_variation([("za n t", "za m t")])

        for p in self.PERSONS:
            self.add_gen_sync_variation([(p+"a f t", p+"a m t")])
            self.add_gen_sync_variation([(p+"a n t", p+"a m t")])

        for n in self.NUMBERS:
            self.add_gen_sync_variation([("z"+n+" f t", "z"+n+" m t")])
            self.add_gen_sync_variation([("z"+n+" n t", "z"+n+" m t")])


        for n in self.NUMBERS:
            for p in self.PERSONS:
                self.add_gen_sync_variation([(p+n+" f t", p+n+" m t")])
                self.add_gen_sync_variation([(p+n+" n t", p+n+" m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t")])
        self.add_gen_sync_variation([("3s n t", "3s m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t")])
        self.add_gen_sync_variation([("3p n t", "3p m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t"),("3s n t", "3s m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t"),("3p n t", "3p m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t"),("3p n t", "3p m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t"),("3s n t", "3s m t")])


        self.add_gen_sync_variation([("3s f AKK", "3s m AKK")])
        self.add_gen_sync_variation([("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3p f GEN", "3p m GEN")])

        self.add_gen_sync_variation([("3s f AKK", "3s m AKK"), ("3s n AKK", "3s m AKK")])
        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3s f GEN", "3s m GEN"), ("3s n GEN", "3s m GEN")])

        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n DAT", "3s m DAT"),
                                     ("3s f GEN", "3s m GEN"), ("3s n GEN", "3s m GEN")])

        self.add_gen_sync_variation([("3s f AKK", "3s m AKK"), ("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n LOC", "3s m LOC")])
        self.add_gen_sync_variation([("3s f INSTR", "3s m INSTR"), ("3s n GEN", "3s m GEN")])


        self.add_gen_sync_variation([("3p f t", "3p m LOC"), ("3p n t", "3p m LOC")])

        self.add_gen_sync_variation([("3s f NOM", "3s m NOM"), ("3p n GEN", "3p m GEN")])
        self.add_gen_sync_variation([("3p f NOM", "3p m NOM"), ("3s n AKK", "3s m AKK")])


    def _create_syncretic_TENSE_files(self):

        self.add_ten_sync_variation([("za g AKK", "za g GEN")])
        self.add_ten_sync_variation([("1a g AKK", "1a g GEN")])
        self.add_ten_sync_variation([("2a g AKK", "2a g GEN")])
        self.add_ten_sync_variation([("3a g AKK", "3a g GEN")])
        self.add_ten_sync_variation([("zs g AKK", "zs g GEN")])
        self.add_ten_sync_variation([("zd g AKK", "zd g GEN")])
        self.add_ten_sync_variation([("zp g AKK", "zp g GEN")])

        self.add_ten_sync_variation([("za g AKK", "za g GEN"),("za g DAT", "za g GEN")])
        self.add_ten_sync_variation([("1a g AKK", "1a g GEN"),("1a g DAT", "1a g GEN")])
        self.add_ten_sync_variation([("2a g AKK", "2a g GEN"),("2a g DAT", "2a g GEN")])
        self.add_ten_sync_variation([("3a g AKK", "3a g GEN"),("3a g DAT", "3a g GEN")])
        self.add_ten_sync_variation([("zs g AKK", "zs g GEN"),("zs g DAT", "zs g GEN")])
        self.add_ten_sync_variation([("zd g AKK", "zd g GEN"),("zd g DAT", "zd g GEN")])
        self.add_ten_sync_variation([("zp g AKK", "zp g GEN"),("zp g DAT", "zp g GEN")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT"),("za g INSTR", "za g LOC")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT"),("1a g INSTR", "1a g LOC")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT"),("2a g INSTR", "2a g LOC")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT"),("3a g INSTR", "3a g LOC")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT"),("zs g INSTR", "zs g LOC")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT"),("zd g INSTR", "zd g LOC")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT"),("zp g INSTR", "zp g LOC")])

    def _create_syncretic_X_files(self):
        pass




class PermSynCreatorPR_SLAV_S(PermSynCreatorPR_SLAV):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_SLAV_S"

        self.GENDERS = ["m", "f", "n"]
        self.PERSONS = ["1", "2", "3","r"]
        self.NUMBERS = ["s","d","p"]
        self.TENSES_CASES = ["NOM", "AKKs", "DATs", "AKK", "DAT", "PROP"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

    def _create_variations(self):
        # randoms:
        self._create_random_PERM_files()
        self._create_random_SYN_files()
        self._create_random_PERM_dims_files()
        self._create_random_SYN_dims_files()
        # permutations:
        self._create_permutation_PERS_files()
        self._create_permutation_NUM_files()
        self._create_permutation_GEN_files()
        self._create_permutation_TENSE_files()
        self._create_permutation_X_files()
        # syncretic variants:
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_GEN_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()


    def _create_permutation_PERS_files(self):
        #3s
        #print("HERE")
        #for i, j in self.org_conj_dict.items():
        #    print(i,j)


        self.add_pers_perm_variation(
                [("2a g AKK", "1a g AKK"),
                 ("2a g AKKs", "1a g AKKs")])



        self.add_pers_perm_variation(
                [("2a g AKK", "1a g AKK"),
                 ("2a g AKKs", "1a g AKKs"),
                 ("2a g DAT", "1a g DAT"),
                 ("2a g DATs", "1a g DATs")
                 ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g AKKs", "2a g AKKs"),
             ("3a g DAT", "1a g DAT"),
             ("3a g DATs", "1a g DATs")
             ])


        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g DATs", "2a g DATs")
             ])


        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g AKKs", "2a g AKKs"),
             ("1a g DAT", "2a g DAT"),
             ("1a g DATs", "2a g DATs")
             ])


        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("1a g AKKs", "2a g AKKs"),
             ("1a g DAT", "2a g DAT"),
             ("1a g DATs", "3a g DATs")
             ])



        self.add_pers_perm_variation(
                [("3s g AKK", "1s g AKK"),
                 ("3s g PROP", "1s g PROP")])

        self.add_pers_perm_variation(
                [("3s g AKK", "1s g AKK")])


        self.add_pers_perm_variation(
                [("3s g DAT", "2s g DAT"),
                 ("3s g DATs", "2s g DATs")])


        self.add_pers_perm_variation(
                [("3s g PROP", "2s g PROP")])


        self.add_pers_perm_variation(
                [("1s g DAT", "2s g DAT"),
                 ("1s g AKKs", "2s g AKKs"),
                 ("1s g PROP", "2s g PROP")])


        self.add_pers_perm_variation(
                [("1s g DAT", "2s g DAT"),
                 ("1s g DATs", "2s g DATs")])


        self.add_pers_perm_variation(
                [("1s g DAT", "2s g DAT"),
                 ("2s g AKK", "3s g AKK"),
                 ("1s g PROP", "3s g PROP")])

        self.add_pers_perm_variation(
                [("1s f DAT", "2s f DAT"),
                 ("1s f AKKs", "2s f AKKs"),
                 ("1s f PROP", "2s f PROP")])

        self.add_pers_perm_variation(
                [("1s g AKK", "2s g AKK"),
                 ("1s g PROP", "2s g PROP"),
                 ("2d g AKK", "1d g AKK"),
                 ("2d g PROP", "1d g PROP")])


        self.add_pers_perm_variation(
                [("2p g AKK", "1p g AKK"),
                 ("2p g PROP", "1p g PROP"),
                 ("2d g AKK", "1d g AKK"),
                 ("2d g PROP", "1d g PROP")])


        self.add_pers_perm_variation(
                [("2p g AKK", "1p g AKK"),
                 ("2p g PROP", "1p g PROP"),
                 ("2p g AKKs", "1p g AKKs"),
                 ("2d g AKK", "1d g AKK"),
                 ("2d g PROP", "1d g PROP"),
                 ("2d g AKKs", "1d g AKKs")])



        self.add_pers_perm_variation(
                [("2p g AKK", "1p g AKK"),
                 ("2p g PROP", "1p g PROP"),
                 ("2p g AKKs", "1p g AKKs")])




        self.add_pers_perm_variation(
                [("1s f DAT", "2s f DAT"),
                 ("1s f DATs", "2s f DATs")])


        self.add_pers_perm_variation(
                [("1s m DAT", "2s m DAT"),
                 ("2s n AKK", "3s n AKK"),
                 ("1s f PROP", "3s f PROP")])


        self.add_pers_perm_variation(
                [("1s g DAT", "2s g DAT"),
                 ("2s g AKK", "3s g AKK"),
                 ("1s g PROP", "3s g PROP")])



        self.add_pers_perm_variation(
              [("1p g DAT", "2p g DAT"),
               ("1d g DAT", "2d g DAT")])


        self.add_pers_perm_variation(
              [("1p g AKK", "2p g AKK"),
               ("1d g AKK", "2d g AKK")])


        self.add_pers_perm_variation(
              [("1p g AKK", "2p g AKK"),
               ("1d g AKK", "2d g AKK"),
               ("1p g DAT", "2p g DAT"),
               ("1d g DAT", "2d g DAT"),
               ("1p g PROP", "2p g PROP"),
               ("1d g PROP", "2d g PROP")
               ])


        self.add_pers_perm_variation(
              [("1p g DATs", "2p g DATs"),
               ("1d g DATs", "2d g DATs"),
               ("1p g DAT", "2p g DAT"),
               ("1d g DAT", "2d g DAT")
               ])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT"),
             ("3p g PROP", "2p g PROP"),
             ("3d g PROP", "2d g PROP")
             ])

        self.add_pers_perm_variation(
            [("1p g DATs", "3p g DATs"),
             ("1d g DATs", "3d g DATs"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT")
             ])


        self.add_pers_perm_variation(
            [("1p g DATs", "3p g DATs"),
             ("3p g DAT", "2p g DAT")
             ])


        self.add_pers_perm_variation(
            [("3p g AKK", "2p g AKK"),
             ("3d g DAT", "1d g DAT")
             ])


        self.add_pers_perm_variation(
            [("1p g NOM", "2p g NOM"),
             ("1d g NOM", "2d g NOM"),
             ("1p g DATs", "2p g DATs"),
             ("1d g DATs", "2d g DATs"),
             ("1p g AKKs", "2p g AKKs"),
             ("1d g AKKs", "2d g AKKs")
             ])


        self.add_pers_perm_variation([
             ("1s g DATs", "2s g DATs")
             ])

        self.add_pers_perm_variation([
             ("2s g DATs", "3s g DATs")
             ])

        self.add_pers_perm_variation([
             ("2s g DATs", "3s g DATs"),
             ("2s g AKKs", "3s g AKKs")
             ])



        self.add_pers_perm_variation(
            [("1p m NOM", "2p m NOM"),
             ("1d f NOM", "2d f NOM"),
             ("1p n DATs", "2p n DATs"),
             ("1d n DATs", "2d n DATs"),
             ("1p f AKKs", "2p f AKKs"),
             ("1d m AKKs", "2d m AKKs")
             ])


        self.add_pers_perm_variation(
            [("1p m NOM", "2p m NOM"),
             ("1d m NOM", "2d m NOM"),
             ("1p n DATs", "2p n DATs"),
             ("1d n DATs", "2d n DATs"),
             ("1p f AKKs", "2p f AKKs"),
             ("1d f AKKs", "2d f AKKs")
             ])

        self.add_pers_perm_variation(
            rotate_right_list=
        [("1p g PROP", "2p g PROP", "3p g PROP")]
             )

        #print(self.pers_perm_count)

    def _create_permutation_NUM_files(self):
        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM")])

        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK")])


        for c in ["DAT","DATs","AKKs", "PROP"]:
            self.add_num_perm_variation(
                [("2d g "+c, "2p g "+c)])

            self.add_num_perm_variation(
                [("2d g "+c, "2p g "+c),
                 ("1d g "+c, "1p g "+c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("3d g " + c, "3p g " + c)])

            self.add_num_perm_variation(
                [("1d g " + c, "1p g " + c),
                 ("3d g " + c, "3p g " + c)])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("2d g DATs", "2p g DATs")])


        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g DATs", "3p g DATs")])


        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g DATs", "3p g DATs"),
             ("1d g AKKs", "1p g AKKs")])



        self.add_num_perm_variation(
            [("2d m DAT", "2p m DAT"),
             ("3d f DAT", "2p f DAT"),
             ("3d n DATs", "3p n DATs"),
             ("1d m DATs", "1p m DATs"),
             ("1d f AKKs", "1p f AKKs"),
             ("2d n AKKs", "2p n AKKs")
             ])




        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM"),
             ("2s g AKK", "2p g AKK"),
             ("1s g DAT", "1d g DAT"),
             ("2s g PROP", "2d g PROP")])


        self.add_num_perm_variation(
            [("3s m NOM", "3p m NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3d n DAT")])


        self.add_num_perm_variation(
            [("3s m NOM", "3d m NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3p n DAT")])


        self.add_num_perm_variation(
            [("3s f NOM", "3d f NOM"),
             ("3s m AKKs", "3p m AKKs"),
             ("3s n DAT", "3p n DAT")])



        self.add_num_perm_variation(
            [("3p f NOM", "3d f NOM"),
             ("3s f AKKs", "3p f AKKs"),
             ("3d n DAT", "3p n DAT")])



        self.add_num_perm_variation(
            [("3p m NOM", "3d m NOM"),
             ("3s m AKKs", "3p m AKKs"),
             ("3d n DAT", "3p n DAT")])



        self.add_num_perm_variation(
            [("3p m NOM", "3d m NOM"),
             ("3s m AKKs", "3p m AKKs"),
             ("3s n DATs", "3p n DATs"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM")])


        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")],
        rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM")])



        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s m PROP", "3d m PROP", "3p m PROP"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ])



        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s m PROP", "3d m PROP", "3p m PROP"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ],
        rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM"),
                           ("3s f AKK", "3d f AKK", "3p f AKK")])



        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m NOM", "3d m NOM", "3p m NOM"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("3s m PROP", "3d m PROP", "3p m PROP"),
             ("1s n DAT", "1d n DAT", "1p n DAT")
             ])


        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m DAT", "3d m DAT", "3p m DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("2s m AKK", "2d m AKK", "2p m AKK"),
             ])


        self.add_num_perm_variation(
            rotate_left_list=
            [("3s m DAT", "3d m DAT", "3p m DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT")],
        rotate_right_list =[
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("2s m AKK", "2d m AKK", "2p m AKK")
             ])


        self.add_num_perm_variation(
            rotate_left_list=
            [("2s g DAT", "2d g DAT", "2p g DAT"),
             ("3s f DAT", "3d f DAT", "3p f DAT")],
        rotate_right_list =[
             ("1s g AKK", "1d g AKK", "1p g AKK"),
             ("3s f AKK", "3d f AKK", "3p f AKK")
             ])

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"),("1s g DAT", "1p g DAT"),("1d g PROP", "1p g PROP"),
                ("1s g AKK", "1d g AKK"),("2s g DAT", "2d g DAT"),("2s g PROP", "2d g PROP"),
                ("3s g AKK", "3p g AKK"),("3d g DAT", "3p g DAT"),("3s g PROP", "3p g PROP"),
                ("2p g AKKs", "2d g AKKs"), ("1s g DATs", "1d g DATs"),
                ("1p g AKKs", "1d g AKKs"), ("2s g DATs", "2d g DATs"),
                ("3p g AKKs", "3d g AKKs"), ("3s g DATs", "3d g DATs")
             ]
        )

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g PROP", "1p g PROP"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g PROP", "2d g PROP"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g PROP", "3p g PROP"),
                ("2p g AKKs", "2d g AKKs"), ("1s g DATs", "1d g DATs"),
                ("1p g AKKs", "1d g AKKs"), ("2s g DATs", "2d g DATs"),
                ("3p g AKKs", "3d g AKKs"), ("3s g DATs", "3d g DATs")
            ]
        )
        self.add_num_perm_variation(
            rotate_left_list = [
                ("1s g PROP","1d g PROP","1p g PROP"),
                ("2s g AKK", "2d g AKK", "2p g AKK"),
                ("3s n DATs","3d n DATs","3p n DATs"),
            ],
            rotate_right_list = [
                ("2s g PROP", "2d g PROP", "2p g PROP"),
                ("1s g DAT","1d g DAT","1p g DAT"),
                ("3s m DATs","3d m DATs","3p m DATs"),
            ]
        )


    def _create_permutation_GEN_files(self):

        self.add_gen_perm_variation(
            rotate_right_list=
        [
         ("3s m PROP", "3s f PROP", "3s n PROP")],
             )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m DATs", "3s f DATs", "3s n DATs")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m DATs", "3s f DATs", "3s n DATs")],
            rotate_left_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK"),
                ("3s m AKKs", "3s f AKKs", "3s n AKKs")],
        )


###

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT"),
                ("3s m AKKs", "3s f AKKs", "3s n AKKs")],
        )


        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKKs", "3s f AKKs", "3s n AKKs")],
            rotate_left_list=
            [
                ("3s m DAT", "3s f DAT", "3s n DAT")],
        )

        self.add_gen_perm_variation(
                [("3s m DAT", "3s f DAT"),
                 ("3s m AKKs", "3s f AKKs")
                 ])


        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK"),
                ("3s m PROP", "3s f PROP", "3s n PROP"),
                ("3s m AKKs", "3s f AKKs", "3s n AKKs"),],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKK", "3s f AKK", "3s n AKK")],
            rotate_left_list=
            [
                ("3s m PROP", "3s f PROP", "3s n PROP"),
                ("3s m AKKs", "3s f AKKs", "3s n AKKs")],
        )


        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("2s m DAT", "2s f DAT", "2s n DAT"),
                ("2s m AKKs", "2s f AKKs", "2s n AKKs")],
            rotate_left_list=
            [
                ("1s m PROP", "1s f PROP", "1s n PROP"),
                ("1s m AKKs", "1s f AKKs", "1s n AKKs")],
        )


        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s m AKKs", "3s f AKKs", "3s n AKKs")],
            rotate_left_list=
            [
                ("3s m PROP", "3s f PROP", "3s n PROP"),
                ("3s m AKK", "3s f AKK", "3s n AKK")],
        )

        self.add_gen_perm_variation(
                [("3s m AKK", "3s f AKK"),
                 ("3s m PROP", "3s f PROP"),
                 ("3s m AKKs", "3s f AKKs")
                 ])


        for g in ["m","n"]:
            self.add_gen_perm_variation(
                                    [("3s "+g+" AKK","3s f AKK"),
                                     ("3s "+g+" DATs","3s f DATs")])
            self.add_gen_perm_variation(
                                    [("3s "+g+" AKK","3s f AKK"),
                                     ("3s "+g+" AKKs","3s f AKKs")])
            self.add_gen_perm_variation(
                                    [("3s "+g+" AKK","3s f AKK"),
                                     ("3s "+g+" AKKs", "3s f AKKs"),
                                     ("3s "+g+" DAT", "3s f DAT"),
                                     ("3s "+g+" DATs","3s f DATs")])
            self.add_gen_perm_variation(
                                    [("3s "+g+" NOM","3s f NOM")])
            self.add_gen_perm_variation(
                                    [("3s "+g+" AKK","3s f AKK"),
                                     ("3s "+g+" PROP","3s f PROP")])

            self.add_gen_perm_variation(
                                    [("3s "+g+" AKK","3s f AKK"),
                                     ("3s "+g+" PROP","3s f PROP")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s m NOM", "2s f NOM"),
             ("1s m AKK", "1s f AKK"),
             ("3s m DATs", "3s f DATs"),
             ("1s m AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n AKKs", "3s f AKKs"),
             ("3p m DATs", "3p f DATs"),
             ("3s n NOM", "3s m NOM"),
             ("3d m PROP", "3d f PROP")])

        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s n NOM", "2s f NOM"),
             ("1s m PROP", "1s f PROP"),
             ("3s m DATs", "3s n DATs"),
             ("1s m AKK", "1s f AKK")])


        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n AKKs", "3s n AKKs"),
             ("3p m DATs", "3p f DATs"),
             ("3s n NOM", "3s m NOM"),
             ("3d m PROP", "3d f PROP"),
             ("2s m AKK", "2s f AKK"),
             ("2d n DAT", "2d f DAT"),
             ("2s n AKKs", "2s f AKKs"),
             ("1p m DATs", "1p f DATs"),
             ("1s n NOM", "1s m NOM"),
             ("1d m PROP", "1d f PROP")
             ])



        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n AKKs", "3s n AKKs"),
             ("3p m DATs", "3p f DATs"),
             ("3s n NOM", "3s m NOM"),
             ("3d m PROP", "3d f PROP"),
             ("2s f AKK", "2s n AKK"),
             ("2d n DAT", "2d m DAT"),
             ("2s n AKKs", "2s m AKKs"),
             ("1p n DATs", "1p f DATs"),
             ("1s f NOM", "1s m NOM"),
             ("1d m PROP", "1d f PROP")
             ])



        self.add_gen_perm_variation(
            [
             ("2s f AKK", "2s n AKK"),
             ("2d n DAT", "2d m DAT"),
             ("2p n AKKs", "2p m AKKs"),
             ("1p n DATs", "1p f DATs"),
             ("1s f NOM", "1s m NOM"),
             ("1d m PROP", "1d f PROP"),
                ("2s f DAT", "2s n DAT"),
                ("2d n PROP", "2d m PROP"),
                ("2p n NOM", "2p m NOM"),
                ("1p n PROP", "1p f PROP"),
                ("1s f AKKs", "1s m AKKs"),
                ("1d m NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d n DATs", "2d m DATs"),
                ("2p n PROP", "2p m PROP"),
                ("1p n AKK", "1p f AKK"),
                ("1s f PROP", "1s m PROP"),
                ("1d m DATs", "1d f DATs")
             ])



        self.add_gen_perm_variation(
            [
             ("2s f AKKs", "2s n AKKs"),
             ("2d n AKK", "2d m AKK"),
             ("2p n AKKs", "2p m AKKs"),
             ("1p n DATs", "1p f DATs"),
             ("1s f NOM", "1s m NOM"),
             ("1d m PROP", "1d f PROP"),
                ("2s f DATs", "2s n DATs"),
                ("2d n PROP", "2d f PROP"),
                ("2p n NOM", "2p f NOM"),
                ("1p n PROP", "1p f PROP"),
                ("1s f AKKs", "1s n AKKs"),
                ("1d n NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d f DATs", "2d m DATs"),
                ("2p f PROP", "2p m PROP"),
                ("1p n AKK", "1p f AKK"),
                ("1s n PROP", "1s m PROP"),
                ("1d m DATs", "1d f DATs")
             ])



        self.add_gen_perm_variation(
            [("3s m AKK", "3s f AKK"),
             ("2s f AKK", "2s n AKK"),("2d m AKK", "2d n AKK"),("2p f AKK", "2p m AKK"),
             ("2s m DAT", "2s n DAT"),("1d f DAT", "1d n DAT"),("1s f DAT", "1s m DAT"),
             ("1d m DATs","1d n DATs"),("3d m DATs","3d f DATs"),("2p m DATs","2p f DATs"),
             ("2s m AKKs", "2s n AKKs"),("1d f AKKs", "1d n AKKs"),("1s f AKKs", "1s m AKKs")])

        self.add_gen_perm_variation(
            rotate_right_list=
                [("3p m AKK", "3p f AKK", "3p n AKK"),
                 ("3s m DAT", "3s f DAT", "3s n DAT")],
            rotate_left_list =
                [("3d m NOM", "3d f NOM", "3d n NOM"),
                 ("3s m DATs", "3s f DATs", "3s n DATs")]
        )

    def _create_permutation_TENSE_files(self):
        self.add_ten_perm_variation(
            [("za g NOM", "za g DATs")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g DATs"),
             ("za g DAT", "za g PROP")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g DATs"),
             ("za g DAT", "za g PROP"),
             ("za g AKKs", "za g NOM")])

        self.add_ten_perm_variation(
            rotate_left_list = [
                ("1p g AKK", "1p g PROP", "1p g AKKs"),
                ("1d g AKK", "1d g PROP", "1d g AKKs")],
                rotate_right_list = [
                ("2d g AKK", "2d g PROP", "2d g AKKs"),
                ("2d g AKK", "2d g PROP", "2d g AKKs")])


        self.add_ten_perm_variation(
           [
                ("1p g AKK", "1p g PROP"),
                ("1d g AKK", "1d g PROP"),
                ("2d g AKK", "2d g AKKs"),
                ("2d g AKK","2d g AKKs")])


        self.add_ten_perm_variation(
            [
                ("1p g PROP", "1p g AKKs"),
                ("1d g PROP", "1d g AKKs"),
                ("2d g AKK", "2d g AKKs"),
                ("2d g AKK", "2d g AKKs"),
                ("1s g AKK", "1s g PROP")
            ])


        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m PROP"),
                ("1d g AKK", "1d g PROP"),
                ("1p g AKK", "1p g PROP"),
                ("2s g AKK", "2s g PROP")
            ])
###


        self.add_ten_perm_variation(
            rotate_left_list = [
                ("1p g AKK", "1p g DATs", "1p g AKKs"),
                ("1d g AKK", "1d g DATs", "1d g AKKs")],
                rotate_right_list = [
                ("2d g AKK", "2d g PROP", "2d g DATs"),
                ("2d g AKK", "2d g PROP", "2d g DATs")])


        self.add_ten_perm_variation(
           [
                ("1p g NOM", "1p g PROP"),
                ("1d g NOM", "1d g PROP"),
                ("2d g AKK", "2d g DATs"),
                ("2d g AKK","2d g DATs")])


        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g AKKs"),
                ("1d g NOM", "1d g AKKs"),
                ("2d g AKK", "2d g DATs"),
                ("2d g AKK", "2d g DATs"),
                ("1s g AKK", "1s g NOM")
            ])


        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m DATs"),
                ("1d g AKK", "1d g DATs"),
                ("1p g AKK", "1p g DATs"),
                ("2s g AKK", "2s g DATs")
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m AKKs"),
                ("1s g DAT", "1s g AKKs"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m AKKs"),
                ("3s n DAT", "3s n AKKs"),
            ])


        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g AKKs"),
                ("2s g DAT", "2s g AKKs"),
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s m PROP", "3s m AKKs"),
                ("1s g PROP", "1s g AKKs"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m AKK", "3s m AKKs"),
                ("1s g AKK", "1s g AKKs"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s m AKKs", "3s m AKK"),
                ("3s n AKKs", "3s n AKK"),
            ])
        self.add_ten_perm_variation(
            [
                ("3s m DAT", "3s m AKK"),
                ("3s n DAT", "3s n AKK"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g DATs"),
                ("2s g DAT", "2s g DATs"),
            ])

###

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g DATs"),
             ("zp g AKK", "zp g DATs"),
             ("zs g DAT", "zs g PROP"),
             ("zs g AKKs", "zs g NOM")])


        self.add_ten_perm_variation(
            [("3p g PROP", "3p g DATs")])


        self.add_ten_perm_variation(
            [("3p g DAT", "3p g DATs"),
             ("3d g DAT", "3d g DATs")])


        self.add_ten_perm_variation(
            [("3p g PROP", "3p g DAT"),
             ("2p g PROP", "2p g DATs")])


        self.add_ten_perm_variation(
            [("3p g PROP", "3p g DATs"),
             ("1p g PROP", "1p g DAT")])



        self.add_ten_perm_variation(
            [("3p g PROP", "3p g DAT"),
             ("2p g PROP", "2p g DATs"),
             ("3d g PROP", "3d g DAT"),
             ("2d g PROP", "2d g DATs")
             ])


        self.add_ten_perm_variation(
            [("3p g PROP", "3p g DATs"),
             ("1p g PROP", "1p g DAT"),
             ("3d g PROP", "3d g DATs"),
             ("1d g PROP", "1d g DAT")
             ])

        self.add_ten_perm_variation(
            [("1s g DATs", "1s g DAT"),
             ("2s g DATs", "2s g PROP"),
             ])


        self.add_ten_perm_variation(
            [("1s g DATs", "1s g DAT"),
             ("2s g DATs", "2s g PROP"),
             ("3s f DATs", "3s f AKKs"),
             ])



        self.add_ten_perm_variation(
            [("1s g DATs", "1s g DAT"),
             ("2s g DATs", "2s g PROP"),
             ("1d g DAT", "1d g PROP"),
             ("2p g DATs", "2p g AKKs"),
             ])



        self.add_ten_perm_variation(
            [("1s g DATs", "1s g DAT"),
             ("2s g DATs", "2s g PROP"),
             ("1d g DAT", "1d g PROP"),
             ("2p g DATs", "2p g AKKs"),
             ("3d g AKKs", "3d g PROP"),
             ("3p g DAT", "3p g DATs"),
             ])



        self.add_ten_perm_variation(
            [("zd g AKK", "zd g AKKs"),
             ("zp g AKK", "zp g AKKs"),
             ("zs g DAT", "zs g DATs")])


        self.add_ten_perm_variation(
            [("zd m AKK", "zd m AKKs"),
             ("zp f AKK", "zp f AKKs"),
             ("zs n DAT", "zs n DATs")])


        self.add_ten_perm_variation(
            [("1a g NOM", "1a g DATs")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g DATs")])


        self.add_ten_perm_variation(
            [("1a g AKK", "1a g DAT")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g PROP")])


        self.add_ten_perm_variation(
            [("1a g NOM", "1a g DAT"),
             ("3a g NOM", "3a g AKK"),
             ("1a g NOM", "1a g PROP")])


        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g NOM", "1a g AKK"),
             ("2a g NOM", "2a g PROP")])


        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g AKKs", "1a g AKK"),
             ("3a g NOM", "3a g PROP")])


        self.add_ten_perm_variation(
            [("2a g DATs", "2a g DAT"),
             ("1a g AKKs", "1a g AKK"),
             ("3a f NOM", "3a f PROP")])


        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])


        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])


        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT"),
             ("1s g AKKs", "1s g DATs")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("2p g AKKs", "2p g DATs"),
             ("2d g AKKs", "2d g DATs")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2s g AKKs", "2s g DATs"),
             ("1p g AKKs", "1p g DATs"),
             ("1d g AKKs", "1d g DATs")
             ])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2p g AKKs", "2p g DATs"),
             ("2d g AKKs", "2d g DATs"),
             ("1p g AKKs", "1p g DATs"),
             ("1d g AKKs", "1d g DATs")
             ])

        self.add_ten_perm_variation(
            [("1s g DAT", "1s g DATs")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g DATs")])


        self.add_ten_perm_variation(
            [("2s g DAT", "2s g DATs"),
             ("1s g AKK", "1s g AKKs")])


        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s n DAT", "3s n DATs"),
             ("3s f AKK", "3s f AKKs")])


        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s n DAT", "3s n DATs"),
             ("3s f AKK", "3s f AKKs"),
             ("2p g NOM", "2p g PROP"),
             ("2d g AKK", "2d g AKKs")
        ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s n DAT", "3s n DATs"),
             ("3s f AKK", "3s f AKKs"),
             ("2p m NOM", "2p m PROP"),
             ("2d n AKK", "2d n AKKs")
             ])


        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s f DAT", "3s f DATs"),
             ("3s n AKK", "3s n AKKs"),
             ("2p m NOM", "2p m PROP"),
             ("2d n AKK", "2d n DAT")
             ])


        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s f DAT", "3s f DATs"),
             ("3s n AKK", "3s n AKKs"),
             ("2p g NOM", "2p g PROP"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g DATs"),
             ("2p g NOM", "2p g AKKs")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3s f DAT", "3s f DATs"),
             ("3s n AKK", "3s n AKKs"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g DAT"),
             ("2p g NOM", "2p g AKK")
             ])

        self.add_ten_perm_variation(
            [("3s m DAT", "3s m DATs"),
             ("3p f DAT", "3p f DATs"),
             ("3d n AKK", "3d n AKKs"),
             ("2d m AKK", "2d m DAT"),
             ("1d f NOM", "1d f DAT"),
             ("2p n NOM", "2p n AKK")
             ])


        self.add_ten_perm_variation(
            [("1s m NOM", "3s m DATs"),
             ("2p f NOM", "3p f AKKs"),
             ("2d n NOM", "3d n PROP"),
             ("2d m NOM", "2d m DAT"),
             ("1d f NOM", "1d f AKK"),
             ])


        self.add_ten_perm_variation(
            [("3a g AKK", "3a g PROP")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g PROP")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g PROP"),
             ("1a g AKK", "1a g PROP")])


        self.add_ten_perm_variation(
            [("zs g AKK", "zs g PROP")])


        self.add_ten_perm_variation(
            [("zp g AKK", "zp g PROP"),
             ("zd g AKK", "zd g PROP")])


        self.add_ten_perm_variation(
            rotate_left_list =
            [("1p g AKK", "1p g PROP", "1p g DAT")],
            rotate_right_list =
            [("2p g AKK", "2p g PROP", "2p g DAT")]
        )

        self.add_ten_perm_variation(
            rotate_left_list =
            [("1p g AKK", "1p g PROP", "1p g DAT"),
             ("3p m AKKs", "3p m NOM", "3p m DATs")],
            rotate_right_list =
            [("2p g AKK", "2p g PROP", "2p g DAT"),
             ("3p n AKKs", "3p n NOM", "3p n DATs")]
        )

    def _create_permutation_X_files(self):
        self.add_xross_perm_variation(
            [("3p g AKKs", "2s g AKKs")])

        self.add_xross_perm_variation(
            [("3s m DATs", "3s n PROP"),
             ("2s m DAT", "3s n AKKs")])

        self.add_xross_perm_variation(
            [("3p f NOM", "3p n AKK")])


        self.add_xross_perm_variation(
            [("3d f AKK", "3s n NOM"),
             ("3d n AKK", "3s f NOM")])


        self.add_xross_perm_variation(
        [("3s n AKK", "3p f NOM"),
         ("2d g AKK", "1s g NOM")])


        self.add_xross_perm_variation(
            [("3s m DATs", "3s m PROP"),
             ("2s n DAT", "3s n AKKs")])

        self.add_xross_perm_variation(
            rotate_right_list=
        [("1p g PROP", "2p g PROP", "3p g PROP"),
         ("3s m PROP", "3s f PROP", "3s n PROP")],
             )

        self.add_xross_perm_variation(
            [("1p g DAT", "2p g PROP")]
        )

        self.add_xross_perm_variation(
            [("3s n AKK", "3s n AKKs"),
             ("3s n AKK", "3s n DATs")])

        self.add_xross_perm_variation(
        [("2s g NOM", "3p g DATs"),
         ("2s g NOM", "2p g AKKs")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g DATs")])


        self.add_xross_perm_variation(
            [("rs g PROP", "rp g DATs")])


        self.add_xross_perm_variation(
            [("rd g PROP", "rp g DATs")])


        self.add_xross_perm_variation(
            [("rs m PROP","3p m AKKs"),
             ("rp f PROP","3p f AKKs"),
             ("rd n PROP","3p n AKKs")])



        self.add_xross_perm_variation(
            [("rs m PROP","3p m AKKs"),
             ("rp f PROP","3p f AKKs"),
             ("rd n PROP","3p n AKKs"),

             ("rs m DATs", "3d m DAT"),
             ("rp f DATs", "3d f DAT"),
             ("rd n DATs", "3d n DAT")
             ])

        self.add_xross_perm_variation(
            [("rs m PROP", "3p m AKKs"),
             ("rp f PROP", "3p f AKKs"),
             ("rd n PROP", "3p n AKKs"),

             ("rs m DATs", "3d m DAT"),
             ("rp f DATs", "3d f DAT"),
             ("rd n DATs", "3d n DAT"),

             ("rs m DAT", "3p m DATs"),
             ("rp f DAT", "3p f DATs"),
             ("rd n DAT", "3p n DATs"),

             ("rs m AKKs", "3d m PROP"),
             ("rp f AKKs", "3d f PROP"),
             ("rd n AKKs", "3d n PROP")
             ])


        self.add_xross_perm_variation(
            [("1s g DAT", "1s g DATs"),
             ("3s f DAT", "3s m DAT"),
             ("3s f DATs", "3s m DATs")])


        self.add_xross_perm_variation(
            [("3s g NOM", "2p g DATs"),
             ("3s m PROP", "2p f DAT"),
             ("3s n PROP", "1s f NOM"),
             ("3s f DAT", "1p f NOM")])




        self.add_xross_perm_variation(
            [("1s g NOM", "2p g DATs"),
             ("2s g DAT", "2s g AKKs"),
             ("2s g AKK", "1p g DATs"),
             ("1p g PROP", "1s g AKKs"),
             ("2p g DAT", "2s g DATs"),
             ("3p g NOM", "1d g DATs"),
             ("1d g AKK", "3d g AKKs"),
             ("2d g PROP", "3p g DATs"),
             ("3d g NOM", "1d g AKKs")])


        self.add_xross_perm_variation(
            [("1p g AKK", "2p g AKKs"),
             ("1d g AKK", "2d g AKKs"),
             ("1s g DAT", "2s g DATs"),
             ("3s m AKK", "3s n DAT"),
             ("3s m NOM", "3s n DATs")])



        self.add_xross_perm_variation(
            [
                 ("1s f NOM","2s n NOM"),("2s m PROP","1s m DAT"),("2s n DAT","1s m AKK"),
                 ("1s n PROP","1s f DAT"),("1p f PROP","1p m PROP"),("2s n PROP","2s f PROP"),
                 ("1p f DAT","1p m DAT"),("1s m PROP","1s n DAT"),("2p f AKK","2s m AKK"),
                 ("2s f DAT","2p m AKK"),("1p n DAT","2p n PROP"),("1s n NOM","1s m NOM"),
                 ("2s f NOM","1p n NOM"),("1s f AKK","1p m AKK"),("1p f NOM","1p m NOM"),
                 ("1p f AKK","2s m NOM"),("2s n AKK","2s f AKK"),("1p n AKK","1s n AKK"),
                 ("1p n PROP","1s f PROP"),("2p f NOM","2s m DAT"),("2p f DAT","2p n DAT"),
                 ("2p n NOM","2p m DAT"),("2p m PROP","2p m NOM"),("2p f PROP","2p n AKK")
             ])



        self.add_xross_perm_variation(
            [
                ("1s m AKK","2p m NOM"), ("1s f PROP","1s f NOM"), ("1s m PROP","2p m DAT"),
                ("1s n DAT","2p m AKK"),("2s f AKK","1s n PROP"),("1p m DAT", "1p n DAT"),
                ("2s m AKK","1s f DAT"), ("2s n PROP","1s m NOM"), ("1p m NOM", "1p f NOM"),
                ("2s m NOM", "2s m DAT"), ("2s m PROP", "1p m PROP"), ("2p m PROP", "2p f PROP"),
                ("2s f DAT","2s n NOM"), ("2s n AKK","2p f AKK"), ("1p n PROP", "2s n DAT"),
                ("2p n AKK","2s f NOM"), ("1s f AKK","1s n NOM"), ("1s m DAT","1s n AKK"),
                ("1p n NOM","2p n NOM"), ("1p f AKK","2s f PROP"), ("1p f DAT","1p f PROP"),
                ("2p n PROP","1p m AKK"), ("2p f DAT","2p n DAT"), ("2p f NOM","1p n AKK"),
            ])


        self.add_xross_perm_variation(
            [
                ("1s m AKK", "1s f AKK"),("1p f DAT", "1p n DAT"),("1p n PROP","2p n AKK"),
                ("1s m NOM", "2s m AKK"),("2p f AKK", "1p f NOM"),("1s f PROP", "1s n PROP"),
                ("1p n AKK", "2s n NOM"),("2s f NOM", "1p f AKK"),("2p f PROP", "2p n PROP"),
                ("1p m NOM", "1s f DAT"),("1s n DAT", "2p m AKK"),("2p f NOM", "2p n NOM"),
                ("1s n NOM", "1s m DAT"),("1p n NOM", "2s f DAT"), ("2s n DAT", "1s f NOM"),
                ("2s m DAT", "2p m NOM"),("1s m PROP", "1p m DAT"), ("1s n AKK", "2p m PROP"),
                ("1p f PROP", "2p f DAT"),("2s m NOM", "2p m DAT"),("2s f AKK", "2s n AKK"),
                ("2s m PROP",  "2p n DAT"),("1p m PROP", "2s f PROP"),("2s n PROP", "1p m AKK")
            ])



        self.add_xross_perm_variation(
            [("1p n PROP",  "3s n NOM"), ("3p m AKK", "1p n AKK"), ("3s n PROP", "2s n DAT"),
             ("2s m DAT", "2s f DAT"), ("2p f DAT", "1s n AKK"), ("1p m AKK", "2p n AKK"),
             ("1s f NOM",  "1s n DAT"), ("3s n AKK", "2s f NOM"), ("3p n NOM", "2s f PROP"),
             ("2p n DAT", "2p m NOM"), ("3s m NOM", "2s n AKK"), ("2p n PROP", "1p m PROP"),
             ("1s m AKK", "3p n PROP"), ("1p f NOM", "2s n PROP"), ("1s f DAT", "3s f DAT"),
             ("2s m PROP", "1p f AKK"),("1s m DAT", "2s n NOM"),("2p m DAT", "2s m NOM"),
             ("2p m AKK", "2p f AKK"),("1p n NOM", "3p f PROP"),("1p m DAT", "3p n DAT"),
             ])


        self.add_xross_perm_variation(
            [
                ("1s n AKKs", "1s m DATs"), ("2s m DATs", "1s m NOM"), ("3s f DATs","3s f AKKs"),
                ("1s m AKK","1s n DAT"), ("1p n PROP","2s m PROP"), ("3s m AKKs","1s f AKK"),
                ("2s f DATs", "3s m NOM"), ("2s f PROP", "3s n NOM"), ("1s f NOM","2p m DATs"),
                ("2p n DAT","2s n DATs"), ("2p n PROP", "2s m NOM"), ("1s n NOM","2p f DAT"),
                ("1p f DAT","1p m DAT"), ("3s n PROP","3p n DAT"), ("1p n DAT","2s f NOM"),
                ("2s n PROP","2p m PROP"), ("2p f PROP","2s n NOM"), ("3s f NOM", "3s n AKKs"),
        ("3p n PROP","3p n AKK"),("1p m PROP","3p f DATs"),("1p f AKKs","3p f NOM"),
        ("3s m DAT","3s n DATs"),("1p n AKK","3p m NOM"),("3p n NOM", "1p n NOM"),
        ("3s f PROP","1p f PROP"),("1p m AKK","3p m DATs"),("1p m NOM", "1p f NOM"),
                ("1s f DATs", "3s m PROP"),
            ]
        )



        self.add_xross_perm_variation(
            [
                ("2p g AKK", "2p g PROP"), ("1p g AKK", "2p g NOM"),
                ("1p g DAT", "2p g DAT"), ("1p g PROP", "1p g NOM"),
                ("3s f DAT",  "3p f AKK"),("3p m AKK", "3p f DAT"),("3s m DAT", "3p n AKK"),
                ("3s n AKK",  "3p n NOM"),("3s n PROP", "3p n PROP"),("3s f DAT", "3s n DAT")
            ])





        self.add_xross_perm_variation(
            [
                ("3s m PROP", "3p f DAT"),("3p n DAT", "3s f PROP"),("3s f DAT", "3s f AKK"),
                ("3s n NOM", "3s m DAT"),("3s m AKK","3p m DAT"),("3s f NOM", "3p m NOM"),
                ("3p m PROP", "3p f PROP"),("3p f NOM","3p n AKK"),("3s n AKK", "3s m NOM"),
                ("3p m AKK", "3p n PROP"),("3p f AKK", "3p n NOM"),("3s n DAT", "3s n PROP")
            ]
        )


        self.add_xross_perm_variation(
            [
                ("3s g PROP","2s g NOM"),("2s g PROP", "1p g PROP"),("3s g DAT","1s g AKK"),
                ("2s g DAT","2p g PROP"),("3s g NOM", "1p g DAT"),("2s g AKK", "2p g AKK"),
                ("2p g NOM", "2p g DAT"),("3p g NOM",  "1s g PROP"),("1p g AKK",  "1p g NOM"),
                ("1s g DAT", "3p g DAT"),("3p g PROP", "1s g NOM"),("3p g AKK", "3s g AKK"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("3a g PROP", "2a g NOM"),
                ("2a g AKK", "1a g DAT"),
                ("1a g DAT", "2a g NOM"),
                ("3a g DAT", "3a g PROP"),
            ]
        )


        self.add_xross_perm_variation(
            [
                ("zd g PROP", "zs g NOM"),
                ("zd g AKKs", "zp g PROP"),
                ("zp g DATs", "zs g NOM"),
            ]
        )


        self.add_xross_perm_variation(
            [
                ("1s g AKKs", "1s g DAT"),
                ("2d g AKKs", "2s g NOM"),
                ("3p g AKKs", "3s g PROP"),
                ("1p g DATs", "2s g DAT"),
                ("2d g DATs", "1s g NOM"),
                ("3p g DATs", "3s g AKK"),
            ]
        )




    def _create_syncretic_PERS_files(self):
        self.add_pers_sync_variation([("1a g AKK", "2a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g DAT", "2a g DAT"), ("1a g PROP", "2a g PROP")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g DAT", "3a g DAT"), ("2a g PROP", "3a g PROP")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g DAT", "1a g DAT"), ("2a g PROP", "1a g PROP")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g DAT", "3a g DAT"), ("1a g PROP", "3a g PROP")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g DAT", "1a g DAT"), ("3a g PROP", "1a g PROP")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g DAT", "2a g DAT"), ("3a g PROP", "2a g PROP")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g PROP", "2a g PROP")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g PROP", "3a g PROP")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g PROP", "1a g PROP")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g PROP", "3a g PROP")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g PROP", "1a g PROP")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g PROP", "2a g PROP")])


        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g AKKs", "2a g AKKs")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g AKKs", "3a g AKKs")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g AKKs", "1a g AKKs")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g AKKs", "3a g AKKs")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g AKKs", "1a g AKKs")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g AKKs", "2a g AKKs")])

        self.add_pers_sync_variation([("1s g AKK", "2s g AKK"),
                                      ("1p g DAT", "2p g DAT"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("3s g PROP", "rs g PROP")])


        self.add_pers_sync_variation([("1s g AKK", "3s g AKK"),
                                      ("2d g DAT", "3d g DAT"),
                                      ("1p g PROP", "2p g PROP")])


        self.add_pers_sync_variation([("1s m AKK", "3s m AKK"),
                                      ("2d f DAT", "3d f DAT")])


        self.add_pers_sync_variation([("1p g AKK", "2p g AKK"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("1s g PROP", "2s g PROP")])


        self.add_pers_sync_variation([("1p g AKKs", "2p g AKKs"),
                                      ("1d g DATs", "2d g DATs")])


        self.add_pers_sync_variation([("2p g AKKs", "3p g AKKs"),
                                      ("2p g DATs", "3p g DATs")])

    def _create_syncretic_NUM_files(self):

        for p in ["1","2","3"]:
            self.add_num_sync_variation([(p+"s g AKKs", p+"p g AKKs")])
            self.add_num_sync_variation([(p+"s g DATs", p+"p g DATs")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g DATs", p+"p g DATs")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g DATs", p+"p g DATs"),
                                         (p + "s g AKK", p + "p g AKK"),
                                         (p + "s g AKKs", p + "p g AKKs")
                                         ])


            self.add_num_sync_variation([(p+"s g AKKs", p+"p m AKKs"),
                                        (p+"s g DATs", p+"p m DATs")])

            self.add_num_sync_variation([(p+"s g AKKs", p+"d m AKKs"),
                                        (p+"s g DATs", p+"d m DATs")])

            self.add_num_sync_variation([(p+"s g t", p+"p g t")])

        self.add_num_sync_variation([("zs g t", "zp g t")])
        self.add_num_sync_variation([("zd g t", "zp g t")])
        self.add_num_sync_variation([("1s g t", "1p g t"),
                                     ("2s g t", "2p g t")])


    def _create_syncretic_GEN_files(self):
        #self.add_gen_sync_variation([("za g t", "za g t")])

        self.add_gen_sync_variation([("za f t", "za m t")])
        self.add_gen_sync_variation([("za n t", "za m t")])

        for p in self.PERSONS:
            self.add_gen_sync_variation([(p+"a f t", p+"a m t")])
            self.add_gen_sync_variation([(p+"a n t", p+"a m t")])

        for n in self.NUMBERS:
            self.add_gen_sync_variation([("z"+n+" f t", "z"+n+" m t")])
            self.add_gen_sync_variation([("z"+n+" n t", "z"+n+" m t")])


        for n in self.NUMBERS:
            for p in self.PERSONS:
                self.add_gen_sync_variation([(p+n+" f t", p+n+" m t")])
                self.add_gen_sync_variation([(p+n+" n t", p+n+" m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t")])
        self.add_gen_sync_variation([("3s n t", "3s m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t")])
        self.add_gen_sync_variation([("3p n t", "3p m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t"),("3s n t", "3s m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t"),("3p n t", "3p m t")])


        self.add_gen_sync_variation([("3s f t", "3s m t"),("3p n t", "3p m t")])
        self.add_gen_sync_variation([("3p f t", "3p m t"),("3s n t", "3s m t")])


        self.add_gen_sync_variation([("3s f AKK", "3s m AKK")])
        self.add_gen_sync_variation([("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3p f PROP", "3p m PROP")])

        self.add_gen_sync_variation([("3s f AKK", "3s m AKK"), ("3s n AKK", "3s m AKK")])
        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3s f PROP", "3s m PROP"), ("3s n PROP", "3s m PROP")])

        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n DAT", "3s m DAT"),
                                     ("3s f PROP", "3s m PROP"), ("3s n PROP", "3s m PROP")])

        self.add_gen_sync_variation([("3s f AKK", "3s m AKK"), ("3s n DAT", "3s m DAT")])
        self.add_gen_sync_variation([("3s f DAT", "3s m DAT"), ("3s n DATs", "3s m DATs")])
        self.add_gen_sync_variation([("3s f AKKs", "3s m AKKs"), ("3s n PROP", "3s m PROP")])


        self.add_gen_sync_variation([("3p f t", "3p m DATs"), ("3p n t", "3p m DATs")])

        self.add_gen_sync_variation([("3s f NOM", "3s m NOM"), ("3p n PROP", "3p m PROP")])
        self.add_gen_sync_variation([("3p f NOM", "3p m NOM"), ("3s n AKK", "3s m AKK")])


    def _create_syncretic_TENSE_files(self):

        self.add_ten_sync_variation([("za g AKK", "za g PROP")])
        self.add_ten_sync_variation([("1a g AKK", "1a g PROP")])
        self.add_ten_sync_variation([("2a g AKK", "2a g PROP")])
        self.add_ten_sync_variation([("3a g AKK", "3a g PROP")])
        self.add_ten_sync_variation([("zs g AKK", "zs g PROP")])
        self.add_ten_sync_variation([("zd g AKK", "zd g PROP")])
        self.add_ten_sync_variation([("zp g AKK", "zp g PROP")])

        self.add_ten_sync_variation([("za g AKK", "za g PROP"),("za g DAT", "za g PROP")])
        self.add_ten_sync_variation([("1a g AKK", "1a g PROP"),("1a g DAT", "1a g PROP")])
        self.add_ten_sync_variation([("2a g AKK", "2a g PROP"),("2a g DAT", "2a g PROP")])
        self.add_ten_sync_variation([("3a g AKK", "3a g PROP"),("3a g DAT", "3a g PROP")])
        self.add_ten_sync_variation([("zs g AKK", "zs g PROP"),("zs g DAT", "zs g PROP")])
        self.add_ten_sync_variation([("zd g AKK", "zd g PROP"),("zd g DAT", "zd g PROP")])
        self.add_ten_sync_variation([("zp g AKK", "zp g PROP"),("zp g DAT", "zp g PROP")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT"),("za g AKKs", "za g DATs")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT"),("1a g AKKs", "1a g DATs")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT"),("2a g AKKs", "2a g DATs")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT"),("3a g AKKs", "3a g DATs")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT"),("zs g AKKs", "zs g DATs")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT"),("zd g AKKs", "zd g DATs")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT"),("zp g AKKs", "zp g DATs")])

    def _create_syncretic_X_files(self):
        pass





class PermSynCreatorPR_SLAV_W(PermSynCreatorPR_SLAV):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_SLAV_W"

        self.GENDERS = ["v", "i", "f", "n"]
        self.NUMBERS = ["s", "d", "p"]
        self.PERSONS = ["1", "2", "3","r"]
        self.TENSES_CASES = ["NOM","AKK","DAT","GEN","INSTR","LOC","GENs","DATs","AKKs"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40


    def _create_variations(self):
        # randoms:
        self._create_random_PERM_files()
        self._create_random_SYN_files()
        self._create_random_PERM_dims_files()
        self._create_random_SYN_dims_files()
        # permutations:
        #self._create_permutation_PERS_files()
        #self._create_permutation_NUM_files()
        #self._create_permutation_GEN_files()
        #self._create_permutation_TENSE_files()
        #self._create_permutation_X_files()
        # syncretic variants:
        #self._create_syncretic_NUM_files()
        #self._create_syncretic_PERS_files()
        #self._create_syncretic_TENSE_files()
        #self._create_syncretic_GEN_files()
        #self._create_syncretic_X_files()
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

                if "d" in line[0]:
                    d_list.append(line[0])
                elif "p" in line[0]:
                    p_list.append(line[0])

                for count, tense in enumerate(self.TENSES_CASES, start=1):
                    cont_dict[tense][line[0]] = line[count]

        #add dual
        add_list_p = list()
        if d_list == list():
            for elem in cont_dict["NOM"].keys():
                if "p" in elem:
                    add_list_p.append(elem)
        for elem in add_list_p:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem.replace("p","d")] = cont_dict[tense][elem]

        # add reflexiv:
        if "rs" in cont_dict["NOM"].keys():
            if "rp" not in cont_dict["NOM"].keys():
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["rp"] = cont_dict[tense]["rs"]
            if "rd" not in cont_dict["NOM"].keys():
                for tense in self.TENSES_CASES:
                    cont_dict[tense]["rd"] = cont_dict[tense]["rs"]

        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in [x+y for y in self.NUMBERS for x in self.PERSONS]:
                keys_list = cont_dict[tense].keys()
                # print()
                # print(keys_list)
                # print(feat)
                if feat in keys_list:  # e.g. 1s
                    res_dict[feat + " v " + tense] = cont_dict[tense][feat]
                    res_dict[feat + " i " + tense] = cont_dict[tense][feat]
                    res_dict[feat + " f " + tense] = cont_dict[tense][feat]
                    res_dict[feat + " n " + tense] = cont_dict[tense][feat]
                else:
                    if feat + " v" in keys_list:
                        res_dict[feat + " v " + tense] = cont_dict[tense][feat + " v"]
                    if feat + " i" in keys_list:
                        res_dict[feat + " i " + tense] = cont_dict[tense][feat + " i"]
                    if feat + " m" in keys_list:
                        res_dict[feat + " v " + tense] = cont_dict[tense][feat + " m"]
                        res_dict[feat + " i " + tense] = cont_dict[tense][feat + " m"]

                    if feat + " f" in keys_list:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " f"]
                    else:
                        res_dict[feat + " f " + tense] = cont_dict[tense][feat + " i"]

                    if feat + " n" in keys_list:
                        res_dict[feat + " n " + tense] = cont_dict[tense][feat + " n"]
                    else:
                        res_dict[feat + " n " + tense] = cont_dict[tense][feat + " i"]

        return res_dict

    def _create_permutation_PERS_files(self):
        # 3s
        # print("HERE")
        # for i, j in self.org_conj_dict.items():
        #    print(i,j)

        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g LOC", "1a g LOC")])


        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g GEN", "1a g GEN"),
             ("2a g INSTR", "1a g INSTR"),
             ("2a g GENs", "1a g GENs")
             ])


        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g GENs", "1a g GENs")
             ])


        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g LOC", "1a g LOC"),
             ("2a g DAT", "1a g DAT"),
             ("2a g INSTR", "1a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g LOC", "2a g LOC"),
             ("3a g DAT", "1a g DAT"),
             ("3a g INSTR", "1a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g INSTR", "2a g INSTR")
             ])

#

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g GEN", "2a g GEN"),
             ("3a g INSTR", "1a g INSTR"),
             ("3a g GENs", "1a g GENs")
             ])


        self.add_pers_perm_variation(
            [("3a g GENs", "2a g GENs"),
             ("3a g GEN", "2a g GEN"),
             ("3a g INSTR", "1a g INSTR"),
             ("3a g AKK", "1a g AKK")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g GEN", "2a g GEN")
             ])


        self.add_pers_perm_variation(
            [("3a g INSTR", "2a g INSTR"),
             ("3a g GENs", "2a g GENs")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g GEN", "2a g GEN"),
             ("3a g INSTR", "2a g INSTR"),
             ("3a g GENs", "2a g GENs")
             ])
        #

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g LOC", "2a g LOC"),
             ("1a g DAT", "2a g DAT"),
             ("1a g INSTR", "2a g INSTR")
             ])


        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("1a g LOC", "2a g LOC"),
             ("1a g DAT", "2a g DAT"),
             ("1a g INSTR", "3a g INSTR")
             ])

        self.add_pers_perm_variation(
            [("3s g AKK", "1s g AKK"),
             ("3s g GEN", "1s g GEN")])

        self.add_pers_perm_variation(
            [("3s g AKK", "1s g AKK")])

        self.add_pers_perm_variation(
            [("3s g DAT", "2s g DAT"),
             ("3s g INSTR", "2s g INSTR")])

        self.add_pers_perm_variation(
            [("3s g GEN", "2s g GEN")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g LOC", "2s g LOC"),
             ("1s g GEN", "2s g GEN")])


        self.add_pers_perm_variation(
            [("1d g DAT", "2d g DAT"),
             ("1d g INSTR", "2d g INSTR"),
             ("1d g GEN", "2d g GEN")])

        self.add_pers_perm_variation(
            rotate_left_list =
            [("1d g DAT", "2d g DAT", "3d g DAT"),
             ("1d g INSTR", "2d g INSTR", "3d g INSTR"),
             ("1d g GEN", "2d g GEN", "3d g GEN")])


        self.add_pers_perm_variation(
            rotate_left_list =
            [("1d g DAT", "2d g DAT", "3d g DAT"),
             ("1d g INSTR", "2d g INSTR", "3d g INSTR")],
             rotate_right_list =
             [("1d g GEN", "2d g GEN", "3d g GEN")])


        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g LOC", "2s g LOC")])


        self.add_pers_perm_variation(
            [("1s n DAT", "2s n DAT"),
             ("1s n LOC", "2s n LOC"),
             ("1s n LOC", "2s n LOC")])


        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g INSTR", "2s g INSTR")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("2s g AKK", "3s g AKK"),
             ("1s g GEN", "3s g GEN")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f LOC", "2s f LOC"),
             ("1s f GEN", "2s f GEN")])

        self.add_pers_perm_variation(
            [("1s g AKK", "2s g AKK"),
             ("1s g GEN", "2s g GEN"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2p g LOC", "1p g LOC"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GEN", "1d g GEN"),
             ("2d g LOC", "1d g LOC")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GEN", "1p g GEN"),
             ("2p g LOC", "1p g LOC")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f INSTR", "2s f INSTR")])

        self.add_pers_perm_variation(
            [("1s i DAT", "2s i DAT"),
             ("2s n AKK", "3s n AKK"),
             ("1s f GEN", "3s f GEN")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("2s g AKK", "3s g AKK"),
             ("1s g GEN", "3s g GEN")])

        self.add_pers_perm_variation(
            [("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT")])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK")])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK"),
             ("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT"),
             ("1p g GEN", "2p g GEN"),
             ("1d g GEN", "2d g GEN")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "2p g INSTR"),
             ("1d g INSTR", "2d g INSTR"),
             ("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g AKK", "2p g AKK"),
             ("1d g AKK", "2d g AKK"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT"),
             ("3p g GEN", "2p g GEN"),
             ("3d g GEN", "2d g GEN")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "3p g INSTR"),
             ("1d g INSTR", "3d g INSTR"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g INSTR", "3p g INSTR"),
             ("3p g DAT", "2p g DAT")
             ])

        self.add_pers_perm_variation(
            [("3p g AKK", "2p g AKK"),
             ("3d g DAT", "1d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g NOM", "2p g NOM"),
             ("1d g NOM", "2d g NOM"),
             ("1p g INSTR", "2p g INSTR"),
             ("1d g INSTR", "2d g INSTR"),
             ("1p g LOC", "2p g LOC"),
             ("1d g LOC", "2d g LOC")
             ])

        self.add_pers_perm_variation([
            ("1s g INSTR", "2s g INSTR")
        ])

        self.add_pers_perm_variation([
            ("2s g INSTR", "3s g INSTR")
        ])

        self.add_pers_perm_variation([
            ("2s g INSTR", "3s g INSTR"),
            ("2s g LOC", "3s g LOC")
        ])

        self.add_pers_perm_variation(
            [("1p i NOM", "2p i NOM"),
             ("1d f NOM", "2d f NOM"),
             ("1p n INSTR", "2p n INSTR"),
             ("1d n INSTR", "2d n INSTR"),
             ("1p f LOC", "2p f LOC"),
             ("1d i LOC", "2d i LOC")
             ])

        self.add_pers_perm_variation(
            [("1p i NOM", "2p i NOM"),
             ("1d i NOM", "2d i NOM"),
             ("1p n INSTR", "2p n INSTR"),
             ("1d n INSTR", "2d n INSTR"),
             ("1p f LOC", "2p f LOC"),
             ("1d f LOC", "2d f LOC")
             ])

        self.add_pers_perm_variation(
            rotate_right_list=
            [("1p g GEN", "2p g GEN", "3p g GEN")]
        )

        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g INSTR", "1a g INSTR")])

        self.add_pers_perm_variation(
            [("3s i LOC", "3s i GENs"),
             ("2s n DAT", "3s n INSTR")])

        self.add_pers_perm_variation(
            [("2a g AKK", "1a g AKK"),
             ("2a g INSTR", "1a g INSTR"),
             ("2a g DAT", "1a g DAT"),
             ("2a g LOC", "1a g LOC")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g INSTR", "2a g INSTR"),
             ("3a g DAT", "1a g DAT"),
             ("3a g LOC", "1a g LOC")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g LOC", "2a g LOC")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("3a g INSTR", "2a g INSTR"),
             ("1a g DAT", "2a g DAT"),
             ("1a g LOC", "2a g LOC")
             ])

        self.add_pers_perm_variation(
            [("3a g AKK", "2a g AKK"),
             ("1a g INSTR", "2a g INSTR"),
             ("1a g DAT", "2a g DAT"),
             ("1a g LOC", "3a g LOC")
             ])

        self.add_pers_perm_variation(
            [("3s g DAT", "2s g DAT"),
             ("3s g LOC", "2s g LOC")])

        self.add_pers_perm_variation(
            [("3s g GENs", "2s g GENs")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g INSTR", "2s g INSTR"),
             ("1s g GENs", "2s g GENs")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("1s g LOC", "2s g LOC")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),
             ("2s g AKK", "3s g AKK"),
             ("1s g GENs", "3s g GENs")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f INSTR", "2s f INSTR"),
             ("1s f GENs", "2s f GENs")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GENs", "1p g GENs"),
             ("2p g INSTR", "1p g INSTR"),
             ("2d g AKK", "1d g AKK"),
             ("2d g GENs", "1d g GENs"),
             ("2d g INSTR", "1d g INSTR")])

        self.add_pers_perm_variation(
            [("2p g AKK", "1p g AKK"),
             ("2p g GENs", "1p g GENs"),
             ("2p g INSTR", "1p g INSTR")])

        self.add_pers_perm_variation(
            [("1s f DAT", "2s f DAT"),
             ("1s f LOC", "2s f LOC")])

        self.add_pers_perm_variation(
            [("1p g LOC", "2p g LOC"),
             ("1d g LOC", "2d g LOC"),
             ("1p g DAT", "2p g DAT"),
             ("1d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g LOC", "3p g LOC"),
             ("1d g LOC", "3d g LOC"),
             ("3p g DAT", "2p g DAT"),
             ("3d g DAT", "2d g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g LOC", "3p g LOC"),
             ("3p g DAT", "2p g DAT")
             ])

        self.add_pers_perm_variation(
            [("1p g NOM", "2p g NOM"),
             ("1d g NOM", "2d g NOM"),
             ("1p g LOC", "2p g LOC"),
             ("1d g LOC", "2d g LOC"),
             ("1p g INSTR", "2p g INSTR"),
             ("1d g INSTR", "2d g INSTR")
             ])

        self.add_pers_perm_variation([
            ("1s g LOC", "2s g LOC")
        ])

        self.add_pers_perm_variation([
            ("2s g LOC", "3s g LOC")
        ])

        self.add_pers_perm_variation([
            ("2s g LOC", "3s g LOC"),
            ("2s g INSTR", "3s g INSTR")
        ])

        self.add_pers_perm_variation(
            [("1p i NOM", "2p i NOM"),
             ("1d f NOM", "2d f NOM"),
             ("1p n LOC", "2p n LOC"),
             ("1d n LOC", "2d n LOC"),
             ("1p f INSTR", "2p f INSTR"),
             ("1d i INSTR", "2d i INSTR")
             ])

        self.add_pers_perm_variation(
            [("1p i NOM", "2p i NOM"),
             ("1d i NOM", "2d i NOM"),
             ("1p n LOC", "2p n LOC"),
             ("1d n LOC", "2d n LOC"),
             ("1p f INSTR", "2p f INSTR"),
             ("1d f INSTR", "2d f INSTR")
             ])

    def _create_permutation_NUM_files(self):
        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM")])

        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK")])


        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK"),
             ("3d n GEN", "3p n GEN")])

        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK"),
             ("3d n INSTR", "3p n INSTR")])


        self.add_num_perm_variation(
            [("3d n NOM", "3p n NOM"),
             ("3d n AKK", "3p n AKK"),
             ("3d n GEN", "3p n GEN"),
             ("3d n GENs", "3p n GENs"),
             ("3d n INSTR", "3p n INSTR")])

        for c in ["DAT", "INSTR", "LOC", "GEN"]:
            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("1d g " + c, "1p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("3d g " + c, "3p g " + c)])

            self.add_num_perm_variation(
                [("1d g " + c, "1p g " + c),
                 ("3d g " + c, "3p g " + c)])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("2d g INSTR", "2p g INSTR")])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g INSTR", "3p g INSTR")])


        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("2d g GEN", "2p g GEN"),
             ("3d g INSTR", "3p g INSTR")])



        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g INSTR", "3p g INSTR"),
             ("1d g LOC", "1p g LOC")])

        self.add_num_perm_variation(
            [("2d i DAT", "2p i DAT"),
             ("3d f DAT", "2p f DAT"),
             ("3d n INSTR", "3p n INSTR"),
             ("1d i INSTR", "1p i INSTR"),
             ("1d f LOC", "1p f LOC"),
             ("2d n LOC", "2p n LOC")
             ])

        self.add_num_perm_variation(
            [("1s g NOM", "1p g NOM"),
             ("2s g AKK", "2p g AKK"),
             ("1s g DAT", "1d g DAT"),
             ("2s g GEN", "2d g GEN")])

        self.add_num_perm_variation(
            [("3s i NOM", "3p i NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3d n DAT")])

        self.add_num_perm_variation(
            [("3s i NOM", "3d i NOM"),
             ("3s f AKK", "3p f AKK"),
             ("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3s f NOM", "3d f NOM"),
             ("3s i LOC", "3p i LOC"),
             ("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p f NOM", "3d f NOM"),
             ("3s f LOC", "3p f LOC"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p i NOM", "3d i NOM"),
             ("3s i LOC", "3p i LOC"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p i NOM", "3d i NOM"),
             ("3s i LOC", "3p i LOC"),
             ("3s n INSTR", "3p n INSTR"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(rotate_left_list=
                                    [("3s i NOM", "3d i NOM", "3p i NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i NOM", "3d i NOM", "3p i NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i NOM", "3d i NOM", "3p i NOM"),
             ("3s n NOM", "3d n NOM", "3p n NOM")],
            rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i NOM", "3d i NOM", "3p i NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s i GEN", "3d i GEN", "3p i GEN"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i NOM", "3d i NOM", "3p i NOM"),
             ("3s n AKK", "3d n AKK", "3p n AKK"),
             ("3s i GEN", "3d i GEN", "3p i GEN"),
             ("3s n DAT", "3d n DAT", "3p n DAT")
             ],
            rotate_right_list=[("3s f NOM", "3d f NOM", "3p f NOM"),
                               ("3s f AKK", "3d f AKK", "3p f AKK")])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i NOM", "3d i NOM", "3p i NOM"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("3s i GEN", "3d i GEN", "3p i GEN"),
             ("1s n DAT", "1d n DAT", "1p n DAT")
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i DAT", "3d i DAT", "3p i DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT"),
             ("2s n AKK", "2d n AKK", "2p n AKK"),
             ("2s i AKK", "2d i AKK", "2p i AKK"),
             ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("3s i DAT", "3d i DAT", "3p i DAT"),
             ("3s n DAT", "3d n DAT", "3p n DAT")],
            rotate_right_list=[
                ("2s n AKK", "2d n AKK", "2p n AKK"),
                ("2s i AKK", "2d i AKK", "2p i AKK")
            ])

        self.add_num_perm_variation(
            rotate_left_list=
            [("2s g DAT", "2d g DAT", "2p g DAT"),
             ("3s f DAT", "3d f DAT", "3p f DAT")],
            rotate_right_list=[
                ("1s g AKK", "1d g AKK", "1p g AKK"),
                ("3s f AKK", "3d f AKK", "3p f AKK")
            ])

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GEN", "1p g GEN"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GEN", "2d g GEN"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GEN", "3p g GEN"),
                ("2p g LOC", "2d g LOC"), ("1s g INSTR", "1d g INSTR"),
                ("1p g LOC", "1d g LOC"), ("2s g INSTR", "2d g INSTR"),
                ("3p g LOC", "3d g LOC"), ("3s g INSTR", "3d g INSTR")
            ]
        )

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GEN", "1p g GEN"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GEN", "2d g GEN"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GEN", "3p g GEN"),
                ("2p g LOC", "2d g LOC"), ("1s g INSTR", "1d g INSTR"),
                ("1p g LOC", "1d g LOC"), ("2s g INSTR", "2d g INSTR"),
                ("3p g LOC", "3d g LOC"), ("3s g INSTR", "3d g INSTR")
            ]
        )
        self.add_num_perm_variation(
            rotate_left_list=[
                ("1s g GEN", "1d g GEN", "1p g GEN"),
                ("2s g AKK", "2d g AKK", "2p g AKK"),
                ("3s n INSTR", "3d n INSTR", "3p n INSTR"),
            ],
            rotate_right_list=[
                ("2s g GEN", "2d g GEN", "2p g GEN"),
                ("1s g DAT", "1d g DAT", "1p g DAT"),
                ("3s i INSTR", "3d i INSTR", "3p i INSTR"),
            ]
        )

        for c in ["LOC", "INSTR"]:
            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("1d g " + c, "1p g " + c)])

            self.add_num_perm_variation(
                [("2d g " + c, "2p g " + c),
                 ("3d g " + c, "3p g " + c)])

            self.add_num_perm_variation(
                [("1d g " + c, "1p g " + c),
                 ("3d g " + c, "3p g " + c)])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("2d g LOC", "2p g LOC")])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g LOC", "3p g LOC")])

        self.add_num_perm_variation(
            [("2d g DAT", "2p g DAT"),
             ("3d g LOC", "3p g LOC"),
             ("1d g INSTR", "1p g INSTR")])

        self.add_num_perm_variation(
            [("2d i DAT", "2p i DAT"),
             ("3d f DAT", "2p f DAT"),
             ("3d n LOC", "3p n LOC"),
             ("1d i LOC", "1p i LOC"),
             ("1d f INSTR", "1p f INSTR"),
             ("2d n INSTR", "2p n INSTR")
             ])

        self.add_num_perm_variation(
            [("3s f NOM", "3d f NOM"),
             ("3s i INSTR", "3p i INSTR"),
             ("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p f NOM", "3d f NOM"),
             ("3s f INSTR", "3p f INSTR"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p i NOM", "3d i NOM"),
             ("3s i INSTR", "3p i INSTR"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [("3p i NOM", "3d i NOM"),
             ("3s i INSTR", "3p i INSTR"),
             ("3s n LOC", "3p n LOC"),
             ("3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GENs", "1p g GENs"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GENs", "2d g GENs"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GENs", "3p g GENs"),
                ("2p g INSTR", "2d g INSTR"), ("1s g LOC", "1d g LOC"),
                ("1p g INSTR", "1d g INSTR"), ("2s g LOC", "2d g LOC"),
                ("3p g INSTR", "3d g INSTR"), ("3s g LOC", "3d g LOC")
            ]
        )

        self.add_num_perm_variation(
            [
                ("2s g AKK", "2d g AKK"), ("1s g DAT", "1p g DAT"), ("1d g GENs", "1p g GENs"),
                ("1s g AKK", "1d g AKK"), ("2s g DAT", "2d g DAT"), ("2s g GENs", "2d g GENs"),
                ("3s g AKK", "3p g AKK"), ("3d g DAT", "3p g DAT"), ("3s g GENs", "3p g GENs"),
                ("2p g INSTR", "2d g INSTR"), ("1s g LOC", "1d g LOC"),
                ("1p g INSTR", "1d g INSTR"), ("2s g LOC", "2d g LOC"),
                ("3p g INSTR", "3d g INSTR"), ("3s g LOC", "3d g LOC")
            ]
        )
        self.add_num_perm_variation(
            rotate_left_list=[
                ("1s g GENs", "1d g GENs", "1p g GENs"),
                ("2s g AKK", "2d g AKK", "2p g AKK"),
                ("3s n LOC", "3d n LOC", "3p n LOC"),
            ],
            rotate_right_list=[
                ("2s g GENs", "2d g GENs", "2p g GENs"),
                ("1s g DAT", "1d g DAT", "1p g DAT"),
                ("3s i LOC", "3d i LOC", "3p i LOC"),
            ]
        )

    def _create_permutation_GEN_files(self):
        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i GEN", "3s f GEN", "3s n GEN")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
            rotate_left_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK"),
                ("3s i LOC", "3s f LOC", "3s n LOC")],
        )

        ###

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i LOC", "3s f LOC", "3s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i LOC", "3s f LOC", "3s n LOC")],
            rotate_left_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT")],
        )

        self.add_gen_perm_variation(
            [("3s i DAT", "3s f DAT"),
             ("3s i LOC", "3s f LOC")
             ])

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK"),
                ("3s i GEN", "3s f GEN", "3s n GEN"),
                ("3s i LOC", "3s f LOC", "3s n LOC"), ],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK")],
            rotate_left_list=
            [
                ("3s i GEN", "3s f GEN", "3s n GEN"),
                ("3s i LOC", "3s f LOC", "3s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("2s i DAT", "2s f DAT", "2s n DAT"),
                ("2s i LOC", "2s f LOC", "2s n LOC")],
            rotate_left_list=
            [
                ("1s i GEN", "1s f GEN", "1s n GEN"),
                ("1s i LOC", "1s f LOC", "1s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i LOC", "3s f LOC", "3s n LOC")],
            rotate_left_list=
            [
                ("3s i GEN", "3s f GEN", "3s n GEN"),
                ("3s i AKK", "3s f AKK", "3s n AKK")],
        )

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3s i GEN", "3s f GEN"),
             ("3s i LOC", "3s f LOC")
             ])

        for g in ["v", "i", "n"]:
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " INSTR", "3s f INSTR")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " LOC", "3s f LOC")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " LOC", "3s f LOC"),
                 ("3s " + g + " DAT", "3s f DAT"),
                 ("3s " + g + " INSTR", "3s f INSTR")])
            self.add_gen_perm_variation(
                [("3s " + g + " NOM", "3s f NOM")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GEN", "3s f GEN")])

            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GEN", "3s f GEN")])

        self.add_gen_perm_variation(
            [("3s v AKK", "3s f AKK"),
             ("3s v LOC", "3s f LOC"),
             ("3s v DAT", "3s f DAT"),
             ("3s v INSTR", "3s f INSTR"),
             ("3s i AKK", "3s n AKK"),
             ("3s i LOC", "3s n LOC"),
             ("3s i DAT", "3s n DAT"),
             ("3s i INSTR", "3s n INSTR")
             ])
        self.add_gen_perm_variation(
            [("3s v NOM", "3s f NOM"),
             ("3s i NOM", "3s n NOM")])
        self.add_gen_perm_variation(
            [("3s v AKK", "3s f AKK"),
             ("3s v GEN", "3s f GEN"),
             ("3s i AKK", "3s n AKK"),
             ("3s i GEN", "3s n GEN")])

        self.add_gen_perm_variation(
            [("3s v AKK", "3s f AKK"),
             ("3s v GEN", "3s f GEN"),
             ("3s i AKK", "3s n AKK"),
             ("3s i GEN", "3s n GEN")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s i NOM", "2s f NOM"),
             ("1s i AKK", "1s f AKK"),
             ("3s i INSTR", "3s f INSTR"),
             ("1s i AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s f LOC"),
             ("3p i INSTR", "3p f INSTR"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GEN", "3d f GEN")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s n NOM", "2s f NOM"),
             ("1s i GEN", "1s f GEN"),
             ("3s i INSTR", "3s n INSTR"),
             ("1s i AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s n LOC"),
             ("3p i INSTR", "3p f INSTR"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GEN", "3d f GEN"),
             ("2s i AKK", "2s f AKK"),
             ("2d n DAT", "2d f DAT"),
             ("2s n LOC", "2s f LOC"),
             ("1p i INSTR", "1p f INSTR"),
             ("1s n NOM", "1s i NOM"),
             ("1d i GEN", "1d f GEN")
             ])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n LOC", "3s n LOC"),
             ("3p i INSTR", "3p f INSTR"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GEN", "3d f GEN"),
             ("2s f AKK", "2s n AKK"),
             ("2d n DAT", "2d i DAT"),
             ("2s n LOC", "2s i LOC"),
             ("1p n INSTR", "1p f INSTR"),
             ("1s f NOM", "1s i NOM"),
             ("1d i GEN", "1d f GEN")
             ])

        self.add_gen_perm_variation(
            [
                ("2s f AKK", "2s n AKK"),
                ("2d n DAT", "2d i DAT"),
                ("2p n LOC", "2p i LOC"),
                ("1p n INSTR", "1p f INSTR"),
                ("1s f NOM", "1s i NOM"),
                ("1d i GEN", "1d f GEN"),
                ("2s f DAT", "2s n DAT"),
                ("2d n GEN", "2d i GEN"),
                ("2p n NOM", "2p i NOM"),
                ("1p n GEN", "1p f GEN"),
                ("1s f LOC", "1s i LOC"),
                ("1d i NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d n INSTR", "2d i INSTR"),
                ("2p n GEN", "2p i GEN"),
                ("1p n AKK", "1p f AKK"),
                ("1s f GEN", "1s i GEN"),
                ("1d i INSTR", "1d f INSTR")
            ])

        self.add_gen_perm_variation(
            [
                ("2s f LOC", "2s n LOC"),
                ("2d n AKK", "2d i AKK"),
                ("2p n LOC", "2p i LOC"),
                ("1p n INSTR", "1p f INSTR"),
                ("1s f NOM", "1s i NOM"),
                ("1d i GEN", "1d f GEN"),
                ("2s f INSTR", "2s n INSTR"),
                ("2d n GEN", "2d f GEN"),
                ("2p n NOM", "2p f NOM"),
                ("1p n GEN", "1p f GEN"),
                ("1s f LOC", "1s n LOC"),
                ("1d n NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d f INSTR", "2d i INSTR"),
                ("2p f GEN", "2p i GEN"),
                ("1p n AKK", "1p f AKK"),
                ("1s n GEN", "1s i GEN"),
                ("1d i INSTR", "1d f INSTR")
            ])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s f AKK", "2s n AKK"), ("2d i AKK", "2d n AKK"), ("2p f AKK", "2p i AKK"),
             ("2s i DAT", "2s n DAT"), ("1d f DAT", "1d n DAT"), ("1s f DAT", "1s i DAT"),
             ("1d i INSTR", "1d n INSTR"), ("3d i INSTR", "3d f INSTR"), ("2p i INSTR", "2p f INSTR"),
             ("2s i LOC", "2s n LOC"), ("1d f LOC", "1d n LOC"), ("1s f LOC", "1s i LOC")])

        self.add_gen_perm_variation(
            rotate_right_list=
            [("3p i AKK", "3p f AKK", "3p n AKK"),
             ("3s i DAT", "3s f DAT", "3s n DAT")],
            rotate_left_list=
            [("3d i NOM", "3d f NOM", "3d n NOM"),
             ("3s i INSTR", "3s f INSTR", "3s n INSTR")]
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i LOC", "3s f LOC", "3s n LOC")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i LOC", "3s f LOC", "3s n LOC")],
            rotate_left_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
        )

        ###

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
            rotate_left_list=
            [
                ("3s i DAT", "3s f DAT", "3s n DAT")],
        )

        self.add_gen_perm_variation(
            [("3s i DAT", "3s f DAT"),
             ("3s i INSTR", "3s f INSTR")
             ])

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK"),
                ("3s i GENs", "3s f GENs", "3s n GENs"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR"), ],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i AKK", "3s f AKK", "3s n AKK")],
            rotate_left_list=
            [
                ("3s i GENs", "3s f GENs", "3s n GENs"),
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("2s i DAT", "2s f DAT", "2s n DAT"),
                ("2s i INSTR", "2s f INSTR", "2s n INSTR")],
            rotate_left_list=
            [
                ("1s i GENs", "1s f GENs", "1s n GENs"),
                ("1s i INSTR", "1s f INSTR", "1s n INSTR")],
        )

        self.add_gen_perm_variation(
            rotate_right_list=
            [
                ("3s i INSTR", "3s f INSTR", "3s n INSTR")],
            rotate_left_list=
            [
                ("3s i GENs", "3s f GENs", "3s n GENs"),
                ("3s i AKK", "3s f AKK", "3s n AKK")],
        )

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3s i GENs", "3s f GENs"),
             ("3s i INSTR", "3s f INSTR")
             ])

        for g in ["v","i", "n"]:
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " LOC", "3s f LOC")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " INSTR", "3s f INSTR")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " INSTR", "3s f INSTR"),
                 ("3s " + g + " DAT", "3s f DAT"),
                 ("3s " + g + " LOC", "3s f LOC")])
            self.add_gen_perm_variation(
                [("3s " + g + " NOM", "3s f NOM")])
            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GENs", "3s f GENs")])

            self.add_gen_perm_variation(
                [("3s " + g + " AKK", "3s f AKK"),
                 ("3s " + g + " GENs", "3s f GENs")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s i NOM", "2s f NOM"),
             ("1s i AKK", "1s f AKK"),
             ("3s i LOC", "3s f LOC"),
             ("1s i AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n INSTR", "3s f INSTR"),
             ("3p i LOC", "3p f LOC"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GENs", "3d f GENs")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s n NOM", "2s f NOM"),
             ("1s i GENs", "1s f GENs"),
             ("3s i LOC", "3s n LOC"),
             ("1s i AKK", "1s f AKK")])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n INSTR", "3s n INSTR"),
             ("3p i LOC", "3p f LOC"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GENs", "3d f GENs"),
             ("2s i AKK", "2s f AKK"),
             ("2d n DAT", "2d f DAT"),
             ("2s n INSTR", "2s f INSTR"),
             ("1p i LOC", "1p f LOC"),
             ("1s n NOM", "1s i NOM"),
             ("1d i GENs", "1d f GENs")
             ])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("3d n DAT", "3d f DAT"),
             ("3s n INSTR", "3s n INSTR"),
             ("3p i LOC", "3p f LOC"),
             ("3s n NOM", "3s i NOM"),
             ("3d i GENs", "3d f GENs"),
             ("2s f AKK", "2s n AKK"),
             ("2d n DAT", "2d i DAT"),
             ("2s n INSTR", "2s i INSTR"),
             ("1p n LOC", "1p f LOC"),
             ("1s f NOM", "1s i NOM"),
             ("1d i GENs", "1d f GENs")
             ])

        self.add_gen_perm_variation(
            [
                ("2s f AKK", "2s n AKK"),
                ("2d n DAT", "2d i DAT"),
                ("2p n INSTR", "2p i INSTR"),
                ("1p n LOC", "1p f LOC"),
                ("1s f NOM", "1s i NOM"),
                ("1d i GENs", "1d f GENs"),
                ("2s f DAT", "2s n DAT"),
                ("2d n GENs", "2d i GENs"),
                ("2p n NOM", "2p i NOM"),
                ("1p n GENs", "1p f GENs"),
                ("1s f INSTR", "1s i INSTR"),
                ("1d i NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d n LOC", "2d i LOC"),
                ("2p n GENs", "2p i GENs"),
                ("1p n AKK", "1p f AKK"),
                ("1s f GENs", "1s i GENs"),
                ("1d i LOC", "1d f LOC")
            ])

        self.add_gen_perm_variation(
            [
                ("2s f INSTR", "2s n INSTR"),
                ("2d n AKK", "2d i AKK"),
                ("2p n INSTR", "2p i INSTR"),
                ("1p n LOC", "1p f LOC"),
                ("1s f NOM", "1s i NOM"),
                ("1d i GENs", "1d f GENs"),
                ("2s f LOC", "2s n LOC"),
                ("2d n GENs", "2d f GENs"),
                ("2p n NOM", "2p f NOM"),
                ("1p n GENs", "1p f GENs"),
                ("1s f INSTR", "1s n INSTR"),
                ("1d n NOM", "1d f NOM"),
                ("2s f NOM", "2s n NOM"),
                ("2d f LOC", "2d i LOC"),
                ("2p f GENs", "2p i GENs"),
                ("1p n AKK", "1p f AKK"),
                ("1s n GENs", "1s i GENs"),
                ("1d i LOC", "1d f LOC")
            ])

        self.add_gen_perm_variation(
            [("3s i AKK", "3s f AKK"),
             ("2s f AKK", "2s n AKK"), ("2d i AKK", "2d n AKK"), ("2p f AKK", "2p i AKK"),
             ("2s i DAT", "2s n DAT"), ("1d f DAT", "1d n DAT"), ("1s f DAT", "1s i DAT"),
             ("1d i LOC", "1d n LOC"), ("3d i LOC", "3d f LOC"), ("2p i LOC", "2p f LOC"),
             ("2s i INSTR", "2s n INSTR"), ("1d f INSTR", "1d n INSTR"), ("1s f INSTR", "1s i INSTR")])

        self.add_gen_perm_variation(
            rotate_right_list=
            [("3p i AKK", "3p f AKK", "3p n AKK"),
             ("3s i DAT", "3s f DAT", "3s n DAT")],
            rotate_left_list=
            [("3d i NOM", "3d f NOM", "3d n NOM"),
             ("3s i LOC", "3s f LOC", "3s n LOC")]
        )

    def _create_permutation_TENSE_files(self):
        self.add_ten_perm_variation(
            [("za g NOM", "za g INSTR")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g INSTR"),
             ("za g DAT", "za g GEN")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g INSTR"),
             ("za g DAT", "za g GEN"),
             ("za g LOC", "za g NOM")])

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g GEN", "1p g LOC"),
                ("1d g AKK", "1d g GEN", "1d g LOC")],
            rotate_right_list=[
                ("2d g AKK", "2d g GEN", "2d g LOC"),
                ("2d g AKK", "2d g GEN", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g AKK", "1p g GEN"),
                ("1d g AKK", "1d g GEN"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g GEN", "1p g LOC"),
                ("1d g GEN", "1d g LOC"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC"),
                ("1s g AKK", "1s g GEN")
            ])

        self.add_ten_perm_variation(
            [
                ("3s i AKK", "3s i GEN"),
                ("1d g AKK", "1d g GEN"),
                ("1p g AKK", "1p g GEN"),
                ("2s g AKK", "2s g GEN")
            ])
        ###

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g INSTR", "1p g LOC"),
                ("1d g AKK", "1d g INSTR", "1d g LOC")],
            rotate_right_list=[
                ("2d g AKK", "2d g GEN", "2d g INSTR"),
                ("2d g AKK", "2d g GEN", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g GEN"),
                ("1d g NOM", "1d g GEN"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g LOC"),
                ("1d g NOM", "1d g LOC"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR"),
                ("1s g AKK", "1s g NOM")
            ])

        self.add_ten_perm_variation(
            [
                ("3s i AKK", "3s i INSTR"),
                ("1d g AKK", "1d g INSTR"),
                ("1p g AKK", "1p g INSTR"),
                ("2s g AKK", "2s g INSTR")
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s i DAT", "3s i LOC"),
                ("1s g DAT", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i DAT", "3s i LOC"),
                ("3s n DAT", "3s n LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g LOC"),
                ("2s g DAT", "2s g LOC"),
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s i GEN", "3s i LOC"),
                ("1s g GEN", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i AKK", "3s i LOC"),
                ("1s g AKK", "1s g LOC"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i LOC", "3s i AKK"),
                ("3s n LOC", "3s n AKK"),
            ])
        self.add_ten_perm_variation(
            [
                ("3s i DAT", "3s i AKK"),
                ("3s n DAT", "3s n AKK"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g INSTR"),
                ("2s g DAT", "2s g INSTR"),
            ])

        ###

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g INSTR"),
             ("zp g AKK", "zp g INSTR"),
             ("zs g DAT", "zs g GEN"),
             ("zs g LOC", "zs g NOM")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR")])

        self.add_ten_perm_variation(
            [("3p g DAT", "3p g INSTR"),
             ("3d g DAT", "3d g INSTR")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g DAT"),
             ("2p g GEN", "2p g INSTR")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR"),
             ("1p g GEN", "1p g DAT")])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g DAT"),
             ("2p g GEN", "2p g INSTR"),
             ("3d g GEN", "3d g DAT"),
             ("2d g GEN", "2d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("3p g GEN", "3p g INSTR"),
             ("1p g GEN", "1p g DAT"),
             ("3d g GEN", "3d g INSTR"),
             ("1d g GEN", "1d g DAT")
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("3s f INSTR", "3s f LOC"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("1d g DAT", "1d g GEN"),
             ("2p g INSTR", "2p g LOC"),
             ])

        self.add_ten_perm_variation(
            [("1s g INSTR", "1s g DAT"),
             ("2s g INSTR", "2s g GEN"),
             ("1d g DAT", "1d g GEN"),
             ("2p g INSTR", "2p g LOC"),
             ("3d g LOC", "3d g GEN"),
             ("3p g DAT", "3p g INSTR"),
             ])

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g LOC"),
             ("zp g AKK", "zp g LOC"),
             ("zs g DAT", "zs g INSTR")])

        self.add_ten_perm_variation(
            [("zd i AKK", "zd i LOC"),
             ("zp f AKK", "zp f LOC"),
             ("zs n DAT", "zs n INSTR")])

        self.add_ten_perm_variation(
            [("1a g NOM", "1a g INSTR")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g INSTR")])

        self.add_ten_perm_variation(
            [("1a g AKK", "1a g DAT")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g GEN")])

        self.add_ten_perm_variation(
            [("1a g NOM", "1a g DAT"),
             ("3a g NOM", "3a g AKK"),
             ("1a g NOM", "1a g GEN")])

        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g NOM", "1a g AKK"),
             ("2a g NOM", "2a g GEN")])

        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g LOC", "1a g AKK"),
             ("3a g NOM", "3a g GEN")])

        self.add_ten_perm_variation(
            [("2a g INSTR", "2a g DAT"),
             ("1a g LOC", "1a g AKK"),
             ("3a f NOM", "3a f GEN")])

        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT")])

        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT"),
             ("1s g LOC", "1s g INSTR")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("2p g LOC", "2p g INSTR"),
             ("2d g LOC", "2d g INSTR")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2s g LOC", "2s g INSTR"),
             ("1p g LOC", "1p g INSTR"),
             ("1d g LOC", "1d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2p g LOC", "2p g INSTR"),
             ("2d g LOC", "2d g INSTR"),
             ("1p g LOC", "1p g INSTR"),
             ("1d g LOC", "1d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("1s g DAT", "1s g INSTR")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g INSTR")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g INSTR"),
             ("1s g AKK", "1s g LOC")])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC")])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC"),
             ("2p g NOM", "2p g GEN"),
             ("2d g AKK", "2d g LOC")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s n DAT", "3s n INSTR"),
             ("3s f AKK", "3s f LOC"),
             ("2p i NOM", "2p i GEN"),
             ("2d n AKK", "2d n LOC")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2p i NOM", "2p i GEN"),
             ("2d n AKK", "2d n DAT")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2p g NOM", "2p g GEN"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g INSTR"),
             ("2p g NOM", "2p g LOC")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3s f DAT", "3s f INSTR"),
             ("3s n AKK", "3s n LOC"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g DAT"),
             ("2p g NOM", "2p g AKK")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i INSTR"),
             ("3p f DAT", "3p f INSTR"),
             ("3d n AKK", "3d n LOC"),
             ("2d i AKK", "2d i DAT"),
             ("1d f NOM", "1d f DAT"),
             ("2p n NOM", "2p n AKK")
             ])

        self.add_ten_perm_variation(
            [("1s i NOM", "3s i INSTR"),
             ("2p f NOM", "3p f LOC"),
             ("2d n NOM", "3d n GEN"),
             ("2d i NOM", "2d i DAT"),
             ("1d f NOM", "1d f AKK"),
             ])

        self.add_ten_perm_variation(
            [("3a g AKK", "3a g GEN")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g GEN")])

        self.add_ten_perm_variation(
            [("2a g AKK", "2a g GEN"),
             ("1a g AKK", "1a g GEN")])

        self.add_ten_perm_variation(
            [("zs g AKK", "zs g GEN")])

        self.add_ten_perm_variation(
            [("zp g AKK", "zp g GEN"),
             ("zd g AKK", "zd g GEN")])

        self.add_ten_perm_variation(
            rotate_left_list=
            [("1p g AKK", "1p g GEN", "1p g DAT")],
            rotate_right_list=
            [("2p g AKK", "2p g GEN", "2p g DAT")]
        )

        self.add_ten_perm_variation(
            rotate_left_list=
            [("1p g AKK", "1p g GEN", "1p g DAT"),
             ("3p i LOC", "3p i NOM", "3p i INSTR")],
            rotate_right_list=
            [("2p g AKK", "2p g GEN", "2p g DAT"),
             ("3p n LOC", "3p n NOM", "3p n INSTR")]
        )

        self.add_ten_perm_variation(
            [("za g NOM", "za g LOC")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g LOC"),
             ("za g DAT", "za g GENs")])

        self.add_ten_perm_variation(
            [("za g AKK", "za g LOC"),
             ("za g DAT", "za g GENs"),
             ("za g INSTR", "za g NOM")])

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g GENs", "1p g INSTR"),
                ("1d g AKK", "1d g GENs", "1d g INSTR")],
            rotate_right_list=[
                ("2d g AKK", "2d g GENs", "2d g INSTR"),
                ("2d g AKK", "2d g GENs", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g AKK", "1p g GENs"),
                ("1d g AKK", "1d g GENs"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR")])

        self.add_ten_perm_variation(
            [
                ("1p g GENs", "1p g INSTR"),
                ("1d g GENs", "1d g INSTR"),
                ("2d g AKK", "2d g INSTR"),
                ("2d g AKK", "2d g INSTR"),
                ("1s g AKK", "1s g GENs")
            ])

        self.add_ten_perm_variation(
            rotate_left_list=[
                ("1p g AKK", "1p g LOC", "1p g INSTR"),
                ("1d g AKK", "1d g LOC", "1d g INSTR")],
            rotate_right_list=[
                ("2d g AKK", "2d g GENs", "2d g LOC"),
                ("2d g AKK", "2d g GENs", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g GENs"),
                ("1d g NOM", "1d g GENs"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC")])

        self.add_ten_perm_variation(
            [
                ("1p g NOM", "1p g INSTR"),
                ("1d g NOM", "1d g INSTR"),
                ("2d g AKK", "2d g LOC"),
                ("2d g AKK", "2d g LOC"),
                ("1s g AKK", "1s g NOM")
            ])

        self.add_ten_perm_variation(
            [
                ("3s i AKK", "3s i LOC"),
                ("1d g AKK", "1d g LOC"),
                ("1p g AKK", "1p g LOC"),
                ("2s g AKK", "2s g LOC")
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s i DAT", "3s i INSTR"),
                ("1s g DAT", "1s g INSTR"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i DAT", "3s i INSTR"),
                ("3s n DAT", "3s n INSTR"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g INSTR"),
                ("2s g DAT", "2s g INSTR"),
            ])

        ####

        self.add_ten_perm_variation(
            [
                ("3s i GENs", "3s i INSTR"),
                ("1s g GENs", "1s g INSTR"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i AKK", "3s i INSTR"),
                ("1s g AKK", "1s g INSTR"),
            ])

        self.add_ten_perm_variation(
            [
                ("3s i INSTR", "3s i AKK"),
                ("3s n INSTR", "3s n AKK"),
            ])

        self.add_ten_perm_variation(
            [
                ("1s g DAT", "1s g LOC"),
                ("2s g DAT", "2s g LOC"),
            ])

        ###

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g LOC"),
             ("zp g AKK", "zp g LOC"),
             ("zs g DAT", "zs g GENs"),
             ("zs g INSTR", "zs g NOM")])

        self.add_ten_perm_variation(
            [("3p g GENs", "3p g LOC")])

        self.add_ten_perm_variation(
            [("3p g DAT", "3p g LOC"),
             ("3d g DAT", "3d g LOC")])

        self.add_ten_perm_variation(
            [("3p g GENs", "3p g DAT"),
             ("2p g GENs", "2p g LOC")])

        self.add_ten_perm_variation(
            [("3p g GENs", "3p g LOC"),
             ("1p g GENs", "1p g DAT")])

        self.add_ten_perm_variation(
            [("3p g GENs", "3p g DAT"),
             ("2p g GENs", "2p g LOC"),
             ("3d g GENs", "3d g DAT"),
             ("2d g GENs", "2d g LOC")
             ])

        self.add_ten_perm_variation(
            [("3p g GENs", "3p g LOC"),
             ("1p g GENs", "1p g DAT"),
             ("3d g GENs", "3d g LOC"),
             ("1d g GENs", "1d g DAT")
             ])

        self.add_ten_perm_variation(
            [("1s g LOC", "1s g DAT"),
             ("2s g LOC", "2s g GENs"),
             ])

        self.add_ten_perm_variation(
            [("1s g LOC", "1s g DAT"),
             ("2s g LOC", "2s g GENs"),
             ("3s f LOC", "3s f INSTR"),
             ])

        self.add_ten_perm_variation(
            [("1s g LOC", "1s g DAT"),
             ("2s g LOC", "2s g GENs"),
             ("1d g DAT", "1d g GENs"),
             ("2p g LOC", "2p g INSTR"),
             ])

        self.add_ten_perm_variation(
            [("1s g LOC", "1s g DAT"),
             ("2s g LOC", "2s g GENs"),
             ("1d g DAT", "1d g GENs"),
             ("2p g LOC", "2p g INSTR"),
             ("3d g INSTR", "3d g GENs"),
             ("3p g DAT", "3p g LOC"),
             ])

        self.add_ten_perm_variation(
            [("zd g AKK", "zd g INSTR"),
             ("zp g AKK", "zp g INSTR"),
             ("zs g DAT", "zs g LOC")])

        self.add_ten_perm_variation(
            [("zd i AKK", "zd i INSTR"),
             ("zp f AKK", "zp f INSTR"),
             ("zs n DAT", "zs n LOC")])

        self.add_ten_perm_variation(
            [("1a g NOM", "1a g LOC")])

        self.add_ten_perm_variation(
            [("3a g NOM", "3a g LOC")])

        self.add_ten_perm_variation(
            [("2a g NOM", "2a g DAT"),
             ("1a g INSTR", "1a g AKK"),
             ("3a g NOM", "3a g GENs")])

        self.add_ten_perm_variation(
            [("2a g LOC", "2a g DAT"),
             ("1a g INSTR", "1a g AKK"),
             ("3a f NOM", "3a f GENs")])

        self.add_ten_perm_variation(
            [("1s g AKK", "1s g DAT"),
             ("1s g INSTR", "1s g LOC")])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("2p g INSTR", "2p g LOC"),
             ("2d g INSTR", "2d g LOC")])

        self.add_ten_perm_variation(
            [("2s g AKK", "2s g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2s g INSTR", "2s g LOC"),
             ("1p g INSTR", "1p g LOC"),
             ("1d g INSTR", "1d g LOC")
             ])

        self.add_ten_perm_variation(
            [("2p g AKK", "2p g DAT"),
             ("2d g AKK", "2d g DAT"),
             ("1p g AKK", "1p g DAT"),
             ("1d g AKK", "1d g DAT"),
             ("2p g INSTR", "2p g LOC"),
             ("2d g INSTR", "2d g LOC"),
             ("1p g INSTR", "1p g LOC"),
             ("1d g INSTR", "1d g LOC")
             ])

        self.add_ten_perm_variation(
            [("1s g DAT", "1s g LOC")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g LOC")])

        self.add_ten_perm_variation(
            [("2s g DAT", "2s g LOC"),
             ("1s g AKK", "1s g INSTR")])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s n DAT", "3s n LOC"),
             ("3s f AKK", "3s f INSTR")])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s n DAT", "3s n LOC"),
             ("3s f AKK", "3s f INSTR"),
             ("2p g NOM", "2p g GENs"),
             ("2d g AKK", "2d g INSTR")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s n DAT", "3s n LOC"),
             ("3s f AKK", "3s f INSTR"),
             ("2p i NOM", "2p i GENs"),
             ("2d n AKK", "2d n INSTR")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s f DAT", "3s f LOC"),
             ("3s n AKK", "3s n INSTR"),
             ("2p i NOM", "2p i GENs"),
             ("2d n AKK", "2d n DAT")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s f DAT", "3s f LOC"),
             ("3s n AKK", "3s n INSTR"),
             ("2p g NOM", "2p g GENs"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g LOC"),
             ("2p g NOM", "2p g INSTR")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3s f DAT", "3s f LOC"),
             ("3s n AKK", "3s n INSTR"),
             ("2d g AKK", "2d g DAT"),
             ("1d g NOM", "1d g DAT"),
             ("2p g NOM", "2p g AKK")
             ])

        self.add_ten_perm_variation(
            [("3s i DAT", "3s i LOC"),
             ("3p f DAT", "3p f LOC"),
             ("3d n AKK", "3d n INSTR"),
             ("2d i AKK", "2d i DAT"),
             ("1d f NOM", "1d f DAT"),
             ("2p n NOM", "2p n AKK")
             ])

        self.add_ten_perm_variation(
            [("1s i NOM", "3s i LOC"),
             ("2p f NOM", "3p f INSTR"),
             ("2d n NOM", "3d n GENs"),
             ("2d i NOM", "2d i DAT"),
             ("1d f NOM", "1d f AKK"),
             ])

        self.add_ten_perm_variation(
            rotate_left_list=
            [("1p g AKK", "1p g GENs", "1p g DAT"),
             ("3p i INSTR", "3p i NOM", "3p i LOC")],
            rotate_right_list=
            [("2p g AKK", "2p g GENs", "2p g DAT"),
             ("3p n INSTR", "3p n NOM", "3p n LOC")]
        )

    def _create_permutation_X_files(self):
        self.add_xross_perm_variation(
            [("3p g LOC", "2s g LOC")])

        self.add_xross_perm_variation(
            [("3s i INSTR", "3s n GEN"),
             ("2s i DAT", "3s n LOC")])

        self.add_xross_perm_variation(
            [("3p f NOM", "3p n AKK")])

        self.add_xross_perm_variation(
            [("3d f AKK", "3s n NOM"),
             ("3d n AKK", "3s f NOM")])

        self.add_xross_perm_variation(
            [("3s n AKK", "3p f NOM"), ("2d g AKK", "1s g NOM")])



        self.add_xross_perm_variation(
            [("3s i INSTR", "3s i GEN"),
             ("2s n DAT", "3s n LOC")])


        self.add_xross_perm_variation(
            rotate_right_list=
            [("1p g GEN", "2p g GEN", "3p g GEN"),
             ("3s i GEN", "3s f GEN", "3s n GEN")],
        )

        self.add_xross_perm_variation(
            [("1p g DAT", "2p g GEN")]
        )

        self.add_xross_perm_variation(
            [("3s n AKK", "3s n LOC"),
             ("3s n AKK", "3s n INSTR")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g INSTR"),
             ("2s g NOM", "2p g LOC")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g INSTR")])


        self.add_xross_perm_variation(
            [("rs g GEN", "rp g INSTR")])


        self.add_xross_perm_variation(
            [("rd g GEN", "rp g INSTR")])


        self.add_xross_perm_variation(
            [("rs v GEN","3p v LOC"),
             ("rs i GEN", "3p i LOC"),
             ("rp f GEN","3p f LOC"),
             ("rd n GEN","3p n LOC")])



        self.add_xross_perm_variation(
            [("rs v GEN","3p v LOC"),
             ("rs i GEN", "3p i LOC"),
             ("rp f GEN","3p f LOC"),
             ("rd n GEN","3p n LOC"),

             ("rs v INSTR", "3d v DAT"),
             ("rs i INSTR", "3d i DAT"),
             ("rp f INSTR", "3d f DAT"),
             ("rd n INSTR", "3d n DAT")
             ])

        self.add_xross_perm_variation(
            [("rs i GEN", "3p i LOC"),
             ("rs v GEN", "3p v LOC"),
             ("rp f GEN", "3p f LOC"),
             ("rd n GEN", "3p n LOC"),

             ("rs v INSTR", "3d v DAT"),
             ("rs i INSTR", "3d i DAT"),
             ("rp f INSTR", "3d f DAT"),
             ("rd n INSTR", "3d n DAT"),

             ("rs v DAT", "3p v INSTR"),
             ("rs i DAT", "3p i INSTR"),
             ("rp f DAT", "3p f INSTR"),
             ("rd n DAT", "3p n INSTR"),

             ("rs v LOC", "3d v GEN"),
             ("rs i LOC", "3d i GEN"),
             ("rp f LOC", "3d f GEN"),
             ("rd n LOC", "3d n GEN")
             ])

        self.add_xross_perm_variation(
            [("1s g DAT", "1s g INSTR"),
             ("3s f DAT", "3s i DAT"),
             ("3s f INSTR", "3s i INSTR")])

        self.add_xross_perm_variation(
            [("3s g NOM", "2p g INSTR"),
             ("3s i GEN", "2p f DAT"),
             ("3s n GEN", "1s f NOM"),
             ("3s f DAT", "1p f NOM")])

        self.add_xross_perm_variation(
            [("1s g NOM", "2p g INSTR"),
             ("2s g DAT", "2s g LOC"),
             ("2s g AKK", "1p g INSTR"),
             ("1p g GEN", "1s g LOC"),
             ("2p g DAT", "2s g INSTR"),
             ("3p g NOM", "1d g INSTR"),
             ("1d g AKK", "3d g LOC"),
             ("2d g GEN", "3p g INSTR"),
             ("3d g NOM", "1d g LOC")])

        self.add_xross_perm_variation(
            [("1p g AKK", "2p g LOC"),
             ("1d g AKK", "2d g LOC"),
             ("1s g DAT", "2s g INSTR"),
             ("3s i AKK", "3s n DAT"),
             ("3s i NOM", "3s n INSTR")])

        self.add_xross_perm_variation(
            [
                ("1s f NOM", "2s n NOM"), ("2s i GEN", "1s i DAT"), ("2s n DAT", "1s i AKK"),
                ("1s n GEN", "1s f DAT"), ("1p f GEN", "1p i GEN"), ("2s n GEN", "2s f GEN"),
                ("1p f DAT", "1p i DAT"), ("1s i GEN", "1s n DAT"), ("2p f AKK", "2s i AKK"),
                ("2s f DAT", "2p i AKK"), ("1p n DAT", "2p n GEN"), ("1s n NOM", "1s i NOM"),
                ("2s f NOM", "1p n NOM"), ("1s f AKK", "1p i AKK"), ("1p f NOM", "1p i NOM"),
                ("1p f AKK", "2s i NOM"), ("2s n AKK", "2s f AKK"), ("1p n AKK", "1s n AKK"),
                ("1p n GEN", "1s f GEN"), ("2p f NOM", "2s i DAT"), ("2p f DAT", "2p n DAT"),
                ("2p n NOM", "2p i DAT"), ("2p i GEN", "2p i NOM"), ("2p f GEN", "2p n AKK")
            ])

        self.add_xross_perm_variation(
            [
                ("1s i AKK", "2p i NOM"), ("1s f GEN", "1s f NOM"), ("1s i GEN", "2p i DAT"),
                ("1s n DAT", "2p i AKK"), ("2s f AKK", "1s n GEN"), ("1p i DAT", "1p n DAT"),
                ("2s i AKK", "1s f DAT"), ("2s n GEN", "1s i NOM"), ("1p i NOM", "1p f NOM"),
                ("2s i NOM", "2s i DAT"), ("2s i GEN", "1p i GEN"), ("2p i GEN", "2p f GEN"),
                ("2s f DAT", "2s n NOM"), ("2s n AKK", "2p f AKK"), ("1p n GEN", "2s n DAT"),
                ("2p n AKK", "2s f NOM"), ("1s f AKK", "1s n NOM"), ("1s i DAT", "1s n AKK"),
                ("1p n NOM", "2p n NOM"), ("1p f AKK", "2s f GEN"), ("1p f DAT", "1p f GEN"),
                ("2p n GEN", "1p i AKK"), ("2p f DAT", "2p n DAT"), ("2p f NOM", "1p n AKK"),
            ])

        self.add_xross_perm_variation(
            [
                ("1s i AKK", "1s f AKK"), ("1p f DAT", "1p n DAT"), ("1p n GEN", "2p n AKK"),
                ("1s i NOM", "2s i AKK"), ("2p f AKK", "1p f NOM"), ("1s f GEN", "1s n GEN"),
                ("1p n AKK", "2s n NOM"), ("2s f NOM", "1p f AKK"), ("2p f GEN", "2p n GEN"),
                ("1p i NOM", "1s f DAT"), ("1s n DAT", "2p i AKK"), ("2p f NOM", "2p n NOM"),
                ("1s n NOM", "1s i DAT"), ("1p n NOM", "2s f DAT"), ("2s n DAT", "1s f NOM"),
                ("2s i DAT", "2p i NOM"), ("1s i GEN", "1p i DAT"), ("1s n AKK", "2p i GEN"),
                ("1p f GEN", "2p f DAT"), ("2s i NOM", "2p i DAT"), ("2s f AKK", "2s n AKK"),
                ("2s i GEN", "2p n DAT"), ("1p i GEN", "2s f GEN"), ("2s n GEN", "1p i AKK")
            ])

        self.add_xross_perm_variation(
            [("1p n GEN", "3s n NOM"), ("3p i AKK", "1p n AKK"), ("3s n GEN", "2s n DAT"),
             ("2s i DAT", "2s f DAT"), ("2p f DAT", "1s n AKK"), ("1p i AKK", "2p n AKK"),
             ("1s f NOM", "1s n DAT"), ("3s n AKK", "2s f NOM"), ("3p n NOM", "2s f GEN"),
             ("2p n DAT", "2p i NOM"), ("3s i NOM", "2s n AKK"), ("2p n GEN", "1p i GEN"),
             ("1s i AKK", "3p n GEN"), ("1p f NOM", "2s n GEN"), ("1s f DAT", "3s f DAT"),
             ("2s i GEN", "1p f AKK"), ("1s i DAT", "2s n NOM"), ("2p i DAT", "2s i NOM"),
             ("2p i AKK", "2p f AKK"), ("1p n NOM", "3p f GEN"), ("1p i DAT", "3p n DAT"),
             ])

        self.add_xross_perm_variation(
            [
                ("1s n LOC", "1s i INSTR"), ("2s i INSTR", "1s i NOM"), ("3s f INSTR", "3s f LOC"),
                ("1s i AKK", "1s n DAT"), ("1p n GEN", "2s i GEN"), ("3s i LOC", "1s f AKK"),
                ("2s f INSTR", "3s i NOM"), ("2s f GEN", "3s n NOM"), ("1s f NOM", "2p i INSTR"),
                ("2p n DAT", "2s n INSTR"), ("2p n GEN", "2s i NOM"), ("1s n NOM", "2p f DAT"),
                ("1p f DAT", "1p i DAT"), ("3s n GEN", "3p n DAT"), ("1p n DAT", "2s f NOM"),
                ("2s n GEN", "2p i GEN"), ("2p f GEN", "2s n NOM"), ("3s f NOM", "3s n LOC"),
                ("3p n GEN", "3p n AKK"), ("1p i GEN", "3p f INSTR"), ("1p f LOC", "3p f NOM"),
                ("3s i DAT", "3s n INSTR"), ("1p n AKK", "3p i NOM"), ("3p n NOM", "1p n NOM"),
                ("3s f GEN", "1p f GEN"), ("1p i AKK", "3p i INSTR"), ("1p i NOM", "1p f NOM"),
                ("1s f INSTR", "3s i GEN"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("2p g AKK", "2p g GEN"), ("1p g AKK", "2p g NOM"),
                ("1p g DAT", "2p g DAT"), ("1p g GEN", "1p g NOM"),
                ("3s f DAT", "3p f AKK"), ("3p i AKK", "3p f DAT"), ("3s i DAT", "3p n AKK"),
                ("3s n AKK", "3p n NOM"), ("3s n GEN", "3p n GEN"), ("3s f DAT", "3s n DAT")
            ])

        self.add_xross_perm_variation(
            [
                ("3s i GEN", "3p f DAT"), ("3p n DAT", "3s f GEN"), ("3s f DAT", "3s f AKK"),
                ("3s n NOM", "3s i DAT"), ("3s i AKK", "3p i DAT"), ("3s f NOM", "3p i NOM"),
                ("3p i GEN", "3p f GEN"), ("3p f NOM", "3p n AKK"), ("3s n AKK", "3s i NOM"),
                ("3p i AKK", "3p n GEN"), ("3p f AKK", "3p n NOM"), ("3s n DAT", "3s n GEN")
            ]
        )

        self.add_xross_perm_variation(
            [
                ("3s g GEN", "2s g NOM"), ("2s g GEN", "1p g GEN"), ("3s g DAT", "1s g AKK"),
                ("2s g DAT", "2p g GEN"), ("3s g NOM", "1p g DAT"), ("2s g AKK", "2p g AKK"),
                ("2p g NOM", "2p g DAT"), ("3p g NOM", "1s g GEN"), ("1p g AKK", "1p g NOM"),
                ("1s g DAT", "3p g DAT"), ("3p g GEN", "1s g NOM"), ("3p g AKK", "3s g AKK"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("3a g GEN", "2a g NOM"),
                ("2a g AKK", "1a g DAT"),
                ("1a g DAT", "2a g NOM"),
                ("3a g DAT", "3a g GEN"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("zd g GEN", "zs g NOM"),
                ("zd g LOC", "zp g GEN"),
                ("zp g INSTR", "zs g NOM"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("1s g LOC", "1s g DAT"),
                ("2d g LOC", "2s g NOM"),
                ("3p g LOC", "3s g GEN"),
                ("1p g INSTR", "2s g DAT"),
                ("2d g INSTR", "1s g NOM"),
                ("3p g INSTR", "3s g AKK"),
            ]
        )

        self.add_xross_perm_variation(
            [("3p g INSTR", "2s g INSTR")])

        self.add_xross_perm_variation(
            [("3s i LOC", "3s n GENs"),
             ("2s i DAT", "3s n INSTR")])

        self.add_xross_perm_variation(
            [("3s n AKK", "3s n INSTR"),
             ("3s n AKK", "3s n LOC")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g LOC"),
             ("2s g NOM", "2p g INSTR")])

        self.add_xross_perm_variation(
            [("2s g NOM", "3p g LOC")])

        self.add_xross_perm_variation(
            [("rs g GENs", "rp g LOC")])

        self.add_xross_perm_variation(
            [("rd g GENs", "rp g LOC")])

        self.add_xross_perm_variation(
            [("rs i GENs", "3p i INSTR"),
             ("rp v GENs", "3p v INSTR"),
             ("rp f GENs", "3p f INSTR"),
             ("rd n GENs", "3p n INSTR")])

        self.add_xross_perm_variation(
            [("rs i GENs", "3p i INSTR"),
             ("rp v GENs", "3p v INSTR"),
             ("rp f GENs", "3p f INSTR"),
             ("rd n GENs", "3p n INSTR"),

             ("rs i LOC", "3d i DAT"),
             ("rs v LOC", "3d v DAT"),
             ("rp f LOC", "3d f DAT"),
             ("rd n LOC", "3d n DAT")
             ])

        self.add_xross_perm_variation(
            [("rs i GENs", "3p i INSTR"),
             ("rs v GENs", "3p v INSTR"),
             ("rp f GENs", "3p f INSTR"),
             ("rd n GENs", "3p n INSTR"),

             ("rs i LOC", "3d i DAT"),
             ("rs v LOC", "3d v DAT"),
             ("rp f LOC", "3d f DAT"),
             ("rd n LOC", "3d n DAT"),

             ("rs i DAT", "3p i LOC"),
             ("rs v DAT", "3p v LOC"),
             ("rp f DAT", "3p f LOC"),
             ("rd n DAT", "3p n LOC"),

             ("rs i INSTR", "3d i GENs"),
             ("rs v INSTR", "3d v GENs"),
             ("rp f INSTR", "3d f GENs"),
             ("rd n INSTR", "3d n GENs")
             ])

        self.add_xross_perm_variation(
            [("1s g DAT", "1s g LOC"),
             ("3s f DAT", "3s i DAT"),
             ("3s f LOC", "3s i LOC")])

        self.add_xross_perm_variation(
            [("3s g NOM", "2p g LOC"),
             ("3s i GENs", "2p f DAT"),
             ("3s n GENs", "1s f NOM"),
             ("3s f DAT", "1p f NOM")])

        self.add_xross_perm_variation(
            [("1s g NOM", "2p g LOC"),
             ("2s g DAT", "2s g INSTR"),
             ("2s g AKK", "1p g LOC"),
             ("1p g GENs", "1s g INSTR"),
             ("2p g DAT", "2s g LOC"),
             ("3p g NOM", "1d g LOC"),
             ("1d g AKK", "3d g INSTR"),
             ("2d g GENs", "3p g LOC"),
             ("3d g NOM", "1d g INSTR")])

        self.add_xross_perm_variation(
            [("1p g AKK", "2p g INSTR"),
             ("1d g AKK", "2d g INSTR"),
             ("1s g DAT", "2s g LOC"),
             ("3s i AKK", "3s n DAT"),
             ("3s i NOM", "3s n LOC")])

        self.add_xross_perm_variation(
            [
                ("1s n INSTR", "1s i LOC"), ("2s i LOC", "1s i NOM"), ("3s f LOC", "3s f INSTR"),
                ("1s i AKK", "1s n DAT"), ("1p n GENs", "2s i GENs"), ("3s i INSTR", "1s f AKK"),
                ("2s f LOC", "3s i NOM"), ("2s f GENs", "3s n NOM"), ("1s f NOM", "2p i LOC"),
                ("2p n DAT", "2s n LOC"), ("2p n GENs", "2s i NOM"), ("1s n NOM", "2p f DAT"),
                ("1p f DAT", "1p i DAT"), ("3s n GENs", "3p n DAT"), ("1p n DAT", "2s f NOM"),
                ("2s n GENs", "2p i GENs"), ("2p f GENs", "2s n NOM"), ("3s f NOM", "3s n INSTR"),
                ("3p n GENs", "3p n AKK"), ("1p i GENs", "3p f LOC"), ("1p f INSTR", "3p f NOM"),
                ("3s i DAT", "3s n LOC"), ("1p n AKK", "3p i NOM"), ("3p n NOM", "1p n NOM"),
                ("3s f GENs", "1p f GENs"), ("1p i AKK", "3p i LOC"), ("1p i NOM", "1p f NOM"),
                ("1s f LOC", "3s i GENs"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("zd g GENs", "zs g NOM"),
                ("zd g INSTR", "zp g GENs"),
                ("zp g LOC", "zs g NOM"),
            ]
        )

        self.add_xross_perm_variation(
            [
                ("1s g INSTR", "1s g DAT"),
                ("2d g INSTR", "2s g NOM"),
                ("3p g INSTR", "3s g GENs"),
                ("1p g LOC", "2s g DAT"),
                ("2d g LOC", "1s g NOM"),
                ("3p g LOC", "3s g AKK"),
            ]
        )

        self.add_xross_perm_variation([("3p v AKK", "3p f DAT"),
                                       ("3p n INSTR", "3p f GEN"),
                                       ("3p f LOC", "3p v GEN"),
                                       ("3p v AKKs", "3p n GEN")
                                       ])

        self.add_xross_perm_variation([("3p f AKK", "3p n DAT"),
                                       ("3p f INSTR", "3p n GEN"),
                                       ("3p f LOC", "3p n GEN"),
                                       ("3p f AKKs", "3p n GEN")
                                       ])



        self.add_xross_perm_variation([("3p f AKK", "3p i DAT"),
                                       ("3p f INSTR", "3p v GEN"),
                                       ("3p f LOC", "3p i GEN"),
                                       ("3p f AKKs", "3p v GEN"),
                                       ("3p n AKK", "3p v DAT"),
                                       ("3p n INSTR", "3p i GEN"),
                                       ("3p n LOC", "3p v GEN"),
                                       ("3p n AKKs", "3p i GEN")
                                       ])


        self.add_xross_perm_variation([("2p g DAT", "1p g GEN"),
                                       ("2p g LOC", "1p g GENs"),
                                       ("2p g NOM", "1p g DATs")
                                       ])


        self.add_xross_perm_variation([("3p v AKK", "3p f DAT"),
                                       ("3p n INSTR", "3p f GEN"),
                                       ("3p f LOC", "3p v GEN"),
                                       ("3p v AKKs", "3p n GEN"),
                                       ("2p g DAT", "1p g GEN"),
                                       ("2p g LOC", "1p g GENs"),
                                       ("2p g NOM", "1p g DATs")
                                       ])


        self.add_xross_perm_variation([("3p v AKK", "3p f DAT"),
                                       ("3p n INSTR", "3p i GEN"),
                                       ("3p f LOC", "3p n GEN"),
                                       ("3p v AKKs", "3p i GEN"),
                                       ("2p g DAT", "1p g GEN"),
                                       ("2p g LOC", "1p g GENs"),
                                       ("2p g NOM", "1p g DATs")
                                       ])

        self.add_xross_perm_variation([("3a v AKK", "3a f DAT"),
                                       ("3a n INSTR", "3a f GEN"),
                                       ("3a f LOC", "3a v GEN"),
                                       ("3a v AKKs", "3a n GEN"),
                                       ("2a g DAT", "1a g GEN"),
                                       ("2a g LOC", "1a g GENs"),
                                       ("2a g NOM", "1a g DATs")
                                       ])



        self.add_xross_perm_variation([("3a f AKK", "3a v DAT"),
                                       ("3a f INSTR", "3a v GEN"),
                                       ("3a f LOC", "3a v GEN"),
                                       ("3a f AKKs", "3a v GEN"),
                                       ("3a n AKK", "3a i DAT"),
                                       ("3a n INSTR", "3a i GEN"),
                                       ("3a n LOC", "3a i GEN"),
                                       ("3a n AKKs", "3a i GEN"),
                                       ("2a g DAT", "1a g GEN"),
                                       ("2a g LOC", "1a g GENs"),
                                       ("2a g NOM", "1a g DATs")
                                       ])

    def _create_syncretic_PERS_files(self):
        self.add_pers_sync_variation([("1a g AKK", "2a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g DAT", "2a g DAT"), ("1a g GEN", "2a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g DAT", "3a g DAT"), ("2a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g DAT", "1a g DAT"), ("2a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g DAT", "3a g DAT"), ("1a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g DAT", "1a g DAT"), ("3a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g DAT", "2a g DAT"), ("3a g GEN", "2a g GEN")])

        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g GEN", "2a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g GEN", "3a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g GEN", "1a g GEN")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g GEN", "2a g GEN")])


        self.add_pers_sync_variation([("1a g AKK", "2a g AKK"), ("1a g INSTR", "2a g INSTR")])
        self.add_pers_sync_variation([("2a g AKK", "3a g AKK"), ("2a g INSTR", "3a g INSTR")])
        self.add_pers_sync_variation([("2a g AKK", "1a g AKK"), ("2a g INSTR", "1a g INSTR")])
        self.add_pers_sync_variation([("1a g AKK", "3a g AKK"), ("1a g INSTR", "3a g INSTR")])
        self.add_pers_sync_variation([("3a g AKK", "1a g AKK"), ("3a g INSTR", "1a g INSTR")])
        self.add_pers_sync_variation([("3a g AKK", "2a g AKK"), ("3a g INSTR", "2a g INSTR")])

        self.add_pers_sync_variation([("1s g AKK", "2s g AKK"),
                                      ("1p g DAT", "2p g DAT"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("3s g GEN", "rs g GEN")])


        self.add_pers_sync_variation([("1s g AKK", "3s g AKK"),
                                      ("2d g DAT", "3d g DAT"),
                                      ("1p g GEN", "2p g GEN")])


        self.add_pers_sync_variation([("1s i AKK", "3s i AKK"),
                                      ("2d f DAT", "3d f DAT")])


        self.add_pers_sync_variation([("1p g AKK", "2p g AKK"),
                                      ("1d g DAT", "2d g DAT"),
                                      ("1s g GEN", "2s g GEN")])


        self.add_pers_sync_variation([("1p g INSTR", "2p g INSTR"),
                                      ("1d g LOC", "2d g LOC")])


        self.add_pers_sync_variation([("2p g INSTR", "3p g INSTR"),
                                      ("2p g LOC", "3p g LOC")])

    def _create_syncretic_NUM_files(self):

        for p in ["1","2","3"]:
            self.add_num_sync_variation([(p+"s g INSTR", p+"p g INSTR")])
            self.add_num_sync_variation([(p+"s g LOC", p+"p g LOC")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g LOC", p+"p g LOC")])
            self.add_num_sync_variation([(p+"s g DAT", p+"p g DAT"),
                                         (p+"s g LOC", p+"p g LOC"),
                                         (p + "s g AKK", p + "p g AKK"),
                                         (p + "s g INSTR", p + "p g INSTR")
                                         ])


            self.add_num_sync_variation([(p+"s g INSTR", p+"p i INSTR"),
                                        (p+"s g LOC", p+"p i LOC")])

            self.add_num_sync_variation([(p+"s g INSTR", p+"d i INSTR"),
                                        (p+"s g LOC", p+"d i LOC")])

            self.add_num_sync_variation([(p+"s g t", p+"p g t")])

        self.add_num_sync_variation([("zs g t", "zp g t")])
        self.add_num_sync_variation([("zd g t", "zp g t")])
        self.add_num_sync_variation([("1s g t", "1p g t"),
                                     ("2s g t", "2p g t")])


    def _create_syncretic_GEN_files(self):
        #self.add_gen_sync_variation([("za g t", "za g t")])

        self.add_gen_sync_variation([("za f t", "za i t")])
        self.add_gen_sync_variation([("za n t", "za i t")])

        for p in self.PERSONS:
            self.add_gen_sync_variation([(p+"a f t", p+"a i t")])
            self.add_gen_sync_variation([(p+"a n t", p+"a i t")])

        for n in self.NUMBERS:
            self.add_gen_sync_variation([("z"+n+" f t", "z"+n+" i t")])
            self.add_gen_sync_variation([("z"+n+" n t", "z"+n+" i t")])


        for n in self.NUMBERS:
            for p in self.PERSONS:
                self.add_gen_sync_variation([(p+n+" f t", p+n+" i t")])
                self.add_gen_sync_variation([(p+n+" n t", p+n+" i t")])


        self.add_gen_sync_variation([("3s f t", "3s i t")])
        self.add_gen_sync_variation([("3s n t", "3s i t")])
        self.add_gen_sync_variation([("3p f t", "3p i t")])
        self.add_gen_sync_variation([("3p n t", "3p i t")])


        self.add_gen_sync_variation([("3s f t", "3s i t"),("3s n t", "3s i t")])
        self.add_gen_sync_variation([("3p f t", "3p i t"),("3p n t", "3p i t")])


        self.add_gen_sync_variation([("3s f t", "3s i t"),("3p n t", "3p i t")])
        self.add_gen_sync_variation([("3p f t", "3p i t"),("3s n t", "3s i t")])


        self.add_gen_sync_variation([("3s f AKK", "3s i AKK")])
        self.add_gen_sync_variation([("3s n DAT", "3s i DAT")])
        self.add_gen_sync_variation([("3p f GEN", "3p i GEN")])

        self.add_gen_sync_variation([("3s f AKK", "3s i AKK"), ("3s n AKK", "3s i AKK")])
        self.add_gen_sync_variation([("3s f DAT", "3s i DAT"), ("3s n DAT", "3s i DAT")])
        self.add_gen_sync_variation([("3s f GEN", "3s i GEN"), ("3s n GEN", "3s i GEN")])

        self.add_gen_sync_variation([("3s f DAT", "3s i DAT"), ("3s n DAT", "3s i DAT"),
                                     ("3s f GEN", "3s i GEN"), ("3s n GEN", "3s i GEN")])

        self.add_gen_sync_variation([("3s f AKK", "3s i AKK"), ("3s n DAT", "3s i DAT")])
        self.add_gen_sync_variation([("3s f DAT", "3s i DAT"), ("3s n LOC", "3s i LOC")])
        self.add_gen_sync_variation([("3s f INSTR", "3s i INSTR"), ("3s n GEN", "3s i GEN")])


        self.add_gen_sync_variation([("3p f t", "3p i LOC"), ("3p n t", "3p i LOC")])

        self.add_gen_sync_variation([("3s f NOM", "3s i NOM"), ("3p n GEN", "3p i GEN")])
        self.add_gen_sync_variation([("3p f NOM", "3p i NOM"), ("3s n AKK", "3s i AKK")])


    def _create_syncretic_TENSE_files(self):

        self.add_ten_sync_variation([("za g AKK", "za g GEN")])
        self.add_ten_sync_variation([("1a g AKK", "1a g GEN")])
        self.add_ten_sync_variation([("2a g AKK", "2a g GEN")])
        self.add_ten_sync_variation([("3a g AKK", "3a g GEN")])
        self.add_ten_sync_variation([("zs g AKK", "zs g GEN")])
        self.add_ten_sync_variation([("zd g AKK", "zd g GEN")])
        self.add_ten_sync_variation([("zp g AKK", "zp g GEN")])

        self.add_ten_sync_variation([("za g AKK", "za g GEN"),("za g DAT", "za g GEN")])
        self.add_ten_sync_variation([("1a g AKK", "1a g GEN"),("1a g DAT", "1a g GEN")])
        self.add_ten_sync_variation([("2a g AKK", "2a g GEN"),("2a g DAT", "2a g GEN")])
        self.add_ten_sync_variation([("3a g AKK", "3a g GEN"),("3a g DAT", "3a g GEN")])
        self.add_ten_sync_variation([("zs g AKK", "zs g GEN"),("zs g DAT", "zs g GEN")])
        self.add_ten_sync_variation([("zd g AKK", "zd g GEN"),("zd g DAT", "zd g GEN")])
        self.add_ten_sync_variation([("zp g AKK", "zp g GEN"),("zp g DAT", "zp g GEN")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT")])

        self.add_ten_sync_variation([("za g AKK", "za g DAT"),("za g INSTR", "za g LOC")])
        self.add_ten_sync_variation([("1a g AKK", "1a g DAT"),("1a g INSTR", "1a g LOC")])
        self.add_ten_sync_variation([("2a g AKK", "2a g DAT"),("2a g INSTR", "2a g LOC")])
        self.add_ten_sync_variation([("3a g AKK", "3a g DAT"),("3a g INSTR", "3a g LOC")])
        self.add_ten_sync_variation([("zs g AKK", "zs g DAT"),("zs g INSTR", "zs g LOC")])
        self.add_ten_sync_variation([("zd g AKK", "zd g DAT"),("zd g INSTR", "zd g LOC")])
        self.add_ten_sync_variation([("zp g AKK", "zp g DAT"),("zp g INSTR", "zp g LOC")])

    def _create_syncretic_X_files(self):
        self.add_xross_sync_variation([("3s f t", "3s i t"),("3s v t", "3s i t"),("3s n t", "3s i t")])

        self.add_xross_sync_variation([("3s f DAT", "3s i DAT"),("3s v DAT", "3s i DAT"),("3s n DAT", "3s i DAT"),
                                       ("3s f AKK", "3s i AKK"),("3s v AKK", "3s i AKK"),("3s n DAT", "3s i AKK")])


        self.add_xross_sync_variation([("1a g DATs", "2a g GENs"),("1a g NOM", "2a g AKKs")])


        self.add_xross_sync_variation([("1a g INSTR", "2a g AKK"),("2a g INSTR", "1a g DAT"),("ra g INSTR", "1a g LOC")])


        self.add_xross_sync_variation([("1s g INSTR", "2s g AKK"),("2s g INSTR", "1s g DAT"),("rs g INSTR", "1s g AKK")])
