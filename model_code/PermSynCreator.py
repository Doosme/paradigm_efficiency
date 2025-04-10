import os

import random
random.seed(1234)

import copy

class PermSynCreator:
    def __init__(self, lang_name, file_ending=".tsv"):
        # dictionary of dictionary containing the permutated conjugation tables.
        # FORMAT: {filename: {feat1 : conj1,...}...}
        self.permutation_dicts = dict()

        # dictionary containing the original conjugation table
        # FORMAT: {feat1 : conj1,...}
        self.org_conj_dict = dict()

        self.lang_type = ""

        self.read_directory = None
        self.write_directory = None

        self.lang_name = lang_name
        self._file_ending = file_ending

        self.pers_perm_count = 0
        self.num_perm_count = 0
        self.ten_perm_count = 0
        self.gen_perm_count = 0
        self.x_perm_count = 0
        self.pers_sync_count = 0
        self.num_sync_count = 0
        self.ten_sync_count = 0
        self.gen_sync_count = 0
        self.x_sync_count = 0
        self.full_var_count = 0 #not used?

        self.GENDERS = ["m","f"]
        self.NUMBERS = ["s","p","d"]
        self.PERSONS = ["1","2","3"]
        self.TENSES_CASES = ["G","V"]

        self.base_length = 1
        self.shuffle_length = 20

    #@staticmethod
    #def _permute_list(perm_dict, swap_list):
    #    for feat1, feat2 in swap_list:
    #        _swap(perm_dict, feat1, feat2)

    @staticmethod
    def _swap(perm_dict, features1, features2):
        perm_dict[features1], perm_dict[features2] = perm_dict[features2], perm_dict[features1]

    @staticmethod
    def _map(perm_dict, features1, features2):
        #maps surface form of feat2 onto feat1. i.e f1 -> f2?
        perm_dict[features1] = perm_dict[features2]

    @staticmethod
    def _rotate_right(perm_dict, f1, f2, f3):
        # 1 -> 2 -> 3
        perm_dict[f1], perm_dict[f2], perm_dict[f3] = perm_dict[f3], perm_dict[f1], perm_dict[f2]

    @staticmethod
    def _rotate_left(perm_dict, f1, f2, f3):
        # 1 <- 2 <- 3
        perm_dict[f1], perm_dict[f2], perm_dict[f3] = perm_dict[f2], perm_dict[f3], perm_dict[f1]

    def _swap_gnzt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    for t in self.TENSES_CASES:
                        self._swap(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                               f2.replace("g", g).replace("a", n).replace("z", z).replace("t", t))
    def _swap_gnt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for t in self.TENSES_CASES:
                    self._swap(cur_perm, f1.replace("g", g).replace("a", n).replace("t", t),
                               f2.replace("g", g).replace("a", n).replace("t", t))
    def _swap_gzt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._swap(cur_perm, f1.replace("g", g).replace("z", z).replace("t", t),
                               f2.replace("g", g).replace("z", z).replace("t", t))
    def _swap_nzt(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._swap(cur_perm, f1.replace("a", n).replace("z", z).replace("t", t),
                           f2.replace("a", n).replace("z", z).replace("t", t))
    def _swap_nt(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for t in self.TENSES_CASES:
                self._swap(cur_perm, f1.replace("a", n).replace("t", t),f2.replace("a", n).replace("t", t))
    def _swap_gt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for t in self.TENSES_CASES:
                self._swap(cur_perm, f1.replace("g", g).replace("t", t),f2.replace("g", g).replace("t", t))
    def _swap_zt(self, cur_perm, f1, f2):
        for z in self.PERSONS:
            for t in self.TENSES_CASES:
                self._swap(cur_perm, f1.replace("z", z).replace("t", t), f2.replace("z", z).replace("t", t))

    def _swap_gnz(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    self._swap(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z),
                               f2.replace("g", g).replace("a", n).replace("z", z))
    def _swap_gn(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                self._swap(cur_perm, f1.replace("g", g).replace("a", n),
                               f2.replace("g", g).replace("a", n))
    def _swap_gz(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for z in self.PERSONS:
                self._swap(cur_perm, f1.replace("g", g).replace("z", z),
                               f2.replace("g", g).replace("z", z))
    def _swap_nz(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                self._swap(cur_perm, f1.replace("a", n).replace("z", z),
                           f2.replace("a", n).replace("z", z))
    def _swap_n(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
                self._swap(cur_perm, f1.replace("a", n),f2.replace("a", n))
    def _swap_g(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            self._swap(cur_perm, f1.replace("g", g),f2.replace("g", g))
    def _swap_z(self, cur_perm, f1, f2):
        for z in self.PERSONS:
            self._swap(cur_perm, f1.replace("z", z), f2.replace("z", z))
    def _swap_t(self, cur_perm, f1, f2):
        for t in self.TENSES_CASES:
            self._swap(cur_perm, f1.replace("t", t), f2.replace("t", t))

    def _rotate_left_gnz(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    self._rotate_left(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z),
                                       f2.replace("g", g).replace("a", n).replace("z", z),
                                       f3.replace("g", g).replace("a", n).replace("z", z)
                                       )
    def _rotate_left_gn(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                self._rotate_left(cur_perm, f1.replace("g", g).replace("a", n),
                                   f2.replace("g", g).replace("a", n),
                                   f3.replace("g", g).replace("a", n))
    def _rotate_left_gz(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for z in self.PERSONS:
                self._rotate_left(cur_perm, f1.replace("g", g).replace("z", z),
                                   f2.replace("g", g).replace("z", z),
                                   f3.replace("g", g).replace("z", z))
    def _rotate_left_nz(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                self._rotate_left(cur_perm, f1.replace("a", n).replace("z", z),
                                   f2.replace("a", n).replace("z", z),
                                   f3.replace("a", n).replace("z", z))
    def _rotate_left_n(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            self._rotate_left(cur_perm, f1.replace("a", n), f2.replace("a", n), f3.replace("a", n))
    def _rotate_left_g(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            self._rotate_left(cur_perm, f1.replace("g", g), f2.replace("g", g), f3.replace("g", g))
    def _rotate_left_z(self, cur_perm, f1, f2, f3):
        for z in self.PERSONS:
            self._rotate_left(cur_perm, f1.replace("z", z), f2.replace("z", z), f3.replace("z", z))

    def _rotate_left_gnzt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    for t in self.TENSES_CASES:
                        self._rotate_left(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                                       f2.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                                       f3.replace("g", g).replace("a", n).replace("z", z).replace("t", t)
                                       )
    def _rotate_left_gnt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for t in self.TENSES_CASES:
                    self._rotate_left(cur_perm, f1.replace("g", g).replace("a", n).replace("t", t),
                                   f2.replace("g", g).replace("a", n).replace("t", t),
                                   f3.replace("g", g).replace("a", n).replace("t", t))
    def _rotate_left_gzt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._rotate_left(cur_perm, f1.replace("g", g).replace("z", z).replace("t", t),
                                   f2.replace("g", g).replace("z", z).replace("t", t),
                                   f3.replace("g", g).replace("z", z).replace("t", t))
    def _rotate_left_nzt(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._rotate_left(cur_perm, f1.replace("a", n).replace("z", z).replace("t", t),
                                   f2.replace("a", n).replace("z", z).replace("t", t),
                                   f3.replace("a", n).replace("z", z).replace("t", t))
    def _rotate_left_nt(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for t in self.TENSES_CASES:
                self._rotate_left(cur_perm, f1.replace("a", n).replace("t", t), f2.replace("a", n).replace("t", t), f3.replace("a", n).replace("t", t))
    def _rotate_left_gt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for t in self.TENSES_CASES:
                self._rotate_left(cur_perm, f1.replace("g", g).replace("t", t), f2.replace("g", g).replace("t", t), f3.replace("g", g).replace("t", t))
    def _rotate_left_zt(self, cur_perm, f1, f2, f3):
        for z in self.PERSONS:
            for t in self.TENSES_CASES:
                self._rotate_left(cur_perm, f1.replace("z", z).replace("t", t), f2.replace("z", z).replace("t", t), f3.replace("z", z).replace("t", t))
    def _rotate_left_t(self, cur_perm, f1, f2, f3):
        for t in self.TENSES_CASES:
            self._rotate_left(cur_perm, f1.replace("t", t), f2.replace("t", t), f3.replace("t", t))

    def _rotate_right_gnz(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    self._rotate_right(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z),
                                       f2.replace("g", g).replace("a", n).replace("z", z),
                                       f3.replace("g", g).replace("a", n).replace("z", z)
                                       )
    def _rotate_right_gn(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                self._rotate_right(cur_perm, f1.replace("g", g).replace("a", n),
                                   f2.replace("g", g).replace("a", n),
                                   f3.replace("g", g).replace("a", n))
    def _rotate_right_gz(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for z in self.PERSONS:
                self._rotate_right(cur_perm, f1.replace("g", g).replace("z", z),
                                   f2.replace("g", g).replace("z", z),
                                   f3.replace("g", g).replace("z", z))
    def _rotate_right_nz(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                self._rotate_right(cur_perm, f1.replace("a", n).replace("z", z),
                                   f2.replace("a", n).replace("z", z),
                                   f3.replace("a", n).replace("z", z))
    def _rotate_right_n(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            self._rotate_right(cur_perm, f1.replace("a", n), f2.replace("a", n), f3.replace("a", n))
    def _rotate_right_g(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            self._rotate_right(cur_perm, f1.replace("g", g), f2.replace("g", g), f3.replace("g", g))
    def _rotate_right_z(self, cur_perm, f1, f2, f3):
        for z in self.PERSONS:
            self._rotate_right(cur_perm, f1.replace("z", z), f2.replace("z", z), f3.replace("z", z))
    def _rotate_right_gnzt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    for t in self.TENSES_CASES:
                        self._rotate_right(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                                        f2.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                                        f3.replace("g", g).replace("a", n).replace("z", z).replace("t", t)
                                        )
    def _rotate_right_gnt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for t in self.TENSES_CASES:
                    self._rotate_right(cur_perm, f1.replace("g", g).replace("a", n).replace("t", t),
                                   f2.replace("g", g).replace("a", n).replace("t", t),
                                   f3.replace("g", g).replace("a", n).replace("t", t))
    def _rotate_right_gzt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._rotate_right(cur_perm, f1.replace("g", g).replace("z", z).replace("t", t),
                                   f2.replace("g", g).replace("z", z).replace("t", t),
                                   f3.replace("g", g).replace("z", z).replace("t", t))
    def _rotate_right_nzt(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._rotate_right(cur_perm, f1.replace("a", n).replace("z", z).replace("t", t),
                                       f2.replace("a", n).replace("z", z).replace("t", t),
                                       f3.replace("a", n).replace("z", z).replace("t", t))
    def _rotate_right_nt(self, cur_perm, f1, f2, f3):
        for n in self.NUMBERS:
            for t in self.TENSES_CASES:
                self._rotate_right(cur_perm, f1.replace("a", n).replace("t", t), f2.replace("a", n).replace("t", t), f3.replace("a", n).replace("t", t))
    def _rotate_right_gt(self, cur_perm, f1, f2, f3):
        for g in self.GENDERS:
            for t in self.TENSES_CASES:
                self._rotate_right(cur_perm, f1.replace("g", g).replace("t", t), f2.replace("g", g).replace("t", t), f3.replace("g", g).replace("t", t))
    def _rotate_right_zt(self, cur_perm, f1, f2, f3):
        for z in self.PERSONS:
            for t in self.TENSES_CASES:
                self._rotate_right(cur_perm, f1.replace("z", z).replace("t", t), f2.replace("z", z).replace("t", t), f3.replace("z", z).replace("t", t))
    def _rotate_right_t(self, cur_perm, f1, f2, f3):
        for t in self.TENSES_CASES:
            self._rotate_right(cur_perm, f1.replace("t", t), f2.replace("t", t), f3.replace("t", t))

    def _map_gnzt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    for t in self.TENSES_CASES:
                        self._map(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z).replace("t", t),
                               f2.replace("g", g).replace("a", n).replace("z", z).replace("t", t))
    def _map_gnt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for t in self.TENSES_CASES:
                    self._map(cur_perm, f1.replace("g", g).replace("a", n).replace("t", t),
                                   f2.replace("g", g).replace("a", n).replace("t", t))
    def _map_gzt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._map(cur_perm, f1.replace("g", g).replace("z", z).replace("t", t),
                               f2.replace("g", g).replace("z", z).replace("t", t))
    def _map_nzt(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                for t in self.TENSES_CASES:
                    self._map(cur_perm, f1.replace("a", n).replace("z", z).replace("t", t),
                           f2.replace("a", n).replace("z", z).replace("t", t))
    def _map_nt(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for t in self.TENSES_CASES:
                self._map(cur_perm, f1.replace("a", n).replace("t", t),f2.replace("a", n).replace("t", t))
    def _map_gt(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for t in self.TENSES_CASES:
                self._map(cur_perm, f1.replace("g", g).replace("t", t),f2.replace("g", g).replace("t", t))
    def _map_zt(self, cur_perm, f1, f2):
        for z in self.PERSONS:
            for t in self.TENSES_CASES:
                self._map(cur_perm, f1.replace("z", z).replace("t", t), f2.replace("z", z).replace("t", t))
    def _map_gnz(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                for z in self.PERSONS:
                    self._map(cur_perm, f1.replace("g", g).replace("a", n).replace("z", z),
                               f2.replace("g", g).replace("a", n).replace("z", z))
    def _map_gn(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for n in self.NUMBERS:
                self._map(cur_perm, f1.replace("g", g).replace("a", n),
                               f2.replace("g", g).replace("a", n))
    def _map_gz(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            for z in self.PERSONS:
                self._map(cur_perm, f1.replace("g", g).replace("z", z),
                               f2.replace("g", g).replace("z", z))
    def _map_nz(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
            for z in self.PERSONS:
                self._map(cur_perm, f1.replace("a", n).replace("z", z),
                           f2.replace("a", n).replace("z", z))
    def _map_n(self, cur_perm, f1, f2):
        for n in self.NUMBERS:
                self._map(cur_perm, f1.replace("a", n),f2.replace("a", n))
    def _map_g(self, cur_perm, f1, f2):
        for g in self.GENDERS:
            self._map(cur_perm, f1.replace("g", g),f2.replace("g", g))
    def _map_z(self, cur_perm, f1, f2):
        for z in self.PERSONS:
            self._map(cur_perm, f1.replace("z", z), f2.replace("z", z))
    def _map_t(self, cur_perm, f1, f2):
        for t in self.TENSES_CASES:
            self._map(cur_perm, f1.replace("t", t), f2.replace("t", t))

    def _perform_swaps(self,cur_perm,swap_list):
        for f1, f2 in swap_list:
            G = (" g " in f1 or " g " in f2) #GEN: m f (n)
            N = ("a " in f1 or "a " in f2) #NUM: s p d
            Z = ("z" in f1 or "z" in f2) #PERS: 1 2 3
            T = (" t" in f1 or " t" in f2) #CASES / TENSES
            if G:
                if N:
                    if Z: #g n z
                        if T:
                            self._swap_gnzt(cur_perm, f1, f2)
                        else:
                            self._swap_gnz(cur_perm, f1, f2)
                    else: #g n
                        if T:
                            self._swap_gnt(cur_perm, f1, f2)
                        else:
                            self._swap_gn(cur_perm, f1, f2)
                elif Z: #g z
                    if T:
                        self._swap_gzt(cur_perm, f1, f2)
                    else:
                        self._swap_gz(cur_perm, f1, f2)
                else: #g
                    if T:
                        self._swap_gt(cur_perm, f1, f2)
                    else:
                        self._swap_g(cur_perm, f1, f2)
            elif N:
                if Z: #n z
                    if T:
                        self._swap_nzt(cur_perm, f1, f2)
                    else:
                        self._swap_nz(cur_perm, f1, f2)
                else: #n
                    if T:
                        self._swap_nt(cur_perm, f1, f2)
                    else:
                        self._swap_n(cur_perm, f1, f2)
            elif Z: #z
                if T:
                    self._swap_zt(cur_perm, f1, f2)
                else:
                    self._swap_z(cur_perm, f1, f2)
            else:
                if T:
                    self._swap_t(cur_perm, f1, f2)
                else:
                    self._swap(cur_perm, f1, f2)

    def _perform_left_rotations(self,cur_perm,rotate_left_list):
        for f1, f2, f3 in rotate_left_list:
            G = (" g " in f1 or " g " in f2 or " g " in f3)
            N = ("a " in f1 or "a " in f2 or "a " in f3)
            Z = ("z" in f1 or "z" in f2 or "z" in f3)
            T = (" t" in f1 or " t" in f2 or " t" in f3)  # CASES / TENSES
            if G:
                if N:
                    if Z:  # g n z
                        if T:
                            self._rotate_left_gnzt(cur_perm, f1, f2, f3)
                        else:
                            self._rotate_left_gnz(cur_perm, f1, f2, f3)
                    else:  # g n
                        if T:
                            self._rotate_left_gnt(cur_perm, f1, f2, f3)
                        else:
                            self._rotate_left_gn(cur_perm, f1, f2, f3)
                elif Z:  # g z
                    if T:
                        self._rotate_left_gzt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_left_gz(cur_perm, f1, f2, f3)
                else:  # g
                    if T:
                        self._rotate_left_gt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_left_g(cur_perm, f1, f2, f3)
            elif N:
                if Z:  # n z
                    if T:
                        self._rotate_left_nzt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_left_nz(cur_perm, f1, f2, f3)
                else:  # n
                    if T:
                        self._rotate_left_nt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_left_n(cur_perm, f1, f2, f3)
            elif Z:  # z
                if T:
                    self._rotate_left_zt(cur_perm, f1, f2, f3)
                else:
                    self._rotate_left_z(cur_perm, f1, f2, f3)
            else:
                if T:
                    self._rotate_left_t(cur_perm, f1, f2, f3)
                else:
                    self._rotate_left(cur_perm, f1, f2, f3)

    def _perform_right_rotations(self,cur_perm,rotate_right_list):
        for f1, f2, f3 in rotate_right_list:
            G = (" g " in f1 or " g " in f2 or " g " in f3)
            N = ("a " in f1 or "a " in f2 or "a " in f3)
            Z = ("z" in f1 or "z" in f2 or "z" in f3)
            T = (" t" in f1 or " t" in f2 or " t" in f3)  # CASES / TENSES
            if G:
                if N:
                    if Z:  # g n z
                        if T:
                            self._rotate_right_gnzt(cur_perm, f1, f2, f3)
                        else:
                            self._rotate_right_gnz(cur_perm, f1, f2, f3)
                    else:  # g n
                        if T:
                            self._rotate_right_gnt(cur_perm, f1, f2, f3)
                        else:
                            self._rotate_right_gn(cur_perm, f1, f2, f3)
                elif Z:  # g z
                    if T:
                        self._rotate_right_gzt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_right_gz(cur_perm, f1, f2, f3)
                else:  # g
                    if T:
                        self._rotate_right_gt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_right_g(cur_perm, f1, f2, f3)
            elif N:
                if Z:  # n z
                    if T:
                        self._rotate_right_nzt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_right_nz(cur_perm, f1, f2, f3)
                else:  # n
                    if T:
                        self._rotate_right_nt(cur_perm, f1, f2, f3)
                    else:
                        self._rotate_right_n(cur_perm, f1, f2, f3)
            elif Z:  # z
                if T:
                    self._rotate_right_zt(cur_perm, f1, f2, f3)
                else:
                    self._rotate_right_z(cur_perm, f1, f2, f3)
            else:
                if T:
                    self._rotate_right_t(cur_perm, f1, f2, f3)
                else:
                    self._rotate_right(cur_perm, f1, f2, f3)


    def _perform_maps(self,cur_syn,syn_list):
        for f1, f2 in syn_list:
            G = (" g " in f1 or " g " in f2)
            N = ("a " in f1 or "a " in f2)
            Z = ("z" in f1 or "z" in f2)
            T = (" t" in f1 or " t" in f2)  # CASES / TENSES
            if G:
                if N:
                    if Z:  # g n z
                        if T:
                            self._map_gnzt(cur_syn, f1, f2)
                        else:
                            self._map_gnz(cur_syn, f1, f2)
                    else:  # g n
                        if T:
                            self._map_gnt(cur_syn, f1, f2)
                        else:
                            self._map_gn(cur_syn, f1, f2)
                elif Z:  # g z
                    if T:
                        self._map_gzt(cur_syn, f1, f2)
                    else:
                        self._map_gz(cur_syn, f1, f2)
                else:  # g
                    if T:
                        self._map_gt(cur_syn, f1, f2)
                    else:
                        self._map_g(cur_syn, f1, f2)
            elif N:
                if Z:  # n z
                    if T:
                        self._map_nzt(cur_syn, f1, f2)
                    else:
                        self._map_nz(cur_syn, f1, f2)
                else:  # n
                    if T:
                        self._map_nt(cur_syn, f1, f2)
                    else:
                        self._map_n(cur_syn, f1, f2)
            elif Z:  # z
                if T:
                    self._map_zt(cur_syn, f1, f2)
                else:
                    self._map_z(cur_syn, f1, f2)
            else:
                if T:
                    self._map_t(cur_syn, f1, f2)
                else:
                    self._map(cur_syn, f1, f2)


    def _perform_full_swap(self,cur_perm,full_swap_list):
        #note: only works if g and T is used
        for g in ["m","f"]:
            for old, new in full_swap_list:
                cur_perm[old[0].replace("g",g)],cur_perm[old[1].replace("g",g)],cur_perm[old[2].replace("g",g)],\
                cur_perm[old[3].replace("g",g)],cur_perm[old[4].replace("g",g)],cur_perm[old[5].replace("g",g)],\
                cur_perm[old[6].replace("g",g)],cur_perm[old[7].replace("g",g)],cur_perm[old[8].replace("g",g)]\
                =\
                cur_perm[new[0].replace("g",g)],cur_perm[new[1].replace("g",g)],cur_perm[new[2].replace("g",g)],\
                cur_perm[new[3].replace("g",g)],cur_perm[new[4].replace("g",g)],cur_perm[new[5].replace("g",g)],\
                cur_perm[new[6].replace("g",g)],cur_perm[new[7].replace("g",g)],cur_perm[new[8].replace("g",g)]


    def _perform_full_swap_7(self,cur_perm,full_swap7_list):
        #note: only for PRON
        for elem in full_swap7_list:
            n1, n2, n3, n4, n5, n6, n7 = list(elem)
            cur_perm["1s"], cur_perm["2s"], cur_perm["3s"], cur_perm["1p"], cur_perm["2p"], cur_perm["3p"], cur_perm["12p"] \
                = cur_perm[n1], cur_perm[n2], cur_perm[n3], cur_perm[n4], cur_perm[n5], cur_perm[n6], cur_perm[n7]


    def _perform_swap_4p(self,cur_perm,swap_4p_list):
        #note: only for PRON
        for elem in swap_4p_list:
            n1, n2, n3, n4 = list(elem)
            cur_perm["1p"], cur_perm["2p"], cur_perm["3p"], cur_perm["12p"] \
                = cur_perm[n1], cur_perm[n2], cur_perm[n3], cur_perm[n4]


    def add_pers_perm_variation(self, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        self.pers_perm_count +=1
        name = "PERM_PERS"+str(self.pers_perm_count)
        self.add_perm_variation(name,swap_list, rotate_left_list, rotate_right_list, full_swap_list, full_swap7_list, swap_4p_list)
    def add_num_perm_variation(self, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        self.num_perm_count +=1
        name = "PERM_NUM"+str(self.num_perm_count)
        self.add_perm_variation(name,swap_list, rotate_left_list, rotate_right_list, full_swap_list, full_swap7_list, swap_4p_list)
    def add_gen_perm_variation(self, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        self.gen_perm_count +=1
        name = "PERM_GEN"+str(self.gen_perm_count)
        self.add_perm_variation(name,swap_list, rotate_left_list, rotate_right_list, full_swap_list, full_swap7_list, swap_4p_list)
    def add_ten_perm_variation(self, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        self.ten_perm_count +=1
        name = "PERM_TEN"+str(self.ten_perm_count)
        self.add_perm_variation(name,swap_list, rotate_left_list, rotate_right_list, full_swap_list, full_swap7_list, swap_4p_list)
    def add_xross_perm_variation(self, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        self.x_perm_count +=1
        name = "PERM_XROSS"+str(self.x_perm_count)
        self.add_perm_variation(name,swap_list, rotate_left_list, rotate_right_list, full_swap_list, full_swap7_list, swap_4p_list)
    def add_pers_sync_variation(self, syn_list):
        self.pers_sync_count +=1
        name = "SYN_PERS"+str(self.pers_sync_count)
        self.add_sync_variation(name,syn_list)
    def add_num_sync_variation(self, syn_list):
        self.num_sync_count +=1
        name = "SYN_NUM"+str(self.num_sync_count)
        self.add_sync_variation(name,syn_list)
    def add_gen_sync_variation(self, syn_list):
        self.gen_sync_count +=1
        name = "SYN_GEN"+str(self.gen_sync_count)
        self.add_sync_variation(name,syn_list)
    def add_ten_sync_variation(self, syn_list):
        self.ten_sync_count +=1
        name = "SYN_TEN"+str(self.ten_sync_count)
        self.add_sync_variation(name,syn_list)
    def add_xross_sync_variation(self, syn_list):
        self.x_sync_count +=1
        name = "SYN_XROSS"+str(self.x_sync_count)
        self.add_sync_variation(name,syn_list)


    def add_sync_variation(self, name, syn_list):
        """adds a new syncretic variation with name @name, where each pair in @syn_list is syncretised (f1 -> f2)"""
        cur_syn = copy.deepcopy(self.org_conj_dict)
        self._perform_maps(cur_syn,syn_list)
        self._add_var(name, cur_syn)

    def add_perm_variation(self, name, swap_list=list(), rotate_left_list=list(), rotate_right_list=list(), full_swap_list=(), full_swap7_list=(), swap_4p_list=()):
        cur_perm = copy.deepcopy(self.org_conj_dict)
        self._perform_swaps(cur_perm,swap_list)
        self._perform_left_rotations(cur_perm,rotate_left_list)
        self._perform_right_rotations(cur_perm,rotate_right_list)
        self._perform_full_swap(cur_perm,full_swap_list)
        self._perform_full_swap_7(cur_perm,full_swap7_list)
        self._perform_swap_4p(cur_perm,swap_4p_list)
        self._add_var(name, cur_perm)


    def add_full_variation(self, full_swap7_list=()):
        self.full_var_count +=1
        name = "FULL_FULL"+str(self.full_var_count)
        cur_perm = copy.deepcopy(self.org_conj_dict)
        self._perform_full_swap_7(cur_perm,full_swap7_list)
        self._add_var(name, cur_perm)

    def _add_var(self, var_name, var_dict):
        filename = self.lang_name + "_" + var_name + self._file_ending
        self.permutation_dicts[filename.split("/")[-1]] = var_dict


    def create_permutations_and_syncretisms(self, read_directory):
        """
        reads in the conjugation table and creates all permutations
        :param read_directory: directory where the file with the conjugation table lies
        :param write_directory: directory where to write the permutation files
        :param name: name of the file with the conjugation table (without file-suffix). Permutation files will use the same file name with added suffixes
        :param file_ending: should be ".tsv"
        """
        self.read_directory = read_directory

        # read in original conjugation table
        baseline_filename = self.read_directory + self.lang_name + self._file_ending
        self.org_conj_dict = self.read_in_conjugation_table(baseline_filename)
        self.permutation_dicts[self.lang_name + "_BASE_BASE1"+ self._file_ending] = copy.deepcopy(self.org_conj_dict)

        # create permutations
        self._create_variations()

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
                cur_feat = line[0].strip()

                if " m" not in cur_feat and " f" not in cur_feat:
                    if "d" in cur_feat:
                        d_list.append(cur_feat + " f")
                        d_list.append(cur_feat + " m")
                    if "p" in cur_feat:
                        p_list.append(cur_feat + " f")
                        p_list.append(cur_feat + " m")
                    for count, tense in enumerate(self.TENSES_CASES, start=1):
                        cont_dict[tense][cur_feat + " m"] = line[count]
                        cont_dict[tense][cur_feat + " f"] = line[count]
                else:
                    if "d" in cur_feat:
                        d_list.append(cur_feat)
                    if "p" in cur_feat:
                        p_list.append(cur_feat)
                    for count, tense in enumerate(self.TENSES_CASES, start=1):
                        cont_dict[tense][cur_feat] = line[count]

        dual_add_list = set([elem.replace("p","d") for elem in p_list]) - set(d_list)
        for elem in dual_add_list:
            for tense in self.TENSES_CASES:
                cont_dict[tense][elem] = cont_dict[tense][elem.replace("d","p")]

        # add m f
        # and tense
        res_dict = dict()
        for tense in self.TENSES_CASES:
            for feat, conj in cont_dict[tense].items():
                if tense == " ":  # PRON
                    res_dict[feat] = conj
                elif "m" not in feat and "f" not in feat:
                    res_dict[feat + " m " + tense] = conj
                    res_dict[feat + " f " + tense] = conj
                else:
                    res_dict[feat + " " + tense] = conj

        #print(res_dict.keys())
        return res_dict

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
        pass

    def _create_permutation_NUM_files(self):
        pass

    def _create_permutation_GEN_files(self):
        pass

    def _create_permutation_TENSE_files(self):
        pass

    def _create_permutation_X_files(self):
        pass

    def _create_syncretic_PERS_files(self):
        pass

    def _create_syncretic_NUM_files(self):
        pass

    def _create_syncretic_GEN_files(self):
        pass

    def _create_syncretic_TENSE_files(self):
        pass

    def _create_syncretic_X_files(self):
        pass

    #RANDOM SWAPS:

    def _create_random_swap(self,perm_type, amount_of_vars, num_of_swaps):
        if perm_type == "NUM":
            element_list = self.NUMBERS
            string_element = "a"
            conj_keys = [p + "a " + g + " " + t for p in self.PERSONS for g in self.GENDERS for t in self.TENSES_CASES]
        elif perm_type == "TEN":
            element_list = self.TENSES_CASES
            string_element = "t"
            conj_keys = [p + n + " " + g + " t" for p in self.PERSONS for g in self.GENDERS for n in self.NUMBERS]
        elif perm_type == "GEN":
            element_list = self.GENDERS
            string_element = "g"
            conj_keys = [p + n + " g " + t for p in self.PERSONS for n in self.NUMBERS for t in self.TENSES_CASES]
        elif perm_type == "PERS":
            element_list = self.PERSONS
            string_element = "z"
            conj_keys = ["z" + n + " " + g + " " + t for g in self.GENDERS for n in self.NUMBERS for t in self.TENSES_CASES]
        else:
            element_list = None
            string_element = None
            conj_keys = None

        for _ in range(0, amount_of_vars):  # number of variations that are created
            swap_list = []
            for _ in range(0, num_of_swaps):  # number of permutations to be performed
                feat = random.choice(conj_keys)
                e1 = random.choice(element_list)
                e2 = random.choice(list(set(element_list) - set(e1)))
                feat_i = feat.replace(string_element, e1)
                feat_j = feat.replace(string_element, e2)
                swap_list.append((feat_i, feat_j))
            if perm_type == "NUM":
                self.add_num_perm_variation(swap_list=swap_list)
            elif perm_type == "PERS":
                self.add_pers_perm_variation(swap_list=swap_list)
            elif perm_type == "GEN":
                self.add_gen_perm_variation(swap_list=swap_list)
            elif perm_type == "TEN":
                self.add_ten_perm_variation(swap_list=swap_list)
            else: raise Exception("type unknown")

    def _create_random_rotation(self, perm_type, amount_of_vars, num_of_rots_l, num_of_rots_r):
        if perm_type == "NUM":
            element_list = self.NUMBERS
            string_element = "a"
            conj_keys = [p + "a " + g + " " + t for p in self.PERSONS for g in self.GENDERS for t in self.TENSES_CASES]
        elif perm_type == "TEN":
            element_list = self.TENSES_CASES
            string_element = "t"
            conj_keys = [p + n + " " + g + " t" for p in self.PERSONS for g in self.GENDERS for n in self.NUMBERS]
        elif perm_type == "GEN":
            element_list = self.GENDERS
            string_element = "g"
            conj_keys = [p + n + " g " + t for p in self.PERSONS for n in self.NUMBERS for t in self.TENSES_CASES]
        elif perm_type == "PERS":
            element_list = self.PERSONS
            string_element = "z"
            conj_keys = ["z" + n + " " + g + " " + t for g in self.GENDERS for n in self.NUMBERS for t in
                         self.TENSES_CASES]
        else:
            element_list = None
            string_element = None
            conj_keys = None

        for _ in range(0, amount_of_vars):  # number of variations that are created
            rot_list_l = []
            rot_list_r = []
            for _ in range(0, num_of_rots_l):  # number of permutations to be performed
                feat = random.choice(conj_keys)
                e1 = random.choice(element_list)
                e2 = random.choice(list(set(element_list) - set(e1)))
                e3 = random.choice(list(set(element_list) - set(e1) - set(e2)))
                feat_i = feat.replace(string_element, e1)
                feat_j = feat.replace(string_element, e2)
                feat_k = feat.replace(string_element, e3)
                rot_list_l.append((feat_i, feat_j, feat_k))
            for _ in range(0, num_of_rots_r):  # number of permutations to be performed
                feat = random.choice(conj_keys)
                e1 = random.choice(element_list)
                e2 = random.choice(list(set(element_list) - set(e1)))
                e3 = random.choice(list(set(element_list) - set(e1) - set(e2)))
                feat_i = feat.replace(string_element, e1)
                feat_j = feat.replace(string_element, e2)
                feat_k = feat.replace(string_element, e3)
                rot_list_r.append((feat_i, feat_j, feat_k))

            if perm_type == "NUM":
                self.add_num_perm_variation(rotate_left_list=rot_list_l, rotate_right_list=rot_list_r)
            elif perm_type == "PERS":
                self.add_pers_perm_variation(rotate_left_list=rot_list_l, rotate_right_list=rot_list_r)
            elif perm_type == "GEN":
                self.add_gen_perm_variation(rotate_left_list=rot_list_l, rotate_right_list=rot_list_r)
            elif perm_type == "TEN":
                self.add_ten_perm_variation(rotate_left_list=rot_list_l, rotate_right_list=rot_list_r)
            else:
                raise Exception("type unknown")

    def _create_random_PERM_dims_files(self):
        #NUM
        if len(self.NUMBERS) >= 2:
            self._create_random_swap("NUM", amount_of_vars=5, num_of_swaps=1)
            self._create_random_swap("NUM", amount_of_vars=5, num_of_swaps=2)
            self._create_random_swap("NUM", amount_of_vars=10, num_of_swaps=5)
            self._create_random_swap("NUM", amount_of_vars=10, num_of_swaps=10)
        if len(self.NUMBERS) >= 3:
            self._create_random_rotation("NUM", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=0)
            self._create_random_rotation("NUM", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=5)

        #PERS
        if len(self.PERSONS) >= 2:
            self._create_random_swap("PERS", amount_of_vars=5, num_of_swaps=1)
            self._create_random_swap("PERS", amount_of_vars=5, num_of_swaps=2)
            self._create_random_swap("PERS", amount_of_vars=10, num_of_swaps=5)
            self._create_random_swap("PERS", amount_of_vars=10, num_of_swaps=10)
        if len(self.PERSONS) >= 3:
            self._create_random_rotation("PERS", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=0)
            self._create_random_rotation("PERS", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=5)

        #GEN
        if len(self.GENDERS) >= 2:
            self._create_random_swap("GEN", amount_of_vars=5, num_of_swaps=1)
            self._create_random_swap("GEN", amount_of_vars=5, num_of_swaps=2)
            self._create_random_swap("GEN", amount_of_vars=10, num_of_swaps=5)
            self._create_random_swap("GEN", amount_of_vars=10, num_of_swaps=10)
        if len(self.GENDERS) >= 3:
            self._create_random_rotation("GEN", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=0)
            self._create_random_rotation("GEN", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=5)

        #TEN
        if len(self.TENSES_CASES) >= 2:
            self._create_random_swap("TEN", amount_of_vars=5, num_of_swaps=1)
            self._create_random_swap("TEN", amount_of_vars=5, num_of_swaps=2)
            self._create_random_swap("TEN", amount_of_vars=10, num_of_swaps=5)
            self._create_random_swap("TEN", amount_of_vars=10, num_of_swaps=10)
        if len(self.TENSES_CASES) >= 3:
            self._create_random_rotation("TEN", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=0)
            self._create_random_rotation("TEN", amount_of_vars=5, num_of_rots_l=5, num_of_rots_r=5)


    def _create_random_PERM_files(self):
        conj_keys = list(self.org_conj_dict.keys())

        for _ in range(0,20): #number of variations that are created

            swap_list = []
            for _ in range(0,40): #number of permutations to be performed
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                swap_list.append((i,j))
            self.add_xross_perm_variation(swap_list=swap_list)

        for _ in range(0, 20):  # number of variations that are created
            conj_keys = list(self.org_conj_dict.keys())

            swap_list = []
            for _ in range(0, 20):  # number of permutations to be performed
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                swap_list.append((i, j))

            left_rotate_list = []
            for _ in range(0, 10):  # number of permutations to be performed
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                k = random.choice(conj_keys)
                left_rotate_list.append((i, j, k))

            right_rotate_list = []
            for _ in range(0, 10):  # number of permutations to be performed
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                k = random.choice(conj_keys)
                left_rotate_list.append((i, j, k))

            self.add_xross_perm_variation(swap_list=swap_list, rotate_right_list=right_rotate_list, rotate_left_list=left_rotate_list)


        for _ in range(0, 10):  # number of variations that are created
            conj_keys = list(self.org_conj_dict.keys())

            left_rotate_list = []
            for _ in range(0, 20):  # number of permutations to be performed
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                k = random.choice(conj_keys)
                left_rotate_list.append((i, j, k))

            self.add_xross_perm_variation(rotate_left_list=left_rotate_list)

    def _create_random_SYN_files(self):

        for _ in range(0,20): #number of variations that are created
            conj_keys = list(self.org_conj_dict.keys())

            map_list = []
            for _ in range(0,10): #number of syncretisms to be added
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                map_list.append((i,j))
            self.add_xross_sync_variation(syn_list=map_list)



        for _ in range(0,10): #number of variations that are created
            conj_keys = list(self.org_conj_dict.keys())

            map_list = []
            for _ in range(0,25): #number of syncretisms to be added
                i = random.choice(conj_keys)
                j = random.choice(conj_keys)
                map_list.append((i,j))
            self.add_xross_sync_variation(syn_list=map_list)


    def _create_random_merge(self, syn_type, amount_of_vars, num_of_merges):
        if syn_type == "NUM":
            element_list = self.NUMBERS
            string_element = "a"
            conj_keys = [p + "a " + g + " " + t for p in self.PERSONS for g in self.GENDERS for t in self.TENSES_CASES]
        elif syn_type == "TEN":
            element_list = self.TENSES_CASES
            string_element = "t"
            conj_keys = [p + n + " " + g + " t" for p in self.PERSONS for g in self.GENDERS for n in self.NUMBERS]
        elif syn_type == "GEN":
            element_list = self.GENDERS
            string_element = "g"
            conj_keys = [p + n + " g " + t for p in self.PERSONS for n in self.NUMBERS for t in self.TENSES_CASES]
        elif syn_type == "PERS":
            element_list = self.PERSONS
            string_element = "z"
            conj_keys = ["z" + n + " " + g + " " + t for g in self.GENDERS for n in self.NUMBERS for t in self.TENSES_CASES]
        else:
            element_list = None
            string_element = None
            conj_keys = None

        for _ in range(0, amount_of_vars):  # number of variations that are created
            map_list = []
            for _ in range(0, num_of_merges):  # number of permutations to be performed
                feat = random.choice(conj_keys)
                e1 = random.choice(element_list)
                e2 = random.choice(list(set(element_list) - set(e1)))
                feat_i = feat.replace(string_element, e1)
                feat_j = feat.replace(string_element, e2)
                map_list.append((feat_i, feat_j))
            if syn_type == "NUM":
                self.add_num_sync_variation(syn_list=map_list)
            elif syn_type == "PERS":
                self.add_pers_sync_variation(syn_list=map_list)
            elif syn_type == "GEN":
                self.add_gen_sync_variation(syn_list=map_list)
            elif syn_type == "TEN":
                self.add_ten_sync_variation(syn_list=map_list)
            else: raise Exception("type unknown")

    def _create_random_SYN_dims_files(self):
        if len(self.GENDERS) > 1:
            self._create_random_merge("GEN", amount_of_vars=5, num_of_merges=1)
            self._create_random_merge("GEN", amount_of_vars=5, num_of_merges=2)
            self._create_random_merge("GEN", amount_of_vars=10, num_of_merges=5)
            self._create_random_merge("GEN", amount_of_vars=5, num_of_merges=10)


        if len(self.TENSES_CASES) > 1:
            self._create_random_merge("TEN", amount_of_vars=5, num_of_merges=1)
            self._create_random_merge("TEN", amount_of_vars=5, num_of_merges=2)
            self._create_random_merge("TEN", amount_of_vars=10, num_of_merges=5)
            self._create_random_merge("TEN", amount_of_vars=5, num_of_merges=10)

        if len(self.PERSONS) > 1:
            self._create_random_merge("PERS", amount_of_vars=5, num_of_merges=1)
            self._create_random_merge("PERS", amount_of_vars=5, num_of_merges=2)
            self._create_random_merge("PERS", amount_of_vars=10, num_of_merges=5)
            self._create_random_merge("PERS", amount_of_vars=5, num_of_merges=10)


        if len(self.NUMBERS) > 1:
            self._create_random_merge("NUM", amount_of_vars=5, num_of_merges=1)
            self._create_random_merge("NUM", amount_of_vars=5, num_of_merges=2)
            self._create_random_merge("NUM", amount_of_vars=10, num_of_merges=5)
            self._create_random_merge("NUM", amount_of_vars=5, num_of_merges=10)



    def _create_SHUF_files(self):
        """creates files where surface forms are swapped"""
        conj_dict = copy.deepcopy(self.org_conj_dict)

        forms_dict = dict()
        for feat, conj in conj_dict.items():
            if conj in forms_dict:
                forms_dict[conj].append(feat)
            else:
                forms_dict[conj] = [feat]

        for i in range(1, self.shuffle_length+1):
            # shuffle values
            values_list = list(forms_dict.values())
            shuffled_values = random.sample(values_list, len(values_list))
            shuffled_dict = dict(zip(forms_dict.keys(), shuffled_values))

            # create new dict
            new_conj_dict = dict()
            for conj, feat_list in shuffled_dict.items():
                for feat in feat_list:
                    new_conj_dict[feat] = conj


            # sort
            final_conj_dict = dict()
            for feature_comb in self.COMBINED:
                final_conj_dict[feature_comb] = new_conj_dict[feature_comb]

            filename = self.lang_name + "_SHUF_SHUF" + str(i) + self._file_ending
            self.permutation_dicts[filename.split("/")[-1]] = final_conj_dict


    def write_permutations_to_files(self, write_directory, permlist_write_directory):
        """
        writes all permutations (including original) to files
        """
        self.write_directory = write_directory + self.lang_name + "/"

        if not os.path.exists(self.write_directory):
            os.makedirs(self.write_directory)

        for perm_filename, perm_dict in self.permutation_dicts.items():
            res = ""
            for feat, conj in perm_dict.items():
                res += str(feat) + "\t" + str(conj) + "\n"

            for i in "abcde":
                with open(self.write_directory + perm_filename[:-4] + i + ".tsv", "w") as g:
                    g.write(res)

            if "BASE_BASE" in perm_filename:
                for i in "fghjk":
                    with open(self.write_directory + perm_filename[:-4] + i + ".tsv", "w") as g:
                        g.write(res)

        if not os.path.exists(permlist_write_directory):
            os.makedirs(permlist_write_directory)
        res = "PERM_PERS\t" + str(self.pers_perm_count) + "\n"
        res += "PERM_GEN\t" + str(self.gen_perm_count) + "\n"
        res += "PERM_NUM\t" + str(self.num_perm_count) + "\n"
        res += "PERM_TEN\t" + str(self.ten_perm_count) + "\n"
        res += "PERM_XROSS\t" + str(self.x_perm_count) + "\n"
        res += "SYN_PERS\t" + str(self.pers_sync_count) + "\n"
        res += "SYN_GEN\t" + str(self.gen_sync_count) + "\n"
        res += "SYN_NUM\t" + str(self.num_sync_count) + "\n"
        res += "SYN_TEN\t" + str(self.ten_sync_count) + "\n"
        res += "SYN_XROSS\t" + str(self.x_sync_count) + "\n"
        res += "SHUF_SHUF\t" + str(self.shuffle_length) + "\n"
        res += "BASE_BASE\t" + str(self.base_length)
        with open(permlist_write_directory + self.lang_name + ".tsv","w") as g:
            g.write(res)
