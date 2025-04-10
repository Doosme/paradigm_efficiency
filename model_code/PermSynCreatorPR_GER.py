from PermSynCreator import PermSynCreator

class PermSynCreatorPR_GER_vh(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_GER"

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "d", "p"]
        self.PERSONS = ["1", "2v", "3", "2h"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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

        # add dual
        add_list_p = list()
        if d_list == list():
            for elem in cont_dict["NOM"].keys():
                if "p" in elem:
                    add_list_p.append(elem)
        for elem in add_list_p:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem.replace("p", "d")] = cont_dict[tense][elem]

        #print("A")
        #print(cont_dict["NOM"].keys())

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


        #print(cont_dict["NOM"].keys())


        # add reflexiv:
        for g in self.GENDERS:
            if "2hs "+g in cont_dict["NOM"].keys():
                if "2hp "+g not in cont_dict["NOM"].keys():
                    for tense in self.TENSES_CASES:
                        cont_dict[tense]["2hp "+g] = cont_dict[tense]["2hs "+g]
                if "2hd "+g not in cont_dict["NOM"].keys():
                    for tense in self.TENSES_CASES:
                        cont_dict[tense]["2hd "+g] = cont_dict[tense]["2hs "+g]

                pass
                #for tense in self.TENSES_CASES:
                #    cont_dict[tense]["2hs "+g] = cont_dict[tense]["2s "+g]
                #    cont_dict[tense]["2hd "+g] = cont_dict[tense]["2s "+g]
                #    cont_dict[tense]["2hp "+g] = cont_dict[tense]["2s "+g]
                #    cont_dict[tense]["2vs "+g] = cont_dict[tense]["2s "+g]
                #    cont_dict[tense]["2vd "+g] = cont_dict[tense]["2s "+g]
                #    cont_dict[tense]["2vp "+g] = cont_dict[tense]["2s "+g]
                #    del cont_dict[tense]["2s "+g]


        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict

    def _create_permutation_PERS_files(self):
        for t in ["AKK","DAT","GEN"]:
            self.add_pers_perm_variation([("1s g "+t, "2vs g "+t)])
            self.add_pers_perm_variation([("1d g "+t, "2vd g "+t),("1p g "+t, "2vp g "+t)])
            self.add_pers_perm_variation([("1a g "+t, "2va g "+t)])
            self.add_pers_perm_variation([("1a g "+t, "3a g "+t)])
            self.add_pers_perm_variation([("2va g "+t, "3a g "+t)])

            self.add_pers_perm_variation([("2va m "+t, "3a m "+t)])
            self.add_pers_perm_variation([("2va f "+t, "3a f "+t)])
            self.add_pers_perm_variation([("1a f "+t, "2va f "+t)])
            self.add_pers_perm_variation([("1a f "+t, "2va f "+t), ("1a n "+t, "2va n "+t)])

            self.add_pers_perm_variation(rotate_left_list=[("1s g "+t, "2vs g "+t, "3s g "+t)])
            self.add_pers_perm_variation(rotate_left_list=[("1d g "+t, "2vd g "+t, "3d g "+t)])
            self.add_pers_perm_variation(rotate_left_list=[("1d g "+t, "2vd g "+t, "3d g "+t),("1p g "+t, "2vp g "+t, "3p g "+t)])

        self.add_pers_perm_variation(
            rotate_left_list=[("1d g DAT", "2vd g DAT", "3d g DAT")],
                rotate_right_list=[("1p g AKK", "2vp g AKK", "3p g AKK")])


        self.add_pers_perm_variation(
    [("1d g DAT", "2vd g DAT"), ("1p g DAT", "2vp g DAT")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2vs g DAT")])

        self.add_pers_perm_variation(
            [("1a g DAT", "2va g DAT")])


        self.add_pers_perm_variation(
            [("1s g DAT", "2vs g DAT"),("1s g AKK", "2vs g AKK")])

        self.add_pers_perm_variation(
            rotate_left_list=[("1d m DAT", "2vd m DAT", "3d m DAT")],
                rotate_right_list=[("1p f AKK", "2vp f AKK", "3p f AKK")])


        self.add_pers_perm_variation(
            [("1d m DAT", "2vd m DAT"),
             ("1p f AKK", "2vp f AKK")])


        self.add_pers_perm_variation(
            [("2hs g t", "2vs g t"),("2hp g t", "2vp g t")])


    def _create_permutation_NUM_files(self):
        self.add_num_perm_variation([("3s g AKK", "3p g AKK")])
        self.add_num_perm_variation([("3s g GEN", "3p g GEN")])
        self.add_num_perm_variation([("3s m AKK", "3p m AKK")])
        self.add_num_perm_variation([("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation([("3s f t", "3p f t")])
        self.add_num_perm_variation([("3s n t", "3p n t")])

        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2vd g DAT", "2vd g DAT")])
        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2vd g DAT", "2vd g DAT"),("3p f NOM", "3s f NOM")])
        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2vd g DAT", "2vd g DAT"),("3s n NOM", "3p n NOM"),("3p f NOM", "3d f NOM")])

        self.add_num_perm_variation([("3p f NOM", "3s f NOM")])

        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM")])
        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM"),("3s g AKK", "3d g AKK", "3p g AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM"),("3s g AKK", "3d g AKK", "3p g AKK"),("3s g DAT", "3d g DAT", "3p g DAT")])

        self.add_num_perm_variation(rotate_left_list=[("zs g NOM", "zd g NOM", "zp g NOM"),("zs g DAT", "zd g DAT", "zp g DAT")],
                                    rotate_right_list=[("zs g AKK", "zd g AKK", "zp g AKK")])

        self.add_num_perm_variation(rotate_left_list=[("3s g AKK", "3d g AKK", "3p g AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g GEN", "3d g GEN", "3p g GEN")])
        self.add_num_perm_variation(rotate_left_list=[("3s m AKK", "3d m AKK", "3p m AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g AKK", "3d g AKK", "3p g AKK"),("3s g DAT", "3d g DAT", "3p g DAT")])
        self.add_num_perm_variation(rotate_left_list=[("3s m AKK", "3d m AKK", "3p m AKK"),("3s m DAT", "3d m DAT", "3p m DAT")])
        self.add_num_perm_variation(rotate_left_list=[("3s f AKK", "3d f AKK", "3p f AKK"),("3s n AKK", "3d n AKK", "3p n AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s n DAT", "3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(rotate_left_list=[("1s n DAT", "1d n DAT", "1p n DAT")])
        self.add_num_perm_variation(rotate_left_list=[("1s n DAT", "1d n DAT", "1p n DAT"),("1s n GEN", "1d n GEN", "1p n GEN")])

        self.add_num_perm_variation(rotate_left_list=[("1s n t", "1d n t", "1p n t")])
        self.add_num_perm_variation(rotate_left_list=[("2vs g t", "2vd g t", "2vp g t")])
        self.add_num_perm_variation(rotate_left_list=[("zs n AKK", "zd n AKK", "zp n AKK")])
        self.add_num_perm_variation(rotate_left_list=[("zs n AKK", "zd n AKK", "zp n AKK"),("zs n DAT", "zd n DAT", "zp n DAT")])

    def _create_permutation_TENSE_files(self):
        self.add_ten_perm_variation([("za g AKK", "za g DAT")])
        self.add_ten_perm_variation([("za g DAT", "za g AKK")])
        self.add_ten_perm_variation([("za g NOM", "za g AKK")])
        self.add_ten_perm_variation([("za g AKK", "za g NOM")])


        for p in self.PERSONS:
            self.add_ten_perm_variation([(p+"a g NOM", p+"a g AKK")])
            self.add_ten_perm_variation([(p+"a g DAT", p+"a g AKK")])
        for n in self.NUMBERS:
            self.add_ten_perm_variation([("z"+n+" g NOM", "z"+n+" g AKK")])
            self.add_ten_perm_variation([("z"+n+" g DAT", "z"+n+" g AKK")])
            for p in self.PERSONS:
                self.add_ten_perm_variation([(p+n+" g NOM", p+n+" g AKK")])
                self.add_ten_perm_variation([(p+n+" g DAT", p+n+" g AKK")])

        for g in self.GENDERS:
            self.add_ten_perm_variation([("za "+g+" NOM", "za "+g+" AKK")])
            self.add_ten_perm_variation([("za "+g+" DAT", "za "+g+" AKK")])

        self.add_ten_perm_variation(rotate_left_list=[("2vp g NOM", "2vp g AKK", "2vp g DAT")])
        self.add_ten_perm_variation(rotate_left_list=[("2ha g NOM", "2ha g AKK", "2ha g DAT")])
        self.add_ten_perm_variation(rotate_left_list=[("2ha g NOM", "2ha g AKK", "2ha g DAT"),
                                                      ("2vp g NOM", "2vp g AKK", "2vp g DAT")])


    def _create_permutation_GEN_files(self):
        self.add_gen_perm_variation([("3s m t", "3s n t")])
        self.add_gen_perm_variation([("3s m AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s m NOM", "3s n NOM")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK"),("3s f GEN", "3s m GEN")])
        self.add_gen_perm_variation([("3s f AKK", "3s m AKK")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3s m DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT"), ("3s f GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN"), ("3s f DAT", "3s m DAT")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN"), ("3s f DAT", "3s m DAT"), ("3s n AKK", "3s m AKK")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT"),("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f GEN", "3s m GEN"),("3s m DAT", "3s n DAT"), ("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3a f DAT", "3a n DAT"),("3a f AKK", "3a n AKK")])
        self.add_gen_perm_variation([("3a f GEN", "3a m GEN"),("3a m DAT", "3a n DAT"), ("3a f AKK", "3a n AKK")])

        self.add_gen_perm_variation([("3p f NOM", "3p m NOM"), ("3d f NOM", "3d m NOM")])

        self.add_gen_perm_variation([("3s f NOM", "3s n NOM"), ("3s f DAT", "3s m DAT")])

        self.add_gen_perm_variation([("3p f NOM", "3p m NOM"), ("3d f NOM", "3d m NOM"),
                                     ("3s f DAT", "3s m DAT"), ("3s f AKK", "3s n AKK")])

        self.add_gen_perm_variation([("3p f GEN", "3p m GEN"), ("3d f GEN", "3d m GEN"),
                                     ("3p n DAT", "3p m DAT"), ("3d n DAT", "3d m DAT")])
        self.add_gen_perm_variation([("3p f GEN", "3p m GEN"), ("3d f GEN", "3d m GEN")])

        self.add_gen_perm_variation([("3s m AKK", "3s n AKK"), ("3s m DAT", "3s n DAT"),("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m AKK", "3s f AKK"), ("3s f GEN", "3s n GEN"), ("3s m DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK"), ("3a m DAT", "3a n DAT"), ("3a m GEN", "3a n GEN")])
        self.add_gen_perm_variation([("3a m AKK", "3a f AKK"), ("3a f GEN", "3a n GEN"), ("3a m DAT", "3a n DAT")])

        self.add_gen_perm_variation([("3p m AKK", "3p f AKK")])
        self.add_gen_perm_variation([("3p m AKK", "3p n AKK")])
        self.add_gen_perm_variation([("3s m DAT", "3s f DAT"),("3s m GEN", "3s f GEN")])
        self.add_gen_perm_variation([("3p m AKK", "3p f AKK"), ("3p m NOM", "3p n NOM")])
        self.add_gen_perm_variation([("3p m AKK", "3p f AKK"), ("3p m NOM", "3p n NOM"),
                                     ("3d m AKK", "3p f AKK"), ("3d m NOM", "3d n NOM")])
        self.add_gen_perm_variation([("3p m DAT", "3p f DAT"), ("3p m GEN", "3p n GEN"),
                                     ("3d m DAT", "3p f DAT"), ("3d m GEN", "3d n GEN")])
        self.add_gen_perm_variation([("3s m DAT", "3s f DAT"), ("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m DAT", "3s n DAT"), ("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m AKK", "3s n AKK"),("3s m DAT", "3s n DAT"), ("3s m GEN", "3s n GEN")])


        self.add_gen_perm_variation([("3p f AKK", "3p n AKK")])
        self.add_gen_perm_variation([("3p f AKK", "3p n AKK"),("3d f AKK", "3d n AKK")])
        self.add_gen_perm_variation([("3a f AKK", "3a n AKK")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK")])


        self.add_gen_perm_variation([("3a m DAT", "3a n DAT"),("3a m GEN", "3a n GEN")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK"),("3a m GEN", "3a f GEN")])

    def _create_permutation_X_files(self):
        pass



    def _create_syncretic_PERS_files(self):
        pass
    def _create_syncretic_NUM_files(self):
        pass
    def _create_syncretic_TENSE_files(self):
        self.add_ten_sync_variation([("za g AKK", "za g DAT")])
        self.add_ten_sync_variation([("za g DAT", "za g AKK")])
        self.add_ten_sync_variation([("za g NOM", "za g AKK")])
        self.add_ten_sync_variation([("za g AKK", "za g NOM")])
        self.add_ten_sync_variation([("za g AKK", "za g NOM"),
                                     ("za g DAT", "za g NOM")])

        for p in self.PERSONS:
            self.add_ten_sync_variation([(p+"a g NOM", p+"a g AKK")])
            self.add_ten_sync_variation([(p+"a g DAT", p+"a g AKK")])

        for n in self.NUMBERS:
            self.add_ten_sync_variation([("z"+n+" g NOM", "z"+n+" g AKK")])
            self.add_ten_sync_variation([("z"+n+" g DAT", "z"+n+" g AKK")])
            for p in self.PERSONS:
                self.add_ten_sync_variation([(p+n+" g NOM", p+n+" g AKK")])
                self.add_ten_sync_variation([(p+n+" g DAT", p+n+" g AKK")])

        self.add_ten_sync_variation([("2vp g AKK", "2vp g NOM"),
                                     ("2vp g DAT", "2vp g NOM"),
                                     ("2vp g GEN", "2vp g NOM")])




    def _create_syncretic_GEN_files(self):
        pass

    def _create_syncretic_X_files(self):
        pass


class PermSynCreatorPR_GER(PermSynCreator):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_GER"

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "d", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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

        # add dual
        add_list_p = list()
        if d_list == list():
            for elem in cont_dict["NOM"].keys():
                if "p" in elem:
                    add_list_p.append(elem)
        for elem in add_list_p:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem.replace("p", "d")] = cont_dict[tense][elem]

        #print("A")
        #print(cont_dict["NOM"].keys())

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


        #print(cont_dict["NOM"].keys())


        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat in cont_dict[tense].keys():
                res_dict[feat+" "+tense] = cont_dict[tense][feat]

        return res_dict

    def _create_permutation_PERS_files(self):
        for t in ["AKK","DAT","GEN"]:
            self.add_pers_perm_variation([("1s g "+t, "2s g "+t)])
            self.add_pers_perm_variation([("1d g "+t, "2d g "+t),("1p g "+t, "2p g "+t)])
            self.add_pers_perm_variation([("1a g "+t, "2a g "+t)])
            self.add_pers_perm_variation([("1a g "+t, "3a g "+t)])
            self.add_pers_perm_variation([("2a g "+t, "3a g "+t)])

            self.add_pers_perm_variation([("2a m "+t, "3a m "+t)])
            self.add_pers_perm_variation([("2a f "+t, "3a f "+t)])
            self.add_pers_perm_variation([("1a f "+t, "2a f "+t)])
            self.add_pers_perm_variation([("1a f "+t, "2a f "+t), ("1a n "+t, "2a n "+t)])

            self.add_pers_perm_variation(rotate_left_list=[("1s g "+t, "2s g "+t, "3s g "+t)])
            self.add_pers_perm_variation(rotate_left_list=[("1d g "+t, "2d g "+t, "3d g "+t)])
            self.add_pers_perm_variation(rotate_left_list=[("1d g "+t, "2d g "+t, "3d g "+t),("1p g "+t, "2p g "+t, "3p g "+t)])

        self.add_pers_perm_variation(
            rotate_left_list=[("1d g DAT", "2d g DAT", "3d g DAT")],
                rotate_right_list=[("1p g AKK", "2p g AKK", "3p g AKK")])


        self.add_pers_perm_variation(
    [("1d g DAT", "2d g DAT"), ("1p g DAT", "2p g DAT")])

        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT")])

        self.add_pers_perm_variation(
            [("1a g DAT", "2a g DAT")])


        self.add_pers_perm_variation(
            [("1s g DAT", "2s g DAT"),("1s g AKK", "2s g AKK")])

        self.add_pers_perm_variation(
            rotate_left_list=[("1d m DAT", "2d m DAT", "3d m DAT")],
                rotate_right_list=[("1p f AKK", "2p f AKK", "3p f AKK")])


        self.add_pers_perm_variation(
            [("1d m DAT", "2d m DAT"),
             ("1p f AKK", "2p f AKK")])


        self.add_pers_perm_variation(
            [("2s g t", "2s g t"),("2p g t", "2p g t")])


    def _create_permutation_NUM_files(self):
        self.add_num_perm_variation([("3s g AKK", "3p g AKK")])
        self.add_num_perm_variation([("3s g GEN", "3p g GEN")])
        self.add_num_perm_variation([("3s m AKK", "3p m AKK")])
        self.add_num_perm_variation([("3s n DAT", "3p n DAT")])

        self.add_num_perm_variation([("3s f t", "3p f t")])
        self.add_num_perm_variation([("3s n t", "3p n t")])

        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2d g DAT", "2d g DAT")])
        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2d g DAT", "2d g DAT"),("3p f NOM", "3s f NOM")])
        self.add_num_perm_variation([("1p g AKK", "1s g AKK"),("2d g DAT", "2d g DAT"),("3s n NOM", "3p n NOM"),("3p f NOM", "3d f NOM")])

        self.add_num_perm_variation([("3p f NOM", "3s f NOM")])

        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM")])
        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM"),("3s g AKK", "3d g AKK", "3p g AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g NOM", "3d g NOM", "3p g NOM"),("3s g AKK", "3d g AKK", "3p g AKK"),("3s g DAT", "3d g DAT", "3p g DAT")])

        self.add_num_perm_variation(rotate_left_list=[("zs g NOM", "zd g NOM", "zp g NOM"),("zs g DAT", "zd g DAT", "zp g DAT")],
                                    rotate_right_list=[("zs g AKK", "zd g AKK", "zp g AKK")])

        self.add_num_perm_variation(rotate_left_list=[("3s g AKK", "3d g AKK", "3p g AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g GEN", "3d g GEN", "3p g GEN")])
        self.add_num_perm_variation(rotate_left_list=[("3s m AKK", "3d m AKK", "3p m AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s g AKK", "3d g AKK", "3p g AKK"),("3s g DAT", "3d g DAT", "3p g DAT")])
        self.add_num_perm_variation(rotate_left_list=[("3s m AKK", "3d m AKK", "3p m AKK"),("3s m DAT", "3d m DAT", "3p m DAT")])
        self.add_num_perm_variation(rotate_left_list=[("3s f AKK", "3d f AKK", "3p f AKK"),("3s n AKK", "3d n AKK", "3p n AKK")])
        self.add_num_perm_variation(rotate_left_list=[("3s n DAT", "3d n DAT", "3p n DAT")])

        self.add_num_perm_variation(rotate_left_list=[("1s n DAT", "1d n DAT", "1p n DAT")])
        self.add_num_perm_variation(rotate_left_list=[("1s n DAT", "1d n DAT", "1p n DAT"),("1s n GEN", "1d n GEN", "1p n GEN")])

        self.add_num_perm_variation(rotate_left_list=[("1s n t", "1d n t", "1p n t")])
        self.add_num_perm_variation(rotate_left_list=[("2s g t", "2d g t", "2p g t")])
        self.add_num_perm_variation(rotate_left_list=[("zs n AKK", "zd n AKK", "zp n AKK")])
        self.add_num_perm_variation(rotate_left_list=[("zs n AKK", "zd n AKK", "zp n AKK"),("zs n DAT", "zd n DAT", "zp n DAT")])

    def _create_permutation_TENSE_files(self):
        self.add_ten_perm_variation([("za g AKK", "za g DAT")])
        self.add_ten_perm_variation([("za g DAT", "za g AKK")])
        self.add_ten_perm_variation([("za g NOM", "za g AKK")])
        self.add_ten_perm_variation([("za g AKK", "za g NOM")])


        for p in self.PERSONS:
            self.add_ten_perm_variation([(p+"a g NOM", p+"a g AKK")])
            self.add_ten_perm_variation([(p+"a g DAT", p+"a g AKK")])
        for n in self.NUMBERS:
            self.add_ten_perm_variation([("z"+n+" g NOM", "z"+n+" g AKK")])
            self.add_ten_perm_variation([("z"+n+" g DAT", "z"+n+" g AKK")])
            for p in self.PERSONS:
                self.add_ten_perm_variation([(p+n+" g NOM", p+n+" g AKK")])
                self.add_ten_perm_variation([(p+n+" g DAT", p+n+" g AKK")])

        for g in self.GENDERS:
            self.add_ten_perm_variation([("za "+g+" NOM", "za "+g+" AKK")])
            self.add_ten_perm_variation([("za "+g+" DAT", "za "+g+" AKK")])

        self.add_ten_perm_variation(rotate_left_list=[("2p g NOM", "2p g AKK", "2p g DAT")])
        self.add_ten_perm_variation(rotate_left_list=[("2a g NOM", "2a g AKK", "2a g DAT")])
        self.add_ten_perm_variation(rotate_left_list=[("2a g NOM", "2a g AKK", "2a g DAT"),
                                                      ("2p g NOM", "2p g AKK", "2p g DAT")])


    def _create_permutation_GEN_files(self):
        self.add_gen_perm_variation([("3s m t", "3s n t")])
        self.add_gen_perm_variation([("3s m AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s m NOM", "3s n NOM")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK"),("3s f GEN", "3s m GEN")])
        self.add_gen_perm_variation([("3s f AKK", "3s m AKK")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3s m DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT"), ("3s f GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN"), ("3s f DAT", "3s m DAT")])
        self.add_gen_perm_variation([("3s f GEN", "3s n GEN"), ("3s f DAT", "3s m DAT"), ("3s n AKK", "3s m AKK")])
        self.add_gen_perm_variation([("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f DAT", "3s n DAT"),("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3s f GEN", "3s m GEN"),("3s m DAT", "3s n DAT"), ("3s f AKK", "3s n AKK")])
        self.add_gen_perm_variation([("3a f DAT", "3a n DAT"),("3a f AKK", "3a n AKK")])
        self.add_gen_perm_variation([("3a f GEN", "3a m GEN"),("3a m DAT", "3a n DAT"), ("3a f AKK", "3a n AKK")])

        self.add_gen_perm_variation([("3p f NOM", "3p m NOM"), ("3d f NOM", "3d m NOM")])

        self.add_gen_perm_variation([("3s f NOM", "3s n NOM"), ("3s f DAT", "3s m DAT")])

        self.add_gen_perm_variation([("3p f NOM", "3p m NOM"), ("3d f NOM", "3d m NOM"),
                                     ("3s f DAT", "3s m DAT"), ("3s f AKK", "3s n AKK")])

        self.add_gen_perm_variation([("3p f GEN", "3p m GEN"), ("3d f GEN", "3d m GEN"),
                                     ("3p n DAT", "3p m DAT"), ("3d n DAT", "3d m DAT")])
        self.add_gen_perm_variation([("3p f GEN", "3p m GEN"), ("3d f GEN", "3d m GEN")])

        self.add_gen_perm_variation([("3s m AKK", "3s n AKK"), ("3s m DAT", "3s n DAT"),("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m AKK", "3s f AKK"), ("3s f GEN", "3s n GEN"), ("3s m DAT", "3s n DAT")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK"), ("3a m DAT", "3a n DAT"), ("3a m GEN", "3a n GEN")])
        self.add_gen_perm_variation([("3a m AKK", "3a f AKK"), ("3a f GEN", "3a n GEN"), ("3a m DAT", "3a n DAT")])

        self.add_gen_perm_variation([("3p m AKK", "3p f AKK")])
        self.add_gen_perm_variation([("3p m AKK", "3p n AKK")])
        self.add_gen_perm_variation([("3s m DAT", "3s f DAT"),("3s m GEN", "3s f GEN")])
        self.add_gen_perm_variation([("3p m AKK", "3p f AKK"), ("3p m NOM", "3p n NOM")])
        self.add_gen_perm_variation([("3p m AKK", "3p f AKK"), ("3p m NOM", "3p n NOM"),
                                     ("3d m AKK", "3p f AKK"), ("3d m NOM", "3d n NOM")])
        self.add_gen_perm_variation([("3p m DAT", "3p f DAT"), ("3p m GEN", "3p n GEN"),
                                     ("3d m DAT", "3p f DAT"), ("3d m GEN", "3d n GEN")])
        self.add_gen_perm_variation([("3s m DAT", "3s f DAT"), ("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m DAT", "3s n DAT"), ("3s m GEN", "3s n GEN")])
        self.add_gen_perm_variation([("3s m AKK", "3s n AKK"),("3s m DAT", "3s n DAT"), ("3s m GEN", "3s n GEN")])


        self.add_gen_perm_variation([("3p f AKK", "3p n AKK")])
        self.add_gen_perm_variation([("3p f AKK", "3p n AKK"),("3d f AKK", "3d n AKK")])
        self.add_gen_perm_variation([("3a f AKK", "3a n AKK")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK")])


        self.add_gen_perm_variation([("3a m DAT", "3a n DAT"),("3a m GEN", "3a n GEN")])
        self.add_gen_perm_variation([("3a m AKK", "3a n AKK"),("3a m GEN", "3a f GEN")])

    def _create_permutation_X_files(self):
        pass



    def _create_syncretic_PERS_files(self):
        pass
    def _create_syncretic_NUM_files(self):
        pass
    def _create_syncretic_TENSE_files(self):
        self.add_ten_sync_variation([("za g AKK", "za g DAT")])
        self.add_ten_sync_variation([("za g DAT", "za g AKK")])
        self.add_ten_sync_variation([("za g NOM", "za g AKK")])
        self.add_ten_sync_variation([("za g AKK", "za g NOM")])
        self.add_ten_sync_variation([("za g AKK", "za g NOM"),
                                     ("za g DAT", "za g NOM")])

        for p in self.PERSONS:
            self.add_ten_sync_variation([(p+"a g NOM", p+"a g AKK")])
            self.add_ten_sync_variation([(p+"a g DAT", p+"a g AKK")])

        for n in self.NUMBERS:
            self.add_ten_sync_variation([("z"+n+" g NOM", "z"+n+" g AKK")])
            self.add_ten_sync_variation([("z"+n+" g DAT", "z"+n+" g AKK")])
            for p in self.PERSONS:
                self.add_ten_sync_variation([(p+n+" g NOM", p+n+" g AKK")])
                self.add_ten_sync_variation([(p+n+" g DAT", p+n+" g AKK")])

        self.add_ten_sync_variation([("2p g AKK", "2p g NOM"),
                                     ("2p g DAT", "2p g NOM"),
                                     ("2p g GEN", "2p g NOM")])




    def _create_syncretic_GEN_files(self):
        pass

    def _create_syncretic_X_files(self):
        pass


class PermSynCreatorPR_GREEK(PermSynCreatorPR_GER):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "PR_GREEK"

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "d", "p"]
        self.PERSONS = ["1", "2", "3"]
        self.TENSES_CASES = ["NOM", "AKK", "DAT", "GEN"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in
                         self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40

class PermSynCreatorPR_INDIRA_S(PermSynCreatorPR_GER):

    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)

        self.GENDERS = ["m", "f", "n"]
        self.NUMBERS = ["s", "p", "d"]
        self.PERSONS = ["1", "2", "3"]

        self.TENSES_CASES = ["NOM", "AKK", "INSTR", "DAT", "ABL", "GEN", "LOC"]

        self.COMBINED = [p + n + " " + g + " " + t for t in self.TENSES_CASES for n in self.NUMBERS for p in
                         self.PERSONS for g in self.GENDERS]

        self.shuffle_length = 40