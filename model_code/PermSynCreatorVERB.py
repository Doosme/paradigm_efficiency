import copy

from PermSynCreator import PermSynCreator


class PermSynCreatorSEM(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "SEM"

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]


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
        self._create_syncretic_GEN_files()
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()


    def _create_permutation_PERS_files(self):
        """
        creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
        """
        # d.m: 2 <-> 3, p.f: 2 <-> 3x
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # s: 1 <-> 2, p:1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # s: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d:1 <-> 3, s: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d:1 <-> 2, s: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # d: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3, d: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # d.f: 1 <-> 3, p.m: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # pfG: 2 <-> 3, sfG: 3<-> 2, dGm: 2<->3
        self.add_pers_perm_variation( [("2p f G", "3p f G"), ("3s f G", "2s f G"), ("3d m G", "2d m G")])

        # sV: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V")] + [("2d g V", "3d g V"), ("1p g V", "2p g V")])

        # sG: 1 <-> 3, dG: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g G", "3s g G"), ("2d g G", "3d g G"), ("1p g V", "2p g V")])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V"), ("2d g V", "3d g V"), ("1p g G", "2p g G")])

        # dm: 1 <-> 2, df: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T) for T
                                                                                       in self.TENSES_CASES])

        # sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T) for T
                                                                                       in self.TENSES_CASES])

        # sm: 1 <-> 2
        self.add_pers_perm_variation( [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # pm: 1 <-> 2
        self.add_pers_perm_variation( [("1p m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3
        self.add_pers_perm_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # pf: 1 <-> 2
        self.add_pers_perm_variation( [("1p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # dm: 1 <-> 2, df: 1 <-> 3, sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T) for
                                                                                          T in self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3, dm: 2 <-> 3, sm: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "3s m " + T) for
                                                                                          T in self.TENSES_CASES])

        # pm: 2 <-> 3
        self.add_pers_perm_variation( [("2p m " + T, "3p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3, df: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "3d f " + T) for T
                                                                                       in self.TENSES_CASES])

        # pf: 1 <-> 2, df: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2p f " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "1d f " + T) for T
                                                                                       in self.TENSES_CASES])

        # d: 1 <-> 2, p: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("3d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s f " + T) for T
                                                                                       in self.TENSES_CASES])

        # dG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g G", "3d g G")])

        # dG: 2 <-> 1, pG: 2 <-> 1, dV: 2 <-> 3, pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g G", "1d g G"), ("2p g G", "1p g G"), ("2d g V", "3d g V"),
                                                ("2p g V", "3p g V")])

        # dm: 2 <-> 3, pm: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T) for T
                                                                                       in self.TENSES_CASES])

        # df: 2 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        self.add_pers_perm_variation( [("2d m G", "3d m G"), ("2p m G", "3p m G")])

        # dfG: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2d f G", "2d f G"), ("2p f G", "2p f G")])

        # dG: 2 <-> 1, pG: 2 <-> 1, smV: 2 <-> 3
        self.add_pers_perm_variation( [("2s m V", "3s m V"), ("1d g G", "2d g G"), ("1p g G", "2p g G")])

        # sfV: 2 <-> 3
        self.add_pers_perm_variation( [("2s f V", "3s f V")])

        # sfV: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2s f V", "3s f V"), ("2p f G", "3p f G")])

        # d,p: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # dV,pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g V"), ("2p g V", "3p g V")])

        # V: 2 <-> 3
        self.add_pers_perm_variation( [("2a g V", "3a g V")])

        # Vs: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # Vs: 1 <-> 3
        self.add_pers_perm_variation( [("1s g V", "3s g V")])

        # dV,pV: 1 <-> 3
        self.add_pers_perm_variation( [("1d g V", "3d g V")] + [("1p g V", "3p g V")])

        # dG,pG: 1 <-> 2, sV: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g G", "2d g G")] + [("1p g G", "2p g G")] + [("1s g V", "2s g V")] + [
                                    ("2p g V", "3p g V")] + [("2d g V", "3d g V")])

        # sG: 1 <-> 2, pG,dG: 2 <-> 3
        self.add_pers_perm_variation( [("1s g G", "2s g G")] + [("2d g G", "3d g G")] + [("2p g G", "3p g G")])

        # V: 1<->2
        self.add_pers_perm_variation( [("1a g V", "2a g V")])

        # G: 2<->3
        self.add_pers_perm_variation( [("2a g G", "3a g G")])

        # STRONG

        # strong permutation 1
        self.add_pers_perm_variation(
                                [("1s m G", "3s m G"), ("2s f G", "1s f G"), ("3s m V", "2s m V"), ("1s f V", "2s f V"),
                                 ("2d m G", "3d m G"), ("3d f G", "1d f G"), ("1d m V", "2d m V"), ("2d f V", "3d f V"),
                                 ("3p m G", "2p m G"), ("1p f G", "2p f G"), ("2p m V", "1p m V"),
                                 ("3p f V", "1p f V")])

        # strong permutation 2
        self.add_pers_perm_variation(
                                [("1s m G", "2s m G"), ("1s f G", "3s f G"), ("1s m V", "2s m V"), ("1s f V", "3s f V"),
                                 ("2d m G", "3d m G"), ("2d f G", "1d f G"), ("2d m V", "1d m V"), ("2d f V", "3d f V"),
                                 ("3p m G", "2p m G"), ("3p f G", "1p f G"), ("3p m V", "1p m V"),
                                 ("3p f V", "1p f V")])

        # strong permutation 3
        rotright = [("1s f G", "2s f G", "3s f G"), ("1d m G", "2d m G", "3d m G"), ("1d m V", "2d m V", "3d m V"),
                    ("1p m G", "2p m G", "3p m G"), ("1p f G", "2p f G", "3p f G"), ("1p f V", "2p f V", "3p f V")]
        rotleft = [("1s m V", "2s m V", "3s m V"), ("1d f G", "2d f G", "3d f G"), ("1d f V", "2d f V", "3d f V"),
                   ("1p m V", "2p m V", "3p m V")]
        self.add_pers_perm_variation( swap_list=list(), rotate_left_list=rotleft, rotate_right_list=rotright)

        # dG: 1 <-> 2, pG: 1 <-> 2
        # dV: 2 <-> 3, pV: 2 <-> 3
        # sV: 1 <-> 3, sG: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d g G", "1d g G")] + [("2p g G", "1p g G")] + [("2d g V", "3d g V")] + [
                                    ("2p g V", "3p g V")] + [("1s g V", "3s g V")] + [("2s g G", "3s g G")])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g G", "3d g G", "1d g G")] + [("2p g G", "3p g G", "1p g G")] + [("2s g V", "3s g V", "1s g V")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [("3s g G", "1s g G", "2s g G")]
        self.add_pers_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        # dfV: 2 <-> 3, pfV: 2 <-> 3
        # sG: 1 <-> 3, sV: 1 <-> 3
        self.add_pers_perm_variation( [("2d m G", "3d m G"), ("2p m G", "3p m G"), ("2d f V", "3d f V"),
                                                ("2p f V", "3p f V")] + [("1s g G", "3s g G")] + [("1s g V", "3s g V")])

        # sG: 1->2->3
        # sV: 3->2->1
        # dG: 1 <-> 3 (daaa dGm: 1<->2),  pG: 1 <-> 3 (daaa pGm: 1<->2)
        # dV: 1 <-> 2 (daaa dVf: 1<->3),  pV: 1 <-> 2 (daaa pVf: 1<->3)
        right = [("2s g G", "3s g G", "1s g G")]
        left = [("3s g V", "1s g V", "2s g V")]
        swap = [("2d m G", "1d m G"), ("2p m G", "1p m G"), ("3d f V", "1d f V"), ("3p f V", "1p f V"),
                ("3d g G", "1d g G"), ("3p g G", "1p g G"), ("2d g V", "1d g V"), ("2p g V", "1p g V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_right_list=right, rotate_left_list=left)

        # dG: 1->2->3,  pG: 1->2->3
        # dV: 3->2->1,  pV: 3->2->1
        # sG: 1 <-> 3
        # sV: 1 <-> 3 (daaa sVm: 1 <-> 2)
        right = [("2d g G", "3d g G", "1d g G")] + [("2p g G", "3p g G", "1p g G")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")]
        swap = [("3s g G", "1s g G")] + [("3s g V", "1s g V")] + [("2s m V", "1s m V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # G: sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation( [("1s m G", "2s m G"), ("1s f G", "3s f G")])

    def _create_permutation_NUM_files(self):
        """
        creates all permutation files where NUM-features are swapped (s <-> d <-> p)
        """

        # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p
        self.add_num_perm_variation( [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2f: s <-> p, 3m: s <-> p
        self.add_num_perm_variation(
                                [("2s f " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3p m " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2m: s <-> p, 3f: d <-> p
        self.add_num_perm_variation(
                                [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3d f " + T) for T
                                                                                       in self.TENSES_CASES])

        # 1m: s <-> p
        self.add_num_perm_variation( [("1s m " + T, "1p m " + T) for T in self.TENSES_CASES])

        # 1m: s <-> d, 2f: d <-> p
        self.add_num_perm_variation(
                                [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2: s <-> d, 3: d <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2G: s <-> p
        self.add_num_perm_variation( [("2s g G", "2p g G")])

        # 2G: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g G", "2p g G")] + [("3d g V", "3p g V")])

        # 3G:s<->p, 2V:d<->p, 1m: s<->d
        self.add_num_perm_variation(
                                [("3s g G", "3p g G"), ("2d g V", "2p g V")] + [("1s m " + T, "1d m " + T) for T in
                                                                                self.TENSES_CASES])

        # 1f: s <-> p
        self.add_num_perm_variation( [("1s f " + T, "1p f " + T) for T in self.TENSES_CASES])

        # 2f: s <-> d, 3m: s <-> d
        self.add_num_perm_variation(
                                [("2s f " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d m " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2m: s <-> d, 1f: s <-> d
        self.add_num_perm_variation(
                                [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "1d f " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2m: s <-> p, 1m: s <-> d
        self.add_num_perm_variation(
                                [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "1d m " + T) for T
                                                                                       in self.TENSES_CASES])

        # 1V: s <-> d, 3G: s <-> d
        self.add_num_perm_variation( [("1s g V", "1d g V")] + [("3s g G", "3d g G")])

        # 1G: s <-> d, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g G", "1d g G")] + [("2p g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # 3f: s <-> p
        self.add_num_perm_variation( [("3s f " + T, "3p f " + T) for T in self.TENSES_CASES])

        # 1: s <-> p, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2V: s <-> p, 3mV: s <-> p
        self.add_num_perm_variation( [("3s m V", "3p m V")] + [("2s g V", "2p g V")])

        # 2fV: s <-> p
        self.add_num_perm_variation( [("2s f V", "2p f V")])

        # 2Vf: s <-> p, 3Gm: s <-> p
        self.add_num_perm_variation( [("2s f V", "2p f V")] + [("3s m G", "3p m G")])

        # 2m: s <-> d, 3f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES])

        # 3mG: s <-> p
        self.add_num_perm_variation( [("3s m G", "3p m G")])

        # f: s -> d -> p;   m: p -> d -> s
        right = [("zs f " + T, "zd f " + T, "zp f " + T) for T in self.TENSES_CASES]
        left = [("zs m " + T, "zd m " + T, "zp m " + T) for T in self.TENSES_CASES]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # f: s <-> p,   m: d <-> p
        self.add_num_perm_variation( [("zs f " + T, "zp f " + T) for T in self.TENSES_CASES])

        # STRONG

        # strong permutation 1
        self.add_num_perm_variation(
                                [("1s m G", "1p m G"), ("1s f G", "1d f G"), ("1s m V", "1d m V"), ("1s f V", "1p f V"),
                                 ("2d m G", "2p m G"), ("2d f G", "2s f G"), ("2d m V", "2p m V"), ("2d f V", "2s f V"),
                                 ("3p m G", "3s m G"), ("3p f G", "3d f G"), ("3p m V", "3s m V"),
                                 ("3p f V", "3s f V")])

        # strong permutation 2
        self.add_num_perm_variation(
                                [("1s m G", "1p m G"), ("1s f G", "1s f G"), ("1p m V", "1d m V"), ("1p f V", "1p f V"),
                                 ("2d m G", "2s m G"), ("2p f G", "2d f G"), ("2s m V", "2p m V"), ("2d f V", "2s f V"),
                                 ("3p m G", "3s m G"), ("3p f G", "3d f G"), ("3d m V", "3p m V"),
                                 ("3d f V", "3s f V")])

        # strong permutation 3
        left = [("2s f G", "2d f G", "2p f G")] + [("1s f G", "1d f G", "1p f G")] + [
            ("2s f V", "2d f V", "2p f V")] + [("3s f G", "3d f G", "3p f G")] + [("3s f V", "3d f V", "3p f V")]
        right = [("1s m G", "1d m G", "1p m G")] + [("1s m V", "1d m V", "1p m V")] + [
            ("2s m G", "2d m G", "2p m G")] + [("2s m V", "2d m V", "2p m V")] + [("3s m G", "3d m G", "3p m G")]
        self.add_num_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # 2mV:  s <-> p, 2fG: s <-> p;
        # 3fV: s <-> p, 3mG: s <-> p; 1G: s <-> p
        self.add_num_perm_variation( [("2s m V", "2p m V"), ("2s f G", "2p f G"), ("3s f V", "3p f V"),
                                               ("3s m G", "3p m G")] + [("1s g G", "3p g G")])

        # 2G s <-> p, 3V s <-> d,
        # 3mG d <-> p, 3fG: s <-> p,
        # 3mV:  s <-> d, 3fV:  d <-> p,
        # 1: s <-> d
        self.add_num_perm_variation( [("3d m G", "3p m G"), ("3s f G", "3p f G"), ("3d m V", "3s m V"),
                                               ("3p f V", "3d f V")] + [("2s g G", "2p g G")] + [
                                    ("3s g V", "3d g V")] + [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

    def _create_permutation_GEN_files(self):
        """
        creates all permutation files where GEN-features are swapped (m <-> f)
        """

        # p2: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # s3: m <-> f
        self.add_gen_perm_variation( [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # p2: m <-> f, s3: m <-> f
        self.add_gen_perm_variation(
                                [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3s f " + T) for T
                                                                                       in self.TENSES_CASES])

        # s2: m <-> f, d3: m <-> f, p2: m <-> f
        self.add_gen_perm_variation(
                                [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3d f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: m <-> f
        self.add_gen_perm_variation( [("2a m " + T, "2a f " + T) for T in self.TENSES_CASES])

        # 3: m <-> f
        self.add_gen_perm_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # s: m <-> f
        self.add_gen_perm_variation( [("zs m " + T, "zs f " + T) for T in self.TENSES_CASES])

        # p: m <-> f
        self.add_gen_perm_variation( [("zp m " + T, "zp f " + T) for T in self.TENSES_CASES])

        # 3dV: m <-> f
        self.add_gen_perm_variation( [("3d m V", "3d f V")])

        # 2pG: m<->f, 3sG: m<->f
        self.add_gen_perm_variation( [("2p m G", "2p f G"), ("3s m G", "3s f G")])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        self.add_gen_perm_variation( [("2p m G", "2p f G"), ("3s m G", "3s f G"), ("3p m V", "3p f V")])

        # STRONG
        # strong permutation 1
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"),
                                 ("2s m G", "2s f G"), ("2d m G", "2d f G"), ("2d m V", "2d f V"), ("2p m V", "2p f V"),
                                 ("3s m G", "3s f G"), ("3p m G", "3p f G"), ("3s m V", "3s f V"),
                                 ("3p m V", "3p f V")])

        # strong permutation 2
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("2s m G", "2s f G"), ("2p m G", "2p f G"),
                                 ("2d m V", "2d f V"), ("3s m G", "3s f G"), ("3d m G", "3d f G"), ("3p m G", "3p f G"),
                                 ("3d m V", "3d f V"), ("3p m V", "3p f V")])

        # strong permutation 3
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"),
                                 ("2p m G", "2p f G"), ("2d m V", "2d f V"), ("2p m V", "2p f V"), ("3s m G", "3s f G"),
                                 ("3d m G", "3d f G"), ("3s m V", "3s f V"), ("3d m V", "3d f V"),
                                 ("3p m V", "3p f V")])

        # strong permutation 4
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"),
                                 ("2s m G", "2s f G"), ("2d m G", "2d f G"), ("2p m G", "2p f G"), ("2s m V", "2s f V"),
                                 ("2p m V", "2p f V"), ("3d m G", "3d f G"), ("3d m V", "3d f V"),
                                 ("3p m V", "3p f V")])

    def _create_permutation_TENSE_files(self):
        """
        creates all permutation files where TENSE-features are swapped (V <-> F)
        """
        # 2s : G <-> V, 3p: G <-> V, 1d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G")] + [("3p g V", "3p g G")] + [("1d g V", "1d g G")])

        # 2sf: G <-> V, 3pm: G <-> V, 3df: G <-> V
        self.add_ten_perm_variation( [("2s f V", "2s f G"), ("3p m V", "3p m G"), ("3d f V", "3d f G")])

        # 1s: G <-> V, 3sm: G <-> V, 1p: G <-> V, 2pm: G <-> V, 2s: G <-> V
        self.add_ten_perm_variation( [("3s m V", "3s f G"), ("2p m V", "2p m G")] + [("1s g V", "1s g G")] + [
            ("1p g V", "1p g G")] + [("2s g V", "2s g G")])

        # 2 : G <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g G")])

        # 3 : G <-> V
        self.add_ten_perm_variation( [("3a g V", "3a g G")])

        # s : G <-> V
        self.add_ten_perm_variation( [("zs g V", "zs g G")])

        # p : G <-> V
        self.add_ten_perm_variation( [("zp g V", "zp g G")])

        # sf : G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("zs f V", "zs f G")] + [("3d g V", "3d g G")])

        # 1pm : G <-> V, 3sm : G <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m G"), ("3s m V", "3s m G")])

        # 1f : G <-> V, 3dm : G <-> V
        self.add_ten_perm_variation( [("3d m V", "3d m G")] + [("1a f V", "1a f G")])

        # sf : G <-> V, 1pm : G <-> V, 2dm : G <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m G"), ("2d m V", "2d m G")] + [("zs m V", "zs m G")])

        # 3sf : G <-> V, 2sm : G <-> V
        self.add_ten_perm_variation( [("3s f V", "3s f G"), ("2s m V", "2s m G")])

        # df : G <-> V
        self.add_ten_perm_variation( [("zd f V", "zd f G")])

        # 1 : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G")])

        # d : G <-> V
        self.add_ten_perm_variation( [("zd g V", "zd g G")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation(
                                [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")] + [
                                    ("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")])

        # STRONG

        # 1dm, 3df, 2pm, 2sm, 1sf, 3s
        self.add_ten_perm_variation(
                                [("1d m G", "1d m V"), ("3d f G", "3d f V"), ("2p m G", "2p m V"), ("2s m G", "2s m V"),
                                 ("1s f G", "1s f V")] + [("3s g G", "3s g V")])

        # 2dm, 3df, 2sf, 1d, 1p, 3sm
        self.add_ten_perm_variation( [("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("3s m G", "3s m V"),
                                                                                                 ("2d m G", "2d m V"),
                                                                                                 ("3d f G", "3d f V"),
                                                                                                 ("2s f G", "2s f V")])

        # 1d, 1p, 2p, 2d, 3s
        self.add_ten_perm_variation(
                                [("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("2d g G", "2d g V")] + [
                                    ("2p g G", "2p g V")] + [("3s g G", "3s g V")])

    def _create_permutation_X_files(self):
        """
        creates all permutation files where several or all features are swapped
        """

        # 2 : G <-> V, 3: s <-> p
        self.add_xross_perm_variation(
                                [("2a g G", "2a g V")] + [("3s g " + T, "3p g " + T) for T in
                                                                               self.TENSES_CASES])

        # 2s: m <-> f, 3p <-> 1s, 2pV <-> 1pV
        self.add_xross_perm_variation(
                                [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1s g " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("2p g V", "1p g V")])

        # 2pG: m <-> f, sG: 3m<-> 2f, dGm: 2<->3
        self.add_xross_perm_variation( [("2p m G", "2p f G"), ("3s m G", "2s f G"), ("3d m G", "2d m G")])

        # 3dfV <-> 1smG, 2pfV <-> 3smV, 2pmG <-> 1dmV, 3sfG <-> 3dmG
        self.add_xross_perm_variation( [("3d f V", "1s m G"), ("2p f V", "3s m V"), ("2p m G", "1d m V"),
                                                ("3s f G", "3d m G")])

        # 1dm <-> 2df, 2pmV <-> 3pfG, 3smG <-> 1pfV
        self.add_xross_perm_variation(
                                [("1d m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("2p m V", "3p f G"),
                                                                                       ("3s m G", "1p f V")])

        # 2G <-> 3V, sG <-> pV
        self.add_xross_perm_variation( [("2a g G", "3a g V")] + [("zs g G", "zp g V")])

        # d: 1G <-> 3V,  p: 1G <-> 3V,
        # s: 3G <-> 2V
        self.add_xross_perm_variation( [("1d g G", "3d g V"), ("1p g G", "3p g V"), ("3s g G", "2s g V")])

        # V: 3p <-> 2s, Vs3 <-> Gs1
        self.add_xross_perm_variation( [("3p g V", "2s g V"), ("3s g V", "1s g G")])

        # STRONG

        # full permutation 1
        self.add_xross_perm_variation(
                                [("1s m G", "3s m V"), ("2s m G", "1d f V"), ("3s m G", "2p f G"), ("1s f G", "3p m V"),
                                 ("2s f G", "2d f G"), ("3s f G", "1p m G"), ("3p m G", "3d m V"), ("1s m V", "2s f V"),
                                 ("2s m V", "2p f V"), ("2p m V", "1p f V"), ("3s f V", "1s f V"), ("3d m G", "1d f G"),
                                 ("2d m G", "1d m V"), ("1d m G", "3d f V"), ("2p m G", "3p f G"), ("3d f G", "1p f G"),
                                 ("2d m V", "3p f V"), ("2d f V", "1p m V")])

        # full permutation 2
        self.add_xross_perm_variation(
                                [("1s m G", "2d m G"), ("1s f G", "3s f V"), ("2s m G", "1s f G"), ("2s f G", "2d f G"),
                                 ("2s m V", "1p m V"), ("2s f V", "1p f V"), ("3p m V", "3p m G"), ("3p f V", "3p f G"),
                                 ("1d m V", "3s m V"), ("1d f V", "1s m G"), ("1s m V", "1p m G"), ("1s f V", "3d m V"),
                                 ("2d m V", "2s m G"), ("2d f V", "1p f G"), ("3d f V", "2s f G"), ("2p m G", "3d f G"),
                                 ("2p f G", "2p m V"), ("3d m G", "2p f V")])

        # full permutation 3
        self.add_xross_perm_variation(
                                [("1s g G", "2d g V"), ("2p g G", "2s g G"), ("3d g G", "1p g V"), ("1s g V", "1p g G"),
                                 ("3s g V", "3s g G"), ("3d g V", "1d g G"), ("1d g V", "2p g V"), ("2s g V", "3p g G"),
                                 ("3p g V", "2d g G")])

        # full permutation 4
        self.add_xross_perm_variation(
                                [("1s g G", "1d g G"), ("2d g G", "2p g G"), ("3s g G", "3p g G"), ("1s g V", "2s g V"),
                                 ("2p g V", "3p g V"), ("1d g V", "3d g V"), ("1p g V", "3d g G"), ("2s g G", "3s g V"),
                                 ("1p g G", "2d g V")])

        # full permutation 5
        self.add_xross_perm_variation(
                                [("1s g G", "2p g V"), ("3p g G", "2s g V"), ("2d g G", "1d g V"), ("1s g V", "3d g G"),
                                 ("2d g V", "2p g G"), ("3p g V", "3s g G"), ("1p g V", "2s g G"), ("3s g V", "1p g G"),
                                 ("3d g V", "1d g G")])

        # full permutation 6
        self.add_xross_perm_variation(
                                [("1s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2p f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "1p f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("1d f " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("2s m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("2d m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # full permutation 7
        self.add_xross_perm_variation(
                                [("1s m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d f " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("3s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2s f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("2d m " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("1p m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2d f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("3p m " + T, "3d f " + T) for T in self.TENSES_CASES])

        # full permutation 8
        self.add_xross_perm_variation(
                                [("1s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s m " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("2p m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s f " + T, "2s m " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("1d m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("1d f " + T, "2s f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("3d f " + T, "2d m " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("3p m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # rotations
        # full permutation 9
        right = [("1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES] + [
            ("2s g " + T, "3p g " + T, "1d g " + T) for T in self.TENSES_CASES] + [("3s g " + T, "1p g " + T, "3d g " + T)
                                                                               for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right)

        # full permutation 10
        right = [("1s g " + T, "2s g " + T, "3s g " + T) for T in self.TENSES_CASES]
        left = [("1d g " + T, "2d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 11
        leftrot = [("1s m " + T, "1p m " + T, "2s f " + T) for T in self.TENSES_CASES] + [
            ("1p f " + T, "2d m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d m " + T, "3d f " + T)
                                                                               for T in self.TENSES_CASES] + [
                      ("2d f " + T, "1p f " + T, "3p m " + T) for T in self.TENSES_CASES]
        rightrot = [("1s f " + T, "3d m " + T, "3p f " + T) for T in self.TENSES_CASES] + [
            ("3s m " + T, "2p m " + T, "1d f " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( swap_list=list(), rotate_left_list=leftrot, rotate_right_list=rightrot)

        # full permutation 12
        leftrot = [("2d g V", "3p g V", "3s g G")] + [("2d g G", "2p g G", "3p g G")] + [("1d g G", "1s g V", "3d g V")]
        rightrot = [("1s g G", "2p g V", "3d g G")] + [("2s g G", "2s g V", "1d g V")] + [
            ("3s g V", "1p g V", "1p g G")]
        self.add_xross_perm_variation( swap_list=list(), rotate_left_list=leftrot, rotate_right_list=rightrot)

        # full permutation 13
        leftrot = [("1s m G", "2s m G", "3p f V"), ("1p m G", "1d f G", "2d m V"), ("3p m G", "3p f G", "1s f G"),
                   ("3s f G", "3s f V", "3d m V"), ("3s m V", "2p m V", "3p m V"), ("1p f G", "2d f G", "3d m G"),
                   ("1s f V", "3d f V", "2d m G"), ("2s f G", "2s f V", "2s m V")]
        rightrot = [("1d m G", "1s m V", "2d f V"), ("1d m V", "2p f G", "1p f V"), ("3s m G", "1p m V", "2p m G"),
                    ("3d f G", "1d f V", "2p f V")]
        self.add_xross_perm_variation( swap_list=list(), rotate_left_list=leftrot, rotate_right_list=rightrot)

        # full permutation 14
        self.add_xross_perm_variation( swap_list=list(),
                                rotate_left_list=[("1a m G", "1a f V", "3a f G")] + [("2a m G", "2a m V", "3a f V")] + [
                                    ("2a f V", "1a f G", "1a m V")] + [("3a m G", "2a f G", "3a m V")])

        # full permutation 15
        leftrot = [("zs m G", "zs m V", "zp m G")] + [("zs f V", "zp m V", "zd f G")] + [("zs f G", "zd m V", "zp f V")]
        rightrot = [("zp f G", "zd m G", "zd f V")]
        self.add_xross_perm_variation( swap_list=list(), rotate_left_list=leftrot, rotate_right_list=rightrot)

        # 2smG <-> 3sfV,
        # 2sfG <-> 2pfG,  3smV  <-> 2smV
        # 1s <-> 1p
        # V: 2d <-> 3d, V:2p <-> 3p
        # 3dG: m <-> f,   3pG: m <-> f
        self.add_xross_perm_variation(
                                [("2s m G", "3s f V"), ("2s f G", "2p f G"), ("3s m V", "2s m V"), ("3d m G", "3d f G"),
                                 ("3p m G", "3p f G")] + [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [
                                    ("2d g V", "3d g V")] + [("2p g V", "3p g V")])

        # 3s: m <-> f
        # 2G: s <-> p
        # Vp: 1 <-> 3, Vd: 1 <-> 3
        # Vs: 1m <-> 2f
        self.add_xross_perm_variation(
                                [("1s m V", "2s f V")] + [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES] + [
                                    ("2s g G", "2p g G")] + [("1p g V", "3p g V")] + [("1d g V", "3d g V")])

        # 3sV: m <-> f
        # 1G: s <-> p
        # V: 1d  <-> 2d, V: 1p <-> 2p
        # 3pV <-> 2pG;  2sG <-> 3pG
        self.add_xross_perm_variation(
                                [("3s m V", "3s f V")] + [("1s g G", "1p g G")] + [("1d g V", "2d g V")] + [
                                    ("1p g V", "2p g V")] + [("3p g V", "2p g G")] + [("3p g G", "2s g G")])

        self.add_xross_perm_variation(
                                [("1s m G", "2d m G"), ("1s f G", "3d m V"), ("2s m G", "3d f G"), ("2s f G", "2p m G"),
                                 ("3s m G", "3p m V"), ("3s f G", "1p f G"), ("1d m G", "3d m G"), ("1d f G", "2s m V"),
                                 ("2d f G", "1d m V"), ("1p m G", "1d f V"), ("2p f G", "3s f V"), ("3p m G", "3s m V"),
                                 ("3p f G", "2s f V"), ("1s m V", "1p f V"), ("1s f V", "2d m V"), ("2d f V", "3d f V"),
                                 ("1p m V", "3p f V"), ("2p f V", "2p m V")])

        self.add_xross_perm_variation(
                                [("1s m G", "3s f G"), ("1s m V", "3s f V"), ("1s f V", "2s f G"), ("2s m V", "2d m G"),
                                 ("2s f V", "3d m G"), ("3s m V", "1s f G"), ("2s m G", "3p m V"), ("1d m G", "2d f G"),
                                 ("1d f G", "1p m G"), ("1p m V", "3s m G"), ("1p f V", "3p f V"), ("2p f V", "2d f V"),
                                 ("3d f G", "2p m V"), ("1p f G", "1d m V"), ("2p m G", "3d f V"), ("2d m V", "3p m G"),
                                 ("2p f G", "1d f V"), ("3p f G", "3d m V")])

        self.add_xross_perm_variation(
                                [("1s m G", "1p m G"), ("1s f G", "3d m G"), ("2s m G", "3p f G"), ("2s f G", "3s f V"),
                                 ("3s m G", "1d m G"), ("3s f G", "2d m V"), ("1d f G", "3d m V"), ("2d m G", "1p m V"),
                                 ("2d f G", "1p f V"), ("3d f G", "1d f V"), ("1p f G", "3s m V"), ("2p m G", "3d f V"),
                                 ("2p f G", "1d m V"), ("3p m G", "2d f V"), ("1s m V", "2p f V"), ("1s f V", "3p f V"),
                                 ("2s m V", "2p m V"), ("2s f V", "3p m V")])

        self.add_xross_perm_variation(
                                [("1s m G", "2s f G"), ("3s m G", "2s m V"), ("1s m V", "1s f G"), ("2s f V", "1s f V"),
                                 ("3s f V", "3s m V"), ("1d m G", "1p f V"), ("2d m G", "1p m G"), ("3d m G", "2s m G"),
                                 ("3d f G", "2p m V"), ("1p m V", "2p m G"), ("2p f V", "2d f G"), ("3p m V", "3p m G"),
                                 ("3p f V", "3p f G"), ("1p f G", "2p f G"), ("1d f V", "3d m V"), ("2d m V", "1d f G"),
                                 ("2d f V", "3s f G"), ("3d f V", "1d m V")])

        self.add_xross_perm_variation(
                                [("1s m G", "3s m G"), ("2s m G", "2s f G"), ("3s f G", "1s f G"), ("1d m G", "2d m G"),
                                 ("2d f G", "3d f G"), ("3d m G", "1p m G"), ("1p f G", "3p f G"), ("2p f G", "1d f G"),
                                 ("3p m G", "2p m G"), ("1s m V", "1s f V"), ("2s m V", "3s f V"), ("3s m V", "2s f V"),
                                 ("1d m V", "3d m V"), ("2d m V", "2d f V"), ("3d f V", "1d f V"), ("1p m V", "3p m V"),
                                 ("1p f V", "2p f V"), ("3p f V", "2p m V")])

        self.add_xross_perm_variation(
                                [("2s m G", "1p f G"), ("2s f G", "1s m G"), ("2d m G", "1p m V"), ("2d f G", "3d f G"),
                                 ("2p m G", "1s m V"), ("2p f G", "3d m G"), ("2s m V", "3d f V"), ("2s f V", "1d m G"),
                                 ("2d m V", "3p m V"), ("2d f V", "3s f G"), ("2p m V", "3d m V"), ("2p f V", "3p m G"),
                                 ("3s m G", "1d m V"), ("1p m G", "3s f V"), ("3p f G", "1p f V"), ("3s m V", "1d f G"),
                                 ("1d f V", "1s f V"), ("3p f V", "1s f G")])

        self.add_xross_perm_variation(
                                [("1s m G", "2d f V"), ("1s f G", "3d m V"), ("1d m G", "3p m G"), ("1d f G", "2p f G"),
                                 ("1p m G", "1s f V"), ("1p f G", "3d f V"), ("1s m V", "2s f V"), ("1d m V", "2p f V"),
                                 ("1d f V", "2d m G"), ("1p m V", "3p f G"), ("1p f V", "3s m V"), ("3d m G", "2d m V"),
                                 ("3d f G", "2s m V"), ("3s m G", "2p m V"), ("3s f G", "2d f G"), ("3s f V", "2s m G"),
                                 ("3p m V", "2p m G"), ("3p f V", "2s f G")])

        self.add_xross_perm_variation(
                                [("1s m G", "2d m G"), ("1s f G", "2p m V"), ("2s f G", "3d f G"), ("3s m G", "1p m V"),
                                 ("3s f G", "1d m V"), ("1d m G", "3p m G"), ("1d f G", "2p m G"), ("2d f G", "2p f V"),
                                 ("3d m G", "3d m V"), ("1p m G", "3p m V"), ("1p f G", "1p f V"), ("2p f G", "3p f G"),
                                 ("1s m V", "2s f V"), ("1s f V", "2d f V"), ("1d f V", "2s m V"), ("2d m V", "3s f V"),
                                 ("3d f V", "2s m G"), ("3p f V", "3s m V")])

        self.add_xross_perm_variation(
                                [("1s f G", "3p f V"), ("1d m G", "1s m G"), ("1d f G", "2s f V"), ("1p m G", "2s f G"),
                                 ("1p f G", "3p f G"), ("1s m V", "3d m G"), ("1s f V", "2d f G"), ("1d m V", "3d m V"),
                                 ("1d f V", "2s m G"), ("1p m V", "2d m G"), ("1p f V", "2d f V"), ("3s f V", "3s m G"),
                                 ("2p m G", "3d f V"), ("2p f G", "3p m G"), ("2s m V", "3d f G"), ("2d m V", "3p m V"),
                                 ("2p m V", "3s m V"), ("2p f V", "3s f G")])

        self.add_xross_perm_variation(
                                [("1s m G", "2d m V"), ("1s f G", "3s f V"), ("3p m G", "2s f G"), ("3p f G", "1d f G"),
                                 ("2s m G", "3s m V"), ("3d m V", "3p m V"), ("3d f V", "1d m V"), ("1d m G", "2d f V"),
                                 ("1p f V", "2p f V"), ("2p m V", "1p m V"), ("3s m G", "1s f V"), ("3s f G", "3p f V"),
                                 ("1d f V", "3d f G"), ("3d m G", "2s m V"), ("1p f G", "1s m V"), ("2d m G", "2s f V"),
                                 ("2d f G", "2p f G"), ("1p m G", "2p m G")])

        self.add_xross_perm_variation(
                                [("1s m G", "3p f G"), ("1s f G", "3d f V"), ("1d m G", "3s f G"), ("1d f G", "2p m G"),
                                 ("1p m G", "3s m V"), ("1p f G", "2d m G"), ("2s m G", "3d f G"), ("2s f G", "2p f G"),
                                 ("3s m G", "3p m V"), ("3d m G", "2d f G"), ("3p m G", "3d m V"), ("1s m V", "1p m V"),
                                 ("1s f V", "2d m V"), ("2s m V", "2p f V"), ("2s f V", "3p f V"), ("2d f V", "1d f V"),
                                 ("2p m V", "1p f V"), ("3s f V", "1d m V")])

        self.add_xross_perm_variation(
                                [("1s m G", "2s f G"), ("1d m G", "1d f V"), ("1d f G", "1d m V"), ("1p m G", "2p f V"),
                                 ("1p f G", "1s f V"), ("2s m G", "2p f G"), ("2d m G", "1p m V"), ("2d f G", "3p f V"),
                                 ("2p m G", "3d f V"), ("2s m V", "3p m V"), ("2s f V", "3p f G"), ("2d m V", "1s m V"),
                                 ("2d f V", "3s f V"), ("3s m G", "2p m V"), ("3d m G", "1s f G"), ("3d f G", "3p m G"),
                                 ("3s m V", "3s f G"), ("3d m V", "1p f V")])

        # full swap 1
        old_list = [("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T,
                     "3d g " + T, "3p g " + T) for T in self.TENSES_CASES]
        new_list = [("2s g " + T, "3p g " + T, "3d g " + T, "3s g " + T, "1p g " + T, "1d g " + T, "1s g " + T,
                     "2p g " + T, "2d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

        # full swap 2
        old_list = [("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T,
                     "3d g " + T, "3p g " + T) for T in self.TENSES_CASES]
        new_list = [("2s g " + T, "1s g " + T, "3s g " + T, "2d g " + T, "1p g " + T, "3p g " + T, "2p g " + T,
                     "1d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

    def _create_syncretic_GEN_files(self):
        """syncretic variations that happened historically (geader syacretism)"""
        # syn: 2V:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f V", "2a m V")])

        # syn: p:f -> m (TRUE)
        self.add_gen_sync_variation( [("zp" + " f " + T, "zp" + " m " + T) for T in self.TENSES_CASES])

        # V3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f V", "3p m V")])

        # Gp: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f G", "zp m G")])

        # 3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f " + T, "3p m " + T) for T in self.TENSES_CASES])

        # syn: 2:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES])

        # syn G3d: f -> m (TRUE)
        self.add_gen_sync_variation( [("3d f G", "3d m G")])

        # syn G2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f G", "2s m G")])

        # syn V2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f V", "2s m V")])

        # syn G2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f G", "2a m G")])

        # syn G3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f G", "3p m G")])

        # syn 2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES])

        # syn Vp: f -> m
        self.add_gen_sync_variation( [("zp f V", "zp m V")])

        # syn p: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f " + T, "zp m " + T) for T in self.TENSES_CASES])

        # syn V1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f V", "1s m V")])

        # syn G3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f G", "3s m G")])

        # syn G2p: f->m (TRUE)
        self.add_gen_sync_variation( [("2p f G", "2p m G")])

        # FALSE

        # syn s/d (FALSE)
        self.add_gen_sync_variation(
                                [("zs f " + T, "zs m " + T) for T in self.TENSES_CASES] + [("zd f " + T, "zd m " + T) for T
                                                                                       in self.TENSES_CASES])

        # syn 3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # syn s: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f " + T, "zs m " + T) for T in self.TENSES_CASES])

        # syn 2s: f->m, 3s: f->m (FALSE)
        self.add_gen_sync_variation(
                                [("2s f " + T, "2s m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3s m " + T) for T
                                                                                       in self.TENSES_CASES])

        # TRUE
        # 2d
        self.add_gen_sync_variation( [("2d f " + T, "2d m " + T) for T in self.TENSES_CASES])

        # Gd
        self.add_gen_sync_variation( [("zd f G", "zd m G")])

        # 2s
        self.add_gen_sync_variation( [("2s f " + T, "2s m " + T) for T in self.TENSES_CASES])

        # 2
        self.add_gen_sync_variation( [("2a f " + T, "2a f " + T) for T in self.TENSES_CASES])

        # V2p
        self.add_gen_sync_variation( [("2p f V", "2p m V")])

        # dG, dV2
        self.add_gen_sync_variation( [("zd f G", "zd m G")] + [("2d f V", "2d m V")])

        # alle
        self.add_gen_sync_variation( [("za f " + T, "za m " + T) for T in self.TENSES_CASES])

        # G2, G3p
        self.add_gen_sync_variation( [("2a f G", "2a m G")] + [("3p f G", "3p m G")])

        # 3d
        self.add_gen_sync_variation( [("3d f " + T, "3d m " + T) for T in self.TENSES_CASES])

        # G2, G3d/p
        self.add_gen_sync_variation( [("2a f G", "2a m G")] + [("3d f G", "3d m G"), ("3p f G", "3p m G")])

        # V2d/p
        self.add_gen_sync_variation( [("2d f V", "2d m V"), ("2p f V", "2p m V")])

        # 2, 3d/p
        self.add_gen_sync_variation(
                                [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES] + [("3d f " + T, "3d m " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("3p f " + T, "3p m " + T) for T in self.TENSES_CASES])

        # 3p/d
        self.add_gen_sync_variation(
                                [("3d f " + T, "3d m " + T) for T in self.TENSES_CASES] + [("3p f " + T, "3p m " + T) for T
                                                                                       in self.TENSES_CASES])

        # Vp/d3
        self.add_gen_sync_variation( [("3p f V", "3p m V"), ("3d f V", "3d m V")])

        # Gp/d
        self.add_gen_sync_variation( [("zd f G", "zd m G")] + [("zp f G", "zp m G")])

        # FALSE

        # syn V3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m V", "3a f V")])

        # syn Vs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f V", "zs m V")])

        # syn G3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m G", "3a f G")])

        # syn Gs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f G", "zs m G")])

        # 3s; 2p
        self.add_gen_sync_variation(
                                [("2p f " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3s m " + T) for T
                                                                                       in self.TENSES_CASES])

        # V2p, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"), ("3s f G", "3s m G")])

        # 3s; 2p/d
        self.add_gen_sync_variation(
                                [("2p f " + T, "2p m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2d m " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("3s f " + T, "3s m " + T) for T in self.TENSES_CASES])

        # V2p/d, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"), ("2d f V", "2d m V"), ("3s f G", "3s m G")])

    def _create_syncretic_PERS_files(self):
        """syncretic variations that happened historically (other thaa Geader)"""
        # syn Vsm: 2 -> 1
        self.add_pers_sync_variation( [("2s m V", "1s m V")])

        # syn Vsf: 2 -> 1
        self.add_pers_sync_variation( [("2s f V", "1s f V")])

        # syn Vdm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V")])

        # syn Vdm: 2->1; Vsm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V"), ("2s m V", "1s m V")])

        # Vd: 2 -> 1
        self.add_pers_sync_variation( [("2d g V", "1d g V")])

        # syn 1 -> 2
        self.add_pers_sync_variation( [("1a g " + T, "2a g " + T) for T in self.TENSES_CASES])

        # syn 2 -> 3
        self.add_pers_sync_variation( [("2a g " + T, "3a g " + T) for T in self.TENSES_CASES])

        # syn 3 -> 1
        self.add_pers_sync_variation( [("3a g " + T, "1a g " + T) for T in self.TENSES_CASES])

        # syn f:3->2
        self.add_pers_sync_variation( [("3a f " + T, "2a f " + T) for T in self.TENSES_CASES])

        # syn fp:3->2
        self.add_pers_sync_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # syn p:  2->1,3->1
        self.add_pers_sync_variation(
                                [("2p g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # syn s:2->3
        self.add_pers_sync_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # syn s:1->2
        self.add_pers_sync_variation( [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES])

        # syn p:2->3
        self.add_pers_sync_variation( [("2p g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # syn Vp:3->2
        self.add_pers_sync_variation( [("3p g V", "2p g V")])

        # Gp: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G")])

        # Vs: 2->1
        self.add_pers_sync_variation( [("2s g V", "1s g V")])

        # Gpf: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G")])

        # G:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G")] + [("3d f G", "2d f G")])

        # G: d/p: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G")] + [("3d g G", "2d g G")])

        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")] + [("3a g G", "1a g G")])

        # mp:3->2, fp:3->1
        self.add_pers_sync_variation(
                                [("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3p f " + T, "1p f " + T) for T
                                                                                       in self.TENSES_CASES])

        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")] + [("2a f G", "1a f G")])

    def _create_syncretic_NUM_files(self):
        # syn: d -> p
        self.add_num_sync_variation( [("zd" + " g " + T, "zp" + " g " + T) for T in self.TENSES_CASES])

        # 1: d -> p
        self.add_num_sync_variation( [("1d" + " g " + T, "1p" + " g " + T) for T in self.TENSES_CASES])

        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m V", "3s m V")])

        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g V", "1p g V")])

        # syn G1: s->p
        self.add_num_sync_variation( [("1s g G", "1p g G")])

        # 3m: p->s
        self.add_num_sync_variation( [("3p m " + T, "3s m " + T) for T in self.TENSES_CASES])

        # FASLE
        # syn p->d
        self.add_num_sync_variation( [("zp g " + T, "zd g " + T) for T in self.TENSES_CASES])

        # syn s->p
        self.add_num_sync_variation( [("zs g " + T, "zp g " + T) for T in self.TENSES_CASES])

        # syn s->d
        self.add_num_sync_variation( [("zs g " + T, "zd g " + T) for T in self.TENSES_CASES])

        # syn 3: d-> p
        self.add_num_sync_variation( [("3d g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 2: d->p
        self.add_num_sync_variation( [("2d g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # G1: s/d->p
        self.add_num_sync_variation( [("1d g G", "1p g G")] + [("1s g G", "1p g G")])

        # V3f: s->p
        self.add_num_sync_variation( [("3s f V", "3p f V")])

        # 3m: d->s
        self.add_num_sync_variation( [("3d m " + T, "3s m " + T) for T in self.TENSES_CASES])

        # V3: d->s
        self.add_num_sync_variation( [("3d g V", "3s g V")])


        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")] + [("zd g G", "zs g G")])

        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V")] + [("3s g G", "3p g G")])

        # 2:d->p, 3:d->s
        self.add_num_sync_variation(
                                [("2d g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3d g " + T, "3s g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 1:d->s, 2:p->s
        self.add_num_sync_variation(
                                [("1d g " + T, "1s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "2s g " + T) for T
                                                                                       in self.TENSES_CASES])

        # m: p->s
        self.add_num_sync_variation( [("zp m " + T, "zs m " + T) for T in self.TENSES_CASES])

        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V"), ("3s f G", "3d f G")])

        # f: p->s
        self.add_num_sync_variation( [("zp f " + T, "zs f " + T) for T in self.TENSES_CASES])

        # f: p/d->s
        self.add_num_sync_variation(
                                [("zp f " + T, "zs f " + T) for T in self.TENSES_CASES] + [("zd f " + T, "zs f " + T) for T
                                                                                       in self.TENSES_CASES])

        # m: p/d->s
        self.add_num_sync_variation(
                                [("zp m " + T, "zs m " + T) for T in self.TENSES_CASES] + [("zd m " + T, "zs m " + T) for T
                                                                                       in self.TENSES_CASES])

        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation(
                                [("zp m G", "zs m G")] + [("zd m G", "zs m G")] + [("zp f V", "zs f V")] + [
                                    ("zd f V", "zs f V")])

        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")] + [("zd m G", "zp m G")])

        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g G", "3p g G")] + [("zp f V", "zd f V")])

    def _create_syncretic_X_files(self):
        # syn G3sf -> G2sm
        self.add_xross_sync_variation( [("3s f G", "2s m G")])

        # syn G3sm -> G1pm
        self.add_xross_sync_variation( [("3s m G", "1p m G")])

        # syn V3p -> V3sm,  V3d->V3sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")] + [("3d g V", "3s m V")])

        # syn G3:d->pf
        self.add_xross_sync_variation( [("3d g G", "3p f G")])

        # syn V3:dm->pf
        self.add_xross_sync_variation( [("3d m V", "3p f V")])

        # syn V3:p->sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")])

        # syn Gd: 3f->2m
        self.add_xross_sync_variation( [("3d f G", "2d m G")])

        # FALSE

        # syn G2sf -> G3pm
        self.add_xross_sync_variation( [("2s f G", "3p m G")])

        # syn G3pf -> G2pm
        self.add_xross_sync_variation( [("3p f G", "2p m G")])

        # syn G2sm -> G1pm
        self.add_xross_sync_variation( [("2s m G", "1p m G")])

        # syn G2p -> G2sf; G2d -> G2sf
        self.add_xross_sync_variation( [("2p g G", "2s f G")] + [("2d g G", "2d f G")])

        # syn G3p ->  G1sm
        self.add_xross_sync_variation( [("3p g G", "1s m G")])

        # G: s/d: 3f -> 2m
        self.add_xross_sync_variation( [("3d f G", "2d m G"), ("3s f G", "2s m G")])

        # s: 3f -> 2m
        self.add_xross_sync_variation( [("3s f " + T, "2s m " + T) for T in self.TENSES_CASES])

        # Vs: 2f -> 1(m)
        self.add_xross_sync_variation( [("2s f V", "1s m V")])

        # G: 3sf -> 2sm, 2pm -> 2sm
        self.add_xross_sync_variation( [("3s f G", "2s m G")])

        # Vs: 2m->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])

        # Vs: 2m->1, 3f->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])

        # 3: d->pm
        self.add_xross_sync_variation( [("3d g " + T, "3p m " + T) for T in self.TENSES_CASES])

        # G2:pf->sm
        self.add_xross_sync_variation( [("2p f G", "2s m G")])

        # G2:p/df->sm
        self.add_xross_sync_variation( [("2p f G", "2s m G"), ("2d f G", "2s m G")])

        # G: 2pf->3sm
        self.add_xross_sync_variation( [("2p f G", "3s m G")])

        # V3:pf->sm
        self.add_xross_sync_variation( [("3p f V", "3s m V")])

        # G:3pf->2sf
        self.add_xross_sync_variation( [("3p f G", "2s f G")])

    def _create_syncretic_TENSE_files(self):
        # syn p: G -> V
        self.add_ten_sync_variation( [("zp g G", "zp g V")])

        # syn s: G -> V
        self.add_ten_sync_variation( [("zs g G", "zs g V")])

        # syn 2: G -> V
        self.add_ten_sync_variation( [("2a g G", "2a g V")])

        # syn 3: G -> V
        self.add_ten_sync_variation( [("3a g G", "3a g V")])

        # syn p: V -> G
        self.add_ten_sync_variation( [("zp g V", "zp g G")])

        # syn s: V -> G
        self.add_ten_sync_variation( [("zs g V", "zs g G")])

        # syn 2: V -> G
        self.add_ten_sync_variation( [("2a g V", "2a g G")])

        # syn 3: V -> G
        self.add_ten_sync_variation( [("3a g V", "3a g G")])

        # syn 3p: V -> G,  2s: G -> V
        self.add_ten_sync_variation( [("3p g V", "3p g G"), ("2s g G", "2s g V")])

        # syn 2: V -> G,  p: G -> V
        self.add_ten_sync_variation( [("2a g V", "3a g G")] + [("zp g G", "zp g V")])



class PermSynCreatorSA(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "SA"

        self.TENSES_CASES = ["G", "V", "S"]
        self.TENSES_CASES_PC = ["G", "S"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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
        self._create_syncretic_GEN_files()
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

    def _create_permutation_PERS_files(self):
        """
        creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
        """
        # d.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES])
        # s: 1 <-> 2, p:1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for
                                                                                          T in self.TENSES_CASES])
        # s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])
        # s: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for
                                                                                          T in self.TENSES_CASES])
        # d:1 <-> 3, s: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "3d g " + T) for
                                                                                          T in self.TENSES_CASES])
        # d:1 <-> 2, s: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T) for
                                                                                          T in self.TENSES_CASES])
        # s.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES])
        # d: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])
        # s.m: 2 <-> 3, p.f: 2 <-> 3, d: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])
        # d.f: 1 <-> 3, p.m: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T) for
                                                                                          T in self.TENSES_CASES])
        # pfG: 2 <-> 3, sfG: 3<-> 2, dGm: 2<->3
        self.add_pers_perm_variation( [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("3s f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "2d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC])
        # sV: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])
        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V"), ("2d g V", "3d g V"), ("1p g V", "2p g V")])
        # sG: 1 <-> 3, dG: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation(
                                [("1p g V", "2p g V")] + [("1s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])
        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation(
                                [("1s g V", "3s g V"), ("2d g V", "3d g V")] + [("1p g " + PC, "2p g " + PC) for PC in
                                                                                self.TENSES_CASES_PC])
        # dm: 1 <-> 2, df: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T) for
                                                                                          T in self.TENSES_CASES])
        # sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T) for
                                                                                          T in self.TENSES_CASES])
        # sm: 1 <-> 2
        self.add_pers_perm_variation( [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES])
        # pm: 1 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES])
        # pm: 1 <-> 2
        self.add_pers_perm_variation( [("1p m " + T, "2p m " + T) for T in self.TENSES_CASES])
        # pf: 2 <-> 3
        self.add_pers_perm_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])
        # pf: 1 <-> 2
        self.add_pers_perm_variation( [("1p f " + T, "2p f " + T) for T in self.TENSES_CASES])
        # dm: 1 <-> 2, df: 1 <-> 3, sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T)
                                                                                             for T in self.TENSES_CASES])
        # pm: 1 <-> 3, pf: 2 <-> 3, dm: 2 <-> 3, sm: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES] + [
                                    ("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "3s m " + T)
                                                                                             for T in self.TENSES_CASES])
        # pm: 2 <-> 3
        self.add_pers_perm_variation( [("2p m " + T, "3p m " + T) for T in self.TENSES_CASES])
        # pf: 2 <-> 3, df: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "3d f " + T) for
                                                                                          T in self.TENSES_CASES])
        # pf: 1 <-> 2, df: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2p f " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "1d f " + T) for
                                                                                          T in self.TENSES_CASES])
        # d: 1 <-> 2, p: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for
                                                                                          T in self.TENSES_CASES])
        # d: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("3d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "2p g " + T) for
                                                                                          T in self.TENSES_CASES])
        # sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s f " + T) for
                                                                                          T in self.TENSES_CASES])
        # dG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])
        # dG: 2 <-> 1, pG: 2 <-> 1, dV: 2 <-> 3, pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g V", "3d g V"), ("2p g V", "3p g V")])
        # dm: 2 <-> 3, pm: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T) for
                                                                                          T in self.TENSES_CASES])
        # df: 2 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for
                                                                                          T in self.TENSES_CASES])
        # dmG: 2 <-> 3, pmG: 2 <-> 3
        self.add_pers_perm_variation( [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])
        # dfG: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2d f " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC])
        # dG: 2 <-> 1, pG: 2 <-> 1, smV: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s m V", "3s m V")] + [("1d g " + PC, "2d g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])
        # sfV: 2 <-> 3
        self.add_pers_perm_variation( [("2s f V", "3s f V")])
        # sfV: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s f V", "3s f V")] + [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])
        # d,p: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "3p g " + T) for
                                                                                          T in self.TENSES_CASES])
        # dV,pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g V"), ("2p g V", "3p g V")])
        # V: 2 <-> 3
        self.add_pers_perm_variation( [("2a g V", "3a g V")])
        # Vs: 2 <-> 3x
        self.add_pers_perm_variation( [("2s g V", "3s g V")])
        # Vs: 1 <-> 3
        self.add_pers_perm_variation( [("1s g V", "3s g V")])
        # dV,pV: 1 <-> 3
        self.add_pers_perm_variation( [("1d g V", "3d g V"), ("1p g V", "3p g V")])
        # dG,pG: 1 <-> 2, sV: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g G", "2d g G"), ("1p g G", "2p g G"), ("1s g V", "2s g V"), ("2p g V", "3p g V"),
                                 ("2d g V", "3d g V")])
        # sG: 1 <-> 2, pG,dG: 2 <-> 3
        self.add_pers_perm_variation( [("1s g G", "2s g G"), ("2d g G", "3d g G"), ("2p g G", "3p g G")])
        # V: 1<->2
        self.add_pers_perm_variation( [("1a g V", "2a g V")])
        # G: 2<->3
        self.add_pers_perm_variation( [("2a g G", "3a g G")])
        # strong permutations
        self.add_pers_perm_variation( [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2s f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("3d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m V", "2s m V"),
                                                                                                ("1s f V", "2s f V"),
                                                                                                ("1d m V", "2d m V"),
                                                                                                ("2d f V", "3d f V"),
                                ("2p m V", "1p m V"), ("3p f V", "1p f V")])
        # strong permutation 2
        self.add_pers_perm_variation( [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("2d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "2s m V"),
                                                                                                ("1s f V", "3s f V"),
                                                                                                ("2d m V", "1d m V"),
                                                                                                ("2d f V", "3d f V"),
                                ("3p m V", "1p m V"), ("3p f V", "1p f V")])


        # strong permutation 3
        right = [("1s f " + PC, "2s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1d m " + PC, "2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1p m " + PC, "2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1p f " + PC, "2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1d m V", "2d m V", "3d m V")] + [("1p f V", "2p f V", "3p f V")]
        left = [("1d f V", "2d f V", "3d f V")] + [("1p m V", "2p m V", "3p m V")] + [
            ("1s m V", "2s m V", "3s m V")] + [
                   ("1d f " + PC, "2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dG: 1 <-> 2, pG: 1 <-> 2
        # dV: 2 <-> 3, pV: 2 <-> 3
        # sV: 1 <-> 3, sG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g V"), ("2p g V", "3p g V"), ("1s g V", "3s g V")] + [
            ("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + PC, "1p g " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("2s g " + PC, "3s g " + PC)
                                    for PC in self.TENSES_CASES_PC])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2s g V", "3s g V", "1s g V")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [
            ("3s g " + PC, "1s g " + PC, "2s g " + PC) for PC in self.TENSES_CASES_PC]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        # dfV: 2 <-> 3, pfV: 2 <-> 3
        # sG: 1 <-> 3, sV: 1 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "3p m " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("2d f V", "3d f V")] + [("2p f V", "3p f V")] + [("1s g " + PC, "3s g " + PC) for
                                                                                      PC in
                                                                                      self.TENSES_CASES_PC] + [
                                    ("1s g V", "3s g V")])

        # sG: 1->2->3
        # sV: 3->2->1
        # dG: 1 <-> 3 (daaa dGm: 1<->2),  pG: 1 <-> 3 (daaa pGm: 1<->2)
        # dV: 1 <-> 2 (daaa dVf: 1<->3),  pV: 1 <-> 2 (daaa pVf: 1<->3)
        right = [("2s g " + PC, "3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3s g V", "1s g V", "2s g V")]
        swap = [("3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("3p g " + PC, "1p g " + PC) for PC in
                                                                            self.TENSES_CASES_PC] + [
                   ("2d g V", "1d g V")] + [
                   ("2p g V", "1p g V")] + [("2d m " + PC, "1d m " + PC) for PC in self.TENSES_CASES_PC] + [
                   ("2p m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("3d f V", "1d f V")] + [
                   ("3p f V", "1p f V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # dG: 1->2->3,  pG: 1->2->3
        # dV: 3->2->1,  pV: 3->2->1
        # sG: 1 <-> 3
        # sV: 1 <-> 3 (daaa sVm: 1 <-> 2)
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")]
        swap = [("3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC] + [("3s g V", "1s g V")] + [
            ("2s m V", "1s m V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # G: sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s f " + PC, "3s f " + PC)
                                    for PC in self.TENSES_CASES_PC])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g G", "3d g G", "1d g G")] + [("2p g G", "3p g G", "1p g G")] + [
            ("2s g V", "3s g V", "1s g V")] + [
                    ("1p m S", "2p m S", "3p m S")] + [("1d f S", "2d f S", "3d f S")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [
            ("3s g G", "1s g G", "2s g G")] + [
                   ("1d m S", "2d m S", "3d m S")]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # strong permutation 1
        self.add_pers_perm_variation(
                                [("1s m G", "3s m G")] + [("2s f G", "1s f G")] + [("3s m V", "2s m V")] + [
                                    ("1s f V", "2s f V")] + [("1s m S", "2s m S")] + [("2s f S", "3s f S")] + [
                                    ("2d m G", "3d m G")] + [
                                    ("3d f G", "1d f G")] + [("1d m V", "2d m V")] + [("2d f V", "3d f V")] + [
                                    ("3d m S", "2d m S")] + [("2d f S", "3d f S")] + [("1d m S", "2d m S")] + [
                                    ("3p m G", "2p m G")] + [("1p f G", "2p f G")] + [("2p m V", "1p m V")] + [
                                    ("3p f V", "1p f V")] + [("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [
                                    ("1p f S", "2p f S")])

        # strong permutation 2
        self.add_pers_perm_variation(
                                [("1s m G", "2s m G")] + [("1s f G", "3s f G")] + [("1s m V", "2s m V")] + [
                                    ("1s f V", "3s f V")] + [("2s m S", "1s m S")] + [("3s f S", "1s f S")] + [
                                    ("3s f S", "2s f S")] + [
                                    ("2d m G", "3d m G")] + [("2d f G", "1d f G")] + [("2d m V", "1d m V")] + [
                                    ("2d f V", "3d f V")] + [("3d m S", "2d m S")] + [("1d f S", "2d f S")] + [
                                    ("3p m G", "2p m G")] + [("3p f G", "1p f G")] + [("3p m V", "1p m V")] + [
                                    ("3p f V", "1p f V")] + [("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [
                                    ("1p f S", "2p f S")])

    def _create_permutation_NUM_files(self):
        """
        creates all permutation files where NUM-features are swapped (s <-> d <-> p)
        """

        # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p
        self.add_num_perm_variation( [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2f: s <-> p, 3m: s <-> p
        self.add_num_perm_variation( [("2s f " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3p m " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p, 3f: d <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3d f " + T) for T in self.TENSES_CASES])

        # 1m: s <-> p
        self.add_num_perm_variation( [("1s m " + T, "1p m " + T) for T in self.TENSES_CASES])

        # 1m: s <-> d, 2f: d <-> p
        self.add_num_perm_variation( [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: s <-> d, 3: d <-> p
        self.add_num_perm_variation( [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T) for T in self.TENSES_CASES])

        # 2G: s <-> p
        self.add_num_perm_variation( [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("3d g V", "3p g V")] +[("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # 3G:s<->p, 2V:d<->p, 1m: s<->d
        self.add_num_perm_variation( [("2d g V", "2p g V")] +[("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] +[("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])

        # 1f: s <-> p
        self.add_num_perm_variation( [("1s f " + T, "1p f " + T) for T in self.TENSES_CASES])

        # 2f: s <-> d, 3m: s <-> d
        self.add_num_perm_variation( [("2s f " + T, "2d f " + T) for T in self.TENSES_CASES] +[("3s m " + T, "3d m " + T) for T in self.TENSES_CASES])

        # 2m: s <-> d, 1f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES] +[("1s f " + T, "1d f " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p, 1m: s <-> d
        self.add_num_perm_variation(
        [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] +[("1s m " + T, "1d m " + T) for T in
        self.TENSES_CASES])

        # 1V: s <-> d, 3G: s <-> d
        self.add_num_perm_variation(
        [("1s g V", "1d g V")] +[("3s g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # 1G: s <-> d, 2: d <-> p
        self.add_num_perm_variation(
        [("1s g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] +[("2p g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # 3f: s <-> p
        self.add_num_perm_variation( [("3s f " + T, "3p f " + T) for T in self.TENSES_CASES])

        # 1: s <-> p, 2: d <-> p
        self.add_num_perm_variation(
        [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] +[("2d g " + T, "2p g " + T) for T in
        self.TENSES_CASES])

        # 2V: s <-> p, 3mV: s <-> p
        self.add_num_perm_variation( [("2s g V", "2p g V")] +[("3s m V", "3p m V")])

        # 2fV: s <-> p
        self.add_num_perm_variation( [("2s f V", "2p f V")])

        # 2Vf: s <-> p, 3Gm: s <-> p
        self.add_num_perm_variation(
        [("2s f V", "2p f V")] +[("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # 2m: s <-> d, 3f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES])

        # 3mG: s <-> p
        self.add_num_perm_variation( [("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # f: s -> d -> p;   m: p -> d -> s
        self.add_num_perm_variation( rotate_right_list=[("zs f " + T, "zd f " + T, "zp f " + T) for T in self.TENSES_CASES], rotate_left_list=[("zs m " + T, "zd m " + T, "zp m " + T) for T in self.TENSES_CASES])

        # f: s <-> p,   m: d <-> p
        self.add_num_perm_variation( [("zs f " + T, "zp f " + T) for T in self.TENSES_CASES]+[("zd m " + T, "zp m " + T) for T in self.TENSES_CASES])

        # STRONG

        # strong permutation 1
        self.add_num_perm_variation( [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC]+[("1s f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC]+[("2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC]+[("2d f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC]+[("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC]+[("3p f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC]+[("1s m V", "1d m V")]+[("1s f V", "1p f V")]+[("2d m V", "2p m V")]+[("2d f V", "2s f V")]+[("3p m V", "3s m V")]+[("3p f V", "3s f V")])

        # strong permutation 2
        self.add_num_perm_variation( [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC]+[("1d f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC]+[("2d m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC]+[("2p f " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC]+[("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC]+[("3s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC]+[("1p m V", "1d m V")]+[("1s f V", "1p f V")]+[("2s m V", "2p m V")]+[("2d f V", "2s f V")]+[("3d m V", "3p m V")]+[("3p f V", "3s f V")])

        # strong permutation 3
        right=[("1s m " + PC, "1d m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC]+[("2s m " + PC, "2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC]+[("3s m " + PC, "3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC]+[("1s m V", "1d m V", "1p m V")]+[("2s m V", "2d m V", "2p m V")]
        left=[("1s f " + PC, "1d f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC]+[("2s f " + PC, "2d f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC]+[("3s f " + PC, "3d f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC]+[("2s f V", "2d f V", "2p f V")]+[("3s f V", "3d f V", "3p f V")]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 2mV:  s <-> p, 2fG: s <-> p;
        # 3fV: s <-> p, 3mG: s <-> p; 1G: s <-> p
        self.add_num_perm_variation( [("2s m V", "2p m V")]+[("3s f V", "3p f V")]+[("2s f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC]+[("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC]+[("1s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G s <-> p, 3V s <-> d,
        # 3mG d <-> p, 3fG: s <-> p,
        # 3mV:  s <-> d, 3fV:  d <-> p,
        # 1: s <-> d
        self.add_num_perm_variation( [("3d m V", "3s m V")]+[("3p f V", "3d f V")]+[("3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC]+[("3s f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC]+[("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC]+[("3s g V", "3d g V")]+[("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # strong permutation 1
        self.add_num_perm_variation( [("1s m G", "1p m G")]+[("1s f G", "1d f G")]+[("1s m G", "1d m G")]+[("1s f G", "1p f G")]+[("1s m V", "1d m V")]+[("1s f V", "1p f V")]+[("1s m S", "1p m S")]+[("1s f S", "1p f S")]+[("2d m G", "2p m G")]+[("2d f G", "2s f G")]+[("2d m V", "2p m V")]+[("2d f V", "2s f V")]+[("2s m S", "2p m S")]+[("2s f S", "2p f S")]+[("3p m G", "3s m G")]+[("3p f G", "3d f G")]+[("3p m V", "3s m V")]+[("3p f V", "3s f V")]+[("3d m S", "3s m S")]+[("3d f S", "3p f S")])


        # strong permutation 2
        self.add_num_perm_variation( [("1s m G", "1p m G")]+[("1d f G", "1s f G")]+[("1p m V", "1d m V")]+[("1s f V", "1p f V")]+[("1d m S", "1s m S")]+[("1d f S", "1p f S")]+[("2d m G", "2s m G")]+[("2p f G", "2d f G")]+[("2s m V", "2p m V")]+[("2d f V", "2s f V")]+[("2s m S", "2p m S")]+[("2d f S", "2p f S")]+[("3p m G", "3s m G")]+[("3s f G", "3d f G")]+[("3d m V", "3p m V")]+[("3p f V", "3s f V")]+[("3s f S", "3d f S")]+[("3p m S", "3s m S")])

        # strong permutation 3
        right=[("1s m G", "1d m G", "1p m G")]+[("1s m V", "1d m V", "1p m V")]+[("2s m G", "2d m G", "2p m G")]+[("2s m V", "2d m V", "2p m V")]+[("2s f S", "2d f S", "2p f S")]+[("3s m G", "3d m G", "3p m G")]
        left=[("3s f G", "3d f G", "3p f G")]+[("3s f V", "3d f V", "3p f V")]+[("2s f G", "2d f G", "2p f G")]+[("2s f V", "2d f V", "2p f V")]+[("1s f G", "1d f G", "1p f G")]+[("1s f S", "1d f S", "1p f S")]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 1V: s <-> d, 3G: s <-> d, 2C: s <-> d, 2S: s <-> d
        self.add_num_perm_variation( [("1s g V", "1d g V")]+[("3s g G", "3d g G")]+[("3s g S", "3d g S")])

        # 1G: s <-> d, 2S: s <-> p; 3C: d <-> p
        self.add_num_perm_variation( [("1s g G", "1d g G")]+[("2s g S", "2p g S")]+[("3d g S", "3p g S")])

        # 2G: s <-> p, 3S: s <-> p
        self.add_num_perm_variation( [("2s g G", "2p g G")]+[("3s g S", "3p g S")])

        # 2C: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g V", "2p g V")]+[("3d g V", "3p g V")])

        # 3G:s<->p, 2S:d<->p, 1m: s<->d
        self.add_num_perm_variation( [("3s g G", "3p g G")]+[("2d g S", "2p g S")]+[("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])

    def _create_permutation_GEN_files(self):
        """
        creates all permutation files where GEN-features are swapped (m <-> f)
        """

        # p2: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # s3: m <-> f
        self.add_gen_perm_variation( [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # p2: m <-> f, s3: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES] +
                                [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # s2: m <-> f, d3: m <-> f, p2: m <-> f
        self.add_gen_perm_variation( [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] +
                                [("3d m " + T, "3d f " + T) for T in self.TENSES_CASES] +
                                [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: m <-> f
        self.add_gen_perm_variation( [("2a m " + T, "2a f " + T) for T in self.TENSES_CASES])

        # 3: m <-> f
        self.add_gen_perm_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # s: m <-> f
        self.add_gen_perm_variation( [("zs m " + T, "zs f " + T) for T in self.TENSES_CASES])

        # p: m <-> f
        self.add_gen_perm_variation( [("zp m " + T, "zp f " + T) for T in self.TENSES_CASES])

        # 3dV: m <-> f
        self.add_gen_perm_variation( [("3d m V", "3d f V")])

        # 2pG: m<->f, 3sG: m<->f
        self.add_gen_perm_variation( [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] +
                                [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        self.add_gen_perm_variation( [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] +
                                [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] +
                                [("3p m V", "3p f V")])

        # STRONG

        # strong permutation 1
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC)
                                                                                            for
                                                                                            PC in self.TENSES_CASES_PC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d m " + PC, "2d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("1s m V", "1s f V")] + [("1d m V", "1d f V")] + [("2d m V", "2d f V")] + [
                                    ("2p m V", "2p f V")] + [("3s m V", "3s f V")] + [("3p m V", "3p f V")])

        # strong permutation 2
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC)
                                                                                            for
                                                                                            PC in self.TENSES_CASES_PC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "2p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m V", "2d f V")] + [
                                    ("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 3
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC)
                                                                                            for
                                                                                            PC in self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s m " + PC, "3s f " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [
                                    ("3s m V", "3s f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 4
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC)
                                                                                            for
                                                                                            PC in self.TENSES_CASES_PC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d m " + PC, "2d f " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("1s m V", "1s f V")] + [("1d m V", "1d f V")] + [("2s m V", "2s f V")] + [
                                    ("2p m V", "2p f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 1
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1s m S", "1s f S")] + [("1p m S", "1p f S")] + [
                                    ("2s m G", "2s f G")] + [
                                    ("2d m G", "2d f G")] + [("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [
                                    ("2p m S", "2p f S")] + [("2p m S", "2p f S")] + [("3s m G", "3s f G")] + [
                                    ("3p m G", "3p f G")] + [("3s m V", "3s f V")] + [("3p m V", "3p f V")] + [
                                    ("3p m S", "3p f S")] + [("3s m S", "3s f S")])

        # strong permutation 2
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m S", "1s f S")] + [
                                    ("1d m S", "1d f S")] + [("2s m G", "2s f G")] + [("2p m G", "2p f G")] + [
                                    ("2d m V", "2d f V")] + [
                                    ("3s m G", "3s f G")] + [("3d m G", "3d f G")] + [("3p m G", "3p f G")] + [
                                    ("3d m V", "3d f V")] + [("3p m V", "3p f V")] + [("3d m S", "3d f S")] + [
                                    ("3s m S", "3s f S")])

        # strong permutation 3
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1d m S", "1d f S")] + [("1p m S", "1p f S")] + [
                                    ("2p m G", "2p f G")] + [
                                    ("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [("2s m S", "2s f S")] + [
                                    ("2p m S", "2p f S")] + [("3s m G", "3s f G")] + [("3d m G", "3d f G")] + [
                                    ("3s m V", "3s f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")] + [
                                    ("3s m S", "3s f S")] + [("3p m S", "3p f S")])

        # strong permutation 4
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1s m S", "1s f S")] + [("1p m S", "1p f S")] + [
                                    ("1d m S", "1d f S")] + [
                                    ("2s m G", "2s f G")] + [("2d m G", "2d f G")] + [("2p m G", "2p f G")] + [
                                    ("2s m V", "2s f V")] + [("2p m V", "2p f V")] + [("2p m S", "2p f S")] + [
                                    ("2d m S", "2d f S")] + [("3d m G", "3d f G")] + [("3d m V", "3d f V")] + [
                                    ("3p m V", "3p f V")] + [("3s m S", "3s f S")] + [("3p m S", "3p f S")])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        # 3pS: m<->f, 2sC: m<->f
        self.add_gen_perm_variation(
                                [("2p m G", "2p f G")] + [("3s m G", "3s f G")] + [("3p m V", "3p f V")] + [
                                    ("3p m S", "3p f S")] + [("2s m V", "2s f V")])

        # 3pS: m<->f, 2sS: m<->f
        # 2sC: m<->f, 3sC: m<->f
        self.add_gen_perm_variation(
                                [("3p m S", "3p f S")] + [("2s m S", "2s f S")] + [("2s m V", "2s f V")] + [
                                    ("3s m V", "3s f V")])

    def _create_permutation_TENSE_files(self):
        """
        creates all permutation files where TENSE-features are swapped (V <-> F)
        """
        # 2s : G <-> V, 3p: G <-> V, 1d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G")] + [("3p g V", "3p g G")] + [("1d g V", "1d g G")])

        # 2sf: G <-> V, 3pm: G <-> V, 3df: G <-> V
        self.add_ten_perm_variation( [("2s f V", "2s f G")] + [("3p m V", "3p m G")] + [("3d f V", "3d f G")])

        # 1s: G <-> V, 3sm: G <-> V, 1p: G <-> V, 2pm: G <-> V, 2s: G <-> V
        self.add_ten_perm_variation(
                                [("1s g V", "1s g G")] + [("1p g V", "1p g G")] + [("2s g V", "2s g G")] + [
                                    ("3s m V", "3s f G")] + [("2p m V", "2p m G")])

        # 2 : G <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g G")])

        # 3 : G <-> V
        self.add_ten_perm_variation( [("3a g V", "3a g G")])

        # s : G <-> V
        self.add_ten_perm_variation( [("zs g V", "zs g G")])

        # p : G <-> V
        self.add_ten_perm_variation( [("zp g V", "zp g G")])

        # sf : G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("zs f V", "zs f G")] + [("3d g V", "3d g G")])

        # 1pm : G <-> V, 3sm : G <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m G")] + [("3s m V", "3s m G")])

        # 1f : G <-> V, 3dm : G <-> V
        self.add_ten_perm_variation( [("1a f V", "1a f G")] + [("3d m V", "3d m G")])

        # sf : G <-> V, 1pm : G <-> V, 2dm : G <-> V
        self.add_ten_perm_variation( [("zs m V", "zs m G")] + [("1p m V", "1p m G")] + [("2d m V", "2d m G")])

        # 3sf : G <-> V, 2sm : G <-> V
        self.add_ten_perm_variation( [("3s f V", "3s f G")] + [("2s m V", "2s m G")])

        # df : G <-> V
        self.add_ten_perm_variation( [("zd f V", "zd f G")])

        # 1 : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G")])

        # d : G <-> V
        self.add_ten_perm_variation( [("zd g V", "zd g G")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation(
                                [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")] + [
                                    ("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")])

        # 1dm, 3df, 2pm, 2sm, 1sf, 3s
        self.add_ten_perm_variation(
                                [("1d m G", "1d m V")] + [("3d f G", "3d f V")] + [("2p m G", "2p m V")] + [
                                    ("2s m G", "2s m V")] + [("1s f G", "1s f V")] + [("3s g G", "3s g V")])

        # 2dm, 3df, 2sf, 1d, 1p, 3sm
        self.add_ten_perm_variation(
                                [("2d m G", "2d m V")] + [("3d f G", "3d f V")] + [("2s f G", "2s f V")] + [
                                    ("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("3s m G", "3s m V")])

        # 1d, 1p, 2p, 2d, 3s
        self.add_ten_perm_variation(
                                [("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("2d g G", "2d g V")] + [
                                    ("2p g G", "2p g V")] + [("3s g G", "3s g V")])

        # 3p,2s: G -> S
        self.add_ten_perm_variation( [("3p g G", "3p g S")] + [("2s g G", "2s g S")])

    def _create_permutation_X_files(self):
        """
        creates all permutation files where several or all features are swapped
        """

        # 2 : G <-> V, 3: s <-> p
        self.add_xross_perm_variation(
                                [("2a g G", "2a g V")] + [("3s g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 2s: m <-> f, 3p <-> 1s, 2pV <-> 1pV
        self.add_xross_perm_variation(
                                [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1s g " + T) for T in
                                                                                       self.TENSES_CASES] + [
                                    ("2p g V", "1p g V")])

        # 2pG: m <-> f, sG: 3m<-> 2f, dGm: 2<->3
        self.add_xross_perm_variation( [("2p m G", "2p f G")] + [("3s m G", "2s f G")] + [("3d m G", "2d m G")])

        # 3dfV <-> 1smG, 2pfV <-> 3smV, 2pmG <-> 1dmV, 3sfG <-> 3dmG
        self.add_xross_perm_variation(
                                [("3d f V", "1s m G")] + [("2p f V", "3s m V")] + [("2p m G", "1d m V")] + [
                                    ("3s f G", "3d m G")])

        # 1dm <-> 2df, 2pmV <-> 3pfG, 3smG <-> 1pfV
        self.add_xross_perm_variation(
                                [("1d m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("2p m V", "3p f G")] + [
                                    ("3s m G", "1p f V")])

        # 2G <-> 3V, sG <-> pV
        self.add_xross_perm_variation( [("2a g G", "3a g V")] +
                                [("zs g G", "zp g V")])

        # d: 1G <-> 3V,  p: 1G <-> 3V,
        # s: 3G <-> 2V
        self.add_xross_perm_variation( [("1d g G", "3d g V")] + [("1p g G", "3p g V")] + [("3s g G", "2s g V")])

        # V: 3p <-> 2s, Vs3 <-> Gs1
        self.add_xross_perm_variation( [("3p g V", "2s g V")] + [("3s g V", "1s g G")])

        # STRONG
        # full permutation 1
        self.add_xross_perm_variation(
                                [("1s m G", "3s m V")] + [("2s m G", "1d f V")] + [("3s m G", "2p f G")] + [
                                    ("1s f G", "3p m V")] + [("2s f G", "2d f G")] + [("3s f G", "1p m G")] + [
                                    ("3p m G", "3d m V")] + [
                                    ("1s m V", "2s f V")] + [("2s m V", "2p f V")] + [("2p m V", "1p f V")] + [
                                    ("3s f V", "1s f V")] + [("3d m G", "1d f G")] + [("2d m G", "1d m V")] + [
                                    ("1d m G", "3d f V")] + [("2p m G", "3p f G")] + [("3d f G", "1p f G")] + [
                                    ("2d m V", "3p f V")] + [("2d f V", "1p m V")])

        # full permutation 2
        self.add_xross_perm_variation(
                                [("1s m G", "2d m G")] + [("1s f G", "3s f V")] + [("2s m G", "1s f G")] + [
                                    ("2s f G", "2d f G")] + [("2s m V", "1p m V")] + [("2s f V", "1p f V")] + [
                                    ("3p m V", "3p m G")] + [
                                    ("3p f V", "3p f G")] + [("1d m V", "3s m V")] + [("1d f V", "1s m G")] + [
                                    ("1s m V", "1p m G")] + [("1s f V", "3d m V")] + [("2d m V", "2s m G")] + [
                                    ("2d f V", "1p f G")] + [("3d f V", "2s f G")] + [("2p m G", "3d f G")] + [
                                    ("2p f G", "2p m V")] + [("3d m G", "2p f V")])

        # full permutation 3
        self.add_xross_perm_variation(
                                [("1s g G", "2d g V")] + [("2p g G", "2s g G")] + [("3d g G", "1p g V")] + [
                                    ("1s g V", "1p g G")] + [("3s g V", "3s g G")] + [("3d g V", "1d g G")] + [
                                    ("1p g S", "2p g V")] + [
                                    ("2s g V", "3p g G")] + [("3p g V", "2d g G")] + [("1d g S", "3s g S")])

        # full permutation 4
        self.add_xross_perm_variation(
                                [("1s g G", "1d g G")] + [("2d g G", "2p g G")] + [("3s g G", "3p g G")] + [
                                    ("1p g V", "3d g G")] + [("2s g G", "3s g V")] + [("1p g G", "2d g V")] + [
                                    ("1s g " + T, "2s g " + T) for T in
                                    ["V", "S"]] + [
                                    ("2p g " + T, "3p g " + T) for T in ["V", "S"]] + [("1d g " + T, "3d g " + T) for T in
                                                                                       ["V", "S"]])

        # full permutation 5
        self.add_xross_perm_variation(
                                [("1s g G", "2p g V")] + [("3p g G", "2s g V")] + [("2d g G", "1d g V")] + [
                                    ("1s g V", "3d g G")] + [("2d g V", "2p g G")] + [("3p g V", "3s g G")] + [
                                    ("1p g V", "2s g G")] + [
                                    ("3s g V", "1p g G")] + [("3d g V", "1d g G")] + [("1s g S", "3p g S")] + [
                                    ("3d g S", "2d g S")] + [("2s g S", "3s g S")] + [("1d g S", "2p g S")])

        # full permutation 6
        self.add_xross_perm_variation(
                                [("1s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2p f " + T) for T in
                                                                                       self.TENSES_CASES] + [
                                    ("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "1p f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("1d f " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("2s m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("2d m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # full permutation 7
        self.add_xross_perm_variation(
                                [("1s m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d f " + T) for T in
                                                                                       self.TENSES_CASES] + [
                                    ("3s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2s f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("2d m " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3p f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("1p m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2d f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("3p m " + T, "3d f " + T) for T in self.TENSES_CASES])

        # full permutation 8
        self.add_xross_perm_variation(
                                [("1s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s m " + T) for T in
                                                                                       self.TENSES_CASES] + [
                                    ("2p m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s f " + T, "2s m " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("1d m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("1d f " + T, "2s f " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("3d f " + T, "2d m " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for
                                                                                          T
                                                                                          in self.TENSES_CASES] + [
                                    ("3p m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # rotations
        # full permutation 9
        right = [("1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES] + [
            ("2s g " + T, "3p g " + T, "1d g " + T)
            for T in self.TENSES_CASES] + [
                    ("3s g " + T, "1p g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right)

        # full permutation 10
        # s: 1->2->3
        # d: 3->2->1
        right = [("1s g " + T, "2s g " + T, "3s g " + T) for T in self.TENSES_CASES]
        left = [("1d g " + T, "2d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 11
        right = [("1s f " + T, "3d m " + T, "3p f " + T) for T in self.TENSES_CASES] + [
            ("3s m " + T, "2p m " + T, "1d f " + T)
            for T in self.TENSES_CASES]
        left = [("1s m " + T, "1p m " + T, "2s f " + T) for T in self.TENSES_CASES] + [
            ("1p f " + T, "2d m " + T, "3s f " + T)
            for T in self.TENSES_CASES] + [
                   ("2s m " + T, "1d m " + T, "3d f " + T) for T in self.TENSES_CASES] + [
                   ("2d f " + T, "1p f " + T, "3p m " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 12
        right = [("1s g G", "2p g V", "3d g G")] + [("2s g G", "2s g V", "1d g V")] + [
            ("3s g V", "1p g V", "1p g G")] + [
                    ("1p g S", "2d g S", "1s g S")] + [("3d g S", "3s g S", "2s g S")]
        left = [("2d g V", "3p g V", "3s g G")] + [("2d g G", "2p g G", "3p g G")] + [("1d g G", "1s g V", "3d g V")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 13
        left = [("1s m G", "2s m G", "3p f V")] + [("1p m G", "1d f G", "2d m V")] + [
            ("3p m G", "3p f G", "1s f G")] + [
                   ("3s f G", "3s f V", "3d m V")] + [("3s m V", "2p m V", "3p m V")] + [
                   ("1p f G", "2d f G", "3d m G")] + [
                   ("1s f V", "3d f V", "2d m G")]
        right = [("2s f G", "2s f V", "2s m V")] + [("1d m V", "2p f G", "1p f V")] + [
            ("3s m G", "1p m V", "2p m G")] + [
                    ("3d f G", "1d f V", "2p f V")] + [("1d m G", "1s m V", "2d f V")] + [
                    ("3s m S", "3d f S", "2p m S")] + [
                    ("1p m S", "1d f S", "3p m S")] + [("3p f S", "1s f S", "2s m S")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 14
        left = [("1a m G", "1a f V", "3a f G")] + [("2a m G", "2a m V", "3a f V")] + [
            ("2a f V", "1a f G", "1a m V")] + [
                   ("3a m G", "2a f G", "3a m V")]
        right = [("2a m S", "1a m S", "1a f S")] + [("3a m S", "2a f S", "3a f S")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 15
        left = [("zs m G", "zs m V", "zp m G")] + [("zs f S", "zd m S", "zp f S")]
        right = [("zp f G", "zd m G", "zd f V")] + [("zs f V", "zp m V", "zd f G")] + [("zs f G", "zd m V", "zp f V")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 2smG <-> 3sfV,
        # 2sfG <-> 2pfG,  3smV  <-> 2smV
        # 1s <-> 1p
        # V: 2d <-> 3d, V:2p <-> 3p
        # 3dG: m <-> f,   3pG: m <-> f
        self.add_xross_perm_variation(
                                [("2s m G", "3s f V")] + [("2s f G", "2p f G")] + [("3s m V", "2s m V")] + [
                                    ("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g V", "3d g V")] + [
                                    ("2p g V", "3p g V")] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # 3s: m <-> f
        # 2G: s <-> p
        # Vp: 1 <-> 3, Vd: 1 <-> 3
        # Vs: 1m <-> 2f
        self.add_xross_perm_variation(
                                [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2s g G", "2p g G")] + [
                                    ("1p g V", "3p g V")] + [("1d g V", "3d g V")] + [("1s m V", "2s f V")])

        # 3sV: m <-> f
        # 1G: s <-> p
        # V: 1d  <-> 2d, V: 1p <-> 2p
        # 3pV <-> 2pG;  2sG <-> 3pG
        self.add_xross_perm_variation(
                                [("3s m V", "3s f V")] + [("1s g G", "1p g G")] + [("1d g V", "2d g V")] + [
                                    ("1p g V", "2p g V")] + [("3p g V", "2p g G")] + [("3p g G", "2s g G")])
        self.add_xross_perm_variation(
                                [("1s m G", "2d m G")] + [("1s f G", "3d m V")] + [("2s m G", "3d f G")] + [
                                    ("2s f G", "2p m G")] + [("3s m G", "3p m V")] + [("3s f S", "1p f G")] + [
                                    ("1d m G", "3d m G")] + [
                                    ("1d f G", "2s m V")] + [("1p m G", "1d f V")] + [("2p f S", "3s f V")] + [
                                    ("3p m G", "2d f S")] + [("3p f G", "2s f V")] + [("1s f V", "2d m V")] + [
                                    ("1p m V", "3p f V")] + [("2p f V", "2p m V")] + [("3p m S", "3d f V")] + [
                                    ("1s m V", "2d f V")] + [("1p f V", "1p m S")] + [("2d f G", "3p f S")])
        self.add_xross_perm_variation(
                                [("1s m G", "3s f G")] + [("1s m V", "3s f V")] + [("1s f V", "2s f G")] + [
                                    ("2s m V", "2d m G")] + [("2s f V", "3d m G")] + [("3s m V", "1s f G")] + [
                                    ("2s m G", "3p m V")] + [
                                    ("1d m G", "2d f G")] + [("1d f G", "1p m G")] + [("1p m V", "3s m G")] + [
                                    ("1p f V", "3p f V")] + [("2p f V", "2d f V")] + [("3d f G", "2p m V")] + [
                                    ("2p m G", "3d f V")] + [("2d m V", "3p m G")] + [("2p f G", "1d f V")] + [
                                    ("3p f S", "3p f G")] + [("3p m S", "3d f S")] + [("1d m V", "1p m S")] + [
                                    ("1p f S", "3d m V")] + [("2d f S", "1p f G")])
        self.add_xross_perm_variation(
                                [("1s m G", "1p m G")] + [("1s f G", "3d m G")] + [("2s m G", "3p f G")] + [
                                    ("2s f G", "3s f V")] + [("3s m G", "1d m G")] + [("3s f G", "2d m V")] + [
                                    ("1d f G", "3d m V")] + [
                                    ("2d m G", "1p m V")] + [("2d f G", "1p f V")] + [("3d f G", "1d f V")] + [
                                    ("1p f G", "3s m V")] + [("1s m V", "2p f V")] + [("1s f V", "3p f V")] + [
                                    ("2s m V", "2p m V")] + [("2s f V", "3p m V")] + [("1s m S", "3p m G")] + [
                                    ("1s f S", "2d f V")] + [("2s m S", "3s m S")] + [("2s f S", "3s f V")] + [
                                    ("3s f S", "1d m V")] + [("1d f S", "2p f G")] + [("2d m S", "3d f V")] + [
                                    ("2d f S", "2p m G")] + [("3d f S", "2p m S")])
        self.add_xross_perm_variation(
                                [("1s m G", "2s f G")] + [("3s m G", "2s m V")] + [("1s m V", "1s f G")] + [
                                    ("2s f V", "1s f V")] + [("3s f V", "3s m V")] + [("1d m G", "1p f V")] + [
                                    ("2d m G", "1p m G")] + [
                                    ("3d m G", "2s m G")] + [("3d f G", "2p m V")] + [("1p m V", "2p m G")] + [
                                    ("2p f V", "2d f G")] + [("3p m S", "3p m G")] + [("3p f S", "3p f G")] + [
                                    ("1p f G", "2p f G")] + [("1d f S", "3d m V")] + [("3p m V", "1d f G")] + [
                                    ("2d f S", "3s f G")] + [("3p f V", "1d m V")] + [("1p f S", "2p f S")] + [
                                    ("1d f V", "2d m V")] + [("2d f V", "3s f S")] + [("3d f V", "1d m S")])
        self.add_xross_perm_variation(
                                [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + PC, "2s f " + PC)
                                                                                            for
                                                                                            PC in self.TENSES_CASES_PC] + [
                                    ("3s f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1d m " + PC, "2d m " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "1p m " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("1p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p f " + PC, "1d f " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [
                                    ("2s m V", "3s f V")] + [("3s m V", "2s f V")] + [("1d m V", "3d m V")] + [
                                    ("2d m V", "2d f V")] + [("3d f V", "1d f V")] + [("1p m V", "3p m V")] + [
                                    ("1p f V", "2p f V")] + [("3p f V", "2p m V")])
        self.add_xross_perm_variation(
                                [("2s m G", "1p f G")] + [("2s f S", "1s m G")] + [("2d m S", "1p m V")] + [
                                    ("2d f S", "3d f G")] + [("2p m S", "1s m V")] + [("2p f S", "3d m G")] + [
                                    ("3s f G", "3d f V")] + [
                                    ("3d m V", "1d m G")] + [("2p f V", "3p m G")] + [("3s m G", "1d m V")] + [
                                    ("1p m G", "3s f V")] + [("3p f G", "1p f V")] + [("3s m V", "1d f G")] + [
                                    ("1d f V", "1s f V")] + [("3p f V", "1s f G")] + [("2s f G", "2p f G")] + [
                                    ("2d m G", "2d m V")] + [("2d f G", "2s m V")] + [("2p m G", "2s f V")] + [
                                    ("2d f V", "2p m V")])
        self.add_xross_perm_variation(
                                [("1s m G", "2d f V")] + [("1s f G", "3d m V")] + [("1d m G", "3p m G")] + [
                                    ("1d f G", "2p f G")] + [("1p m G", "1s f V")] + [("1p f G", "3d f V")] + [
                                    ("1s m V", "2s f V")] + [
                                    ("1d m V", "2p f V")] + [("1d f V", "2d m G")] + [("1p m V", "3p f G")] + [
                                    ("1p f V", "3s m V")] + [("3s f G", "2d f G")] + [("1p m S", "2d m V")] + [
                                    ("1p f S", "3s f V")] + [("1s m S", "2p m V")] + [("1d f S", "3p m V")] + [
                                    ("3d f S", "2p m G")] + [("1d m S", "3p f V")] + [("2s m V", "2s f G")] + [
                                    ("3d m G", "3s m G")] + [("3s f S", "3d f G")] + [("1s f S", "2s m G")] + [
                                    ("3p m S", "2p f S")] + [("2d m S", "3p f S")] + [("3d m S", "2d f S")] + [
                                    ("3s m S", "2p m S")] + [("2s f S", "2s m S")])
        self.add_xross_perm_variation(
                                [("1s f G", "2p m V")] + [("3s m G", "1p m V")] + [("3s f G", "1d m V")] + [
                                    ("2d f G", "2p f V")] + [("3d m G", "3d m V")] + [("1p m G", "3p m V")] + [
                                    ("1p f G", "1p f V")] + [
                                    ("2s m G", "3d f V")] + [("1s m V", "2s f V")] + [("1s f V", "2d f V")] + [
                                    ("1d f V", "2s m V")] + [("2d m V", "3s f V")] + [("3p f V", "3s m V")] + [
                                    ("2s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1d m " + PC, "3p m " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("1d f " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + PC, "2d m " + PC) for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])
        self.add_xross_perm_variation(
                                [("1s f G", "3p f V")] + [("1d m G", "1s m G")] + [("1d f G", "2s f V")] + [
                                    ("1p m G", "2s f G")] + [("1p f G", "3p f G")] + [("1s m V", "3d m G")] + [
                                    ("1s f V", "2d f G")] + [
                                    ("1d m V", "3d m V")] + [("1d f V", "2s m G")] + [("1p m V", "2d m G")] + [
                                    ("1p f V", "2d f V")] + [("3s f V", "3s m G")] + [("2p m G", "3d f V")] + [
                                    ("2p f G", "3p m G")] + [("2p m V", "3s m V")] + [("1s f S", "3s f G")] + [
                                    ("3s m S", "2s m S")] + [("3s f S", "3d f G")] + [("2d f S", "2p f V")] + [
                                    ("3d m S", "3p m V")] + [("1p m S", "2s m V")] + [("1p f S", "2d m V")])
        self.add_xross_perm_variation(
                                [("1s m G", "2d m V")] + [("1s f G", "3s f V")] + [("3p m G", "2s f G")] + [
                                    ("3p f G", "1d f G")] + [("2s m G", "3s m V")] + [("3d m V", "3p m V")] + [
                                    ("3d f V", "1d m V")] + [
                                    ("1d m G", "2d f V")] + [("1p f V", "2p f V")] + [("2p m V", "1p m V")] + [
                                    ("3s m G", "1s f V")] + [("3s f G", "3p f V")] + [("1d f V", "3d f G")] + [
                                    ("3d m G", "2s m V")] + [("1p f G", "1s m V")] + [("2d m G", "2s f V")] + [
                                    ("2d f G", "2p f G")] + [("1p m G", "2p m G")] + [("1s m S", "2s f S")] + [
                                    ("3s m S", "1s f S")] + [("2d m S", "1p m S")] + [("3d m S", "2s m S")] + [
                                    ("3d f S", "1d m S")] + [("2d f S", "2p m S")])
        self.add_xross_perm_variation(
                                [("1s m G", "3p f G")] + [("1s f G", "3d f V")] + [("1d m G", "3s f G")] + [
                                    ("1d f G", "2p m G")] + [("1p m G", "3s m V")] + [("1p f G", "2d m G")] + [
                                    ("2s m G", "3d f G")] + [
                                    ("2s f G", "2p f G")] + [("3s m G", "3p m V")] + [("3d m G", "2d f G")] + [
                                    ("3p m G", "3d m V")] + [("1s m V", "1p m V")] + [("1s f V", "2d m V")] + [
                                    ("2s m V", "2p f V")] + [("2s f V", "3p f V")] + [("2d f V", "1d f V")] + [
                                    ("2p m V", "1p f V")] + [("3s f V", "1d m V")] + [("3s m S", "1s f S")] + [
                                    ("2d f S", "3d m S")] + [("1p f S", "1p m S")] + [("2s m S", "3s f S")])
        self.add_xross_perm_variation(
                                [("1s m G", "2s f G")] + [("1d m G", "1d f V")] + [("1d f G", "1d m V")] + [
                                    ("1p m G", "2p f V")] + [("1p f G", "1s f V")] + [("2s m G", "2p f G")] + [
                                    ("2d m G", "1p m V")] + [
                                    ("2d f G", "3p f V")] + [("2p m G", "3d f V")] + [("2s m V", "3p m V")] + [
                                    ("2s f V", "3p f G")] + [("2d m V", "1s m V")] + [("3s m G", "2p m V")] + [
                                    ("3d m G", "1s f G")] + [("3s m V", "3s f G")] + [("3d m V", "1p f V")] + [
                                    ("1s m S", "3p f S")] + [("1s f S", "3d f G")] + [("1d m S", "3s f S")] + [
                                    ("1d f S", "2p m S")] + [("1p m S", "3p m G")] + [("1p f S", "2d m S")] + [
                                    ("2s m S", "3d f S")] + [("2s f S", "2p f S")] + [("3s m S", "3s f V")] + [
                                    ("3d m S", "2d f S")] + [("3p m S", "2d f V")])

        # full swap 1
        old_list = [(
            "1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
            "3p g " + T) for T in self.TENSES_CASES]
        new_list = [(
            "2s g " + T, "3p g " + T, "3d g " + T, "3s g " + T, "1p g " + T, "1d g " + T, "1s g " + T, "2p g " + T,
            "2d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

        # full swap 2
        old_list = [(
            "1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
            "3p g " + T) for T in self.TENSES_CASES]
        new_list = [(
            "2s g " + T, "1s g " + T, "3s g " + T, "2d g " + T, "1p g " + T, "3p g " + T, "2p g " + T, "1d g " + T,
            "3d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

    def _create_syncretic_GEN_files(self):
        """syncretic variations that happened historically (geader syacretism)"""
        # syn: 2V:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f V", "2a m V")])
        # syn: p:f -> m (TRUE)
        self.add_gen_sync_variation( [("zp" + " f "+T, "zp" + " m "+T) for T in self.TENSES_CASES])
        # V3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f V", "3p m V")])
        # Gp: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # 3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # syn: 2:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES])
        # syn G3d: f -> m (TRUE)
        self.add_gen_sync_variation( [("3d f "+PC, "3d m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f V", "2s m V")])
        # syn G2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn 2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES])
        # syn Vp: f -> m
        self.add_gen_sync_variation( [("zp f V", "zp m V")])
        # syn p: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f "+T, "zp m "+T) for T in self.TENSES_CASES])
        # syn V1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f V", "1s m V")])
        # syn G3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f G", "3s m G")])
        # syn G2p: f->m (TRUE)
        self.add_gen_sync_variation( [("2p f "+PC, "2p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn s/d: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+T, "zs m "+T) for T in self.TENSES_CASES]+[("zd f "+T, "zd m "+T) for T in self.TENSES_CASES])
        # syn 3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m "+T, "3a f "+T) for T in self.TENSES_CASES])
        # syn s: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+T, "zs m "+T) for T in self.TENSES_CASES])
        # syn 2s: f->m, 3s: f->m (FALSE)
        self.add_gen_sync_variation( [("2s f "+T, "2s m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # 2d
        self.add_gen_sync_variation( [("2d f "+T, "2d m "+T) for T in self.TENSES_CASES])
        # Gd
        self.add_gen_sync_variation( [("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC])
        # 2s
        self.add_gen_sync_variation( [("2s f "+T, "2s m "+T) for T in self.TENSES_CASES])
        # 2
        self.add_gen_sync_variation( [("2a f "+T, "2a f "+T) for T in self.TENSES_CASES])
        # V2p
        self.add_gen_sync_variation( [("2p f V", "2p m V")])
        # dG, dV2
        self.add_gen_sync_variation( [("2d f V", "2d m V")]+[("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC])
        # alle
        self.add_gen_sync_variation( [("za f "+T, "za m "+T) for T in self.TENSES_CASES])
        # G2, G3p
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC]+[("3p f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # 3d
        self.add_gen_sync_variation( [("3d f "+T, "3d m "+T) for T in self.TENSES_CASES])
        # G2, G3d/p
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC]+[("3d f "+PC, "3d m "+PC) for PC in self.TENSES_CASES_PC]+[("3p f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # V2d/p
        self.add_gen_sync_variation( [("2d f V", "2d m V")]+[("2p f V", "2p m V")])
        # 2, 3d/p
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES]+[("3d f "+T, "3d m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # 3p/d
        self.add_gen_sync_variation( [("3d f "+T, "3d m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # Vp/d3
        self.add_gen_sync_variation( [("3p f V", "3p m V")]+[("3d f V", "3d m V")])
        # Gp/d
        self.add_gen_sync_variation( [("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m V", "3a f V")])
        # syn Vs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f V", "zs m V")])
        # syn G3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m G", "3a f G")])
        # syn Gs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f G", "zs m G")])
        # 3s; 2p
        self.add_gen_sync_variation( [("2p f "+T, "2p m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V2p, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("3s f G", "3s m G")])
        # 3s; 2p/d
        self.add_gen_sync_variation( [("2p f "+T, "2p m "+T) for T in self.TENSES_CASES]+[("2d f "+T, "2d m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V2p/d, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("2d f V", "2d m V"),("3s f G", "3s m G")])
        # syn G/S3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G/S3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m "+PC, "3a f "+PC) for PC in self.TENSES_CASES_PC])
        # syn G/Ss: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC])
        # V2p, G/S3s
        self.add_gen_sync_variation( [("2p f V", "2p m V")] + [("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # V2p/d, G/S3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("2d f V", "2d m V")] + [("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])

    def _create_syncretic_PERS_files(self):
        """syncretic variations that happened historically (other thaa Geader)"""
        # syn Vsm: 2 -> 1
        self.add_pers_sync_variation( [("2s m V", "1s m V")])
        # syn Vsf: 2 -> 1
        self.add_pers_sync_variation( [("2s f V", "1s f V")])
        # syn Vdm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V")])
        # syn Vdm: 2->1; Vsm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V"),("2s m V", "1s m V")])
        # Vd: 2->1
        self.add_pers_sync_variation( [("2d g V", "1d g V")])
        # syn 1 -> 2
        self.add_pers_sync_variation( [("1a g "+T, "2a g "+T) for T in self.TENSES_CASES])
        # syn 2 -> 3
        self.add_pers_sync_variation( [("2a g "+T, "3a g "+T) for T in self.TENSES_CASES])
        # syn 3 -> 1
        self.add_pers_sync_variation( [("3a g "+T, "1a g "+T) for T in self.TENSES_CASES])
        # syn f:3->2
        self.add_pers_sync_variation( [("3a f "+T, "2a f "+T) for T in self.TENSES_CASES])
        # syn fp:3->2
        self.add_pers_sync_variation( [("3p f "+T, "2p f "+T) for T in self.TENSES_CASES])
        # syn p:  2->1,3->1
        self.add_pers_sync_variation( [("2p g "+T, "1p g "+T) for T in self.TENSES_CASES]+[("3p g "+T, "1p g "+T) for T in self.TENSES_CASES])
        # syn s:2->3
        self.add_pers_sync_variation( [("2s g "+T, "3s g "+T) for T in self.TENSES_CASES])
        # syn s:1->2
        self.add_pers_sync_variation( [("1s g "+T, "2s g "+T) for T in self.TENSES_CASES])
        # syn p:2->3
        self.add_pers_sync_variation( [("2p g "+T, "3p g "+T) for T in self.TENSES_CASES])
        # syn Vp:3->2
        self.add_pers_sync_variation( [("3p g V", "2p g V")])
        # Gp: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G")])
        # Vs: 2->1
        self.add_pers_sync_variation( [("2s g V", "1s g V")])
        # Gpf: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G")])
        # G:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G"),("3d f G", "2d f G")])
        # G: d/p: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G"),("3d g G", "2d g G")])
        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V"),("3a g G", "1a g G")])
        # mp:3->2, fp:3->1
        self.add_pers_sync_variation( [("3p m "+T, "2p m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "1p f "+T) for T in self.TENSES_CASES])
        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V"),("2a f G", "1a f G")])
        # TRUE
        # G/Sp: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC])
        # G/Spf: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC])
        # G/S:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC]+[("3d f "+PC, "2d f "+PC) for PC in self.TENSES_CASES_PC])
        # G/S: d/p: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC]+[("3d g "+PC, "2d g "+PC) for PC in self.TENSES_CASES_PC])
        # V: 2->3, G/S:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")]+[("3a g "+PC, "1a g "+PC) for PC in self.TENSES_CASES_PC])
        # Cm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")]+[("2a f "+PC, "1a f "+PC) for PC in self.TENSES_CASES_PC])
        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")]+[("3a g "+PC, "1a g "+PC) for PC in self.TENSES_CASES_PC])
        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")]+[("2a f "+PC, "1a f "+PC) for PC in self.TENSES_CASES_PC])

    def _create_syncretic_NUM_files(self):
        # syn: d -> p
        self.add_num_sync_variation( [("zd" + " g "+T, "zp" + " g "+T) for T in self.TENSES_CASES])
        # 1: d -> p
        self.add_num_sync_variation( [("1d" + " g "+T, "1p" + " g "+T) for T in self.TENSES_CASES])
        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m V", "3s m V")])
        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g V", "1p g V")])
        # syn G1: s->p
        self.add_num_sync_variation( [("1s g G", "1p g G")])
        # 3m: p->s
        self.add_num_sync_variation( [("3p m "+T, "3s m "+T) for T in self.TENSES_CASES])
        # FASLE
        self.add_num_sync_variation( [("zp g "+T, "zd g "+T) for T in self.TENSES_CASES])
        # syn s->p
        self.add_num_sync_variation( [("zs g "+T, "zp g "+T) for T in self.TENSES_CASES])
        # syn s->d
        self.add_num_sync_variation( [("zs g "+T, "zd g "+T) for T in self.TENSES_CASES])
        # syn 3: d->p
        self.add_num_sync_variation( [("3d g "+T, "3p g "+T) for T in self.TENSES_CASES])
        # 2: d->p
        self.add_num_sync_variation( [("2d g "+T, "2p g "+T) for T in self.TENSES_CASES])
        # G1: s/d->p
        self.add_num_sync_variation( [("1d g G", "1p g G"),("1s g G", "1p g G")])
        # V3f: s->p
        self.add_num_sync_variation( [("3s f V", "3p f V")])
        # 3m: d->s
        self.add_num_sync_variation( [("3d m "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V3: d->s
        self.add_num_sync_variation( [("3d g V", "3s g V")])
        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")]+[("zd g G", "zs g G")])
        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V"),("3s g G", "3p g G")])
        # 2:d->p, 3:d->s
        self.add_num_sync_variation( [("2d g "+T, "2p g "+T) for T in self.TENSES_CASES]+[("3d g "+T, "3s g "+T) for T in self.TENSES_CASES])
        # 1:d->s, 2:p->s
        self.add_num_sync_variation( [("1d g "+T, "1s g "+T) for T in self.TENSES_CASES]+[("2p g "+T, "2s g "+T) for T in self.TENSES_CASES])
        # m: p->s
        self.add_num_sync_variation( [("zp m "+T, "zs m "+T) for T in self.TENSES_CASES])
        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V"),("3s f G", "3d f G")])
        # f: p->s
        self.add_num_sync_variation( [("zp f "+T, "zs f "+T) for T in self.TENSES_CASES])
        # f: p/d->s
        self.add_num_sync_variation( [("zp f "+T, "zs f "+T) for T in self.TENSES_CASES]+[("zd f "+T, "zs f "+T) for T in self.TENSES_CASES])
        # m: p/d->s
        self.add_num_sync_variation( [("zp m "+T, "zs m "+T) for T in self.TENSES_CASES]+[("zd m "+T, "zs m "+T) for T in self.TENSES_CASES])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m G", "zs m G")]+[("zd m G", "zs m G")]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")]+[("zd m G", "zp m G")])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g G", "3p g G")]+[("zp f V", "zd f V")])
        # syn G1: s->p
        self.add_num_sync_variation( [("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # G1: s/d->p
        self.add_num_sync_variation( [("1d g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC]+[("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zd m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")]+[("zd m "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zd f V")])
        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")]+[("zd g "+PC, "zs g "+PC) for PC in self.TENSES_CASES_PC])
        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V")]+[("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC])
        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V")]+ [("3s f "+PC, "3d f "+PC) for PC in self.TENSES_CASES_PC])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zd m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")] + [("zd m "+PC, "zp m "+PC)  for PC in self.TENSES_CASES_PC])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zd f V")])

    def _create_syncretic_X_files(self):
        # syn G3sf -> G2sm
        self.add_xross_sync_variation( [("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3sm -> G1pm
        self.add_xross_sync_variation( [("3s m "+PC, "1p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3p -> V3sm,  V3d->V3sm
        self.add_xross_sync_variation( [("3p g V", "3s m V"),("3d g V", "3s m V")])
        # syn G3:d->pf
        self.add_xross_sync_variation( [("3d g "+PC, "3p f "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3:dm->pf
        self.add_xross_sync_variation( [("3d m V", "3p f V")])
        # syn V3:p->sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")])
        # syn Gd: 3f->2m
        self.add_xross_sync_variation( [("3d f "+PC, "2d m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2sf -> G3pm
        self.add_xross_sync_variation( [("2s f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3pf -> G2pm
        self.add_xross_sync_variation( [("3p f "+PC, "2p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2sm -> G1pm
        self.add_xross_sync_variation( [("2s m "+PC, "1p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2p -> G2sf; G2d -> G2sf
        self.add_xross_sync_variation( [("2p g "+PC, "2s f "+PC) for PC in self.TENSES_CASES_PC]+[("2d g "+PC, "2d f "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3p ->  G1sm
        self.add_xross_sync_variation( [("3p g "+PC, "1s m "+PC) for PC in self.TENSES_CASES_PC])
        # G: s/d: 3f -> 2m
        self.add_xross_sync_variation( [("3d f "+PC, "2d m "+PC) for PC in self.TENSES_CASES_PC]+[("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # s: 3f -> 2m
        self.add_xross_sync_variation( [("3s f "+T, "2s m "+T) for T in self.TENSES_CASES])
        # Vs: 2f -> 1(m)
        self.add_xross_sync_variation( [("2s f V", "1s m V")])
        # G: 3sf -> 2sm, 2pm -> 2sm
        self.add_xross_sync_variation( [("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # Vs: 2m->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])
        # Vs: 2m->1, 3f->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])
        # 3: d->pm
        self.add_xross_sync_variation( [("3d g "+T, "3p m "+T) for T in self.TENSES_CASES])
        # G2:pf->sm
        self.add_xross_sync_variation( [("2p f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # G2:p/df->sm
        self.add_xross_sync_variation( [("2p f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC]+[("2d f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # G: 2pf->3sm
        self.add_xross_sync_variation( [("2p f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # V3:pf->sm
        self.add_xross_sync_variation( [("3p f V", "3s m V")])
        # G:3pf->2sf
        self.add_xross_sync_variation( [("3p f "+PC, "2s f "+PC) for PC in self.TENSES_CASES_PC])




        # # pC -> pS; sC -> sG
        # filename = self.write_directory + self.name + "_SYN_XROSS35" + self._file_ending
        # self.permutation_name_dictionary[filename.split("/")[-1]] = "syn G3p ->  G1sm"
        # syn_tX35 = copy.deepcopy(self.org_conj_dict)
        #:
        #
        #
        #             syn_tX35[(P + N + " g G")] = syn_tX35[(P + N + " g G")]
        # self.add_xross_sync_variation( TODO)


        #G:2p -> 1s
        self.add_xross_sync_variation( [("2p g "+PC, "1s g "+PC) for PC in self.TENSES_CASES_PC])
        #G:3p -> 2s
        self.add_xross_sync_variation( [("3p g "+PC, "2s g "+PC) for PC in self.TENSES_CASES_PC])
        #G:3p -> 3d
        self.add_xross_sync_variation( [("3p g "+PC, "3d g "+PC) for PC in self.TENSES_CASES_PC])
        #G3p -> S2d
        self.add_xross_sync_variation( [("3p g G", "2d g S")])
        #G3p -> S3p, S3s -> G2s
        self.add_xross_sync_variation( [("3p g G", "3p g S"),("3s g S", "2s g G")])

    def _create_syncretic_TENSE_files(self):
        # syn p: G -> V
        self.add_ten_sync_variation( [("zp g G", "zp g V")])
        # syn s: G -> V
        self.add_ten_sync_variation( [("zs g G", "zs g V")])
        # syn 2: G -> V
        self.add_ten_sync_variation( [("2a g G","2a g V")])
        # syn 3: G -> V
        self.add_ten_sync_variation( [("3a g G", "3a g V")])
        # syn p: V -> G
        self.add_ten_sync_variation( [("zp g V", "zp g G")])
        # syn s: V -> G
        self.add_ten_sync_variation( [("zs g V", "zs g G")])
        # syn 2: V -> G
        self.add_ten_sync_variation( [("2a g V", "2a g G")])
        # syn 3: V -> G
        self.add_ten_sync_variation( [("3a g V", "3a g G")])
        # syn 3p: V -> G,  2s: G -> V
        self.add_ten_sync_variation( [("3p g V", "3p g G"),("2s g G", "2s g V")])
        # syn 2: V -> G,  p: G -> V
        self.add_ten_sync_variation( [("2a g V", "3a g G")]+[("zp g G", "zp g V")])
        # syn 2s: G -> S
        self.add_ten_sync_variation( [("zp g S", "zp g G")])
        # syn p: S -> G
        self.add_ten_sync_variation( [("zp g S","zp g G")])
        # syn 3p: V -> S,  2s: G -> S
        self.add_ten_sync_variation( [("3p g V", "3p g S"),("2s g G", "2s g S")])
        # syn 2: G -> V,  p: S -> V
        self.add_ten_sync_variation( [("2a g G", "3a g V")]+[("zp g S", "zp g V")])
        #3p: G -> S
        self.add_ten_sync_variation( [("3p g G", "3p g S")])
        #2s: S -> G
        self.add_ten_sync_variation( [("2s g S", "2s g G")])


class PermSynCreatorETH(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "ETH"

        self.TENSES_CASES = ["G", "V", "S", "C"]

        self.TENSES_CASES_PC = ["G", "S"]
        self.TENSES_CASES_SC = ["V", "C"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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
        self._create_syncretic_GEN_files()
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

    def _create_permutation_PERS_files(self):
        """
        creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
        """
        # d.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # s: 1 <-> 2, p:1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # s: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d:1 <-> 3, s: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "3d g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d:1 <-> 2, s: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T)
                                                                                           for T in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3, d: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # d.f: 1 <-> 3, p.m: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T)
                                                                                           for T in self.TENSES_CASES])

        # pfG: 2 <-> 3, sfG: 3<-> 2, dGm: 2<->3
        self.add_pers_perm_variation( [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("3s f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "2d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC])

        # sV: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC] + [
            ("2d g " + SC, "3d g " + SC) for SC in self.TENSES_CASES_SC] + [("1p g " + SC, "2p g " + SC) for SC in
                                                                        self.TENSES_CASES_SC])

        # sG: 1 <-> 3, dG: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC] + [("1p g " + SC, "2p g " + SC) for SC in
                                                                        self.TENSES_CASES_SC])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC] + [
            ("2d g " + SC, "3d g " + SC) for SC in self.TENSES_CASES_SC] + [("1p g " + PC, "2p g " + PC) for PC in
                                                                        self.TENSES_CASES_PC])

        # dm: 1 <-> 2, df: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 2
        self.add_pers_perm_variation( [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # pm: 1 <-> 2
        self.add_pers_perm_variation( [("1p m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3
        self.add_pers_perm_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # pf: 1 <-> 2
        self.add_pers_perm_variation( [("1p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # dm: 1 <-> 2, df: 1 <-> 3, sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3, dm: 2 <-> 3, sm: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "3s m " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES])

        # pm: 2 <-> 3
        self.add_pers_perm_variation( [("2p m " + T, "3p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3, df: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "3d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # pf: 1 <-> 2, df: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2p f " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "1d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 1 <-> 2, p: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("3d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s f " + T)
                                                                                           for T in self.TENSES_CASES])

        # dG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 2 <-> 1, pG: 2 <-> 1, dV: 2 <-> 3, pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g " + SC, "3d g " + SC) for SC in
                                                                        self.TENSES_CASES_SC] + [
                                    ("2p g " + SC, "3p g " + SC) for SC in self.TENSES_CASES_SC])

        # dm: 2 <-> 3, pm: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T)
                                                                                           for T in self.TENSES_CASES])

        # df: 2 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        self.add_pers_perm_variation( [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # dfG: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2d f " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 2 <-> 1, pG: 2 <-> 1, smV: 2 <-> 3
        self.add_pers_perm_variation( [("1d g " + PC, "2d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1p g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + SC, "3s m " + SC) for SC in
                                                                        self.TENSES_CASES_SC])

        # sfV: 2 <-> 3
        self.add_pers_perm_variation( [("2s f " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC])

        # sfV: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2s f " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC] + [
            ("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # d,p: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "3p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # dV,pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g V")] + [("2p g V", "3p g V")])

        # V: 2 <-> 3
        self.add_pers_perm_variation( [("2a g V", "3a g V")])

        # Vs: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # Vs: 1 <-> 3
        self.add_pers_perm_variation( [("1s g V", "3s g V")])

        # dV,pV: 1 <-> 3
        self.add_pers_perm_variation( [("1d g V", "3d g V")] + [("1p g V", "3p g V")])

        # dG,pG: 1 <-> 2, sV: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g G", "2d g G")] + [("1p g G", "2p g G")] + [("1s g V", "2s g V")] + [
                                    ("2p g V", "3p g V")] + [("2d g V", "3d g V")])

        # sG: 1 <-> 2, pG,dG: 2 <-> 3
        self.add_pers_perm_variation( [("1s g G", "2s g G")] + [("2d g G", "3d g G")] + [("2p g G", "3p g G")])

        # V: 1<->2
        self.add_pers_perm_variation( [("1a g V", "2a g V")])

        # G: 2<->3
        self.add_pers_perm_variation( [("2a g G", "3a g G")])

        # strong permutation 1
        self.add_pers_perm_variation( [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2s f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("3d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s m " + SC, "2s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s f " + SC, "2s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d m " + SC, "2d m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d f " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2p m " + SC, "1p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "1p f " + SC) for SC in self.TENSES_CASES_SC])

        # strong permutation 2
        self.add_pers_perm_variation( [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("2d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "2s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s f " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d m " + SC, "1d m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d f " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p m " + SC, "1p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "1p f " + SC) for SC in self.TENSES_CASES_SC])

        # strong permutation 3
        right = [("1s f " + PC, "2s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1d m " + PC, "2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1p m " + PC, "2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1p f " + PC, "2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("1d m " + SC, "2d m " + SC, "3d m " + SC) for SC in self.TENSES_CASES_SC] + [
                    ("1p f " + SC, "2p f " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC]
        left = [("1d f " + SC, "2d f " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
            ("1p m " + SC, "2p m " + SC, "3p m " + SC) for SC in self.TENSES_CASES_SC] + [
                   ("1d f " + PC, "2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                   ("1s m " + SC, "2s m " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dG: 1 <-> 2, pG: 1 <-> 2
        # dV: 2 <-> 3, pV: 2 <-> 3
        # sV: 1 <-> 3, sG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2s g " + PC, "3s g " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("2d g " + SC, "3d g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2p g " + SC, "3p g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("2s g " + SC, "3s g " + SC, "1s g " + SC) for SC in self.TENSES_CASES_SC]
        left = [("3d g " + SC, "1d g " + SC, "2d g " + SC) for SC in self.TENSES_CASES_SC] + [
            ("3p g " + SC, "1p g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC] + [
                   ("3s g " + PC, "1s g " + PC, "2s g " + PC) for PC in self.TENSES_CASES_PC]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        # dfV: 2 <-> 3, pfV: 2 <-> 3
        # sG: 1 <-> 3, sV: 1 <-> 3
        self.add_pers_perm_variation( [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f " + SC, "3d f " + SC) for SC in
                                                                        self.TENSES_CASES_SC] + [
                                    ("2p f " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC]
                                )

        # sG: 1->2->3
        # sV: 3->2->1
        # dG: 1 <-> 3 (dann dGm: 1<->2),  pG: 1 <-> 3 (dann pGm: 1<->2)
        # dV: 1 <-> 2 (dann dVf: 1<->3),  pV: 1 <-> 2 (dann pVf: 1<->3)
        right = [("2s g " + PC, "3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3s g " + SC, "1s g " + SC, "2s g " + SC) for SC in self.TENSES_CASES_SC]
        swap = [("3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("3p g " + PC, "1p g " + PC) for PC in
                                                                                 self.TENSES_CASES_PC] + [
                        ("2d g " + SC, "1d g " + SC) for SC in self.TENSES_CASES_SC] + [("2p g " + SC, "1p g " + SC) for SC
                                                                                    in self.TENSES_CASES_SC] + [
                        ("2d m " + PC, "1d m " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "1p m " + PC) for PC
                                                                                    in self.TENSES_CASES_PC] + [
                        ("3d f " + SC, "1d f " + SC) for SC in self.TENSES_CASES_SC] + [("3p f " + SC, "1p f " + SC) for SC
                                                                                    in self.TENSES_CASES_SC]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # dG: 1->2->3,  pG: 1->2->3
        # dV: 3->2->1,  pV: 3->2->1
        # sG: 1 <-> 3
        # sV: 1 <-> 3 (dann sVm: 1 <-> 2)
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3d g " + SC, "1d g " + SC, "2d g " + SC) for SC in self.TENSES_CASES_SC] + [
            ("3p g " + SC, "1p g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC]
        swap = [("3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC] + [("3s g " + SC, "1s g " + SC) for SC in
                                                                            self.TENSES_CASES_SC] + [
                   ("2s m " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # G: sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation( [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g G", "3d g G", "1d g G")] + [("2p g G", "3p g G", "1p g G")] + [
            ("2s g V", "3s g V", "1s g V")] + [("1s m C", "2s m C", "3s m C")] + [("1p m S", "2p m S", "3p m S")] + [
                    ("1d f S", "2d f S", "3d f S")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [
            ("3s g G", "1s g G", "2s g G")] + [("1s f C", "2s f C", "3s f C")] + [("1p f C", "2p f C", "3p f C")] + [
                   ("1d m S", "2d m S", "3d m S")]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # strong permutation 1
        self.add_pers_perm_variation(
                                [("1s m G", "3s m G")] + [("2s f G", "1s f G")] + [("3s m V", "2s m V")] + [
                                    ("1s f V", "2s f V")] + [("1s m S", "2s m S")] + [("2s f C", "3s f C")] + [
                                    ("1s m C", "3s m C")] + [("2d m G", "3d m G")] + [("3d f G", "1d f G")] + [
                                    ("1d m V", "2d m V")] + [("2d f V", "3d f V")] + [("3d m S", "2d m S")] + [
                                    ("2d f S", "3d f S")] + [("1d m C", "2d m C")] + [("3p m G", "2p m G")] + [
                                    ("1p f G", "2p f G")] + [("2p m V", "1p m V")] + [("3p f V", "1p f V")] + [
                                    ("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [("3p m C", "2p m C")] + [
                                    ("1p f C", "2p f C")]
                                )

        # strong permutation 2
        self.add_pers_perm_variation(
                                [("1s m G", "2s m G")] + [("1s f G", "3s f G")] + [("1s m V", "2s m V")] + [
                                    ("1s f V", "3s f V")] + [("2s m S", "1s m S")] + [("3s f S", "1s f S")] + [
                                    ("3s m C", "2s m C")] + [("3s f C", "2s f C")] + [("2d m G", "3d m G")] + [
                                    ("2d f G", "1d f G")] + [("2d m V", "1d m V")] + [("2d f V", "3d f V")] + [
                                    ("3d m S", "2d m S")] + [("1d f C", "2d f C")] + [("3p m G", "2p m G")] + [
                                    ("3p f G", "1p f G")] + [("3p m V", "1p m V")] + [("3p f V", "1p f V")] + [
                                    ("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [("3p m C", "2p m C")] + [
                                    ("1p f C", "2p f C")]
                                )

        # pfG: 2 <-> 3, sfS: 3<-> 2, dGm: 2<->3
        self.add_pers_perm_variation( [("2p f G", "3p f G")] + [("3s f S", "2s f S")] + [("3d m G", "2d m G")]
                                )

        # dC,pC: 2 <-> 3
        self.add_pers_perm_variation( [("2d g C", "3d g C")] + [("2p g C", "3p g C")]
                                )

        # dV/C,pV/C: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + SC, "3d g " + SC) for SC in self.TENSES_CASES_SC] + [
            ("2p g " + SC, "3p g " + SC) for SC in self.TENSES_CASES_SC])

        # Cs: 2 <-> 3
        self.add_pers_perm_variation( [("2s g C", "3s g C")])

        # C: 2 <-> 3
        self.add_pers_perm_variation( [("2a g C", "3a g C")])

        # SC: 2 <-> 3
        self.add_pers_perm_variation( [("2a g " + SC, "3a g " + SC) for SC in self.TENSES_CASES_SC])

        # SC: s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC])

        # dG,pG: 1 <-> 2, sV: 1 <-> 2, sS: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g G", "2d g G")] + [("1p g G", "2p g G")] + [("1s g V", "2s g V")] + [
                                    ("2p g C", "3p g C")] + [("2d g C", "3d g C")] + [("1s g S", "2s g S")]
                                )

        # dC,pC: 1 <-> 2, sG/S: 1 <-> 2, pG/S,dG/S: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g C", "2d g C")] + [("1p g C", "2p g C")] + [("1s g " + PC, "2s g " + PC) for PC
                                                                                   in self.TENSES_CASES_PC] + [
                                    ("2p g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC]
                                )

        # sS: 1 <-> 2, pS,dS: 2 <-> 3
        self.add_pers_perm_variation( [("1s g S", "2s g S")] + [("2d g S", "3d g S")] + [("2p g S", "3p g S")]
                                )

        # S: 1<->2
        self.add_pers_perm_variation( [("1a g S", "2a g S")])

        # C: 2<->3
        self.add_pers_perm_variation( [("2a g C", "3a g C")])

    def _create_permutation_NUM_files(self):
        """
        creates all permutation files where NUM-features are swapped (s <-> d <-> p)]
        """

        # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p
        self.add_num_perm_variation( [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2f: s <-> p, 3m: s <-> p
        self.add_num_perm_variation(
                                [("2s f " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3p m " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2m: s <-> p, 3f: d <-> p
        self.add_num_perm_variation(
                                [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3d f " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 1m: s <-> p
        self.add_num_perm_variation( [("1s m " + T, "1p m " + T) for T in self.TENSES_CASES])

        # 1m: s <-> d, 2f: d <-> p
        self.add_num_perm_variation(
                                [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2p f " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2: s <-> d, 3: d <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2G: s <-> p
        self.add_num_perm_variation( [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G: s <-> p, 3V: d<->p
        self.add_num_perm_variation(
                                [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3d g " + SC, "3p g " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # 3G:s<->p, 2V:d<->p, 1m: s<->d
        self.add_num_perm_variation(
                                [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d g " + SC, "2p g " + SC)
                                    for SC in self.TENSES_CASES_SC] + [
                                    ("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])

        # 1f: s <-> p
        self.add_num_perm_variation( [("1s f " + T, "1p f " + T) for T in self.TENSES_CASES])

        # 2f: s <-> d, 3m: s <-> d
        self.add_num_perm_variation(
                                [("2s f " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d m " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2m: s <-> d, 1f: s <-> d
        self.add_num_perm_variation(
                                [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "1d f " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2m: s <-> p, 1m: s <-> d
        self.add_num_perm_variation(
                                [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "1d m " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 1V: s <-> d, 3G: s <-> d
        self.add_num_perm_variation(
                                [("1s g " + SC, "1d g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s g " + PC, "3d g " + PC)
                                    for PC in self.TENSES_CASES_PC])

        # 1G: s <-> d, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + T, "2d g " + T)
                                                                                             for
                                                                                             T in self.TENSES_CASES])

        # 2m: s <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # 3f: s <-> p
        self.add_num_perm_variation( [("3s f " + T, "3p f " + T) for T in self.TENSES_CASES])

        # 1: s <-> p, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "2p g " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # 2V: s <-> p, 3mV: s <-> p
        self.add_num_perm_variation(
                                [("2s g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + SC, "3p m " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # 2fV: s <-> p
        self.add_num_perm_variation( [("2s f " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC])

        # 2Vf: s <-> p, 3Gm: s <-> p
        self.add_num_perm_variation(
                                [("2s f " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + PC, "3p m " + PC)
                                    for PC in self.TENSES_CASES_PC])

        # 2m: s <-> d, 3f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES])

        # 3mG: s <-> p
        self.add_num_perm_variation( [("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # f: s -> d -> p;   m: p -> d -> s
        right = [("zs f " + T, "zd f " + T, "zp f " + T) for T in self.TENSES_CASES]
        left = [("zs m " + T, "zd m " + T, "zp m " + T) for T in self.TENSES_CASES]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # f: s <-> p,   m: d <-> p
        self.add_num_perm_variation(
                                [("zs f " + T, "zp f " + T) for T in self.TENSES_CASES] + [("zd m " + T, "zp m " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # STRONG",

        # strong permutation 1
        self.add_num_perm_variation(
                                [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s f " + PC, "1d f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "1d m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s f " + SC, "1p f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d f " + PC, "2s f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2d m " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d f " + SC, "2s f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p f " + PC, "3d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3p m " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "3s f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 2
        self.add_num_perm_variation(
                                [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1d f " + PC, "1s f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("1p m " + SC, "1d m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1s f " + SC, "1p f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2d m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p f " + PC, "2d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2s m " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d f " + SC, "2s f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s f " + PC, "3d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + SC, "3p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "3s f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 3
        right = [("1s m " + PC, "1d m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("1s m " + SC, "1d m " + SC, "1p m " + SC) for SC in self.TENSES_CASES_SC] + [
                    ("2s m " + PC, "2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                    ("2s m " + SC, "2d m " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] + [
                    ("3s m " + PC, "3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC]
        left = [("1s f " + PC, "1d f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2s f " + PC, "2d f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                   ("2s f " + SC, "2d f " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC] + [
                   ("3s f " + PC, "3d f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
                   ("3s f " + SC, "3d f " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 2mV:  s <-> p, 2fG: s <-> p;
        # 3fV: s <-> p, 3mG: s <-> p; 1G: s <-> p
        self.add_num_perm_variation(
                                [("2s m " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2s f " + PC, "2p f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("3s f " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + PC, "3p m " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("1s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G s <-> p, 3V s <-> d,
        # 3mG d <-> p, 3fG: s <-> p,
        # 3mV:  s <-> d, 3fV:  d <-> p,
        # 1: s <-> d
        self.add_num_perm_variation(
                                [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s g " + SC, "3d g " + SC)
                                    for SC in self.TENSES_CASES_SC] + [
                                    ("3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s f " + PC, "3p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "3d f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # strong permutation 1
        self.add_num_perm_variation(
                                [("1s m G", "1p m G")] + [("1s f G", "1d f G")] + [("1s m G", "1d m G")] + [
                                    ("1s f G", "1p f G")] + [("1s m V", "1d m V")] + [("1s f V", "1p f V")] + [
                                    ("1s m C", "1p m C")] + [
                                    ("1s f C", "1p f C")] + [("2d m G", "2p m G")] + [("2d f G", "2s f G")] + [
                                    ("2d m V", "2p m V")] + [("2d f V", "2s f V")] + [("2s m C", "2p m C")] + [
                                    ("2s f C", "2p f C")] + [("2s m S", "2p m S")] + [("2s f S", "2p f S")] + [
                                    ("3p m G", "3s m G")] + [("3p f G", "3d f G")] + [("3p m V", "3s m V")] + [
                                    ("3p f V", "3s f V")] + [("3s m C", "3p m C")] + [("3d f C", "3p f C")] + [
                                    ("3d m S", "3s m S")] + [("3d f S", "3p f S")])

        # strong permutation 2
        self.add_num_perm_variation(
                                [("1s m G", "1p m G")] + [("1d f G", "1s f G")] + [("1p m V", "1d m V")] + [
                                    ("1s f V", "1p f V")] + [("1s m C", "1p m C")] + [("1d f C", "1p f C")] + [
                                    ("1d m S", "1s m S")] + [
                                    ("1d f S", "1p f S")] + [("2d m G", "2s m G")] + [("2p f G", "2d f G")] + [
                                    ("2s m V", "2p m V")] + [("2d f V", "2s f V")] + [("2s m C", "2p m C")] + [
                                    ("2d f S", "2p f S")] + [("3p m G", "3s m G")] + [("3s f G", "3d f G")] + [
                                    ("3d m V", "3p m V")] + [("3p f V", "3s f V")] + [("3s f C", "3p f C")] + [
                                    ("3p m S", "3s m S")])

        # strong permutation 3
        right = [("3s m G", "3d m G", "3p m G")] + [("1s m G", "1d m G", "1p m G")] + [
            ("1s m V", "1d m V", "1p m V")] + [
                    ("1s m C", "1d m C", "1p m C")] + [("2s m G", "2d m G", "2p m G")] + [
                    ("2s m V", "2d m V", "2p m V")] + [
                    ("2s m C", "2d m C", "2p m C")] + [("2s f S", "2d f S", "2p f S")]
        left = [("3s f G", "3d f G", "3p f G")] + [("3s f V", "3d f V", "3p f V")] + [
            ("3s f C", "3d f C", "3p f C")] + [
                   ("2s f G", "2d f G", "2p f G")] + [("2s f V", "2d f V", "2p f V")] + [
                   ("1s f S", "1d f S", "1p f S")] + [
                   ("1s f G", "1d f G", "1p f G")]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 1V: s <-> d, 3G: s <-> d, 2C: s <-> d, 2S: s <-> d
        self.add_num_perm_variation(
                                [("1s g V", "1d g V")] + [("3s g G", "3d g G")] + [("2s g C", "2d g C")] + [
                                    ("3s g S", "3d g S")])

        # 1G: s <-> d, 2S: s <-> p; 3C: d <-> p
        self.add_num_perm_variation( [("1s g G", "1d g G")] + [("2s g S", "2p g S")] + [("3d g C", "3p g C")])

        # 2G: s <-> p, 3S: s <-> p
        self.add_num_perm_variation( [("2s g G", "2p g G")] + [("3s g S", "3p g S")])

        # 2C: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g C", "2p g C")] + [("3d g V", "3p g V")])

        # 3G:s<->p, 2S:d<->p, 1m: s<->d
        self.add_num_perm_variation(
                                [("3s g G", "3p g G")] + [("2d g S", "2p g S")] + [("1s m " + T, "1d m " + T) for T in
                                                                                   self.TENSES_CASES])

    def _create_permutation_GEN_files(self):
        """
        creates all permutation files where GEN-features are swapped (m <-> f)
        """

        # p2: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # s3: m <-> f
        self.add_gen_perm_variation( [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # p2: m <-> f, s3: m <-> f
        self.add_gen_perm_variation(
                                [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3s f " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES])

        # s2: m <-> f, d3: m <-> f, p2: m <-> f
        self.add_gen_perm_variation(
                                [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3d f " + T)
                                                                                           for T
                                                                                           in self.TENSES_CASES] + [
                                    ("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: m <-> f
        self.add_gen_perm_variation( [("2a m " + T, "2a f " + T) for T in self.TENSES_CASES])

        # 3: m <-> f
        self.add_gen_perm_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # s: m <-> f
        self.add_gen_perm_variation( [("zs m " + T, "zs f " + T) for T in self.TENSES_CASES])

        # p: m <-> f
        self.add_gen_perm_variation( [("zp m " + T, "zp f " + T) for T in self.TENSES_CASES])

        # 3dV: m <-> f
        self.add_gen_perm_variation( [("3d m " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC])

        # 2pG: m<->f, 3sG: m<->f
        self.add_gen_perm_variation(
                                [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s m " + PC, "3s f " + PC)
                                    for PC in self.TENSES_CASES_PC])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        self.add_gen_perm_variation(
                                [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s m " + PC, "3s f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC])

        # strong permutation 1
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p m " + PC, "1p f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "1s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d m " + SC, "1d f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d m " + PC, "2d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2d m " + SC, "2d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2p m " + SC, "2p f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3s m " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p m " + SC, "3p f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 2
        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p m " + PC, "1p f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "2p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2d m " + SC, "2d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + PC, "3s f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p m " + SC, "3p f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 3

        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p m " + PC, "1p f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "1s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d m " + SC, "1d f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d m " + SC, "2d f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2p m " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + PC, "3s f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3s m " + SC, "3s f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("3d m " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p m " + SC, "3p f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 4

        self.add_gen_perm_variation(
                                [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p m " + PC, "1p f " + PC)
                                    for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "1s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d m " + SC, "1d f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d m " + PC, "2d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2s m " + SC, "2s f " + SC)
                                    for SC in
                                    self.TENSES_CASES_SC] + [
                                    ("2p m " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3d m " + PC, "3d f " + PC)
                                    for PC in
                                    self.TENSES_CASES_PC] + [
                                    ("3d m " + SC, "3d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p m " + SC, "3p f " + SC)
                                    for SC in self.TENSES_CASES_SC])

        # strong permutation 1
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1s m S", "1s f S")] + [("1p m C", "1p f C")] + [
                                    ("2s m G", "2s f G")] + [
                                    ("2d m G", "2d f G")] + [("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [
                                    ("2p m C", "2p f C")] + [("2p m C", "2p f C")] + [("3s m G", "3s f G")] + [
                                    ("3p m G", "3p f G")] + [("3s m V", "3s f V")] + [("3p m V", "3p f V")] + [
                                    ("3p m S", "3p f S")] + [("3s m S", "3s f S")] + [("3s m C", "3s f C")] + [
                                    ("3d m C", "3d f C")])

        # strong permutation 2
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m S", "1s f S")] + [
                                    ("1d m S", "1d f S")] + [("2s m G", "2s f G")] + [("2p m G", "2p f G")] + [
                                    ("2d m V", "2d f V")] + [
                                    ("2s m C", "2s f C")] + [("2d m C", "2d f C")] + [("3s m G", "3s f G")] + [
                                    ("3d m G", "3d f G")] + [("3p m G", "3p f G")] + [("3d m V", "3d f V")] + [
                                    ("3p m V", "3p f V")] + [("3d m S", "3d f S")] + [("3s m C", "3s f C")] + [
                                    ("3d m C", "3d f C")])

        # strong permutation 3
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1d m C", "1d f C")] + [("1p m S", "1p f S")] + [
                                    ("2p m G", "2p f G")] + [
                                    ("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [("2s m C", "2s f C")] + [
                                    ("2d m C", "2d f C")] + [("2s m S", "2s f S")] + [("2p m S", "2p f S")] + [
                                    ("3s m G", "3s f G")] + [("3d m G", "3d f G")] + [("3s m V", "3s f V")] + [
                                    ("3d m V", "3d f V")] + [("3p m V", "3p f V")] + [("3s m C", "3s f C")] + [
                                    ("3p m C", "3p f C")] + [("3s m S", "3s f S")] + [("3p m S", "3p f S")])

        # strong permutation 4
        self.add_gen_perm_variation(
                                [("1s m G", "1s f G")] + [("1p m G", "1p f G")] + [("1s m V", "1s f V")] + [
                                    ("1d m V", "1d f V")] + [("1s m C", "1s f C")] + [("1p m C", "1p f C")] + [
                                    ("1d m S", "1d f S")] + [
                                    ("2s m G", "2s f G")] + [("2d m G", "2d f G")] + [("2p m G", "2p f G")] + [
                                    ("2s m V", "2s f V")] + [("2p m V", "2p f V")] + [("2d m C", "2d f C")] + [
                                    ("2p m C", "2p f C")] + [("2d m S", "2d f S")] + [("3d m G", "3d f G")] + [
                                    ("3d m V", "3d f V")] + [("3p m V", "3p f V")] + [("3s m C", "3s f C")] + [
                                    ("3p m C", "3p f C")] + [("3s m S", "3s f S")] + [("3p m S", "3p f S")])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        # 3pS: m<->f, 2sC: m<->f
        self.add_gen_perm_variation(
                                [("2p m G", "2p f G")] + [("3s m G", "3s f G")] + [("3p m V", "3p f V")] + [
                                    ("3p m S", "3p f S")] + [("2s m C", "2s f C")])

        # 3pS: m<->f, 2sS: m<->f
        # 2sC: m<->f, 3sC: m<->f
        self.add_gen_perm_variation(
                                [("3p m S", "3p f S")] + [("2s m S", "2s f S")] + [("2s m C", "2s f C")] + [
                                    ("3s m C", "3s f C")])

    def _create_permutation_TENSE_files(self):
        """
        creates all permutation files where TENSE-features are swapped (V <-> F)
        """
        # 2s : G <-> V, 3p: G <-> V, 1d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G")] + [("3p g V", "3p g G")] + [("1d g V", "1d g G")])

        # 2sf: G <-> V, 3pm: G <-> V, 3df: G <-> V
        self.add_ten_perm_variation( [("2s f V", "2s f G")] + [("3p m V", "3p m G")] + [("3d f V", "3d f G")])

        # 1s: G <-> V, 3sm: G <-> V, 1p: G <-> V, 2pm: G <-> V, 2s: G <-> V
        self.add_ten_perm_variation(
                                [("1s g V", "1s g G")] + [("1p g V", "1p g G")] + [("2s g V", "2s g G")] + [
                                    ("3s m V", "3s f G")] + [("2p m V", "2p m G")])

        # 2 : G <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g G")])

        # 3 : G <-> V
        self.add_ten_perm_variation( [("3a g V", "3a g G")])

        # s : G <-> V
        self.add_ten_perm_variation( [("zs g V", "zs g G")])

        # p : G <-> V
        self.add_ten_perm_variation( [("zp g V", "zp g G")])

        # sf : G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("zs f V", "zs f G")] + [("3d g V", "3d g G")])

        # 1pm : G <-> V, 3sm : G <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m G")] + [("3s m V", "3s m G")])

        # 1f : G <-> V, 3dm : G <-> V
        self.add_ten_perm_variation( [("1a f V", "1a f G")] + [("3d m V", "3d m G")])

        # sf : G <-> V, 1pm : G <-> V, 2dm : G <-> V
        self.add_ten_perm_variation( [("zs m V", "zs m G")] + [("1p m V", "1p m G")] + [("2d m V", "2d m G")])

        # 3sf : G <-> V, 2sm : G <-> V
        self.add_ten_perm_variation( [("3s f V", "3s f G")] + [("2s m V", "2s m G")])

        # df : G <-> V
        self.add_ten_perm_variation( [("zd f V", "zd f G")])

        # 1 : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G")])

        # d : G <-> V
        self.add_ten_perm_variation( [("zd g V", "zd g G")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation(
                                [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")] + [
                                    ("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")])

        # 1dm, 3df, 2pm, 2sm, 1sf, 3s
        self.add_ten_perm_variation(
                                [("1d m G", "1d m V")] + [("3d f G", "3d f V")] + [("2p m G", "2p m V")] + [
                                    ("2s m G", "2s m V")] + [("1s f G", "1s f V")] + [("3s g G", "3s g V")])

        # 2dm, 3df, 2sf, 1d, 1p, 3sm
        self.add_ten_perm_variation(
                                [("2d m G", "2d m V")] + [("3d f G", "3d f V")] + [("2s f G", "2s f V")] + [
                                    ("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("3s m G", "3s m V")])

        # 1d, 1p, 2p, 2d, 3s
        self.add_ten_perm_variation(
                                [("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("2d g G", "2d g V")] + [
                                    ("2p g G", "2p g V")] + [("3s g G", "3s g V")])

        # 2s : G <-> C, 3p: G <-> C, 1d: G <-> C
        self.add_ten_perm_variation( [("2s g C", "2s g G")] + [("3p g C", "3p g G")] + [("1d g C", "1d g G")])

        # 2s : G <-> C, 3p: G <-> V, 1d: G <-> S
        self.add_ten_perm_variation( [("2s g C", "2s g G")] + [("3p g V", "3p g G")] + [("1d g S", "1d g G")])

        # 2sf: G <-> V, 3pm: G <-> V, 3df: G <-> V
        # 2sf: S <-> C, 3pm: S <-> C, 3df: S <-> C
        self.add_ten_perm_variation(
                                [("2s f V", "2s f G")] + [("3p m V", "3p m G")] + [("3d f V", "3d f G")] + [
                                    ("2s f C", "2s f S")] + [("3p m C", "3p m S")] + [("3d f C", "3d f S")])

        # 2sf: G <-> V, 3pm: G <-> C, 3df: S <-> V
        self.add_ten_perm_variation( [("2s f V", "2s f G")] + [("3p m C", "3p m G")] + [("3d f V", "3d f S")])

        # 1s: G <-> V, 3sm: C <-> V, 1p: G <-> C, 2pm: S <-> V, 2s: G <-> S
        self.add_ten_perm_variation(
                                [("1s g V", "1s g G")] + [("1p g C", "1p g G")] + [("2s g S", "2s g G")] + [
                                    ("3s m V", "3s f C")] + [("2p m V", "2p m S")])

        # 2 : C <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g C")])

        # 3 : S <-> C
        self.add_ten_perm_variation( [("3a g C", "3a g S")])

        # sf : G <-> C, 3d: G <-> S
        # sf : S <-> V, 3d: C <-> V
        self.add_ten_perm_variation(
                                [("zs f C", "zs f G")] + [("zs f V", "zs f S")] + [("3d g V", "3d g S")] + [
                                    ("3d g V", "3d g C")])

        # 1pm : S <-> V, 3sm : S <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m S")] + [("3s m V", "3s m S")])

        # sf : S <-> V, 1pm : G <-> C, 2dm : G <-> V
        self.add_ten_perm_variation( [("zs m V", "zs m S")] + [("1p m C", "1p m G")] + [("2d m V", "2d m G")])

        # 3sf : S <-> V, 2sm : G <-> V
        self.add_ten_perm_variation( [("3s f V", "3s f S")] + [("2s m V", "2s m G")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("3p g S", "3p g C")] + [("3d g S", "3d g V")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g S", "2s g C")] + [("3p g G", "3p g S")] + [("3d g C", "3d g V")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V")] + [("3d g S", "3d g C")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation(
                                [("2s g G", "2s g C")] + [("1p g S", "1p g V")] + [("1d g C", "1d g G")] + [
                                    ("3p g V", "3p g C")] + [("3d g S", "3d g G")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g S")] + [("1p g V", "1p g C")] + [("1d g S", "1d g V")])

        # 3p,2s: G -> S
        self.add_ten_perm_variation( [("3p g G", "3p g S")] + [("2s g G", "2s g S")])

    def _create_permutation_X_files(self):
        """
        creates all permutation files where several or all features are swapped
        """

        # 2 : G <-> V, 3: s <-> p
        self.add_xross_perm_variation(
                                [("2a g G", "2a g V")] + [("3s g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 2s: m <-> f, 3p <-> 1s, 2pV <-> 1pV
        self.add_xross_perm_variation(
                                [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1s g " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("2p g V", "1p g V")])

        # 2pG: m <-> f, sG: 3m<-> 2f, dGm: 2<->3
        self.add_xross_perm_variation( [("2p m G", "2p f G")] + [("3s m G", "2s f G")] + [("3d m G", "2d m G")])

        # 3dfV <-> 1smG, 2pfV <-> 3smV, 2pmG <-> 1dmV, 3sfG <-> 3dmG
        self.add_xross_perm_variation(
                                [("3d f V", "1s m G")] + [("2p f V", "3s m V")] + [("2p m G", "1d m V")] + [
                                    ("3s f G", "3d m G")])

        # 1dm <-> 2df, 2pmV <-> 3pfG, 3smG <-> 1pfV
        self.add_xross_perm_variation(
                                [("1d m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("2p m V", "3p f G")] + [
                                    ("3s m G", "1p f V")])

        # 2G <-> 3V, sG <-> pV
        self.add_xross_perm_variation( [("2a g G", "3a g V")] + [("zs g G", "zp g V")])

        # d: 1G <-> 3V,  p: 1G <-> 3V,
        # s: 3G <-> 2V
        self.add_xross_perm_variation( [("1d g G", "3d g V")] + [("1p g G", "3p g V")] + [("3s g G", "2s g V")])

        # V: 3p <-> 2s, Vs3 <-> Gs1
        self.add_xross_perm_variation( [("3p g V", "2s g V")] + [("3s g V", "1s g G")])

        # full permutation 1
        self.add_xross_perm_variation(
                                [("1s m G", "3s m V")] + [("2s m G", "1d f V")] + [("3s m G", "2p f G")] + [
                                    ("1s f G", "3p m V")] + [("2s f G", "2d f G")] + [("3s f G", "1p m G")] + [
                                    ("3p m G", "3d m V")] + [("1s m V", "2s f V")] + [("2s m V", "2p f V")] + [
                                    ("2p m V", "1p f V")] + [("3s f V", "1s f V")] + [("3d m G", "1d f G")] + [
                                    ("2d m G", "1d m V")] + [("1d m G", "3d f V")] + [("2p m G", "3p f G")] + [
                                    ("3d f G", "1p f G")] + [("2d m V", "3p f V")] + [("2d f V", "1p m V")])

        # full permutation 2
        self.add_xross_perm_variation(
                                [("1s m G", "2d m G")] + [("1s f G", "3s f V")] + [("2s m G", "1s f G")] + [
                                    ("2s f G", "2d f G")] + [("2s m V", "1p m V")] + [("2s f V", "1p f V")] + [
                                    ("3p m V", "3p m G")] + [("3p f V", "3p f G")] + [("1d m V", "3s m V")] + [
                                    ("1d f V", "1s m G")] + [("1s m V", "1p m G")] + [("1s f V", "3d m V")] + [
                                    ("2d m V", "2s m G")] + [("2d f V", "1p f G")] + [("3d f V", "2s f G")] + [
                                    ("2p m G", "3d f G")] + [("2p f G", "2p m V")] + [("3d m G", "2p f V")])

        # full permutation 3
        self.add_xross_perm_variation(
                                [("1s g G", "2d g V")] + [("2p g G", "2s g G")] + [("3d g G", "1p g V")] + [
                                    ("1s g V", "1p g G")] + [("3s g V", "3s g G")] + [("3d g V", "1d g G")] + [
                                    ("1d g G", "2p g V")] + [("2s g V", "3p g G")] + [("3p g V", "2d g G")] + [
                                    ("1s g C", "1p g S")] + [("3s g C", "3s g S")] + [("3d g C", "1d g S")])

        # full permutation 4
        self.add_xross_perm_variation(
                                [("1s g G", "1d g G")] + [("2d g G", "2p g G")] + [("3s g G", "3p g G")] + [
                                    ("1p g V", "3d g G")] + [("2s g G", "3s g V")] + [("1p g G", "2d g V")] + [
                                    ("2d g C", "2p g C")] + [("1s g " + T, "2s g " + T) for T in ["V", "S", "C"]] + [
                                    ("2p g " + T, "3p g " + T) for T in ["V", "S", "C"]] + [("1d g " + T, "3d g " + T)
                                                                                              for T in
                                                                                              ["V", "S", "C"]])

        # full permutation 5
        self.add_xross_perm_variation(
                                [("1s g G", "2p g V")] + [("3p g G", "2s g V")] + [("2d g G", "1d g V")] + [
                                    ("1s g V", "3d g G")] + [("2d g V", "2p g G")] + [("3p g V", "3s g G")] + [
                                    ("1p g V", "2s g G")] + [("3s g V", "1p g G")] + [("3d g V", "1d g G")] + [
                                    ("1s g S", "2p g C")] + [("3p g S", "2s g C")] + [("2d g S", "1d g C")] + [
                                    ("1s g C", "3d g S")] + [("2d g C", "2p g S")] + [("3p g C", "3s g S")] + [
                                    ("1p g C", "2s g S")] + [("3s g C", "1p g S")] + [("3d g C", "1d g S")])

        # full permutation 6
        self.add_xross_perm_variation(
                                [("1s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2p f " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "1p f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("1d f " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("2s m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("2d m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # full permutation 7
        self.add_xross_perm_variation(
                                [("1s m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d f " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("3s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2s f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("2d m " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3p f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("1p m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2d f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("3p m " + T, "3d f " + T) for T in self.TENSES_CASES])

        # full permutation 8
        self.add_xross_perm_variation(
                                [("1s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s m " + T)
                                                                                           for T in
                                                                                           self.TENSES_CASES] + [
                                    ("2p m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s f " + T, "2s m " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("1d m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("1d f " + T, "2s f " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("3d f " + T, "2d m " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T)
                                                                                              for T in
                                                                                              self.TENSES_CASES] + [
                                    ("3p m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # rotations
        # full permutation 9
        self.add_xross_perm_variation( rotate_right_list=[("1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES] + [
            ("2s g " + T, "3p g " + T, "1d g " + T) for T in self.TENSES_CASES] + [
                                    ("3s g " + T, "1p g " + T, "3d g " + T) for T in self.TENSES_CASES])

        # full permutation 10
        right = [("1s g " + T, "2s g " + T, "3s g " + T) for T in self.TENSES_CASES]
        left = [("1d g " + T, "2d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 11
        right = [("1s f " + T, "3d m " + T, "3p f " + T) for T in self.TENSES_CASES] + [
            ("3s m " + T, "2p m " + T, "1d f " + T) for T in self.TENSES_CASES]
        left = [("1s m " + T, "1p m " + T, "2s f " + T) for T in self.TENSES_CASES] + [
            ("1p f " + T, "2d m " + T, "3s f " + T) for T in self.TENSES_CASES] + [
                   ("2s m " + T, "1d m " + T, "3d f " + T) for T in self.TENSES_CASES] + [
                   ("2d f " + T, "1p f " + T, "3p m " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 12
        right = [("1s g G", "2p g V", "3d g G")] + [("2s g G", "2s g V", "1d g V")] + [("3s g V", "1p g V", "1p g G")]
        left = [("2d g V", "3p g V", "3s g G")] + [("2d g G", "2p g G", "3p g G")] + [
            ("1d g G", "1s g V", "3d g V")] + [("1p g S", "1s g C", "2d g C")] + [("3d g S", "1d g C", "3d g C")] + [
                   ("1p g C", "1s g S", "2d g S")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 13
        left = [("1s m G", "2s m G", "3p f V")] + [("1p m S", "1d f S", "2d m C")] + [
            ("3p m S", "3p f S", "1s f S")] + [("1p m G", "1d f G", "2d m V")] + [("3p m G", "3p f G", "1s f G")] + [
                   ("3s f G", "3s f V", "3d m V")] + [("3s m V", "2p m V", "3p m V")] + [
                   ("1p f G", "2d f G", "3d m G")] + [("1s f V", "3d f V", "2d m G")]
        right = [("1d m G", "1s m V", "2d f V")] + [("2s f G", "2s f V", "2s m V")] + [
            ("1d m V", "2p f G", "1p f V")] + [("3s m G", "1p m V", "2p m G")] + [("3d f G", "1d f V", "2p f V")] + [
                    ("1d m C", "2p f S", "1p f C")] + [("3s m S", "1p m C", "2p m S")] + [
                    ("3d f S", "1d f C", "2p f C")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 14
        left = [("1a m G", "1a f V", "3a f G")] + [("2a m G", "2a m V", "3a f V")] + [
            ("2a f V", "1a f G", "1a m V")] + [("3a m G", "2a f G", "3a m V")] + [("1a m S", "1a f C", "3a f S")] + [
                   ("2a m S", "2a m C", "3a f C")] + [("2a f C", "1a f S", "1a m C")] + [("3a m S", "2a f S", "3a m C")]
        self.add_xross_perm_variation( rotate_left_list=left)

        # full permutation 15
        left = [("zs m G", "zs m V", "zp m G")] + [("zs f V", "zp m V", "zd f G")] + [
            ("zs f G", "zd m V", "zp f V")] + [("zs f S", "zd m S", "zp f S")] + [("zp f C", "zd m C", "zd f C")]
        right = [("zp f G", "zd m G", "zd f V")] + [("zp m C", "zs f C", "zs m S")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # 2smG <-> 3sfV,
        # 2sfG <-> 2pfG,  3smV  <-> 2smV
        # 1s <-> 1p
        # V: 2d <-> 3d, V:2p <-> 3p
        # 3dG: m <-> f,   3pG: m <-> f
        self.add_xross_perm_variation(
                                [("2s m G", "3s f V")] + [("2s f G", "2p f G")] + [("3s m V", "2s m V")] + [
                                    ("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [
                                    ("2d g " + SC, "3d g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2p g " + SC, "3p g " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # 3s: m <-> f
        # 2G: s <-> p
        # Vp: 1 <-> 3, Vd: 1 <-> 3
        # Vs: 1m <-> 2f
        self.add_xross_perm_variation(
                                [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2s g G", "2p g G")] + [
                                    ("1p g V", "3p g V")] + [("1d g V", "3d g V")] + [("1s m V", "2s f V")])

        # 3sV: m <-> f
        # 1G: s <-> p
        # V: 1d  <-> 2d, V: 1p <-> 2p
        # 3pV <-> 2pG;  2sG <-> 3pG
        self.add_xross_perm_variation(
                                [("3s m V", "3s f V")] + [("1s g G", "1p g G")] + [("1d g V", "2d g V")] + [
                                    ("1p g V", "2p g V")] + [("3p g V", "2p g G")] + [("3p g G", "2s g G")])

        self.add_xross_perm_variation(
                                [("1s m G", "2d m G")] + [("1s f G", "3d m V")] + [("2s m G", "3d f G")] + [
                                    ("2s f G", "2p m G")] + [("3s m G", "3p m V")] + [("3s f S", "1p f G")] + [
                                    ("1d m G", "3d m G")] + [("1d f G", "2s m V")] + [("2d f S", "1d m C")] + [
                                    ("1p m G", "1d f V")] + [("2p f S", "3s f V")] + [("3p m G", "3s m C")] + [
                                    ("3p f G", "2s f V")] + [("1s m V", "1p f C")] + [("1s f V", "2d m V")] + [
                                    ("2d f C", "3d f C")] + [("1p m V", "3p f V")] + [("2p f V", "2p m V")] + [
                                    ("3p f S", "2d m C")] + [("3p m S", "3d f V")] + [("2p m C", "2d f V")] + [
                                    ("2p f C", "1s m C")] + [("3p f C", "1p m S")] + [("1p f V", "2s m C")] + [
                                    ("2d f G", "2s f C")])
        self.add_xross_perm_variation(
                                [("1s m G", "3s f G")] + [("1s m V", "3s f V")] + [("1s f V", "2s f G")] + [
                                    ("2s m V", "2d m G")] + [("2s f V", "3d m G")] + [("3s m V", "1s f G")] + [
                                    ("2s m G", "3p m V")] + [("1d m G", "2d f G")] + [("1d f G", "1p m G")] + [
                                    ("1p m V", "3s m G")] + [("1p f V", "3p f V")] + [("2p f V", "2d f V")] + [
                                    ("3d f G", "2p m V")] + [("1p f G", "1d m V")] + [("2p m G", "3d f V")] + [
                                    ("2d m V", "3p m G")] + [("2p f G", "1d f V")] + [("3p f G", "3d m V")] + [
                                    ("3p f S", "2d m C")] + [("3p m S", "3d f S")] + [("2p m C", "2d f C")] + [
                                    ("2p f C", "1s m C")] + [("3p f C", "1p m S")] + [("1p f S", "2s m C")] + [
                                    ("2d f S", "2s f C")])
        self.add_xross_perm_variation(
                                [("1s m G", "1p m G")] + [("1s f G", "3d m G")] + [("2s m G", "3p f G")] + [
                                    ("2s f G", "3s f V")] + [("3s m G", "1d m G")] + [("3s f G", "2d m V")] + [
                                    ("1d f G", "3d m V")] + [("2d m G", "1p m V")] + [("2d f G", "1p f V")] + [
                                    ("3d f G", "1d f V")] + [("1p f G", "3s m V")] + [("2p m G", "3d f V")] + [
                                    ("2p f G", "1d m V")] + [("3p m G", "2d f V")] + [("1s m V", "2p f V")] + [
                                    ("1s f V", "3p f V")] + [("2s m V", "2p m V")] + [("2s f V", "3p m V")] + [
                                    ("1s m S", "1p m C")] + [("1s f S", "3d m C")] + [("2s m S", "3p f C")] + [
                                    ("2s f S", "3s f V")] + [("3s m S", "1d m C")] + [("3s f S", "2d m C")] + [
                                    ("1d f S", "3d m C")] + [("2d m S", "1p m C")] + [("2d f S", "1p f C")] + [
                                    ("3d f S", "3s m C")] + [("2p m S", "3d f C")] + [("3p m S", "2d f C")])
        self.add_xross_perm_variation(
                                [("1s m G", "2s f G")] + [("3s m G", "2s m V")] + [("1s m V", "1s f G")] + [
                                    ("2s f V", "1s f V")] + [("3s f V", "3s m V")] + [("1d m G", "1p f V")] + [
                                    ("2d m G", "1p m G")] + [("3d m G", "2s m G")] + [("3d f G", "2p m V")] + [
                                    ("1p m V", "2p m G")] + [("2p f V", "2d f G")] + [("3p m S", "3p m G")] + [
                                    ("3p f S", "3p f G")] + [("1p f G", "2p f G")] + [("1d f S", "3d m V")] + [
                                    ("2d m C", "1d f G")] + [("2d f S", "3s f G")] + [("3d f C", "1d m V")] + [
                                    ("3p m V", "3p m C")] + [("3p f V", "3p f C")] + [("1p f S", "2p f S")] + [
                                    ("1d f V", "3d m C")] + [("2d m V", "1d f C")] + [("2d f V", "3s f S")] + [
                                    ("3d f V", "1d m S")])
        self.add_xross_perm_variation( [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [
            ("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "1s f " + PC) for PC in
                                                                        self.TENSES_CASES_PC] + [
                                    ("1d m " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3d m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + SC, "1s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2s m " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3s m " + SC, "2s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d m " + SC, "3d m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d m " + SC, "2d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3d f " + SC, "1d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1p m " + SC, "3p m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1p f " + SC, "2p f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC])
        self.add_xross_perm_variation(
                                [("2s m G", "1p f G")] + [("2s f S", "1s m G")] + [("2d m S", "1p m V")] + [
                                    ("2d f S", "3d f G")] + [("2p m S", "1s m V")] + [("2p f S", "3d m G")] + [
                                    ("2s m C", "3d f V")] + [("2s f C", "1d m G")] + [("2d m C", "3p m V")] + [
                                    ("2d f C", "3s f G")] + [("2p m C", "3d m V")] + [("2p f V", "3p m G")] + [
                                    ("3s m G", "1d m V")] + [("1p m G", "3s f V")] + [("3p f G", "1p f V")] + [
                                    ("3s m V", "1d f G")] + [("1d f V", "1s f V")] + [("3p f V", "1s f G")] + [
                                    ("2s f G", "2p f G")] + [("2d m G", "2d m V")] + [("2d f G", "2s m V")] + [
                                    ("2p m G", "2s f V")] + [("2d f V", "2p m V")])
        self.add_xross_perm_variation(
                                [("1s m G", "2d f V")] + [("1s f G", "3d m V")] + [("1d m G", "3p m G")] + [
                                    ("1d f G", "2p f G")] + [("1p m G", "1s f V")] + [("1p f G", "3d f V")] + [
                                    ("1s m V", "2s f V")] + [("1d m V", "2p f V")] + [("1d f V", "2d m G")] + [
                                    ("1p m V", "3p f G")] + [("1p f V", "3s m V")] + [("3s f G", "2d f G")] + [
                                    ("2d f C", "2d m V")] + [("1p f S", "3s f V")] + [("1s m S", "2p m V")] + [
                                    ("1d f S", "3p m V")] + [("3d f S", "2p m G")] + [("1d m S", "3p f V")] + [
                                    ("3d m C", "2s f G")] + [("1p m C", "2s m V")] + [("2s m C", "3s m G")] + [
                                    ("3s f S", "3d f G")] + [("1d f C", "3d m G")] + [("1s f S", "2s m G")] + [
                                    ("3p m S", "2p f S")] + [("1p m S", "1s f C")] + [("2d f S", "3d f C")] + [
                                    ("1s m C", "2s f C")] + [("1d m C", "2p f C")] + [("2d m S", "3p f S")] + [
                                    ("1p f C", "3s m C")] + [("3d m S", "2d m C")] + [("3s m S", "2p m C")] + [
                                    ("3s f C", "2s m S")] + [("3p m C", "2p m S")] + [("3p f C", "2s f S")])
        self.add_xross_perm_variation(
                                [("1s f G", "2p m V")] + [("3s m G", "1p m V")] + [("3s f G", "1d m V")] + [
                                    ("2d f G", "2p f V")] + [("3d m G", "3d m V")] + [("1p m G", "3p m V")] + [
                                    ("1p f G", "1p f V")] + [("2s m G", "3d f V")] + [("1s m " + SC, "2s f " + SC) for
                                                                                      SC in self.TENSES_CASES_SC] + [
                                    ("1s f " + SC, "2d f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("1d f " + SC, "2s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2d m " + SC, "3s f " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("3p f " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC] + [
                                    ("2s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1d f " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("1s m " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC] + [
                                    ("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])
        self.add_xross_perm_variation(
                                [("1s f G", "3p f V")] + [("1d m G", "1s m G")] + [("1d f G", "2s f V")] + [
                                    ("1p m G", "2s f G")] + [("1p f G", "3p f G")] + [("1s m V", "3d m G")] + [
                                    ("1s f V", "2d f G")] + [("1d m V", "3d m V")] + [("1d f V", "2s m G")] + [
                                    ("1p m V", "2d m G")] + [("1p f V", "2d f V")] + [("3s f V", "3s m G")] + [
                                    ("2p m G", "3d f V")] + [("2p f G", "3p m G")] + [("2s m V", "3d f G")] + [
                                    ("2d m V", "3p m V")] + [("2p m V", "3s m V")] + [("2p f V", "3s f G")] + [
                                    ("1s f S", "2p m C")] + [("3s m S", "1p m C")] + [("3s f S", "1d m C")] + [
                                    ("2d f S", "2p f C")] + [("3d m S", "3d m C")] + [("1p m S", "3p m C")] + [
                                    ("1p f S", "1p f C")] + [("2s m S", "3d f C")])
        self.add_xross_perm_variation(
                                [("1s m G", "2d m V")] + [("1s f G", "3s f V")] + [("3p m G", "2s f G")] + [
                                    ("3p f G", "1d f G")] + [("2s m G", "3s m V")] + [("3d m V", "3p m V")] + [
                                    ("3d f V", "1d m V")] + [("1d m G", "2d f V")] + [("1p f V", "2p f V")] + [
                                    ("2p m V", "1p m V")] + [("3s m G", "1s f V")] + [("3s f G", "3p f V")] + [
                                    ("1d f V", "3d f G")] + [("3d m G", "2s m V")] + [("1p f G", "1s m V")] + [
                                    ("2d m G", "2s f V")] + [("2d f G", "2p f G")] + [("1p m G", "2p m G")] + [
                                    ("1s m S", "2s f S")] + [("3s m S", "2s m C")] + [("1s m C", "1s f S")] + [
                                    ("2s f C", "1s f C")] + [("3s f C", "3s m C")] + [("1d m S", "1p f C")] + [
                                    ("2d m S", "1p m S")] + [("3d m S", "2s m S")] + [("3d f S", "2p m C")] + [
                                    ("1p m C", "2p m S")] + [("2p f C", "2d f S")])
        self.add_xross_perm_variation(
                                [("1s m G", "3p f G")] + [("1s f G", "3d f V")] + [("1d m G", "3s f G")] + [
                                    ("1d f G", "2p m G")] + [("1p m G", "3s m V")] + [("1p f G", "2d m G")] + [
                                    ("2s m G", "3d f G")] + [("2s f G", "2p f G")] + [("3s m G", "3p m V")] + [
                                    ("3d m G", "2d f G")] + [("3p m G", "3d m V")] + [("1s m V", "1p m V")] + [
                                    ("1s f V", "2d m V")] + [("2s m V", "2p f V")] + [("2s f V", "3p f V")] + [
                                    ("2d f V", "1d f V")] + [("2p m V", "1p f V")] + [("3s f V", "1d m V")] + [
                                    ("1s f S", "2p m C")] + [("3s m S", "1p m C")] + [("3s f S", "1d m C")] + [
                                    ("2d f S", "2p f C")] + [("3d m S", "3d m C")] + [("1p m S", "3p m C")] + [
                                    ("1p f S", "1p f C")] + [("2s m S", "3d f C")])
        self.add_xross_perm_variation(
                                [("1s m G", "2s f G")] + [("1d m G", "1d f V")] + [("1d f G", "1d m V")] + [
                                    ("1p m G", "2p f V")] + [("1p f G", "1s f V")] + [("2s m G", "2p f G")] + [
                                    ("2d m G", "1p m V")] + [("2d f G", "3p f V")] + [("2p m G", "3d f V")] + [
                                    ("2s m V", "3p m V")] + [("2s f V", "3p f G")] + [("2d m V", "1s m V")] + [
                                    ("2d f V", "3s f V")] + [("3s m G", "2p m V")] + [("3d m G", "1s f G")] + [
                                    ("3d f G", "3p m G")] + [("3s m V", "3s f G")] + [("3d m V", "1p f V")] + [
                                    ("1s m S", "3p f S")] + [("1s f S", "3d f C")] + [("1d m S", "3s f S")] + [
                                    ("1d f S", "2p m S")] + [("1p m S", "3s m C")] + [("1p f S", "2d m S")] + [
                                    ("2s m S", "3d f S")] + [("2s f S", "2p f S")] + [("3s m S", "3p m C")] + [
                                    ("3d m S", "2d f S")] + [("3p m S", "3d m C")] + [("1s m C", "1p m C")] + [
                                    ("1s f C", "2d m C")] + [("2s m C", "2p f C")] + [("2s f C", "3p f C")] + [
                                    ("2d f C", "1d f C")] + [("2p m C", "1p f C")] + [("3s f C", "1d m C")])

        # full swap 1
        old_list = [
            ("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
             "3p g " + T) for T in self.TENSES_CASES]
        new_list = [
            ("2s g " + T, "3p g " + T, "3d g " + T, "3s g " + T, "1p g " + T, "1d g " + T, "1s g " + T, "2p g " + T,
             "2d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

        # full swap 2
        old_list = [
            ("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
             "3p g " + T) for T in self.TENSES_CASES]
        new_list = [
            ("2s g " + T, "1s g " + T, "3s g " + T, "2d g " + T, "1p g " + T, "3p g " + T, "2p g " + T, "1d g " + T,
             "3d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

    def _create_syncretic_GEN_files(self):
        """syncretic variations that happened historically (gender syncretism)"""
        # syn: 2V:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f V", "2a m V")])

        # syn: p:f -> m (TRUE)
        self.add_gen_sync_variation( [("zp" + " f " + T, "zp" + " m " + T) for T in self.TENSES_CASES])

        # V3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f V", "3p m V")])

        # Gp: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f " + PC, "zp m " + PC) for PC in self.TENSES_CASES_PC])

        # 3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f " + T, "3p m " + T) for T in self.TENSES_CASES])

        # syn: 2:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES])

        # syn G3d: f -> m (TRUE)
        self.add_gen_sync_variation( [("3d f " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC])

        # syn V2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f V", "2s m V")])

        # syn G2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + PC, "2a m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn 2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES])

        # syn Vp: f -> m
        self.add_gen_sync_variation( [("zp f V", "zp m V")])

        # syn p: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f " + T, "zp m " + T) for T in self.TENSES_CASES])

        # syn V1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f V", "1s m V")])

        # syn G3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f G", "3s m G")])

        # syn G2p: f->m (TRUE)
        self.add_gen_sync_variation( [("2p f " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn s/d: f->m (FALSE)
        self.add_gen_sync_variation(
                                [("zs f " + T, "zs m " + T) for T in self.TENSES_CASES] + [("zd f " + T, "zd m " + T) for T
                                                                                           in self.TENSES_CASES])

        # syn 3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # syn s: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f " + T, "zs m " + T) for T in self.TENSES_CASES])

        # syn 2s: f->m, 3s: f->m (FALSE)
        self.add_gen_sync_variation(
                                [("2s f " + T, "2s m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3s m " + T) for T
                                                                                           in self.TENSES_CASES])

        # 2d
        self.add_gen_sync_variation( [("2d f " + T, "2d m " + T) for T in self.TENSES_CASES])

        # Gd
        self.add_gen_sync_variation( [("zd f " + PC, "zd m " + PC) for PC in self.TENSES_CASES_PC])

        # 2s
        self.add_gen_sync_variation( [("2s f " + T, "2s m " + T) for T in self.TENSES_CASES])

        # 2
        self.add_gen_sync_variation( [("2a f " + T, "2a f " + T) for T in self.TENSES_CASES])

        # V2p
        self.add_gen_sync_variation( [("2p f V", "2p m V")])

        # dG, dV2
        self.add_gen_sync_variation(
                                [("zd f " + PC, "zd m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f V", "2d m V")])

        # alle
        self.add_gen_sync_variation( [("za f " + T, "za m " + T) for T in self.TENSES_CASES])

        # G2, G3p
        self.add_gen_sync_variation(
                                [("2a f " + PC, "2a m " + PC) for PC in self.TENSES_CASES_PC] + [("3p f " + PC, "3p m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # 3d
        self.add_gen_sync_variation( [("3d f " + T, "3d m " + T) for T in self.TENSES_CASES])

        # G2, G3d/p
        self.add_gen_sync_variation(
                                [("2a f " + PC, "2a m " + PC) for PC in self.TENSES_CASES_PC] + [("3d f " + PC, "3d m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC] + [
                                    ("3p f " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # V2d/p
        self.add_gen_sync_variation( [("2d f V", "2d m V")] + [("2p f V", "2p m V")])

        # 2, 3d/p
        self.add_gen_sync_variation(
                                [("2a f " + T, "2a m " + T) for T in self.TENSES_CASES] + [("3d f " + T, "3d m " + T) for T
                                                                                           in self.TENSES_CASES] + [
                                    ("3p f " + T, "3p m " + T) for T in self.TENSES_CASES])

        # 3p/d
        self.add_gen_sync_variation(
                                [("3d f " + T, "3d m " + T) for T in self.TENSES_CASES] + [("3p f " + T, "3p m " + T) for T
                                                                                           in self.TENSES_CASES])

        # Vp/d3
        self.add_gen_sync_variation( [("3p f V", "3p m V")] + [("3d f V", "3d m V")])

        # Gp/d
        self.add_gen_sync_variation(
                                [("zd f " + PC, "zd m " + PC) for PC in self.TENSES_CASES_PC] + [("zp f " + PC, "zp m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # syn V3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m V", "3a f V")])

        # syn Vs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f V", "zs m V")])

        # syn G3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m " + PC, "3a f G") for PC in self.TENSES_CASES_PC])

        # syn Gs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f G", "zs m G")])

        # 3s; 2p
        self.add_gen_sync_variation(
                                [("2p f " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3s m " + T) for T
                                                                                           in self.TENSES_CASES])

        # V2p, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V")] + [("3s f G", "3s m G")])

        # 3s; 2p/d
        self.add_gen_sync_variation(
                                [("2p f " + T, "2p m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2d m " + T) for T
                                                                                           in self.TENSES_CASES] + [
                                    ("3s f " + T, "3s m " + T) for T in self.TENSES_CASES])

        # V2p/d, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V")] + [("2d f V", "2d m V")] + [("3s f G", "3s m G")])

        # syn: 2C:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f C", "2a m C")])

        # C3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f C", "3p m C")])

        # syn C2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f C", "2s m C")])

        # syn Cp: f -> m
        self.add_gen_sync_variation( [("zp f C", "zp m C")])

        # syn C1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f C", "1s m C")])

        # C2p
        self.add_gen_sync_variation( [("2p f C", "2p m C")])

        # dG, dC2
        self.add_gen_sync_variation( [("zd f G", "zd m G")] + [("2d f C", "2d m C")])

        # C2d/p
        self.add_gen_sync_variation( [("2d f C", "2d m C")] + [("2p f C", "2p m C")])

        # Cp/d3
        self.add_gen_sync_variation( [("3p f C", "3p m C")] + [("3d f C", "3d m C")])

        # syn: 2V/C:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f " + SC, "2a m " + SC) for SC in self.TENSES_CASES_SC])

        # V/C3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f " + SC, "3p m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/C2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f " + SC, "2s m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/Cp: f -> m
        self.add_gen_sync_variation( [("zp f " + SC, "zp m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/C1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC])

        # V/C2p
        self.add_gen_sync_variation( [("2p f " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC])

        # dG, dV/C2
        self.add_gen_sync_variation( [("zd f " + PC, "zd m " + PC) for PC in self.TENSES_CASES_PC] +
                                [("2d f " + SC, "2d m " + SC) for SC in self.TENSES_CASES_SC])

        # V/C2d/p
        self.add_gen_sync_variation(
                                [("2d f " + SC, "2d m " + SC) for SC in self.TENSES_CASES_SC] + [("2p f " + SC, "2p m " + SC)
                                                                                             for SC in self.TENSES_CASES_SC])

        # V/Cp/d3
        self.add_gen_sync_variation(
                                [("3p f " + SC, "3p m " + SC) for SC in self.TENSES_CASES_SC] + [("3d f " + SC, "3d m " + SC)
                                                                                             for SC in self.TENSES_CASES_SC])

        # syn G/S3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])

        # syn C3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m C", "3a f C")])

        # syn V3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m " + SC, "3a f " + SC) for SC in self.TENSES_CASES_SC])

        # syn Cs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f C", "zs m C")])

        # syn Vs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f " + SC, "zs m " + SC) for SC in self.TENSES_CASES_SC])

        # syn G/S3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m " + PC, "3a f " + PC) for PC in self.TENSES_CASES_PC])

        # syn G/Ss: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f " + PC, "zs m " + PC) for PC in self.TENSES_CASES_PC])

        # V2p, G/S3s
        self.add_gen_sync_variation( [("2p f " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] +
                                [("3s f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])

        # V2p, G/S3s
        self.add_gen_sync_variation( [("2p f C", "2p m C")] +
                                [("3s f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])

        # V2p/d, G/S3s
        self.add_gen_sync_variation(
                                [("2p f " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] + [("2d f " + SC, "2d m " + SC)
                                                                                             for SC in self.TENSES_CASES_SC] +
                                [("3s f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])

        # V2p/d, G/S3s
        self.add_gen_sync_variation( [("2p f C", "2p m C")] + [("2d f C", "2d m C")] +
                                [("3s f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])


    def _create_syncretic_PERS_files(self):
        """syncretic variations that happened historically (other than Gender)"""
        # syn Vsm: 2 -> 1
        self.add_pers_sync_variation( [("2s m V", "1s m V")])

        # syn Vsf: 2 -> 1
        self.add_pers_sync_variation( [("2s f V", "1s f V")])

        # syn Vdm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V")])

        # syn Vdm: 2->1; Vsm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V")] + [("2s m V", "1s m V")])

        # Vd: 2->1
        self.add_pers_sync_variation( [("2d g V", "1d g V")])

        # syn 1 -> 2
        self.add_pers_sync_variation( [("1a g " + T, "2a g " + T) for T in self.TENSES_CASES])

        # syn 2 -> 3
        self.add_pers_sync_variation( [("2a g " + T, "3a g " + T) for T in self.TENSES_CASES])

        # syn 3 -> 1
        self.add_pers_sync_variation( [("3a g " + T, "1a g " + T) for T in self.TENSES_CASES])

        # syn f:3->2
        self.add_pers_sync_variation( [("3a f " + T, "2a f " + T) for T in self.TENSES_CASES])

        # syn fp:3->2
        self.add_pers_sync_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # syn p:  2->1,3->1
        self.add_pers_sync_variation(
                                [("2p g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1p g " + T) for T
                                                                                           in self.TENSES_CASES])

        # syn s:2->3
        self.add_pers_sync_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # syn s:1->2
        self.add_pers_sync_variation( [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES])

        # syn p:2->3
        self.add_pers_sync_variation( [("2p g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # syn Vp:3->2
        self.add_pers_sync_variation( [("3p g V", "2p g V")])

        # Gp: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G")])

        # Vs: 2->1
        self.add_pers_sync_variation( [("2s g V", "1s g V")])

        # Gpf: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G")])

        # G:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f G", "2p f G")] + [("3d f G", "2d f G")])

        # G: d/p: 3->2
        self.add_pers_sync_variation( [("3p g G", "2p g G")] + [("3d g G", "2d g G")])

        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")] + [("3a g G", "1a g G")])

        # mp:3->2, fp:3->1
        self.add_pers_sync_variation(
                                [("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3p f " + T, "1p f " + T) for T
                                                                                           in self.TENSES_CASES])

        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")] + [("2a f G", "1a f G")])

        # G/Sp: 3->2
        self.add_pers_sync_variation( [("3p g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # G/Spf: 3->2
        self.add_pers_sync_variation( [("3p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC])

        # G/S:p/d:f: 3->2
        self.add_pers_sync_variation(
                                [("3p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3d f " + PC, "2d f " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # G/S: d/p: 3->2
        self.add_pers_sync_variation(
                                [("3p g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [("3d g " + PC, "2d g " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # syn Csm: 2 -> 1
        self.add_pers_sync_variation( [("2s m C", "1s m C")])

        # syn Csf: 2 -> 1
        self.add_pers_sync_variation( [("2s f C", "1s f C")])

        # syn Cdm: 2->1
        self.add_pers_sync_variation( [("2d m C", "1d m C")])

        # syn Cdm: 2->1; Csm: 2->1
        self.add_pers_sync_variation( [("2d m C", "1d m C")] + [("2s m C", "1s m C")])

        # Cd: 2->1
        self.add_pers_sync_variation( [("2d g C", "1d g C")])

        # Cs: 2->1
        self.add_pers_sync_variation( [("2s g C", "1s g C")])

        ######

        # syn V/Csm: 2 -> 1
        self.add_pers_sync_variation( [("2s m " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/Csf: 2 -> 1
        self.add_pers_sync_variation( [("2s f " + SC, "1s f " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/Cdm: 2->1
        self.add_pers_sync_variation( [("2d m " + SC, "1d m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V/Cdm: 2->1; Vsm: 2->1
        self.add_pers_sync_variation(
                                [("2d m " + SC, "1d m " + SC) for SC in self.TENSES_CASES_SC] + [("2s m " + SC, "1s m " + SC)
                                                                                             for SC in self.TENSES_CASES_SC])

        # V/Cd: 2->1
        self.add_pers_sync_variation( [("2d g " + SC, "1d g " + SC) for SC in self.TENSES_CASES_SC])

        # V/Cs: 2->1
        self.add_pers_sync_variation( [("2s g " + SC, "1s g " + SC) for SC in self.TENSES_CASES_SC])

        # syn Cp:3->2
        self.add_pers_sync_variation( [("3p g C", "2p g C")])

        # C: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g C", "3a g C")] +
                                [("3a g " + PC, "1a g " + PC) for PC in self.TENSES_CASES_PC])

        # Cm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m C", "3a m C")] +
                                [("2a f " + PC, "1a f " + PC) for PC in self.TENSES_CASES_PC])

        # syn Vp:3->2
        self.add_pers_sync_variation( [("3p g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC])

        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g " + SC, "3a g " + SC) for SC in self.TENSES_CASES_SC] +
                                [("3a g " + PC, "1a g " + PC) for PC in self.TENSES_CASES_PC])

        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m " + SC, "3a m " + SC) for SC in self.TENSES_CASES_SC] +
                                [("2a f " + PC, "1a f " + PC) for PC in self.TENSES_CASES_PC])


    def _create_syncretic_NUM_files(self):
        # syn: d -> p
        self.add_num_sync_variation( [("zd" + " g " + T, "zp" + " g " + T) for T in self.TENSES_CASES])

        # 1: d -> p
        self.add_num_sync_variation( [("1d" + " g " + T, "1p" + " g " + T) for T in self.TENSES_CASES])

        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m V", "3s m V")])

        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g V", "1p g V")])

        # syn G1: s->p
        self.add_num_sync_variation( [("1s g G", "1p g G")])

        # 3m: p->s
        self.add_num_sync_variation( [("3p m " + T, "3s m " + T) for T in self.TENSES_CASES])

        #
        self.add_num_sync_variation( [("zp g " + T, "zd g " + T) for T in self.TENSES_CASES])

        # syn s->p
        self.add_num_sync_variation( [("zs g " + T, "zp g " + T) for T in self.TENSES_CASES])

        # syn s->d
        self.add_num_sync_variation( [("zs g " + T, "zd g " + T) for T in self.TENSES_CASES])

        # syn 3: d-> p
        self.add_num_sync_variation( [("3d g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 2: d->p
        self.add_num_sync_variation( [("2d g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # G1: s/d->p
        self.add_num_sync_variation( [("1d g G", "1p g G")] + [("1s g G", "1p g G")])

        # V3f: s->p
        self.add_num_sync_variation( [("3s f V", "3p f V")])

        # 3m: d->s
        self.add_num_sync_variation( [("3d m " + T, "3s m " + T) for T in self.TENSES_CASES])

        # V3: d->s
        self.add_num_sync_variation( [("3d g V", "3s g V")])

        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")] + [("zd g G", "zs g G")])

        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V")] + [("3s g G", "3p g G")])

        # 2:d->p, 3:d->s
        self.add_num_sync_variation(
                                [("2d g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3d g " + T, "3s g " + T) for T
                                                                                           in self.TENSES_CASES])

        # 1:d->s, 2:p->s
        self.add_num_sync_variation(
                                [("1d g " + T, "1s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "2s g " + T) for T
                                                                                           in self.TENSES_CASES])

        # m: p->s
        self.add_num_sync_variation( [("zp m " + T, "zs m " + T) for T in self.TENSES_CASES])

        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V")] + [("3s f G", "3d f G")])

        # f: p->s
        self.add_num_sync_variation( [("zp f " + T, "zs f " + T) for T in self.TENSES_CASES])

        # f: p/d->s
        self.add_num_sync_variation(
                                [("zp f " + T, "zs f " + T) for T in self.TENSES_CASES] + [("zd f " + T, "zs f " + T) for T
                                                                                           in self.TENSES_CASES])

        # m: p/d->s
        self.add_num_sync_variation(
                                [("zp m " + T, "zs m " + T) for T in self.TENSES_CASES] + [("zd m " + T, "zs m " + T) for T
                                                                                           in self.TENSES_CASES])

        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m G", "zs m G")] + [("zd m G", "zs m G")] + [("zp f V", "zs f V")] + [
            ("zd f V", "zs f V")])

        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")] + [("zd m G", "zp m G")])

        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g G", "3p g G")] + [("zp f V", "zd f V")])

        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m C", "3s m C")])

        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g C", "1p g C")])

        # syn G1: s->p
        self.add_num_sync_variation( [("1s g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC])

        # G1: s/d->p
        self.add_num_sync_variation(
                                [("1d g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("1s g " + PC, "1p g " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # V3f: s->p
        self.add_num_sync_variation( [("3s f C", "3p f C")])

        # V3: d->s
        self.add_num_sync_variation( [("3d g C", "3s g C")])

        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC])

        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g " + SC, "1p g " + SC) for SC in self.TENSES_CASES_SC])

        # V3f: s->p
        self.add_num_sync_variation( [("3s f " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC])

        # V3: d->s
        self.add_num_sync_variation( [("3d g " + SC, "3s g " + SC) for SC in self.TENSES_CASES_SC])

        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g C", "zp g C")] +
                                [("zd g " + PC, "zs g " + PC) for PC in self.TENSES_CASES_PC])

        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g C", "2p g C")] +
                                [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC])

        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m C", "2p m C")] +
                                [("3s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC])

        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation(
                                [("zp m " + PC, "zs m " + PC) for PC in self.TENSES_CASES_PC] + [("zd m " + PC, "zs m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC] + [
                                    ("zp f C", "zs f C")] + [("zd f C", "zs f C")])

        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g C", "2p g C")] +
                                [("zd m " + PC, "zp m " + PC) for PC in self.TENSES_CASES_PC])

        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] +
                                [("zp f C", "zd f C")])

        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g " + SC, "zp g " + SC) for SC in self.TENSES_CASES_SC] +
                                [("zd g " + PC, "zs g " + PC) for PC in self.TENSES_CASES_PC])

        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC] +
                                [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC])

        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m " + SC, "2p m " + SC) for SC in self.TENSES_CASES_SC] +
                                [("3s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC])

        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation(
                                [("zp m " + PC, "zs m " + PC) for PC in self.TENSES_CASES_PC] + [("zd m " + PC, "zs m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC] +
                                [("zp f " + SC, "zs f " + SC) for SC in self.TENSES_CASES_SC] + [("zd f " + SC, "zs f " + SC)
                                                                                             for SC in self.TENSES_CASES_SC])

        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g " + SC, "2p g " + SC) for SC in self.TENSES_CASES_SC] +
                                [("zd m " + PC, "zp m " + PC) for PC in self.TENSES_CASES_PC])

        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] +
                                [("zp f " + SC, "zd f " + SC) for SC in self.TENSES_CASES_SC])


    def _create_syncretic_X_files(self):
        # syn G3sf -> G2sm
        self.add_xross_sync_variation( [("3s f " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G3sm -> G1pm
        self.add_xross_sync_variation( [("3s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn V3p -> V3sm,  V3d->V3sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")] + [("3d g V", "3s m V")])

        # syn G3:d->pf
        self.add_xross_sync_variation( [("3d g " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # syn V3:dm->pf
        self.add_xross_sync_variation( [("3d m V", "3p f V")])

        # syn V3:p->sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")])

        # syn Gd: 3f->2m
        self.add_xross_sync_variation( [("3d f " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G2sf -> G3pm
        self.add_xross_sync_variation( [("2s f " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G3pf -> G2pm
        self.add_xross_sync_variation( [("3p f " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G2sm -> G1pm
        self.add_xross_sync_variation( [("2s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC])

        # syn G2p -> G2sf; G2d -> G2sf
        self.add_xross_sync_variation(
                                [("2p g " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d g " + PC, "2d f " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # syn G3p ->  G1sm
        self.add_xross_sync_variation( [("3p g " + PC, "1s m " + PC) for PC in self.TENSES_CASES_PC])

        # G: s/d: 3f -> 2m
        self.add_xross_sync_variation(
                                [("3d f " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "2s m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # s: 3f -> 2m
        self.add_xross_sync_variation( [("3s f " + T, "2s m " + T) for T in self.TENSES_CASES])

        # Vs: 2f -> 1(m)
        self.add_xross_sync_variation( [("2s f V", "1s m V")])

        # G: 3sf -> 2sm, 2pm -> 2sm
        self.add_xross_sync_variation( [("3s f " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC])

        # Vs: 2m->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])

        # Vs: 2m->1, 3f->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])

        # 3: d->pm
        self.add_xross_sync_variation( [("3d g " + T, "3p m " + T) for T in self.TENSES_CASES])

        # G2:pf->sm
        self.add_xross_sync_variation( [("2p f " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC])

        # G2:p/df->sm
        self.add_xross_sync_variation(
                                [("2p f " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f " + PC, "2s m " + PC)
                                                                                             for PC in self.TENSES_CASES_PC])

        # G: 2pf->3sm
        self.add_xross_sync_variation( [("2p f " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC])

        # V3:pf->sm
        self.add_xross_sync_variation( [("3p f V", "3s m V")])

        # G:3pf->2sf
        self.add_xross_sync_variation( [("3p f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC])

        # syn V3p -> V3sm,  V3d->V3sm
        self.add_xross_sync_variation(
                                [("3p g " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC] + [("3d g " + SC, "3s m " + SC)
                                                                                             for SC in self.TENSES_CASES_SC])

        # syn V3:dm->pf
        self.add_xross_sync_variation( [("3d m " + SC, "3p f " + SC) for SC in self.TENSES_CASES_SC])

        # syn V3:p->sm
        self.add_xross_sync_variation( [("3p g " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC])

        # Vs: 2f -> 1(m)
        self.add_xross_sync_variation( [("2s f " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC])

        # Vs: 2m->1
        self.add_xross_sync_variation( [("2s m " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC])

        # Vs: 2m->1, 3f->1
        self.add_xross_sync_variation( [("2s m " + SC, "1s m " + SC) for SC in self.TENSES_CASES_SC])

        # V3:pf->sm
        self.add_xross_sync_variation( [("3p f " + SC, "3s m " + SC) for SC in self.TENSES_CASES_SC])

        # pG -> sC
        self.add_xross_sync_variation( [("zp g G", "zs g C")])

        # 2C -> 2S
        self.add_xross_sync_variation( [("2a g C", "2a g S")])

        # 3pG -> 2sC; 3pV -> 1sC
        self.add_xross_sync_variation( [("3p g G", "2s g C")] + [("3p g V", "1s g C")])

        # pC -> sS; sC -> dG
        self.add_xross_sync_variation( [("zp g C", "zs g S")] + [("zs g C", "zd g G")])

        # G:2p -> 1s
        self.add_xross_sync_variation( [("2p g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC])

        # G:3p -> 2s
        self.add_xross_sync_variation( [("3p g " + PC, "2s g " + PC) for PC in self.TENSES_CASES_PC])

        # G:3p -> 3d
        self.add_xross_sync_variation( [("3p g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # G3p -> S2d
        self.add_xross_sync_variation( [("3p g G", "2d g S")])

        # G3p -> S3p, S3s -> G2s
        self.add_xross_sync_variation( [("3p g G", "3p g S")] + [("3s g S", "2s g G")])


    def _create_syncretic_TENSE_files(self):
        # syn p: G -> V
        self.add_ten_sync_variation( [("zp g G", "zp g V")])

        # syn s: G -> V
        self.add_ten_sync_variation( [("zs g G", "zs g V")])

        # syn 2: G -> V
        self.add_ten_sync_variation( [("2a g G", "2a g V")])

        # syn 3: G -> V
        self.add_ten_sync_variation( [("3a g G", "3a g V")])

        # syn p: V -> G
        self.add_ten_sync_variation( [("zp g V", "zp g G")])

        # syn s: V -> G
        self.add_ten_sync_variation( [("zs g V", "zs g G")])

        # syn 2: V -> G
        self.add_ten_sync_variation( [("2a g V", "2a g G")])

        # syn 3: V -> G
        self.add_ten_sync_variation( [("3a g V", "3a g G")])

        # syn 3p: V -> G,  2s: G -> V
        self.add_ten_sync_variation( [("3p g V", "3p g G")] + [("2s g G", "2s g V")])

        # syn 2: V -> G,  p: G -> V
        self.add_ten_sync_variation( [("2a g V", "3a g G")] + [("zp g G", "zp g V")])

        # syn p: G -> C
        self.add_ten_sync_variation( [("zp g G", "zp g C")])

        # syn s: G -> C
        self.add_ten_sync_variation( [("zs g G", "zs g C")])

        # syn 2: G -> C
        self.add_ten_sync_variation( [("2a g G", "2a g C")])

        # syn 3: G -> C
        self.add_ten_sync_variation( [("3a g G", "3a g C")])

        # syn p: C -> G
        self.add_ten_sync_variation( [("zp g C", "zp g G")])

        # syn s: C -> G
        self.add_ten_sync_variation( [("zs g C", "zs g G")])

        # syn 2: C -> G
        self.add_ten_sync_variation( [("2a g C", "2a g G")])

        # syn 3: C -> G
        self.add_ten_sync_variation( [("3a g C", "3a g G")])

        # syn 3p: C -> G,  2s: G -> C
        self.add_ten_sync_variation( [("3p g C", "3p g G")] + [("2s g G", "2s g C")])

        # syn 2: C -> G,  p: G -> C
        self.add_ten_sync_variation( [("2a g C", "3a g G")] + [("zp g G", "zp g C")])

        # syn p: V -> C
        self.add_ten_sync_variation( [("zp g V", "zp g C")])

        # syn s: C -> V
        self.add_ten_sync_variation( [("zs g C", "zs g V")])

        # syn 2: V -> C
        self.add_ten_sync_variation( [("2a g V", "2a g C")])

        # syn 3: C -> V
        self.add_ten_sync_variation( [("3a g C", "3a g V")])

        # syn 3p: C -> V,  2s: G -> S
        self.add_ten_sync_variation( [("3p g C", "3p g V")] + [("2s g G", "2s g S")])

        # syn 2: V -> C,  p: S -> G
        self.add_ten_sync_variation( [("2a g V", "3a g C")] + [("zp g S", "zp g G")])

        # syn 3p: C -> S,  2s: G -> S
        self.add_ten_sync_variation( [("3p g C", "3p g S")] + [("2s g G", "2s g S")])

        # syn 2: G -> V,  p: S -> V
        self.add_ten_sync_variation( [("2a g G", "3a g V")] + [("zp g S", "zp g V")])

        # 3p: G -> S
        self.add_ten_sync_variation( [("3p g G", "3p g S")])

        # 2s: S -> G
        self.add_ten_sync_variation( [("2s g S", "2s g G")])


class PermSynCreatorAKK(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "AKK"

        self.TENSES_CASES = ["G","V","S","J"]
        self.TENSES_CASES_PC = ["G", "S","J"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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
        self._create_syncretic_GEN_files()
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

    def _create_permutation_NUM_files(self):
        """
            creates all permutation files where NUM-features are swapped (s <-> d <-> p)
            """

        # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p
        self.add_num_perm_variation( [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2f: s <-> p, 3m: s <-> p
        self.add_num_perm_variation( [("2s f " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3p m " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p, 3f: d <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "3d f " + T) for T in self.TENSES_CASES])

        # 1m: s <-> p
        self.add_num_perm_variation( [("1s m " + T, "1p m " + T) for T in self.TENSES_CASES])

        # 1m: s <-> d, 2f: d <-> p
        self.add_num_perm_variation( [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES] + [("2d f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: s <-> d, 3: d <-> p
        self.add_num_perm_variation( [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T) for T in self.TENSES_CASES])

        # 2G: s <-> p
        self.add_num_perm_variation( [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [("3d g V", "3p g V")])

        # 3G:s<->p, 2V:d<->p, 1m: s<->d
        self.add_num_perm_variation( [("3s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g V", "2p g V")] +
                                [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])

        # 1f: s <-> p
        self.add_num_perm_variation( [("1s f " + T, "1p f " + T) for T in self.TENSES_CASES])

        # 2f: s <-> d, 3m: s <-> d
        self.add_num_perm_variation( [("2s f " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d m " + T) for T in self.TENSES_CASES])

        # 2m: s <-> d, 1f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "1d f " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p, 1m: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])

        # 1V: s <-> d, 3G: s <-> d
        self.add_num_perm_variation( [("1s g V", "1d g V")] + [("3s g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # 1G: s <-> d, 2: d <-> p
        self.add_num_perm_variation( [("1s g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # 2m: s <-> p
        self.add_num_perm_variation( [("2s m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # 3f: s <-> p
        self.add_num_perm_variation( [("3s f " + T, "3p f " + T) for T in self.TENSES_CASES])

        # 1: s <-> p, 2: d <-> p
        self.add_num_perm_variation( [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2V: s <-> p, 3mV: s <-> p
        self.add_num_perm_variation( [("2s g V", "2p g V")] + [("3s m V", "3p m V")])

        # 2fV: s <-> p
        self.add_num_perm_variation( [("2s f V", "2p f V")])

        # 2Vf: s <-> p, 3Gm: s <-> p
        self.add_num_perm_variation( [("2s f V", "2p f V")] + [("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # 2m: s <-> d, 3f: s <-> d
        self.add_num_perm_variation( [("2s m " + T, "2d m " + T) for T in self.TENSES_CASES])

        # 3mG: s <-> p
        self.add_num_perm_variation( [("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # f: s -> d -> p;   m: p -> d -> s
        self.add_num_perm_variation( rotate_left_list=[("zs m " + T, "zd m " + T, "zp m " + T) for T in self.TENSES_CASES], rotate_right_list=[("zs f " + T, "zd f " + T, "zp f " + T) for T in self.TENSES_CASES])

        # f: s <-> p,   m: d <-> p
        self.add_num_perm_variation( [("zs f " + T, "zp f " + T) for T in self.TENSES_CASES] + [("zd m " + T, "zp m " + T) for T in self.TENSES_CASES])

        # strong permutation 1
        self.add_num_perm_variation( [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [("3p f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1d m V")] + [("1s f V", "1p f V")] + [("2d m V", "2p m V")] + [("2d f V", "2s f V")] + [("3p m V", "3s m V")] + [("3p f V", "3s f V")])

        # strong permutation 2
        self.add_num_perm_variation( [("1s m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("1d f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [("2p f " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m V", "1d m V")] + [("1s f V", "1p f V")] + [("2s m V", "2p m V")] + [("2d f V", "2s f V")] + [("3d m V", "3p m V")] + [("3p f V", "3s f V")])

        # strong permutation 3
        right = [("1s m " + PC, "1d m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1d m V", "1p m V")] + [("2s m V", "2d m V", "2p m V")] + [("2s m " + PC, "2d m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC]
        left = [("1s f " + PC, "1d f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("2s f " + PC, "2d f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "3d f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("2s f V", "2d f V", "2p f V")] + [("3s f V", "3d f V", "3p f V")]
        self.add_num_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 2mV:  s <-> p, 2fG: s <-> p;
        # 3fV: s <-> p, 3mG: s <-> p; 1G: s <-> p
        self.add_num_perm_variation( [("2s m V", "2p m V")] + [("3s f V", "3p f V")] + [("2s f " + PC, "2p f " + PC) for PC
                                                                                   in self.TENSES_CASES_PC] + [("3s m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s g " + PC, "3p g " + PC) for PC in self.TENSES_CASES_PC])

        # 2G s <-> p, 3V s <-> d, # 3mG d <-> p, 3fG: s <-> p, # 3mV:  s <-> d, 3fV:  d <-> p, # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES] + [("3d m V", "3s m V")] + [("3p f V", "3d f V")] + [("3d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "3p f " + PC) for PC
                                                                                   in self.TENSES_CASES_PC] + [("2s g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC] + [("3s g V", "3d g V")])

        # strong permutation 1
        self.add_num_perm_variation( [("1s m G", "1p m G")] + [("1s f G", "1d f G")] + [("1s m G", "1d m G")] + [("1s f G", "1p f G")] + [("1s m V", "1d m V")] + [("1s f V", "1p f V")] + [("1s m J", "1p m J")] + [("1s f J", "1p f J")] + [("2d m G", "2p m G")] + [("2d f G", "2s f G")] + [("2d m V", "2p m V")] + [("2d f V", "2s f V")] + [("2s m J", "2p m J")] + [("2s f J", "2p f J")] + [("2s m S", "2p m S")] + [("2s f S", "2p f S")] + [("3p m G", "3s m G")] + [("3p f G", "3d f G")] + [("3p m V", "3s m V")] + [("3p f V", "3s f V")] + [("3s m J", "3p m J")] + [("3d f J", "3p f J")] + [("3d m S", "3s m S")] + [("3d f S", "3p f S")])

        # strong permutation 2
        self.add_num_perm_variation( [("1s m G", "1p m G")] + [("1d f G", "1s f G")] + [("1p m V", "1d m V")] + [("1s f V", "1p f V")] + [("1s m J", "1p m J")] + [("1d f J", "1p f J")] + [("1d m S", "1s m S")] + [("1d f S", "1p f S")] + [("2d m G", "2s m G")] + [("2p f G", "2d f G")] + [("2s m V", "2p m V")] + [("2d f V", "2s f V")] + [("2s m J", "2p m J")] + [("2d f S", "2p f S")] + [("3p m G", "3s m G")] + [("3s f G", "3d f G")] + [("3d m V", "3p m V")] + [("3p f V", "3s f V")] + [("3s f J", "3p f J")] + [("3p m S", "3s m S")])

        # strong permutation 3
        right = [("1s m G", "1d m G", "1p m G")] + [("1s m V", "1d m V", "1p m V")] + [("1s m J", "1d m J", "1p m J")] + [("2s m G", "2d m G", "2p m G")] + [("2s m V", "2d m V", "2p m V")] + [("3s m G", "3d m G", "3p m G")] + [("2s m J", "2d m J", "2p m J")] + [("2s f S", "2d f S", "2p f S")]
        left = [("2s f G", "2d f G", "2p f G")] + [("2s f V", "2d f V", "2p f V")] + [("3s f G", "3d f G", "3p f G")] + [("3s f V", "3d f V", "3p f V")] + [("3s f J", "3d f J", "3p f J")] + [("1s f S", "1d f S", "1p f S")] + [("1s f G", "1d f G", "1p f G")]
        self.add_num_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # 1V: s <-> d, 3G: s <-> d, 2C: s <-> d, 2S: s <-> d
        self.add_num_perm_variation( [("1s g V", "1d g V")] + [("3s g G", "3d g G")] + [("2s g J", "2d g J")] + [("3s g S", "3d g S")])

        # 1G: s <-> d, 2S: s <-> p; 3C: d <-> p
        self.add_num_perm_variation( [("1s g G", "1d g G")] + [("2s g S", "2p g S")] + [("3d g J", "3p g J")])

        # 2G: s <-> p, 3S: s <-> p
        self.add_num_perm_variation( [("2s g G", "2p g G")] + [("3s g S", "3p g S")])

        # 2C: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g J", "2p g J")] + [("3d g V", "3p g V")])

        # 3G:s<->p, 2S:d<->p, 1m: s<->d
        self.add_num_perm_variation( [("3s g G", "3p g G")] + [("2d g S", "2p g S")] + [("1s m " + T, "1d m " + T) for T in self.TENSES_CASES])


    def _create_permutation_PERS_files(self):
        """
            creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
            """
        # d.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation( [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # s: 1 <-> 2, p:1 <-> 2
        self.add_pers_perm_variation( [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # s: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d:1 <-> 3, s: 1 <-> 2
        self.add_pers_perm_variation( [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "3d g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d:1 <-> 2, s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T)
                                                                                           for T in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3
        self.add_pers_perm_variation( [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # s.m: 2 <-> 3, p.f: 2 <-> 3, d: 1 <-> 2
        self.add_pers_perm_variation( [("2s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # d.f: 1 <-> 3, p.m: 2 <-> 3
        self.add_pers_perm_variation( [("1d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T)
                                                                                           for T in self.TENSES_CASES])

        # pfG: 2 <-> 3, sfG: 3<-> 2, dGm: 2<->3
        self.add_pers_perm_variation( [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "2d m " + PC) for PC
                                                                                    in self.TENSES_CASES_PC])

        # sV: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V")] + [("2d g V", "3d g V")] + [("1p g V", "2p g V")])

        # sG: 1 <-> 3, dG: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1p g V", "2p g V")] + [("1s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V")] + [("2d g V", "3d g V")] + [("1p g " + PC, "2p g " + PC) for PC
                                                                                   in self.TENSES_CASES_PC])

        # dm: 1 <-> 2, df: 1 <-> 3
        self.add_pers_perm_variation( [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation( [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 2
        self.add_pers_perm_variation( [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation( [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # pm: 1 <-> 2
        self.add_pers_perm_variation( [("1p m " + T, "2p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3
        self.add_pers_perm_variation( [("3p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # pf: 1 <-> 2
        self.add_pers_perm_variation( [("1p f " + T, "2p f " + T) for T in self.TENSES_CASES])

        # dm: 1 <-> 2, df: 1 <-> 3, sm: 1 <-> 3, sf: 1 <-> 2
        self.add_pers_perm_variation( [("1d m " + T, "2d m " + T) for T in self.TENSES_CASES] + [("1d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "2s f " + T) for T in self.TENSES_CASES])

        # pm: 1 <-> 3, pf: 2 <-> 3, dm: 2 <-> 3, sm: 1 <-> 3
        self.add_pers_perm_variation( [("1p m " + T, "3p m " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("1s m " + T, "3s m " + T) for T in self.TENSES_CASES])

        # pm: 2 <-> 3
        self.add_pers_perm_variation( [("2p m " + T, "3p m " + T) for T in self.TENSES_CASES])

        # pf: 2 <-> 3, df: 2 <-> 3
        self.add_pers_perm_variation( [("2p f " + T, "3p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "3d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # pf: 1 <-> 2, df: 1 <-> 2
        self.add_pers_perm_variation( [("2p f " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "1d f " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 1 <-> 2, p: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # d: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation( [("3d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "2p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation( [("1s m " + T, "2s m " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s f " + T)
                                                                                           for T in self.TENSES_CASES])

        # dG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "3d g " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 2 <-> 1, pG: 2 <-> 1, dV: 2 <-> 3, pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g V", "3d g V")] + [("2p g V", "3p g V")])

        # dm: 2 <-> 3, pm: 2 <-> 3
        self.add_pers_perm_variation( [("2d m " + T, "3d m " + T) for T in self.TENSES_CASES] + [("2p m " + T, "3p m " + T)
                                                                                           for T in self.TENSES_CASES])

        # df: 2 <-> 3, pf: 2 <-> 3
        self.add_pers_perm_variation( [("2d f " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p f " + T, "3p f " + T)
                                                                                           for T in self.TENSES_CASES])

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        self.add_pers_perm_variation( [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC])

        # dfG: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2d f " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [("2p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 2 <-> 1, pG: 2 <-> 1, smV: 2 <-> 3
        self.add_pers_perm_variation( [("2s m V", "3s m V")] + [("1d g " + PC, "2d g " + PC) for PC in self.TENSES_CASES_PC] + [("1p g " + PC, "2p g " + PC) for PC in self.TENSES_CASES_PC])

        # sfV: 2 <-> 3
        self.add_pers_perm_variation( [("2s f V", "3s f V")])

        # sfV: 2 <-> 3, pfG: 2 <-> 3
        self.add_pers_perm_variation( [("2s f V", "3s f V")] + [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # d,p: 1 <-> 3
        self.add_pers_perm_variation( [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "3p g " + T)
                                                                                           for T in self.TENSES_CASES])

        # dV,pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g V")] + [("2p g V", "3p g V")])

        # V: 2 <-> 3
        self.add_pers_perm_variation( [("2a g V", "3a g V")])

        # Vs: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # Vs: 1 <-> 3
        self.add_pers_perm_variation( [("1s g V", "3s g V")])

        # dV,pV: 1 <-> 3
        self.add_pers_perm_variation( [("1d g V", "3d g V")] + [("1p g V", "3p g V")])

        # dG,pG: 1 <-> 2, sV: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation( [("1d g G", "2d g G")] + [("1p g G", "2p g G")] + [("1s g V", "2s g V")] + [("2p g V", "3p g V")] + [("2d g V", "3d g V")])

        # sG: 1 <-> 2, pG,dG: 2 <-> 3
        self.add_pers_perm_variation( [("1s g G", "2s g G")] + [("2d g G", "3d g G")] + [("2p g G", "3p g G")])

        # V: 1<->2
        self.add_pers_perm_variation( [("1a g V", "2a g V")])

        # G: 2<->3
        self.add_pers_perm_variation( [("2a g G", "3a g G")])

        # strong permutation 1
        self.add_pers_perm_variation( [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [("2s f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [("3d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("1p f " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m V", "2s m V")] + [("1s f V", "2s f V")] + [("1d m V", "2d m V")] + [("2d f V", "3d f V")] + [("2p m V", "1p m V")] + [("3p f V", "1p f V")])

        # strong permutation 2
        self.add_pers_perm_variation( [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [("1s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("3p f " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "2s m V")] + [("1s f V", "3s f V")] + [("2d m V", "1d m V")] + [("2d f V", "3d f V")] + [("3p m V", "1p m V")] + [("3p f V", "1p f V")])

        # strong permutation 3
        left = [("1d f " + PC, "2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "2s m V", "3s m V")] + [("1d f V", "2d f V", "3d f V")] + [("1p m V", "2p m V", "3p m V")]
        right = [("1s f " + PC, "2s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("1d m " + PC, "2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("1p f " + PC, "2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("1d m V", "2d m V", "3d m V")] + [("1p f V", "2p f V", "3p f V")]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dG: 1 <-> 2, pG: 1 <-> 2
        # dV: 2 <-> 3, pV: 2 <-> 3
        # sV: 1 <-> 3, sG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g V", "3d g V")] + [("2p g V", "3p g V")] + [("1s g V", "3s g V")])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2s g V", "3s g V", "1s g V")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [("3s g " + PC, "1s g " + PC, "2s g " + PC) for PC in self.TENSES_CASES_PC]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # dmG: 2 <-> 3, pmG: 2 <-> 3
        # dfV: 2 <-> 3, pfV: 2 <-> 3
        # sG: 1 <-> 3, sV: 1 <-> 3
        self.add_pers_perm_variation( [("2d m " + PC, "3d m " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f V", "3d f V")] + [("2p f V", "3p f V")] + [("1s g " + PC, "3s g " + PC) for PC in self.TENSES_CASES_PC] + [("1s g V", "3s g V")])

        # sG: 1->2->3
        # sV: 3->2->1
        # dG: 1 <-> 3 (dann dGm: 1<->2),  pG: 1 <-> 3 (dann pGm: 1<->2)
        # dV: 1 <-> 2 (dann dVf: 1<->3),  pV: 1 <-> 2 (dann pVf: 1<->3)
        right = [("2s g " + PC, "3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3s g V", "1s g V", "2s g V")]
        swap = [("3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC] + [("2d g V", "1d g V")] + [("2p g V", "1p g V")] + [("2d m " + PC, "1d m " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("3d f V", "1d f V")] + [("3p f V", "1p f V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_right_list=right, rotate_left_list=left)

        # dG: 1->2->3,  pG: 1->2->3
        # dV: 3->2->1,  pV: 3->2->1
        # sG: 1 <-> 3
        # sV: 1 <-> 3 (dann sVm: 1 <-> 2)
        right = [("2d g " + PC, "3d g " + PC, "1d g " + PC) for PC in self.TENSES_CASES_PC] + [("2p g " + PC, "3p g " + PC, "1p g " + PC) for PC in self.TENSES_CASES_PC]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")]
        swap = [("3s g " + PC, "1s g " + PC) for PC in self.TENSES_CASES_PC] + [("3s g V", "1s g V")] + [("2s m V", "1s m V")]
        self.add_pers_perm_variation( swap_list=swap, rotate_left_list=left, rotate_right_list=right)

        # G: sm: 1 <-> 2, sf: 1 <-> 3
        self.add_pers_perm_variation( [("1s m " + PC, "2s m " + PC) for PC in self.TENSES_CASES_PC] + [("1s f " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        right = [("2d g G", "3d g G", "1d g G")] + [("2p g G", "3p g G", "1p g G")] + [("2s g V", "3s g V", "1s g V")] + [("1s m J", "2s m J", "3s m J")] + [("1p m S", "2p m S", "3p m S")] + [("1d f S", "2d f S", "3d f S")]
        left = [("3d g V", "1d g V", "2d g V")] + [("3p g V", "1p g V", "2p g V")] + [("3s g G", "1s g G", "2s g G")] + [("1s f J", "2s f J", "3s f J")] + [("1p f J", "2p f J", "3p f J")] + [("1d m S", "2d m S", "3d m S")]
        self.add_pers_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # strong permutation 1
        self.add_pers_perm_variation( [("1s m G", "3s m G")] + [("2s f G", "1s f G")] + [("3s m V", "2s m V")] + [("1s f V", "2s f V")] + [("1s m S", "2s m S")] + [("2s f J", "3s f J")] + [("1s m J", "3s m J")] + [("2d m G", "3d m G")] + [("3d f G", "1d f G")] + [("1d m V", "2d m V")] + [("2d f V", "3d f V")] + [("3d m S", "2d m S")] + [("2d f S", "3d f S")] + [("1d m J", "2d m J")] + [("3p m G", "2p m G")] + [("1p f G", "2p f G")] + [("2p m V", "1p m V")] + [("3p f V", "1p f V")] + [("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [("3p m J", "2p m J")] + [("1p f J", "2p f J")])

        # strong permutation 2
        self.add_pers_perm_variation( [("1s m G", "2s m G")] + [("1s f G", "3s f G")] + [("1s m V", "2s m V")] + [("1s f V", "3s f V")] + [("2s m S", "1s m S")] + [("3s f S", "1s f S")] + [("3s m J", "2s m J")] + [("3s f J", "2s f J")] + [("2d m G", "3d m G")] + [("2d f G", "1d f G")] + [("2d m V", "1d m V")] + [("2d f V", "3d f V")] + [("3d m S", "2d m S")] + [("1d f J", "2d f J")] + [("3p m G", "2p m G")] + [("3p f G", "1p f G")] + [("3p m V", "1p m V")] + [("3p f V", "1p f V")] + [("3p m S", "2p m S")] + [("3p f S", "1p f S")] + [("3p m J", "2p m J")] + [("1p f J", "2p f J")])

    def _create_permutation_GEN_files(self):
        """
            creates all permutation files where GEN-features are swapped (m <-> f)
            """

        # p2: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # s3: m <-> f
        self.add_gen_perm_variation( [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # p2: m <-> f, s3: m <-> f
        self.add_gen_perm_variation( [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES])

        # s2: m <-> f, d3: m <-> f, p2: m <-> f
        self.add_gen_perm_variation( [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2p f " + T) for T in self.TENSES_CASES])

        # 2: m <-> f
        self.add_gen_perm_variation( [("2a m " + T, "2a f " + T) for T in self.TENSES_CASES])

        # 3: m <-> f
        self.add_gen_perm_variation( [("3a m " + T, "3a f " + T) for T in self.TENSES_CASES])

        # s: m <-> f
        self.add_gen_perm_variation( [("zs m " + T, "zs f " + T) for T in self.TENSES_CASES])

        # p: m <-> f
        self.add_gen_perm_variation( [("zp m " + T, "zp f " + T) for T in self.TENSES_CASES])

        # 3dV: m <-> f
        self.add_gen_perm_variation( [("3d m V", "3d f V")])

        # 2pG: m<->f, 3sG: m<->f
        self.add_gen_perm_variation( [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        self.add_gen_perm_variation( [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m V", "3p f V")])

        # strong permutation 1
        self.add_gen_perm_variation( [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [("1d m V", "1d f V")] + [("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [("3s m V", "3s f V")] + [("3p m V", "3p f V")])

        # strong permutation 2
        self.add_gen_perm_variation( [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m V", "2d f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 3
        self.add_gen_perm_variation( [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3s m " + PC, "3s f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [("1d m V", "1d f V")] + [("2d m V", "2d f V")] + [("2p m V", "2p f V")] + [("3s m V", "3s f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 4
        self.add_gen_perm_variation( [("1s m " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1p m " + PC, "1p f " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("2d m " + PC, "2d f " + PC) for PC in self.TENSES_CASES_PC] + [("2p m " + PC, "2p f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [("1d m V", "1d f V")] + [("2s m V", "2s f V")] + [("2p m V", "2p f V")] + [("3d m V", "3d f V")] + [("3p m V", "3p f V")])

        # strong permutation 1
        self.add_gen_perm_variation( [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"), ("1s m S", "1s f S"), ("1p m J", "1p f J"), ("2s m G", "2s f G"), ("2d m G", "2d f G"), ("2d m V", "2d f V"), ("2p m V", "2p f V"), ("2p m J", "2p f J"), ("2p m J", "2p f J"), ("3s m G", "3s f G"), ("3p m G", "3p f G"), ("3s m V", "3s f V"), ("3p m V", "3p f V"), ("3p m S", "3p f S"), ("3s m S", "3s f S"), ("3s m J", "3s f J"), ("3d m J", "3d f J")])

        # strong permutation 2
        self.add_gen_perm_variation( [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m S", "1s f S"), ("1d m S", "1d f S"), ("2s m G", "2s f G"), ("2p m G", "2p f G"), ("2d m V", "2d f V"), ("2s m J", "2s f J"), ("2d m J", "2d f J"), ("3s m G", "3s f G"), ("3d m G", "3d f G"), ("3p m G", "3p f G"), ("3d m V", "3d f V"), ("3p m V", "3p f V"), ("3d m S", "3d f S"), ("3s m J", "3s f J"), ("3d m J", "3d f J")])

        # strong permutation 3
        self.add_gen_perm_variation( [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"), ("1d m J", "1d f J"), ("1p m S", "1p f S"), ("2p m G", "2p f G"), ("2d m V", "2d f V"), ("2p m V", "2p f V"), ("2s m J", "2s f J"), ("2d m J", "2d f J"), ("2s m S", "2s f S"), ("2p m S", "2p f S"), ("3s m G", "3s f G"), ("3d m G", "3d f G"), ("3s m V", "3s f V"), ("3d m V", "3d f V"), ("3p m V", "3p f V"), ("3s m J", "3s f J"), ("3p m J", "3p f J"), ("3s m S", "3s f S"), ("3p m S", "3p f S")])

        # strong permutation 4
        self.add_gen_perm_variation( [("1s m G", "1s f G"), ("1p m G", "1p f G"), ("1s m V", "1s f V"), ("1d m V", "1d f V"), ("1s m J", "1s f J"), ("1p m J", "1p f J"), ("1d m S", "1d f S"), ("2s m G", "2s f G"), ("2d m G", "2d f G"), ("2p m G", "2p f G"), ("2s m V", "2s f V"), ("2p m V", "2p f V"), ("2d m J", "2d f J"), ("2p m J", "2p f J"), ("2d m S", "2d f S"), ("3d m G", "3d f G"), ("3d m V", "3d f V"), ("3p m V", "3p f V"), ("3s m J", "3s f J"), ("3p m J", "3p f J"), ("3s m S", "3s f S"), ("3p m S", "3p f S")])

        # 2pG: m<->f, 3sG: m<->f, 3pV: m<->f
        # 3pS: m<->f, 2sC: m<->f
        self.add_gen_perm_variation( [("2p m G", "2p f G"), ("3s m G", "3s f G"), ("3p m V", "3p f V"), ("3p m S", "3p f S"), ("2s m J", "2s f J")])

        # 3pS: m<->f, 2sS: m<->f
        # 2sC: m<->f, 3sC: m<->f
        self.add_gen_perm_variation( [("3p m S", "3p f S"), ("2s m S", "2s f S"), ("2s m J", "2s f J"), ("3s m J", "3s f J")])

    def _create_permutation_TENSE_files(self):
        """
            creates all permutation files where TENSE-features are swapped (V <-> F)
            """
        # 2s : G <-> V, 3p: G <-> V, 1d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G")] + [("3p g V", "3p g G")] + [("1d g V", "1d g G")])

        # 2sf: G <-> V, 3pm: G <-> V, 3df: G <-> V
        self.add_ten_perm_variation( [("2s f V", "2s f G")] + [("3p m V", "3p m G")] + [("3d f V", "3d f G")])

        # 1s: G <-> V, 3sm: G <-> V, 1p: G <-> V, 2pm: G <-> V, 2s: G <-> V
        self.add_ten_perm_variation( [("1s g V", "1s g G")] + [("1p g V", "1p g G")] + [("2s g V", "2s g G")] + [("3s m V", "3s f G")] +
                                [("2p m V", "2p m G")])

        # 2 : G <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g G")])

        # 3 : G <-> V
        self.add_ten_perm_variation( [("3a g V", "3a g G")])

        # s : G <-> V
        self.add_ten_perm_variation( [("zs g V", "zs g G")])

        # p : G <-> V
        self.add_ten_perm_variation( [("zp g V", "zp g G")])

        # sf : G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("zs f V", "zs f G")] + [("3d g V", "3d g G")])

        # 1pm : G <-> V, 3sm : G <-> V
        self.add_ten_perm_variation( [("1p m V", "1p m G")] + [("3s m V", "3s m G")])

        # 1f : G <-> V, 3dm : G <-> V
        self.add_ten_perm_variation( [("1a f V", "1a f G")] + [("3d m V", "3d m G")])

        # sf : G <-> V, 1pm : G <-> V, 2dm : G <-> V
        self.add_ten_perm_variation( [("zs m V", "zs m G")] + [("1p m V", "1p m G")] + [("2d m V", "2d m G")])

        # 3sf : G <-> V, 2sm : G <-> V
        self.add_ten_perm_variation( [("3s f V", "3s f G")] + [("2s m V", "2s m G")])

        # df : G <-> V
        self.add_ten_perm_variation( [("zd f V", "zd f G")])

        # 1 : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G")])

        # d : G <-> V
        self.add_ten_perm_variation( [("zd g V", "zd g G")])

        # 2s, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")] + [("3p g G", "3p g V")] + [("3d g G", "3d g V")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g V")] + [("1p g G", "1p g V")] + [("1d g G", "1d g V")])

        # 1dm, 3df, 2pm, 2sm, 1sf, 3s
        self.add_ten_perm_variation( [("1d m G", "1d m V")] + [("3d f G", "3d f V")] + [("2p m G", "2p m V")] + [("2s m G", "2s m V")] + [("1s f G", "1s f V")] +
                                [("3s g G", "3s g V")])

        # 2dm, 3df, 2sf, 1d, 1p, 3sm
        self.add_ten_perm_variation( [("2d m G", "2d m V")] + [("3d f G", "3d f V")] + [("2s f G", "2s f V")] + [("1d g G", "1d g V")] + [("1p g G", "1p g V")] +
                                [("3s m G", "3s m V")])

        # 1d, 1p, 2p, 2d, 3s
        self.add_ten_perm_variation( [("1d g G", "1d g V")] + [("1p g G", "1p g V")] + [("2d g G", "2d g V")] + [("2p g G", "2p g V")] + [("3s g G", "3s g V")])

        # 3p,2s: J -> S
        self.add_ten_perm_variation( [("3p g J", "3p g S")] + [("2s g J", "2s g S")])

        # 3p: J->S, 2s: S->G
        self.add_ten_perm_variation( [("3p g J", "3p g S")] + [("2s g S", "2s g V")])

    def _create_permutation_X_files(self):
        """
            creates all permutation files where several or all features are swapped
            """

        # 2 : G <-> V, 3: s <-> p
        self.add_xross_perm_variation( [("2a g G", "2a g V")] + [("3s g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 2s: m <-> f, 3p <-> 1s, 2pV <-> 1pV
        self.add_xross_perm_variation( [("2s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1s g " + T) for T in self.TENSES_CASES] + [("2p g V", "1p g V")])

        # 2pG: m <-> f, sG: 3m<-> 2f, dGm: 2<->3
        self.add_xross_perm_variation( [("2p m G", "2p f G")] + [("3s m G", "2s f G")] + [("3d m G", "2d m G")])

        # 3dfV <-> 1smG, 2pfV <-> 3smV, 2pmG <-> 1dmV, 3sfG <-> 3dmG
        self.add_xross_perm_variation( [("3d f V", "1s m G")] + [("2p f V", "3s m V")] + [("2p m G", "1d m V")] + [("3s f G", "3d m G")])

        # 1dm <-> 2df, 2pmV <-> 3pfG, 3smG <-> 1pfV
        self.add_xross_perm_variation( [("1d m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("2p m V", "3p f G")] + [("3s m G", "1p f V")])

        # 2G <-> 3V, sG <-> pV
        self.add_xross_perm_variation( [("2a g G", "3a g V")] + [("zs g G", "zp g V")])

        # d: 1G <-> 3V,  p: 1G <-> 3V, # s: 3G <-> 2V
        self.add_xross_perm_variation( [("1d g G", "3d g V")] + [("1p g G", "3p g V")] + [("3s g G", "2s g V")])

        # V: 3p <-> 2s, Vs3 <-> Gs1
        self.add_xross_perm_variation( [("3p g V", "2s g V")] + [("3s g V", "1s g V")])

        # STRONG

        # full permutation 1
        self.add_xross_perm_variation( [("1s m G", "3s m V")] + [("2s m G", "1d f V")] + [("3s m G", "2p f G")] + [("1s f G", "3p m V")] + [("2s f G", "2d f G")] + [("3s f G", "1p m G")] + [("3p m G", "3d m V")] + [("1s m V", "2s f V")] + [("2s m V", "2p f V")] + [("2p m V", "1p f V")] + [("3s f V", "1s f V")] + [("3d m G", "1d f G")] + [("2d m G", "1d m V")] + [("1d m G", "3d f V")] + [("2p m G", "3p f G")] + [("3d f G", "1p f G")] + [("2d m V", "3p f V")] + [("2d f V", "1p m V")])

        # full permutation 2
        self.add_xross_perm_variation( [("1s m G", "2d m G")] + [("1s f G", "3s f V")] + [("2s m G", "1s f G")] + [("2s f G", "2d f G")] + [("2s m V", "1p m V")] + [("2s f V", "1p f V")] + [("3p m V", "3p m G")] + [("3p f V", "3p f G")] + [("1d m V", "3s m V")] + [("1d f V", "1s m G")] + [("1s m V", "1p m G")] + [("1s f V", "3d m V")] + [("2d m V", "2s m G")] + [("2d f V", "1p f G")] + [("3d f V", "2s f G")] + [("2p m G", "3d f G")] + [("2p f G", "2p m V")] + [("3d m G", "2p f V")])

        # full permutation 3
        self.add_xross_perm_variation( [("1s g G", "2d g V")] + [("2p g G", "2s g G")] + [("3d g G", "1p g V")] + [("1s g V", "1p g G")] + [("3s g V", "3s g G")] + [("3d g V", "1d g G")] + [("1d g G", "2p g V")] + [("2s g V", "3p g G")] + [("3p g V", "2d g G")] + [("1s g J", "1p g S")] + [("3s g J", "3s g S")] + [("3d g J", "1d g S")])

        # full permutation 4
        self.add_xross_perm_variation( [("1s g G", "1d g G")] + [("2d g G", "2p g G")] + [("3s g G", "3p g G")] + [("1p g V", "3d g G")] + [("2s g G", "3s g V")] + [("1p g G", "2d g V")] + [("2d g J", "2p g J")] + [("1s g " + T, "2s g " + T) for T in ["V", "S", "J"]] + [("2p g " + T, "3p g " + T) for T in ["V", "S", "J"]] + [("1d g " + T, "3d g " + T) for T in ["V", "S", "J"]])

        # full permutation 5
        self.add_xross_perm_variation( [("1s g G", "2p g V")] + [("3p g G", "2s g V")] + [("2d g G", "1d g V")] + [("1s g V", "3d g G")] + [("2d g V", "2p g G")] + [("3p g V", "3s g G")] + [("1p g V", "2s g G")] + [("3s g V", "1p g G")] + [("3d g V", "1d g G")] + [("1s g S", "2p g J")] + [("3p g S", "2s g J")] + [("2d g S", "1d g J")] + [("1s g J", "3d g S")] + [("2d g J", "2p g S")] + [("3p g J", "3s g S")] + [("1p g J", "2s g S")] + [("3s g J", "1p g S")] + [("3d g J", "1d g S")])

        # full permutation 6
        self.add_xross_perm_variation( [("1s m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("3p m " + T, "2p m " + T) for T in self.TENSES_CASES] + [("3s f " + T, "1p f " + T) for T in self.TENSES_CASES] + [("1d f " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for T in self.TENSES_CASES] + [("2s m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2d m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # full permutation 7
        self.add_xross_perm_variation( [("1s m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1d m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("2d m " + T, "1s f " + T) for T in self.TENSES_CASES] + [("3d m " + T, "3p f " + T) for T in self.TENSES_CASES] + [("1p m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3p m " + T, "3d f " + T) for T in self.TENSES_CASES])

        # full permutation 8
        self.add_xross_perm_variation( [("1s m " + T, "2p f " + T) for T in self.TENSES_CASES] + [("1s f " + T, "3s m " + T) for T in self.TENSES_CASES] + [("2p m " + T, "2d f " + T) for T in self.TENSES_CASES] + [("3s f " + T, "2s m " + T) for T in self.TENSES_CASES] + [("1d m " + T, "1p f " + T) for T in self.TENSES_CASES] + [("1d f " + T, "2s f " + T) for T in self.TENSES_CASES] + [("3d f " + T, "2d m " + T) for T in self.TENSES_CASES] + [("3d m " + T, "1p m " + T) for T in self.TENSES_CASES] + [("3p m " + T, "3p f " + T) for T in self.TENSES_CASES])

        # rotations
        # full permutation 9
        right = [("1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("2s g " + T, "3p g " + T, "1d g " + T) for T in self.TENSES_CASES] + [("3s g " + T, "1p g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right)

        # full permutation 10
        right = [("1s g " + T, "2s g " + T, "3s g " + T) for T in self.TENSES_CASES]
        left = [("1d g " + T, "2d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 11
        right = [("1s f " + T, "3d m " + T, "3p f " + T) for T in self.TENSES_CASES] + [("3s m " + T, "2p m " + T, "1d f " + T) for T in self.TENSES_CASES]
        left = [("1s m " + T, "1p m " + T, "2s f " + T) for T in self.TENSES_CASES] + [("1p f " + T, "2d m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2s m " + T, "1d m " + T, "3d f " + T) for T in self.TENSES_CASES] + [("2d f " + T, "1p f " + T, "3p m " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 12
        right = [("1s g G", "2p g V", "3d g G")] + [("2s g G", "2s g V", "1d g V")] + [("3s g V", "1p g V", "1p g G")]
        left = [("1p g S", "1s g J", "2d g J")] + [("3d g S", "1d g J", "3d g J")] + [("1p g J", "1s g S", "2d g S")] + [("2d g V", "3p g V", "3s g G")] + [("2d g G", "2p g G", "3p g G")] + [("1d g G", "1s g V", "3d g V")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 13
        left = [("1s m G", "2s m G", "3p f V")] + [("1p m G", "1d f G", "2d m V")] + [("3p m G", "3p f G", "1s f G")] + [("3s f G", "3s f V", "3d m V")] + [("3s m V", "2p m V", "3p m V")] + [("1p f G", "2d f G", "3d m G")] + [("1s f V", "3d f V", "2d m G")] + [("1p m S", "1d f S", "2d m J")] + [("3p m S", "3p f S", "1s f S")]
        right = [("1d m G", "1s m V", "2d f V")] + [("2s f G", "2s f V", "2s m V")] + [("1d m V", "2p f G", "1p f V")] + [("3s m G", "1p m V", "2p m G")] + [("3d f G", "1d f V", "2p f V")] + [("1d m J", "2p f S", "1p f J")] + [("3s m S", "1p m J", "2p m S")] + [("3d f S", "1d f J", "2p f J")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # full permutation 14
        left = [("1a m G", "1a f V", "3a f G")] + [("2a m G", "2a m V", "3a f V")] + [("2a f V", "1a f G", "1a m V")] + [("3a m G", "2a f G", "3a m V")] + [("1a m S", "1a f J", "3a f S")] + [("2a m S", "2a m J", "3a f J")] + [("2a f J", "1a f S", "1a m J")] + [("3a m S", "2a f S", "3a m J")]
        self.add_xross_perm_variation( rotate_left_list=left)

        # full permutation 15
        left = [("zs m G", "zs m V", "zp m G")] + [("zp f G", "zd m G", "zd f V")] + [("zs f V", "zp m V", "zd f G")] + [("zs f G", "zd m V", "zp f V")] + [("zs f S", "zd m S", "zp f S")] + [("zp f J", "zd m J", "zd f J")]
        right = [("zp m J", "zs f J", "zs m S")]
        self.add_xross_perm_variation( rotate_right_list=right, rotate_left_list=left)

        # 2smG <-> 3sfV, # 2sfG <-> 2pfG,  3smV  <-> 2smV
        # 1s <-> 1p
        # V: 2d <-> 3d, V:2p <-> 3p
        # 3dG: m <-> f,   3pG: m <-> f
        self.add_xross_perm_variation( [("2s m G", "3s f V")] + [("2s f G", "2p f G")] + [("3s m V", "2s m V")] + [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g V", "3d g V")] + [("2p g V", "3p g V")] + [("3d m " + PC, "3d f " + PC) for
                                                                                      PC in self.TENSES_CASES_PC] + [("3p m " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        # 3s: m <-> f
        # 2G: s <-> p
        # Vp: 1 <-> 3, Vd: 1 <-> 3
        # Vs: 1m <-> 2f
        self.add_xross_perm_variation( [("3s m " + T, "3s f " + T) for T in self.TENSES_CASES] + [("2s g G", "2p g G")] + [("1p g V", "3p g V")] + [("1d g V", "3d g V")] + [("1s m V", "2s f V")])

        # 3sV: m <-> f
        # 1G: s <-> p
        # V: 1d  <-> 2d, V: 1p <-> 2p
        # 3pV <-> 2pG;  2sG <-> 3pG
        self.add_xross_perm_variation( [("3s m V", "3s f V")] + [("1s g G", "1p g G")] + [("1d g V", "2d g V")] + [("1p g V", "2p g V")] + [("3p g V", "2p g G")] + [("3p g G", "2s g G")])

        self.add_xross_perm_variation( [("1s m G", "2d m G")] + [("1s f G", "3d m V")] + [("2s m G", "3d f G")] + [("2s f G", "2p m G")] + [("3s m G", "3p m V")] + [("3s f S", "1p f G")] + [("1d m G", "3d m G")] + [("1d f G", "2s m V")] + [("2d f S", "1d m J")] + [("1p m G", "1d f V")] + [("2p f S", "3s f V")] + [("3p m G", "3s m J")] + [("3p f G", "2s f V")] + [("1s m V", "1p f J")] + [("1s f V", "2d m V")] + [("2d f J", "3d f J")] + [("1p m V", "3p f V")] + [("2p f V", "2p m V")] + [("3p f S", "2d m J")] + [("3p m S", "3d f V")] + [("2p m J", "2d f V")] + [("2p f J", "1s m J")] + [("3p f J", "1p m S")] + [("1p f V", "2s m J")] + [("2d f G", "2s f J")])

        self.add_xross_perm_variation( [("1s m G", "3s f G")] + [("1s m V", "3s f V")] + [("1s f V", "2s f G")] + [("2s m V", "2d m G")] + [("2s f V", "3d m G")] + [("3s m V", "1s f G")] + [("2s m G", "3p m V")] + [("1d m G", "2d f G")] + [("1d f G", "1p m G")] + [("1p m V", "3s m G")] + [("1p f V", "3p f V")] + [("2p f V", "2d f V")] + [("3d f G", "2p m V")] + [("1p f G", "1d m V")] + [("2p m G", "3d f V")] + [("2d m V", "3p m G")] + [("2p f G", "1d f V")] + [("3p f G", "3d m V")] + [("3p f S", "2d m J")] + [("3p m S", "3d f S")] + [("2p m J", "2d f J")] + [("2p f J", "1s m J")] + [("3p f J", "1p m S")] + [("1p f S", "2s m J")] + [("2d f S", "2s f J")])

        self.add_xross_perm_variation( [("1s m G", "1p m G")] + [("1s f G", "3d m G")] + [("2s m G", "3p f G")] + [("2s f G", "3s f V")] + [("3s m G", "1d m G")] + [("3s f G", "2d m V")] + [("1d f G", "3d m V")] + [("2d m G", "1p m V")] + [("2d f G", "1p f V")] + [("3d f G", "1d f V")] + [("1p f G", "3s m V")] + [("2p m G", "3d f V")] + [("2p f G", "1d m V")] + [("3p m G", "2d f V")] + [("1s m V", "2p f V")] + [("1s f V", "3p f V")] + [("2s m V", "2p m V")] + [("2s f V", "3p m V")] + [("1s m S", "1p m J")] + [("1s f S", "3d m J")] + [("2s m S", "3p f J")] + [("2s f S", "3s f V")] + [("3s m S", "1d m J")] + [("3s f S", "2d m J")] + [("1d f S", "3d m J")] + [("2d m S", "1p m J")] + [("2d f S", "1p f J")] + [("3d f S", "3s m J")] + [("2p m S", "3d f J")] + [("3p m S", "2d f J")])

        self.add_xross_perm_variation( [("1s m G", "2s f G")] + [("3s m G", "2s m V")] + [("1s m V", "1s f G")] + [("2s f V", "1s f V")] + [("3s f V", "3s m V")] + [("1d m G", "1p f V")] + [("2d m G", "1p m G")] + [("3d m G", "2s m G")] + [("3d f G", "2p m V")] + [("1p m V", "2p m G")] + [("2p f V", "2d f G")] + [("3p m S", "3p m G")] + [("3p f S", "3p f G")] + [("1p f G", "2p f G")] + [("1d f S", "3d m V")] + [("2d m J", "1d f G")] + [("2d f S", "3s f G")] + [("3d f J", "1d m V")] + [("3p m V", "3p m J")] + [("3p f V", "3p f J")] + [("1p f S", "2p f S")] + [("1d f V", "3d m J")] + [("2d m V", "1d f J")] + [("2d f V", "3s f S")] + [("3d f V", "1d m S")])

        self.add_xross_perm_variation( [("1s m " + PC, "3s m " + PC) for PC in self.TENSES_CASES_PC] + [("2s m " + PC, "2s f " + PC) for PC in self.TENSES_CASES_PC] + [("3s f " + PC, "1s f " + PC) for PC in self.TENSES_CASES_PC] + [("1d m " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC] + [("2d f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("3d m " + PC, "1p m " + PC) for PC in self.TENSES_CASES_PC] + [("1p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC] + [("2p f " + PC, "1d f " + PC) for PC in self.TENSES_CASES_PC] + [("3p m " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s m V", "1s f V")] + [("2s m V", "3s f V")] + [("3s m V", "2s f V")] + [("1d m V", "3d m V")] + [("2d m V", "2d f V")] + [("3d f V", "1d f V")] + [("1p m V", "3p m V")] + [("1p f V", "2p f V")] + [("3p f V", "2p m V")])

        self.add_xross_perm_variation( [("2s m G", "1p f G")] + [("2s f S", "1s m G")] + [("2d m S", "1p m V")] + [("2d f S", "3d f G")] + [("2p m S", "1s m V")] + [("2p f S", "3d m G")] + [("2s m J", "3d f V")] + [("2s f J", "1d m G")] + [("2d m J", "3p m V")] + [("2d f J", "3s f G")] + [("2p m J", "3d m V")] + [("2p f V", "3p m G")] + [("3s m G", "1d m V")] + [("1p m G", "3s f V")] + [("3p f G", "1p f V")] + [("3s m V", "1d f G")] + [("1d f V", "1s f V")] + [("3p f V", "1s f G")] + [("2s f G", "2p f G")] + [("2d m G", "2d m V")] + [("2d f G", "2s m V")] + [("2p m G", "2s f V")] + [("2d f V", "2p m V")])

        self.add_xross_perm_variation( [("1s m G", "2d f V")] + [("1s f G", "3d m V")] + [("1d m G", "3p m G")] + [("1d f G", "2p f G")] + [("1p m G", "1s f V")] + [("1p f G", "3d f V")] + [("1s m V", "2s f V")] + [("1d m V", "2p f V")] + [("1d f V", "2d m G")] + [("1p m V", "3p f G")] + [("1p f V", "3s m V")] + [("3s f G", "2d f G")] + [("2d f J", "2d m V")] + [("1p f S", "3s f V")] + [("1s m S", "2p m V")] + [("1d f S", "3p m V")] + [("3d f S", "2p m G")] + [("1d m S", "3p f V")] + [("3d m J", "2s f G")] + [("1p m J", "2s m V")] + [("2s m J", "3s m G")] + [("3s f S", "3d f G")] + [("1d f J", "3d m G")] + [("1s f S", "2s m G")] + [("3p m S", "2p f S")] + [("1p m S", "1s f J")] + [("2d f S", "3d f J")] + [("1s m J", "2s f J")] + [("1d m J", "2p f J")] + [("2d m S", "3p f S")] + [("1p f J", "3s m J")] + [("3d m S", "2d m J")] + [("3s m S", "2p m J")] + [("3s f J", "2s m S")] + [("3p m J", "2p m S")] + [("3p f J", "2s f S")])

        self.add_xross_perm_variation( [("1s f G", "2p m V")] + [("3s m G", "1p m V")] + [("3s f G", "1d m V")] + [("2d f G", "2p f V")] + [("3d m G", "3d m V")] + [("1p m G", "3p m V")] + [("1p f G", "1p f V")] + [("2s m G", "3d f V")] + [("1s m V", "2s f V")] + [("1s f V", "2d f V")] + [("1d f V", "2s m V")] + [("2d m V", "3s f V")] + [("3p f V", "3s m V")] + [("2s f " + PC, "3d f " + PC) for PC in self.TENSES_CASES_PC] + [("1d m " + PC, "3p m " + PC) for PC in self.TENSES_CASES_PC] + [("1d f " + PC, "2p m " + PC) for PC in self.TENSES_CASES_PC] + [("1s m " + PC, "2d m " + PC) for PC in self.TENSES_CASES_PC] + [("2p f " + PC, "3p f " + PC) for PC in self.TENSES_CASES_PC])

        self.add_xross_perm_variation( [("1s f G", "3p f V")] + [("1d m G", "1s m G")] + [("1d f G", "2s f V")] + [("1p m G", "2s f G")] + [("1p f G", "3p f G")] + [("1s m V", "3d m G")] + [("1s f V", "2d f G")] + [("1d m V", "3d m V")] + [("1d f V", "2s m G")] + [("1p m V", "2d m G")] + [("1p f V", "2d f V")] + [("3s f V", "3s m G")] + [("2p m G", "3d f V")] + [("2p f G", "3p m G")] + [("2s m V", "3d f G")] + [("2d m V", "3p m V")] + [("2p m V", "3s m V")] + [("2p f V", "3s f G")] + [("1s f S", "2p m J")] + [("3s m S", "1p m J")] + [("3s f S", "1d m J")] + [("2d f S", "2p f J")] + [("3d m S", "3d m J")] + [("1p m S", "3p m J")] + [("1p f S", "1p f J")] + [("2s m S", "3d f J")])

        self.add_xross_perm_variation( [("1s m G", "2d m V")] + [("1s f G", "3s f V")] + [("3p m G", "2s f G")] + [("3p f G", "1d f G")] + [("2s m G", "3s m V")] + [("3d m V", "3p m V")] + [("3d f V", "1d m V")] + [("1d m G", "2d f V")] + [("1p f V", "2p f V")] + [("2p m V", "1p m V")] + [("3s m G", "1s f V")] + [("3s f G", "3p f V")] + [("1d f V", "3d f G")] + [("3d m G", "2s m V")] + [("1p f G", "1s m V")] + [("2d m G", "2s f V")] + [("2d f G", "2p f G")] + [("1p m G", "2p m G")] + [("1s m S", "2s f S")] + [("3s m S", "2s m J")] + [("1s m J", "1s f S")] + [("2s f J", "1s f J")] + [("3s f J", "3s m J")] + [("1d m S", "1p f J")] + [("2d m S", "1p m S")] + [("3d m S", "2s m S")] + [("3d f S", "2p m J")] + [("1p m J", "2p m S")] + [("2p f J", "2d f S")])

        self.add_xross_perm_variation( [("1s m G", "3p f G")] + [("1s f G", "3d f V")] + [("1d m G", "3s f G")] + [("1d f G", "2p m G")] + [("1p m G", "3s m V")] + [("1p f G", "2d m G")] + [("2s m G", "3d f G")] + [("2s f G", "2p f G")] + [("3s m G", "3p m V")] + [("3d m G", "2d f G")] + [("3p m G", "3d m V")] + [("1s m V", "1p m V")] + [("1s f V", "2d m V")] + [("2s m V", "2p f V")] + [("2s f V", "3p f V")] + [("2d f V", "1d f V")] + [("2p m V", "1p f V")] + [("3s f V", "1d m V")] + [("1s f S", "2p m J")] + [("3s m S", "1p m J")] + [("3s f S", "1d m J")] + [("2d f S", "2p f J")] + [("3d m S", "3d m J")] + [("1p m S", "3p m J")] + [("1p f S", "1p f J")] + [("2s m S", "3d f J")])

        self.add_xross_perm_variation( [("1s m G", "2s f G")] + [("1d m G", "1d f V")] + [("1d f G", "1d m V")] + [("1p m G", "2p f V")] + [("1p f G", "1s f V")] + [("2s m G", "2p f G")] + [("2d m G", "1p m V")] + [("2d f G", "3p f V")] + [("2p m G", "3d f V")] + [("2s m V", "3p m V")] + [("2s f V", "3p f G")] + [("2d m V", "1s m V")] + [("2d f V", "3s f V")] + [("3s m G", "2p m V")] + [("3d m G", "1s f G")] + [("3d f G", "3p m G")] + [("3s m V", "3s f G")] + [("3d m V", "1p f V")] + [("1s m S", "3p f S")] + [("1s f S", "3d f J")] + [("1d m S", "3s f S")] + [("1d f S", "2p m S")] + [("1p m S", "3s m J")] + [("1p f S", "2d m S")] + [("2s m S", "3d f S")] + [("2s f S", "2p f S")] + [("3s m S", "3p m J")] + [("3d m S", "2d f S")] + [("3p m S", "3d m J")] + [("1s m J", "1p m J")] + [("1s f J", "2d m J")] + [("2s m J", "2p f J")] + [("2s f J", "3p f J")] + [("2d f J", "1d f J")] + [("2p m J", "1p f J")] + [("3s f J", "1d m J")])

        # full swap 1
        old_list = [("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T, "3p g " + T) for T in self.TENSES_CASES]
        new_list = [("2s g " + T, "3p g " + T, "3d g " + T, "3s g " + T, "1p g " + T, "1d g " + T, "1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

        # full swap 2
        old_list = [("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T, "3p g " + T) for T in self.TENSES_CASES]
        new_list = [("2s g " + T, "1s g " + T, "3s g " + T, "2d g " + T, "1p g " + T, "3p g " + T, "2p g " + T, "1d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

    def _create_syncretic_GEN_files(self):
        """syncretic variations that happened historically (gender syncretism)"""
        # syn: 2V:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f V", "2a m V")])
        # syn: p:f -> m (TRUE)
        self.add_gen_sync_variation( [("zp"+" f "+T, "zp"+" m "+T) for T in self.TENSES_CASES])
        # V3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f V", "3p m V")])
        # Gp: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # 3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # syn: 2:f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES])
        # syn G3d: f -> m (TRUE)
        self.add_gen_sync_variation( [("3d f "+PC, "3d m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V2s: f -> m (TRUE)
        self.add_gen_sync_variation( [("2s f V", "2s m V")])
        # syn G2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3p: f -> m (TRUE)
        self.add_gen_sync_variation( [("3p f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn 2: f -> m (TRUE)
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES])
        # syn Vp: f -> m
        self.add_gen_sync_variation( [("zp f V", "zp m V")])
        # syn p: f -> m (TRUE)
        self.add_gen_sync_variation( [("zp f "+T, "zp m "+T) for T in self.TENSES_CASES])
        # syn V1s: f -> m (TRUE)
        self.add_gen_sync_variation( [("1s f V", "1s m V")])
        # syn G3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f G", "3s m G")])
        # syn G2p: f->m (TRUE)
        self.add_gen_sync_variation( [("2p f "+PC, "2p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn s/d: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+T, "zs m "+T) for T in self.TENSES_CASES]+[("zd f "+T, "zd m "+T) for T in self.TENSES_CASES])
        # syn 3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m "+T, "3a f "+T) for T in self.TENSES_CASES])
        # syn s: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+T, "zs m "+T) for T in self.TENSES_CASES])
        # syn 2s: f->m, 3s: f->m (FALSE)
        self.add_gen_sync_variation( [("2s f "+T, "2s m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # 2d
        self.add_gen_sync_variation( [("2d f "+T, "2d m "+T) for T in self.TENSES_CASES])
        # Gd
        self.add_gen_sync_variation( [("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC])
        # 2s
        self.add_gen_sync_variation( [("2s f "+T, "2s m "+T) for T in self.TENSES_CASES])
        # 2
        self.add_gen_sync_variation( [("2a f "+T, "2a f "+T) for T in self.TENSES_CASES])
        # V2p
        self.add_gen_sync_variation( [("2p f V", "2p m V")])
        # dG, dV2
        self.add_gen_sync_variation( [("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC]+[("2d f V", "2d m V")])
        # alle
        self.add_gen_sync_variation( [("za f "+T, "za m "+T) for T in self.TENSES_CASES])
        # G2, G3p
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC]+[("3p f "+PC, "3p m "+PC)
                                                                                               for PC in self.TENSES_CASES_PC])
        # 3d
        self.add_gen_sync_variation( [("3d f "+T, "3d m "+T) for T in self.TENSES_CASES])
        # G2, G3d/p
        self.add_gen_sync_variation( [("2a f "+PC, "2a m "+PC) for PC in self.TENSES_CASES_PC]+[("3d f "+PC, "3d m "+PC) for PC in self.TENSES_CASES_PC]+[("3p f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # V2d/p
        self.add_gen_sync_variation( [("2d f V", "2d m V"), ("2p f V", "2p m V")])
        # 2, 3d/p
        self.add_gen_sync_variation( [("2a f "+T, "2a m "+T) for T in self.TENSES_CASES]+[("3d f "+T, "3d m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # 3p/d
        self.add_gen_sync_variation( [("3d f "+T, "3d m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "3p m "+T) for T in self.TENSES_CASES])
        # Vp/d3
        self.add_gen_sync_variation( [("3p f V", "3p m V"), ("3d f V", "3d m V")])
        # Gp/d
        self.add_gen_sync_variation( [("zd f "+PC, "zd m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m V", "3a f V")])
        # syn Vs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f V", "zs m V")])
        # syn G3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m G", "3a f G")])
        # syn Gs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f G", "zs m G")])
        # 3s; 2p
        self.add_gen_sync_variation( [("2p f "+T, "2p m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V2p, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"), ("3s f G", "3s m G")])
        # 3s; 2p/d
        self.add_gen_sync_variation( [("2p f "+T, "2p m "+T) for T in self.TENSES_CASES]+[("2d f "+T, "2d m "+T) for T in self.TENSES_CASES]+[("3s f "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V2p/d, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"), ("2d f V", "2d m V"), ("3s f G", "3s m G")])
        # syn G/S3s: f->m (FALSE)
        self.add_gen_sync_variation( [("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G/S3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m "+PC, "3a f "+PC) for PC in self.TENSES_CASES_PC])
        # syn G/Ss: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC])
        # V2p, G/S3s
        self.add_gen_sync_variation( [("2p f V", "2p m V")]+[("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # V2p/d, G/S3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("2d f V", "2d m V")]+[("3s f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3: m->f (FALSE)
        self.add_gen_sync_variation( [("3a m S", "3a f S"),("3a m J", "3a f J")])
        # syn Gs: f->m (FALSE)
        self.add_gen_sync_variation( [("zs f G", "zs m G")]+[("zs f J", "zs m J")])
        # V2p, J3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("3s f J", "3s m J")])
        # V2p/d, G3s
        self.add_gen_sync_variation( [("2p f V", "2p m V"),("2d f V", "2d m V"),("3s f J", "3s m J"),("3s f S", "3s m S")])


    def _create_syncretic_PERS_files(self):
        """syncretic variations that happened historically (other than Gender)"""
        # syn Vsm: 2 -> 1
        self.add_pers_sync_variation( [("2s m V", "1s m V")])
        # syn Vsf: 2 -> 1
        self.add_pers_sync_variation( [("2s f V", "1s f V")])
        # syn Vdm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V")])
        # syn Vdm: 2->1; Vsm: 2->1
        self.add_pers_sync_variation( [("2d m V", "1d m V"),("2s m V", "1s m V")])
        # Vd: 2->1
        self.add_pers_sync_variation( [("2d g V", "1d g V")])
        # syn 1 -> 2
        self.add_pers_sync_variation( [("1a g "+T, "2a g "+T) for T in self.TENSES_CASES])
        # syn 2 -> 3
        self.add_pers_sync_variation( [("2a g "+T, "3a g "+T) for T in self.TENSES_CASES])
        # syn 3 -> 1
        self.add_pers_sync_variation( [("3a g "+T, "1a g "+T) for T in self.TENSES_CASES])
        # syn f:3->2
        self.add_pers_sync_variation( [("3a f "+T, "2a f "+T) for T in self.TENSES_CASES])
        # syn fp:3->2
        self.add_pers_sync_variation( [("3p f "+T, "2p f "+T) for T in self.TENSES_CASES])
        # syn p:  2->1,3->1
        self.add_pers_sync_variation( [("2p g "+T, "1p g "+T) for T in self.TENSES_CASES]+[("3p g "+T, "1p g "+T) for T in self.TENSES_CASES])
        # syn s:2->3
        self.add_pers_sync_variation( [("2s g "+T, "3s g "+T) for T in self.TENSES_CASES])
        # syn s:1->2
        self.add_pers_sync_variation( [("1s g "+T, "2s g "+T) for T in self.TENSES_CASES])
        # syn p:2->3
        self.add_pers_sync_variation( [("2p g "+T, "3p g "+T) for T in self.TENSES_CASES])
        # syn Vp:3->2
        self.add_pers_sync_variation( [("3p g V", "2p g V")])
        # Gp: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC])
        # Vs: 2->1
        self.add_pers_sync_variation( [("2s g V", "1s g V")])
        # Gpf: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC])
        # G:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC]+[("3d f "+PC, "2d f "+PC) for PC in self.TENSES_CASES_PC])
        # G: d/p: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC]+[("3d g "+PC, "2d g "+PC) for PC in self.TENSES_CASES_PC])
        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V"),("3a g G", "1a g G")])
        # mp:3->2, fp:3->1
        self.add_pers_sync_variation( [("3p m "+T, "2p m "+T) for T in self.TENSES_CASES]+[("3p f "+T, "1p f "+T) for T in self.TENSES_CASES])
        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V"),("2a f G", "1a f G")])
        # G/Sp: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC])
        # G/Spf: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC])
        # G/S:p/d:f: 3->2
        self.add_pers_sync_variation( [("3p f "+PC, "2p f "+PC) for PC in self.TENSES_CASES_PC]+[("3d f "+PC, "2d f "+PC) for PC in self.TENSES_CASES_PC])
        # G/S: d/p: 3->2
        self.add_pers_sync_variation( [("3p g "+PC, "2p g "+PC) for PC in self.TENSES_CASES_PC]+[("3d g "+PC, "2d g "+PC) for PC in self.TENSES_CASES_PC])
        # V: 2->3, G/S:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")]+[("3a g "+PC, "1a g "+PC) for PC in self.TENSES_CASES_PC])
        # Cm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")]+[("2a f "+PC, "1a f "+PC) for PC in self.TENSES_CASES_PC])
        # V: 2->3, G:3->1
        self.add_pers_sync_variation( [("2a g V", "3a g V")]+[("3a g "+PC, "1a g "+PC) for PC in self.TENSES_CASES_PC])
        # Vm:2->3, Gf:2->1
        self.add_pers_sync_variation( [("2a m V", "3a m V")]+[("2a f "+PC, "1a f "+PC) for PC in self.TENSES_CASES_PC])


    def _create_syncretic_NUM_files(self):
        # syn: d -> p
        self.add_num_sync_variation( [("zd"+" g "+T, "zp"+" g "+T) for T in self.TENSES_CASES])
        # 1: d -> p
        self.add_num_sync_variation( [("1d"+" g "+T, "1p"+" g "+T) for T in self.TENSES_CASES])
        # syn V3m: p -> s
        self.add_num_sync_variation( [("3p m V", "3s m V")])
        # syn V1: d -> p
        self.add_num_sync_variation( [("1d g V", "1p g V")])
        # syn G1: s->p
        self.add_num_sync_variation( [("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # 3m: p->s
        self.add_num_sync_variation( [("3p m "+T, "3s m "+T) for T in self.TENSES_CASES])
        #
        self.add_num_sync_variation( [("zp g "+T, "zd g "+T) for T in self.TENSES_CASES])
        # syn s->p
        self.add_num_sync_variation( [("zs g "+T, "zp g "+T) for T in self.TENSES_CASES])
        # syn s->d
        self.add_num_sync_variation( [("zs g "+T, "zd g "+T) for T in self.TENSES_CASES])
        # syn 3: d-> p
        self.add_num_sync_variation(  [("3d g "+T, "3p g "+T) for T in self.TENSES_CASES])
        # 2: d->p
        self.add_num_sync_variation( [("2d g "+T, "2p g "+T) for T in self.TENSES_CASES])
        # G1: s/d->p
        self.add_num_sync_variation( [("1d g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC]+[("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # V3f: s->p
        self.add_num_sync_variation( [("3s f V", "3p f V")])
        # 3m: d->s
        self.add_num_sync_variation( [("3d m "+T, "3s m "+T) for T in self.TENSES_CASES])
        # V3: d->s
        self.add_num_sync_variation( [("3d g V", "3s g V")])
        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")]+[("zd g G", "zs g G")])
        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V"),("3s g G", "3p g G")])
        # 2:d->p, 3:d->s
        self.add_num_sync_variation( [("2d g "+T, "2p g "+T) for T in self.TENSES_CASES]+[("3d g "+T, "3s g "+T) for T in self.TENSES_CASES])
        # 1:d->s, 2:p->s
        self.add_num_sync_variation( [("1d g "+T, "1s g "+T) for T in self.TENSES_CASES]+[("2p g "+T, "2s g "+T) for T in self.TENSES_CASES])
        # m: p->s
        self.add_num_sync_variation( [("zp m "+T, "zs m "+T) for T in self.TENSES_CASES])
        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V"),("3s f G", "3d f G")])
        # f: p->s
        self.add_num_sync_variation( [("zp f "+T, "zs f "+T) for T in self.TENSES_CASES])
        # f: p/d->s
        self.add_num_sync_variation( [("zp f "+T, "zs f "+T) for T in self.TENSES_CASES]+[("zd f "+T, "zs f "+T) for T in self.TENSES_CASES])
        # m: p/d->s
        self.add_num_sync_variation( [("zp m "+T, "zs m "+T) for T in self.TENSES_CASES]+[("zd m "+T, "zs m "+T) for T in self.TENSES_CASES])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m G", "zs m G")]+[("zd m G", "zs m G")]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("zd m G", "zp m G")]+[("2s g V", "2p g V")])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("zp f V", "zd f V")]+[("3s g G", "3p g G")])
        # syn G1: s->p
        self.add_num_sync_variation( [("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # G1: s/d->p
        self.add_num_sync_variation( [("1d g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC]+[("1s g "+PC, "1p g "+PC) for PC in self.TENSES_CASES_PC])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zd m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("zd m "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC]+[("2s g V", "2p g V")])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zd f V")])
        # V: d->p, G: d->s
        self.add_num_sync_variation( [("zd g V", "zp g V")]+[("zd g "+PC, "zs g "+PC) for PC in self.TENSES_CASES_PC])
        # V2: s->p, G3: s->p
        self.add_num_sync_variation( [("2s g V", "2p g V")]+[("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC])
        # V2m:s->p, G3f:s->d
        self.add_num_sync_variation( [("2s m V", "2p m V")]+[("3s f "+PC, "3d f "+PC) for PC in self.TENSES_CASES_PC])
        # Gm: p/d->s, Vf:p/d->s
        self.add_num_sync_variation( [("zp m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zd m "+PC, "zs m "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zs f V")]+[("zd f V", "zs f V")])
        # V2: s-> p, Gm: d->p
        self.add_num_sync_variation( [("2s g V", "2p g V")]+[("zd m "+PC, "zp m "+PC) for PC in self.TENSES_CASES_PC])
        # G3: s->p, Vf: p->d
        self.add_num_sync_variation( [("3s g "+PC, "3p g "+PC) for PC in self.TENSES_CASES_PC]+[("zp f V", "zd f V")])


    def _create_syncretic_X_files(self):
        # syn G3sf -> G2sm
        self.add_xross_sync_variation( [("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3sm -> G1pm
        self.add_xross_sync_variation( [("3s m "+PC, "1p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3p -> V3sm,  V3d->V3sm
        self.add_xross_sync_variation( [("3p g V", "3s m V"), ("3d g V", "3s m V")])
        # syn G3:d->pf
        self.add_xross_sync_variation( [("3d g "+PC, "3p f "+PC) for PC in self.TENSES_CASES_PC])
        # syn V3:dm->pf
        self.add_xross_sync_variation( [("3d m V", "3p f V")])
        # syn V3:p->sm
        self.add_xross_sync_variation( [("3p g V", "3s m V")])
        # syn Gd: 3f->2m
        self.add_xross_sync_variation( [("3d f "+PC, "2d m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2sf -> G3pm
        self.add_xross_sync_variation( [("2s f "+PC, "3p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3pf -> G2pm
        self.add_xross_sync_variation( [("3p f "+PC, "2p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2sm -> G1pm
        self.add_xross_sync_variation( [("2s m "+PC, "1p m "+PC) for PC in self.TENSES_CASES_PC])
        # syn G2p -> G2sf; G2d -> G2sf
        self.add_xross_sync_variation( [("2p g "+PC, "2s f "+PC) for PC in self.TENSES_CASES_PC]+[("2d g "+PC, "2d f "+PC) for PC in self.TENSES_CASES_PC])
        # syn G3p ->  G1sm
        self.add_xross_sync_variation( [("3p g "+PC, "1s m "+PC) for PC in self.TENSES_CASES_PC])
        # G: s/d: 3f -> 2m
        self.add_xross_sync_variation( [("3d f "+PC, "2d m "+PC) for PC in self.TENSES_CASES_PC]+[("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # s: 3f -> 2m
        self.add_xross_sync_variation( [("3s f "+T, "2s m "+T) for T in self.TENSES_CASES])
        # Vs: 2f -> 1(m)
        self.add_xross_sync_variation( [("2s f V", "1s m V")])
        # G: 3sf -> 2sm, 2pm -> 2sm
        self.add_xross_sync_variation( [("3s f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # Vs: 2m->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])
        # Vs: 2m->1, 3f->1
        self.add_xross_sync_variation( [("2s m V", "1s m V")])
        # 3: d->pm
        self.add_xross_sync_variation( [("3d g "+T, "3p m "+T) for T in self.TENSES_CASES])
        # G2:pf->sm
        self.add_xross_sync_variation( [("2p f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # G2:p/df->sm
        self.add_xross_sync_variation( [("2p f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC]+[("2d f "+PC, "2s m "+PC) for PC in self.TENSES_CASES_PC])
        # G: 2pf->3sm
        self.add_xross_sync_variation( [("2p f "+PC, "3s m "+PC) for PC in self.TENSES_CASES_PC])
        # V3:pf->sm
        self.add_xross_sync_variation( [("3p f V", "3s m V")])
        # G:3pf->2sf
        self.add_xross_sync_variation( [("3p f "+PC, "2s f "+PC) for PC in self.TENSES_CASES_PC])
        # G:2p -> 1s
        self.add_xross_sync_variation( [("2p g "+PC, "1s g "+PC) for PC in self.TENSES_CASES_PC])
        # G:3p -> 2s
        self.add_xross_sync_variation( [("3p g "+PC, "2s g "+PC) for PC in self.TENSES_CASES_PC])
        # G:3p -> 3d
        self.add_xross_sync_variation( [("3p g "+PC, "3d g "+PC) for PC in self.TENSES_CASES_PC])
        # J3p -> S2d
        self.add_xross_sync_variation( [("3p g J", "2d g S")])
        # J3p -> S3p, J3s -> G2s
        self.add_xross_sync_variation( [("3p g J", "3p g S"),("3s g J", "2s g G")])


    def _create_syncretic_TENSE_files(self):
        # syn p: G -> V
        self.add_ten_sync_variation( [("zp g G", "zp g V")])
        # syn s: G -> V
        self.add_ten_sync_variation( [("zs g G", "zs g V")])
        # syn 2: G -> V
        self.add_ten_sync_variation( [("2a g G", "2a g V")])
        # syn 3: G -> V
        self.add_ten_sync_variation( [("3a g G", "3a g V")])
        # syn p: V -> G
        self.add_ten_sync_variation( [("zp g V", "zp g G")])
        # syn s: V -> G
        self.add_ten_sync_variation( [("zs g V", "zs g G")])
        # syn 2: V -> G
        self.add_ten_sync_variation( [("2a g V", "2a g G")])
        # syn 3: V -> G
        self.add_ten_sync_variation( [("3a g V", "3a g G")])
        # syn 3p: V -> G,  2s: G -> V
        self.add_ten_sync_variation( [("3p g V", "3p g G"),("2s g G", "2s g V")])
        # syn 2: V -> G,  p: G -> V
        self.add_ten_sync_variation( [("2a g V", "3a g G")]+[("zp g G", "zp g V")])
        # syn 2s: G -> S
        self.add_ten_sync_variation( [("2s g G", "2s g S")])
        # syn p: S -> G
        self.add_ten_sync_variation( [("zp g S", "zp g G")])
        # syn 3p: V -> S,  2s: G -> S
        self.add_ten_sync_variation( [("3p g V", "3p g S"),("2s g G", "2s g S")])
        # syn 2: G -> V,  p: S -> V
        self.add_ten_sync_variation( [("zp g S", "zp g V")]+[("2a g G", "3a g V")])
        # syn p: G -> V
        self.add_ten_sync_variation( [("zp g "+PC, "zp g V") for PC in self.TENSES_CASES_PC])
        # syn s: G -> V
        self.add_ten_sync_variation( [("zs g "+PC, "zs g V") for PC in self.TENSES_CASES_PC])
        # syn 2: G -> V
        self.add_ten_sync_variation( [("2a g "+PC, "2a g V") for PC in self.TENSES_CASES_PC])
        # syn 3: G -> V
        self.add_ten_sync_variation( [("3a g "+PC, "3a g V") for PC in self.TENSES_CASES_PC])
        # 3p: J -> S
        self.add_ten_sync_variation( [("3p g J", "3p g S")])
        # 2s: S -> J
        self.add_ten_sync_variation(  [("2s g S", "2s g J")])
        # 3p: J/S -> G
        self.add_ten_sync_variation( [("3p g J", "3p g G"),("3p g S", "3p g G")])




class PermSynCreatorGER(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "GER"

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

    def _create_variations(self):
        # randoms:
        self._create_random_PERM_files()
        self._create_random_SYN_files()
        self._create_random_PERM_dims_files()
        self._create_random_SYN_dims_files()
        # permutations:
        self._create_permutation_PERS_files()
        self._create_permutation_NUM_files()
        self._create_permutation_TENSE_files()
        self._create_permutation_X_files()
        # syncretic variants:
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

    def _create_permutation_PERS_files(self):
        """
        creates all permutation files where PERS-features are swapped (1 <-> 2 <-> 3)
        """
        # d: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # s: 1 <-> 2, p:1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # s: 2 <-> 3
        self.add_pers_perm_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # s: 2 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d:1 <-> 3, s: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d:1 <-> 2, s: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d: 1 <-> 2
        self.add_pers_perm_variation( [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # s: 2 <-> 3, p: 2 <-> 3, d: 1 <-> 2
        self.add_pers_perm_variation(
                                [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("1d g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # d: 1 <-> 3, p: 2 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # pG: 2 <-> 3, sG: 3<-> 2, dG: 2<->3
        self.add_pers_perm_variation( [("2a g G", "3a g G")])

        # sV: 1 <-> 3, dV: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g V", "3s g V"), ("2d g V", "3d g V"), ("1p g V", "2p g V")])

        # sG: 1 <-> 3, dG: 2 <-> 3, pV: 1<->2
        self.add_pers_perm_variation( [("1s g G", "3s g G")] + [("2d g G", "3d g G")] + [("1p g V", "2p g V")])

        # d: 1 <-> 3
        self.add_pers_perm_variation( [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES])

        # s: 1 <-> 3
        self.add_pers_perm_variation( [("1s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # s: 1 <-> 2
        self.add_pers_perm_variation( [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES])

        # p: 1 <-> 3
        self.add_pers_perm_variation( [("1p g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # p: 1 <-> 2
        self.add_pers_perm_variation( [("1p g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # p: 2 <-> 3
        self.add_pers_perm_variation( [("3p g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # d: 1 <-> 2, s: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1s g " + T, "3s g " + T) for T
                                                                                       in self.TENSES_CASES])

        # p: 2 <-> 3, d: 2 <-> 3, s: 1 <-> 3
        self.add_pers_perm_variation(
                                [("2p g " + T, "3p g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES] + [
                                    ("1s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # d: 1 <-> 2, p: 1 <-> 2
        self.add_pers_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # d: 2 <-> 3
        self.add_pers_perm_variation( [("2d g G", "3d g G")])

        # dG: 2 <-> 1, pG: 2 <-> 1, dV: 2 <-> 3, pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g G", "1d g G"), ("2p g G", "1p g G"), ("2d g V", "3d g V"),
                                                ("2p g V", "3p g V")])

        # dG: 2 <-> 3, pG: 2 <-> 3
        self.add_pers_perm_variation( [("2d g G", "3d g G"), ("2p g G", "3p g G")])

        # dG: 2 <-> 1, pG: 2 <-> 1, sV: 2 <-> 3
        self.add_pers_perm_variation( [("1d g G", "2d g G"), ("1p g G", "2p g G"), ("2s g V", "3s g V")])

        # sV: 2 <-> 3, pG: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V"), ("2p g G", "3p g G")])

        # d,p: 1 <-> 3
        self.add_pers_perm_variation(
                                [("1d g " + T, "3d g " + T) for T in self.TENSES_CASES] + [("1p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # dV,pV: 2 <-> 3
        self.add_pers_perm_variation( [("2d g V", "3d g G"), ("2p g V", "3p g G")])

        # V: 2 <-> 3
        self.add_pers_perm_variation( [("2a g V", "3a g V")])

        # Vs: 2 <-> 3
        self.add_pers_perm_variation( [("2s g V", "3s g V")])

        # Vs: 1 <-> 3
        self.add_pers_perm_variation( [("1s g V", "3s g V")])

        # dV,pV: 1 <-> 3
        self.add_pers_perm_variation( [("1d g V", "3d g V"), ("1p g V", "3p g V")])

        # dG,pG: 1 <-> 2, sV: 1 <-> 2, pV,dV: 2 <-> 3
        self.add_pers_perm_variation( [("1d g G", "2d g G"), ("1p g G", "2p g G"), ("1s g V", "2s g V"),
                                                ("2p g V", "3p g V")] + [("2d g V", "3d g V")])

        # sG: 1 <-> 2, pG,dG: 2 <-> 3
        self.add_pers_perm_variation( [("1s g G", "2s g G"), ("2d g G", "3d g G"), ("2p g G", "3p g G")])

        # V: 1<->2
        self.add_pers_perm_variation( [("1a g V", "2a g V")])

        # STRONG

        # strong permutation 1
        self.add_pers_perm_variation(
                                [("1s g G", "3s g G"), ("3s g V", "2s g V"), ("2d g G", "3d g G"), ("1d g V", "2d g V"),
                                 ("1p g G", "2p g G"), ("3p g V", "1p g V")])

        # strong permutation 2
        self.add_pers_perm_variation(
                                [("1s g G", "2s g G"), ("1s g V", "2s g V"), ("2d g G", "3d g G"), ("2d g V", "1d g V"),
                                 ("3p g G", "2p g G"), ("3p g V", "1p g V")])

        # strong permutation 3
        self.add_pers_perm_variation(
                                rotate_right_list=[("1s g G", "2s g G", "3s g G"), ("1d g G", "2d g G", "3d g G"),
                                                   ("1p g G", "2p g G", "3p g G"), ("1p g V", "2p g V", "3p g V")],
                                rotate_left_list=[("1d g V", "2d g V", "3d g V")])

        # dG: 1 <-> 2, pG: 1 <-> 2
        # dV: 2 <-> 3, pV: 2 <-> 3
        # sV: 1 <-> 3, sG: 2 <-> 3
        self.add_pers_perm_variation(
                                [("2d g G", "1d g G"), ("2p g G", "1p g G"), ("2d g V", "3d g V"), ("2p g V", "3p g V"),
                                 ("1s g V", "3s g V"), ("2s g G", "3s g G")])

        # dG: 1->2->3, pG: 1->2->3;  sV: 1->2->3
        # dV: 3->2->1, pV: 3->2->1;  sG: 3->2->1
        self.add_pers_perm_variation(
                                rotate_left_list=[("3d g V", "1d g V", "2d g V"), ("3p g V", "1p g V", "2p g V"),
                                                  ("3s g G", "1s g G", "2s g G")],
                                rotate_right_list=[("2d g G", "3d g G", "1d g G"), ("2p g G", "3p g G", "1p g G"),
                                                   ("2s g V", "3s g V", "1s g V")])

        # dG: 2 <-> 3, pG: 2 <-> 3
        # dV: 1 <-> 2, pV: 1 <-> 2
        # sG: 1 <-> 3, sV: 1 <-> 3
        self.add_pers_perm_variation(
                                [("2d g G", "3d g G"), ("2p g G", "3p g G"), ("2d g V", "1d g V"), ("2p g V", "1p g V"),
                                 ("1s g G", "3s g G"), ("1s g V", "3s g V")])

        # sG: 1->2->3
        # sV: 3->2->1
        # dG: 1 <-> 3,  pG: 1 <-> 3
        # dV: 1 <-> 2,  pV: 1 <-> 2
        self.add_pers_perm_variation( rotate_left_list=[("3s g V", "1s g V", "2s g V")],
                                rotate_right_list=[("2s g G", "3s g G", "1s g G")],
                                swap_list=[("3d g G", "1d g G"), ("3p g G", "1p g G"), ("2d g V", "1d g V"),
                                           ("2p g V", "1p g V")])

        # dG: 1->2->3,  pG: 1->2->3
        # dV: 3->2->1,  pV: 3->2->1
        # s: 1 <-> 3
        self.add_pers_perm_variation(
                                rotate_left_list=[("3d g V", "1d g V", "2d g V"), ("3p g V", "1p g V", "2p g V")],
                                rotate_right_list=[("2d g G", "3d g G", "1d g G"), ("2p g G", "3p g G", "1p g G")],
                                swap_list=[("3s g G", "1s g G"), ("3s g V", "1s g V")])

    def _create_permutation_NUM_files(self):
        """
        creates all permutation files where NUM-features are swapped (s <-> d <-> p)
        """

        # 1: s <-> d
        self.add_num_perm_variation( [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p
        self.add_num_perm_variation( [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES])

        # 2: s <-> p, 3: s <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3s g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2: s <-> p, 3: d <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 1: s <-> p
        self.add_num_perm_variation( [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES])

        # 1: s <-> d, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g " + T, "1d g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2: s <-> d, 3: d <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2G: s <-> p
        self.add_num_perm_variation( [("2s g G", "2p g G")])

        # 2G: s <-> p, 3V: d<->p
        self.add_num_perm_variation( [("2s g G", "2p g G"), ("3d g V", "3p g V")])

        # 3G:s<->p, 2V:d<->p, 1: s<->d
        self.add_num_perm_variation(
                                [("3s g G", "3p g G"), ("2d g V", "2p g V")] + [("1s g " + T, "1d g " + T) for T in
                                                                                self.TENSES_CASES])

        # 2: s <-> d, 3: s <-> d
        self.add_num_perm_variation(
                                [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("3s g " + T, "3d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2: s <-> d, 1: s <-> d
        self.add_num_perm_variation(
                                [("2s g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("1s g " + T, "1d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2: s <-> p, 1: s <-> d
        self.add_num_perm_variation(
                                [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("1s g " + T, "1d g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 1V: s <-> d, 3G: s <-> d
        self.add_num_perm_variation( [("1s g V", "1d g V"), ("3s g G", "3d g G")])

        # 1G: s <-> d, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g G", "1d g G")] + [("2p g " + T, "2d g " + T) for T in self.TENSES_CASES])

        # 3: s <-> p
        self.add_num_perm_variation( [("3s g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 1: s <-> p, 2: d <-> p
        self.add_num_perm_variation(
                                [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2d g " + T, "2p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # 2V: s <-> p, 3V: s <-> p
        self.add_num_perm_variation( [("2s g V", "2p g V"), ("3s g V", "3p g V")])

        # 2V: s <-> p
        self.add_num_perm_variation( [("2s g V", "2p g V")])

        # 2V: s <-> p, 3G: s <-> p
        self.add_num_perm_variation( [("2s g V", "2p g V"), ("3s g G", "3p g G")])

        # 3G: s <-> p
        self.add_num_perm_variation( [("3s g G", "3p g G")])

        # 1: s -> d -> p;   3: p -> d -> s
        self.add_num_perm_variation(
                                rotate_left_list=[("3s g " + T, "3d g " + T, "3p g " + T) for T in self.TENSES_CASES],
                                rotate_right_list=[("1s g " + T, "1d g " + T, "1p g " + T) for T in self.TENSES_CASES])

        # 3: s -> d -> p;   2: p -> d -> s
        self.add_num_perm_variation(
                                rotate_left_list=[("2s g " + T, "2d g " + T, "2p g " + T) for T in self.TENSES_CASES],
                                rotate_right_list=[("3s g " + T, "3d g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # V: s -> d -> p
        self.add_num_perm_variation( rotate_left_list=[("zs g V", "zd g V", "zp g V")],
                                rotate_right_list=[("zs g V", "zd g V", "zp g V")])

        # 1G: s <-> p
        self.add_num_perm_variation( [("1s g G", "1p g G")])

        # strong permutation 1
        self.add_num_perm_variation(
                                [("1s g G", "1p g G"), ("1s g V", "1d g V"), ("2d g G", "2p g G"), ("2d g V", "2s g V"),
                                 ("3p g G", "3s g G"), ("3p g V", "3s g V")])

        # strong permutation 2
        self.add_num_perm_variation(
                                [("1s g G", "1p g G"), ("1s g V", "1d g V"), ("2d g G", "2s g G"), ("2d g V", "2p g V"),
                                 ("3p g G", "3s g G"), ("3d g V", "3p g V")])

        # strong permutation 3
        self.add_num_perm_variation(
                                rotate_left_list=[("1s g G", "1d g G", "1p g G")] + [("2s g V", "2d g V", "2p g V")] + [
                                    ("3s g G", "3d g G", "3p g G")] + [("3s g V", "3d g V", "3p g V")],
                                rotate_right_list=[("2s g G", "2d g G", "2p g G")])

        # 2:  s <-> p
        # 3V: s <-> p, 1G: s <-> p
        self.add_num_perm_variation(
                                [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3s g V", "3p g V"),
                                                                                       ("1s g G", "3p g G")])

        # 2G s <-> p, 3V s <-> d,
        # 3G d <-> p
        # 1: s <-> d
        self.add_num_perm_variation( [("2s g G", "2p g G"), ("3s g V", "3d g V"), ("3d g G", "3p g G")] + [
            ("1s g " + T, "1d g " + T) for T in self.TENSES_CASES])

    def _create_permutation_TENSE_files(self):
        """
        creates all permutation files where TENSE-features are swapped (V <-> F)
        """
        # 2s : G <-> V, 3p: G <-> V, 1d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G"), ("3p g V", "3p g G"), ("1d g V", "1d g G")])

        # 2s: G <-> V, 3p: G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("2s g V", "2s g G"), ("3p g V", "3p g G"), ("3d g V", "3d g G")])

        # 1s: G <-> V, 3s: G <-> V, 1p: G <-> V, 2p: G <-> V
        self.add_ten_perm_variation( [("1s g V", "1s g G"), ("1p g V", "1p g G"), ("3s g V", "3s g G"),
                                              ("2p g V", "2p g G")])

        # 2 : G <-> V
        self.add_ten_perm_variation( [("2a g V", "2a g G")])

        # 3 : G <-> V
        self.add_ten_perm_variation( [("3a g V", "3a g G")])

        # s : G <-> V
        self.add_ten_perm_variation( [("zs g V", "zs g G")])

        # p : G <-> V
        self.add_ten_perm_variation( [("zp g V", "zp g G")])

        # s : G <-> V, 3d: G <-> V
        self.add_ten_perm_variation( [("3d g V", "3d g G")] + [("zs g V", "zs g G")])

        # 1p : G <-> V, 3s : G <-> V
        self.add_ten_perm_variation( [("1p g V", "1p g G"), ("3s g V", "3s g G")])

        # 1 : G <-> V, 3d : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G"), ("3d g V", "3d g G")])

        # s : G <-> V, 1p : G <-> V, 2d : G <-> V
        self.add_ten_perm_variation( [("1p g V", "1p g G"), ("2d g V", "2d g G")] + [("zs g V", "zs g G")])

        # 3s : G <-> V, 2s : G <-> V
        self.add_ten_perm_variation( [("3s g V", "3s g G"), ("2s g V", "2s g G")])

        # p, d : G <-> V
        self.add_ten_perm_variation( [("zd g V", "zd g G")] + [("zp g V", "zp g G")])

        # 1 : G <-> V
        self.add_ten_perm_variation( [("1a g V", "1a g G")])

        # 3p, 3d
        self.add_ten_perm_variation( [("3p g G", "3p g V"), ("3d g G", "3d g V")])

        # 2s, 1p, 1d, 3p, 3d
        self.add_ten_perm_variation(
                                [("2s g G", "2s g V"), ("1p g G", "1p g V"), ("1d g G", "1d g V"), ("3p g G", "3p g V"),
                                 ("3d g G", "3d g V")])

        # 2s, 1p, 1d
        self.add_ten_perm_variation( [("2s g G", "2s g V"), ("1p g G", "1p g V"), ("1d g G", "1d g V")])

        # 3d, 2p, 2s, 1s, 3s
        self.add_ten_perm_variation(
                                [("3d g G", "3d g V"), ("2p g G", "2p g V"), ("2s g G", "2s g V"), ("1s g G", "1s g V"),
                                 ("3s g G", "3s g V")])

        # 2d, 3d, 2s, 1d, 1p
        self.add_ten_perm_variation(
                                [("2d g G", "2d g V"), ("3d g G", "3d g V"), ("2s g G", "2s g V"), ("1d g G", "1d g V"),
                                 ("1p g G", "1p g V")])

        # 1d, 1p, 2p, 2d, 3s
        self.add_ten_perm_variation(
                                [("1d g G", "1d g V"), ("1p g G", "1p g V"), ("2d g G", "2d g V"), ("2p g G", "2p g V"),
                                 ("3s g G", "3s g V")])

    def _create_permutation_X_files(self):
        """
        creates all permutation files where many fields are swapped
        """

        # full permutation 1
        perm_full1 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "3s g V")] + [("2s g G", "1d g V")] + [("3s g G", "2p g G")] + [
                                    ("3p g G", "3d g V")] + [(
                                    "1s g V", "2s g V")] + [("2p g V", "1p g V")] + [("3d g G", "1d g G")] + [
                                    ("2d g G", "2d g V")] + [(
                                    "1p g G", "3p g V")]
                                )

        # full permutation 2
        perm_full2 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "2d g G")] + [("2s g V", "1p g V")] + [("3p g V", "3p g G")] + [
                                    ("1d g V", "3s g V")] + [(
                                    "1s g V", "3d g V")] + [("3d g G", "2p g V")] + [("2d g V", "2s g G")] + [
                                    ("3s g G", "1d g G")] + [(
                                    "1p g G", "2p g G")]
                                )

        # full permutation 3
        perm_full3 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "2d g V")] + [("2p g G", "2s g G")] + [("3d g G", "1p g V")] + [
                                    ("1s g V", "1p g G")] + [(
                                    "3s g V", "3s g G")] + [("3d g V", "1d g G")] + [("1d g G", "2p g V")] + [
                                    ("2s g V", "3p g G")] + [(
                                    "3p g V", "2d g G")]
                                )

        # full permutation 4
        perm_full4 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "1d g G")] + [("2d g G", "2p g G")] + [("3s g G", "3p g G")] + [
                                    ("1s g V", "2s g V")] + [(
                                    "2p g V", "3p g V")] + [("1d g V", "3d g V")] + [("1p g V", "3d g G")] + [
                                    ("2s g G", "3s g V")] + [(
                                    "1p g G", "2d g V")]
                                )

        # full permutation 5
        perm_full5 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "2p g V")] + [("3p g G", "2s g V")] + [("2d g G", "1d g V")] + [
                                    ("1s g V", "3d g G")] + [(
                                    "2d g V", "2p g G")] + [("3p g V", "3s g G")] + [("1p g V", "2s g G")] + [
                                    ("3s g V", "1p g G")] + [(
                                    "3d g V", "1d g G")]
                                )

        # full permutation 6
        perm_full6 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g " + T, "2s g " + T) for T in self.TENSES_CASES] + [("1d g " + T, "2p g " + T) for T
                                                                                       in
                                                                                       self.TENSES_CASES] + [
                                    ("3s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [(
                                    "2d g " + T, "3p g " + T) for T in self.TENSES_CASES]
                                )

        # full permutation 7
        perm_full7 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("2s g " + T, "1d g " + T) for T
                                                                                       in
                                                                                       self.TENSES_CASES] + [
                                    ("3s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [(
                                    "3d g " + T, "3p g " + T) for T in self.TENSES_CASES]
                                )

        # full permutation 8
        perm_full8 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3s g " + T, "2s g " + T) for T
                                                                                       in
                                                                                       self.TENSES_CASES] + [
                                    ("1d g " + T, "1p g " + T) for T in self.TENSES_CASES] + [(
                                    "3p g " + T, "2d g " + T) for T in self.TENSES_CASES]
                                )

        # rotations
        # full permutation 9
        perm_full9 = copy.deepcopy(self.org_conj_dict)

        right = [("1s g " + T, "2p g " + T, "2d g " + T) for T in self.TENSES_CASES] + [
            ("2s g " + T, "3p g " + T, "1d g " + T)
            for T in self.TENSES_CASES] + [
                    ("3s g " + T, "1p g " + T,
                     "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_right_list=right)

        # full permutation 10
        perm_full10 = copy.deepcopy(self.org_conj_dict)

        right = [("1s g " + T, "2s g " + T, "3s g " + T) for T in self.TENSES_CASES]
        left = [("1d g " + T, "2d g " + T, "3d g " + T) for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 11
        perm_full11 = copy.deepcopy(self.org_conj_dict)

        right = [("3s g " + T, "2p g " + T, "1d g " + T) for T in self.TENSES_CASES]
        left = [("1s g " + T, "1p g " + T, "2s g " + T) for T in self.TENSES_CASES] + [
            ("3d g " + T, "2d g " + T, "3p g " + T)
            for T in self.TENSES_CASES]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 12
        perm_full12 = copy.deepcopy(self.org_conj_dict)
        right = [("1s g G", "2p g V", "3d g G")] + [("2s g G", "2s g V", "1d g V")] + [("3s g V", "1p g V", "1p g G")]
        left = [("2d g V", "3p g V", "3s g G")] + [("2d g G", "2p g G", "3p g G")] + [("1d g G", "1s g V", "3d g V")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 13
        perm_full13 = copy.deepcopy(self.org_conj_dict)
        right = [("1d g G", "1s g V", "2d g V")]
        left = [("1s g G", "2s g G", "3p g V")] + [("1p g G", "1d g V", "2d g G")] + [
            ("3s g G", "3s g V", "3d g V")] + [
                   ("3p g G",
                    "3d g G",
                    "1p g V")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # full permutation 14
        perm_full14 = copy.deepcopy(self.org_conj_dict)
        left = [("1a g G", "1a g V", "3a g G")] + [("2a g G", "2a g V", "3a g V")]
        self.add_xross_perm_variation( rotate_left_list=left)

        # full permutation 15
        perm_full15 = copy.deepcopy(self.org_conj_dict)

        left = [("zs g G", "zs g V", "zp g G")]
        right = [("zp g V", "zd g G", "zd g V")]
        self.add_xross_perm_variation( rotate_left_list=left, rotate_right_list=right)

        # 2sG <-> 3sV,
        # 2pG<-> 2sV
        # 1s <-> 1p
        # V: 2d <-> 3d, V:2p <-> 3p
        # 3G: d <-> p
        perm_full16 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("2s g G", "3s g V")] + [("2p g G", "2s g V")] + [("1s g " + T, "1p g " + T) for T in
                                                                                   self.TENSES_CASES] + [("2d g V",
                                                                                                      "3d g V")] + [(
                                    "2p g V", "3p g V")] + [("3d g G", "3p g G")]
                                )

        # 2G: s <-> p
        # Vp: 1 <-> 3, Vd: 1 <-> 3
        # Vs: 1 <-> 2
        perm_full17 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("2s g G", "2p g G")] + [("1p g V", "3p g V")] + [("1d g V", "3d g V")] + [
                                    ("1s g V", "2s g V")]
                                )

        # 1G: s <-> p
        # V: 1d  <-> 2d, V: 1p <-> 2p
        # 3pV <-> 2pG;  2sG <-> 3pG
        perm_full18 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "1p g G")] + [("1d g V", "2d g V")] + [("1p g V", "2p g V")] + [
                                    ("3p g V", "2p g G")] + [(
                                    "3p g G", "2s g G")]
                                )

        perm_full19 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "2d g G")] + [("1s g V", "3d g V")] + [("2s g G", "3d g G")] + [
                                    ("2s g V", "2p g G")] + [(
                                    "3s g G", "3p g V")] + [("3s g V", "1p g G")] + [("1d g G", "3p g G")] + [
                                    ("1d g V", "2d g V")] + [(
                                    "1p g V", "2p g V")]
                                )

        perm_full20 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "1s g V")] + [("2s g G", "3p g G")] + [("2s g V", "3s g G")] + [
                                    ("2p g V", "3s g V")] + [(
                                    "3p g V", "1p g V")] + [("1p g G", "2d g V")] + [("2p g G", "1d g V")] + [
                                    ("3d g V", "2d g G")] + [(
                                    "1d g G", "3d g G")]
                                )

        perm_full21 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("3s g V", "2d g V")] + [("2p g G", "3d g V")] + [("1d g V", "1p g G")] + [
                                    ("2s g V", "1s g V")] + [(
                                    "2d g G", "3d g G")] + [("3p g V", "3p g G")] + [("1s g G", "2s g G")] + [
                                    ("3s g G", "1d g G")] + [(
                                    "1p g V", "2p g V")]
                                )

        perm_full22 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("3d g V", "2d g V")] + [("2p g G", "1p g G")] + [("1s g V", "1d g V")] + [
                                    ("2s g V", "3s g V")] + [(
                                    "2d g G", "2p g V")] + [("3d g G", "3p g G")] + [("1s g G", "1p g V")] + [
                                    ("2s g G", "1d g G")] + [(
                                    "3s g G", "3p g V")]
                                )

        perm_full23 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "3d g V")] + [("2d g G", "1s g V")] + [("2s g G", "2p g G")] + [
                                    ("3d g G", "2s g V")] + [(
                                    "3s g G", "1p g G")] + [("3p g V", "3s g V")] + [("1d g G", "2d g V")] + [
                                    ("3p g G", "1d g V")] + [(
                                    "1p g V", "2p g V")]
                                )

        perm_full24 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "3d g G")] + [("3s g V", "2d g V")] + [("2s g G", "3p g V")] + [
                                    ("3d g V", "2s g V")] + [(
                                    "1s g V", "2p g G")] + [("3s g G", "3p g G")] + [("1d g V", "1p g V")] + [
                                    ("2p g V", "2d g G")] + [(
                                    "1p g G", "1d g G")]
                                )

        perm_full25 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "1s g V")] + [("2d g G", "3d g V")] + [("2s g G", "2s g V")] + [
                                    ("3d g G", "2p g G")] + [(
                                    "3s g G", "3s g V")] + [("3p g V", "1p g G")] + [("1d g G", "1d g V")] + [
                                    ("3p g G", "2d g V")] + [(
                                    "1p g V", "2p g V")]
                                )

        perm_full26 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "3s g G")] + [("2s g G", "1d g G")] + [("2d g G", "3p g V")] + [
                                    ("3d g G", "3p g G")] + [(
                                    "1s g V", "3s g V")] + [("2s g V", "1d g V")] + [("3d g V", "1p g G")] + [
                                    ("2p g G", "2d g V")]
                                )

        perm_full27 = copy.deepcopy(self.org_conj_dict)
        self.add_xross_perm_variation(
                                [("1s g G", "3p g V")] + [("3d g G", "3p g G")] + [("2d g G", "2d g V")] + [
                                    ("2p g G", "2s g V")] + [(
                                    "3d g V", "1p g G")] + [("3s g G", "1d g V")] + [("2s g G", "1d g G")]
                                )

        # NORMAL

        # 2 : G <-> V, 3: s <-> p
        self.add_xross_perm_variation(
                                [("2a g G", "2a g V")] + [("3s g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # 3p <-> 1s, pV: 2 <-> 1
        self.add_xross_perm_variation(
                                [("2p g V", "1p g V")] + [("3p g " + T, "1s g " + T) for T in self.TENSES_CASES])

        # 3dV <-> 1sG, 2pV <-> 3sV, 2pG <-> 1dV, 3sG <-> 3dG
        self.add_xross_perm_variation(
                                [("3d g V", "1s g G")] + [("2p g V", "3s g V")] + [("2p g G", "1d g V")] + [
                                    ("3s g G", "3d g G")])

        # 1d <-> 2d, 2pV <-> 3pG, 3sG <-> 1pV
        self.add_xross_perm_variation(
                                [("1d g " + T, "2d g " + T) for T in self.TENSES_CASES] + [("2p g V", "3p g G")] + [
                                    ("3s g G", "1p g V")])

        # 2G <-> 3V, sG <-> pV
        self.add_xross_perm_variation( [("2a g G", "3a g V")] + [("zs g G", "zp g V")])

        # d: 1G <-> 3V,  p: 1G <-> 3V,
        # s: 3G <-> 2V
        self.add_xross_perm_variation(
                                [("1d g G", "3d g V")] + [("1p g G", "3p g V")] + [("3s g G", "2s g V")])

        # V: 3p <-> 2s, Vs3 <-> Gs1
        self.add_xross_perm_variation( [("3p g V", "2s g V"), ("3s g V", "1s g G")])

        # full swap 1
        old_list = [
            ("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
             "3p g " + T) for T in self.TENSES_CASES]
        new_list = [
            ("2s g " + T, "3p g " + T, "3d g " + T, "3s g " + T, "1p g " + T, "1d g " + T, "1s g " + T, "2p g " + T,
             "2d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

        # full swap 2
        old_list = [
            ("1s g " + T, "1d g " + T, "1p g " + T, "2s g " + T, "2d g " + T, "2p g " + T, "3s g " + T, "3d g " + T,
             "3p g " + T) for T in self.TENSES_CASES]
        new_list = [
            ("2s g " + T, "1s g " + T, "3s g " + T, "2d g " + T, "1p g " + T, "3p g " + T, "2p g " + T, "1d g " + T,
             "3d g " + T) for T in self.TENSES_CASES]
        full_swap = [(old_list[i], new_list[i]) for i in range(len(old_list))]
        self.add_xross_perm_variation( full_swap_list=full_swap)

    def _create_syncretic_NUM_files(self):
        # syn: d -> p (TRUE)
        self.add_num_sync_variation( [("zd" + " g " + T, "zp" + " g " + T) for T in self.TENSES_CASES])

        # syn: s -> p (FALSE)
        self.add_num_sync_variation( [("zs" + " g " + T, "zp" + " g " + T) for T in self.TENSES_CASES])

        # syn: s -> d (FALSE)
        self.add_num_sync_variation( [("zs" + " g " + T, "zd" + " g " + T) for T in self.TENSES_CASES])

        # syn: V: s -> p (FALSE)
        self.add_num_sync_variation( [("zs" + " g V", "zp" + " g V")])

        # syn: 2: s -> p, 3: p -> s (FALSE)
        self.add_num_sync_variation(
                                [("2s g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "3s g " + T) for T
                                                                                       in self.TENSES_CASES])

        # V2: s -> d; G3: p -> d (FALSE)
        self.add_num_sync_variation( [("2s g V", "2d g V"), ("3p g G", "3d g G")])

        # syn: 1: s -> p (FALSE)
        self.add_num_sync_variation( [("1s g " + T, "1p g " + T) for T in self.TENSES_CASES])

        # syn: p -> d (FALSE)
        self.add_num_sync_variation( [("zp" + " g " + T, "zd" + " g " + T) for T in self.TENSES_CASES])

    def _create_syncretic_PERS_files(self):
        # syn: p: 1 -> 3 (TRUE)
        self.add_pers_sync_variation( [("1p g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # syn: V: 1 -> 3 (TRUE)
        self.add_pers_sync_variation( [("1a g V", "3a g V")])

        # syn: Vs: 1 -> 3 (TRUE)
        self.add_pers_sync_variation( [("1s g V", "3s g V")])

        # syn: V,Gp: 1 -> 3 (TRUE)
        self.add_pers_sync_variation( [("1p g G", "3p g G"), ("1a g V", "3a g V")])

        # syn: p: 1 -> 3, 2 -> 3 (TRUE)
        self.add_pers_sync_variation(
                                [("1p g " + T, "3p g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # syn: p,Vs: 1 -> 3, 2 -> 3 (TRUE)
        self.add_pers_sync_variation(
                                [("1s g V", "3s g V"), ("2s g V", "3s g V")] + [("1p g " + T, "3p g " + T) for T in
                                                                                self.TENSES_CASES] + [
                                    ("2p g " + T, "3p g " + T) for T in self.TENSES_CASES])

        # NOTES:
        ## syn: p: 3 -> 1 (TRUE)
        ## syn: V: 3 -> 1 (TRUE)
        ## syn: Vs: 3 -> 1 (TRUE)
        ## syn: Gs: 2 -> 3 (TRUE)
        ## syn: p: 2 -> 1, 3 -> 1 (TRUE)
        ## syn: V: 3 -> 1, 2 -> 1 (TRUE)

        # NOTES:
        ## syn: V: 2 -> 3 (FALSE)
        ## syn: Gs: 1 -> 3 (FALSE)
        ## syn: s: 2 -> 3 (FALSE)
        ## syn: s: 2 -> 1, p: 2 -> 3 (FALSE)
        ## syn: V: 2 -> 1, G: 2 -> 3 (FALSE)
        ## syn: p: 3-> 2, Gs: 2 -> 1 (FALSE)

        # syn: V: 2 -> 3 (FALSE)
        self.add_pers_sync_variation( [("2a g V", "3a g V")])

        # syn: Gs: 1 -> 3 (FALSE)
        self.add_pers_sync_variation( [("1s g G", "3s g G")])

        # syn: s: 2 -> 3 (FALSE)
        self.add_pers_sync_variation( [("2s g " + T, "3s g " + T) for T in self.TENSES_CASES])

        # syn: s: 2 -> 1, p: 2 -> 3 (FALSE)
        self.add_pers_sync_variation(
                                [("2s g " + T, "1s g " + T) for T in self.TENSES_CASES] + [("2p g " + T, "3p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # syn: V: 2 -> 1, G: 2 -> 3 (FALSE)
        self.add_pers_sync_variation( [("2a g V", "1a g V"), ("2a g G", "3a g G")])

        # syn: p: 3-> 2, Gs: 2 -> 1 (FALSE)
        self.add_pers_sync_variation(
                                [("3p g " + T, "2p g " + T) for T in self.TENSES_CASES] + [("2s g G", "1s g G")])

        ###
        # syn: p: 3 -> 1 (FALSE)
        self.add_pers_sync_variation( [("3p g " + T, "1p g " + T) for T in self.TENSES_CASES])

        # syn: V: 3 -> 1 (FALSE)
        self.add_pers_sync_variation( [("3a g V", "1a g V")])

        # syn: Vs: 3 -> 1 (FALSE)
        self.add_pers_sync_variation( [("3s g V", "1s g V")])

        # syn: p: 2 -> 1, 3 -> 1 (FALSE)
        self.add_pers_sync_variation(
                                [("2p g " + T, "1p g " + T) for T in self.TENSES_CASES] + [("3p g " + T, "1p g " + T) for T
                                                                                       in self.TENSES_CASES])

        # syn: V: 3 -> 1, 2 -> 1 (FALSE)
        self.add_pers_sync_variation( [("2a g V", "1a g V"), ("3a g V", "1a g V")])

    def _create_syncretic_TENSE_files(self):
        # syn: 1: G -> V (FALSE)
        self.add_ten_sync_variation( [("1a g G", "1a g V")])

        # syn: 2: G -> V (FALSE)
        self.add_ten_sync_variation( [("2a g G", "2a g V")])

        # syn: 3: V -> G (FALSE)
        self.add_ten_sync_variation( [("3a g V", "3a g G")])

        # syn: s: G -> V (FALSE)
        self.add_ten_sync_variation( [("zs g G", "zs g V")])

        # syn: d: V -> G (FALSE)
        self.add_ten_sync_variation( [("zd g V", "zd g G")])

        # syn: 2s: V -> G, 3p: V -> G (FALSE)
        self.add_ten_sync_variation( [("2s g V", "2s g G"), ("3p g V", "3p g G")])

        # syn: 1s: G -> V, 3d: V -> G (FALSE)
        self.add_ten_sync_variation( [("1s g G", "1s g V"), ("3d g V", "3d g G")])

        # NOTES:
        # syn: 1: G -> V (FALSE)
        # syn: 2: G -> V (FALSE)
        # syn: 3: V -> G (FALSE)
        # syn: s: G -> V (FALSE)
        # syn: d: V -> G (FALSE)
        # syn: 2s: V -> G, 3p: V -> G (FALSE)
        # syn: 1s: G -> V, 3d: V -> G (FALSE)

        # syn: p: V -> G (FALSE)
        # syn: 1s: V->G, 2p: V->G (FALSE)
        # syn: 3s: V->G, 2p: G->V (FALSE)
        # syn: 3s: V->G, 1d: G->V (FALSE)

        # syn: p: V -> G (FALSE)
        self.add_ten_sync_variation( [("zp g V", "zp g G")])

        # syn: 1s: V->G, 2p: V->G (FALSE)
        self.add_ten_sync_variation( [("1s g V", "1s g G"), ("2p g V", "2p g G")])

        # syn: 3s: V->G, 2p: G->V (FALSE)
        self.add_ten_sync_variation( [("3s g V", "3s g G"), ("2p g G", "2p g V")])

        # syn: 3s: V->G, 1d: G->V (FALSE)
        self.add_ten_sync_variation( [("3s g V", "3s g G"), ("1d g G", "1d g V")])

    def _create_syncretic_X_files(self):
        # syn: G:3s -> 2p (TRUE)
        self.add_xross_sync_variation( [("3s g G", "2p g G")])

        # syn: G:3p -> 1s (TRUE)
        self.add_xross_sync_variation( [("3p g G", "1s g G")])

        # syn: V: 3p -> 2s (FALSE)
        self.add_xross_sync_variation( [("3p g V", "2s g V")])

        # syn: V: 1p -> 2s, 3p -> 3s (FALSE)
        self.add_xross_sync_variation( [("1p g V", "2s g V"), ("3p g V", "3s g V")])

        # syn: 3p -> 2s (FALSE)
        self.add_xross_sync_variation( [("3p g " + T, "2s g " + T) for T in self.TENSES_CASES])

        # syn: V: 3 -> 2, G: p -> s (FALSE)
        self.add_xross_sync_variation( [("3a g V", "2a g V")] + [("zp g G", "zs g G")])

        # syn: V: 3s -> 2p, G: s -> p (FALSE)
        self.add_xross_sync_variation( [("3s g V", "2p g V")] + [("zs g G", "zp g G")])

        # syn: V: 2 -> 1, G: 2 -> 3 (FALSE)
        self.add_xross_sync_variation( [("2a g V", "1a g V"), ("2a g G", "3a g G")])

        # Vs -> Gp
        self.add_xross_sync_variation( [("zs g V", "zp g G")])

        # V1 -> G2
        self.add_xross_sync_variation( [("1a g V", "2a g G")])

        # V2p -> Gs3; G2s -> Vp1
        self.add_xross_sync_variation( [("2p g V", "3s g G"), ("2s g G", "1p g V")])



class PermSynCreatorROM(PermSynCreator):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "ROM"

        self.TENSES_CASES = ["G", "V", "S", "C"]

        self.COMBINED = [p+n+" "+g+" "+t for t in self.TENSES_CASES for n in self.NUMBERS for p in self.PERSONS for g in self.GENDERS]

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
        self._create_syncretic_GEN_files()
        self._create_syncretic_NUM_files()
        self._create_syncretic_PERS_files()
        self._create_syncretic_TENSE_files()
        self._create_syncretic_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

class PermSynCreatorRob(PermSynCreatorSEM):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "rob_unif"

    def _create_variations(self):
        # randoms:
        self._create_random_PERM_files()
        self._create_random_PERM_dims_files()
        # permutations:
        self._create_permutation_PERS_files()
        self._create_permutation_NUM_files()
        self._create_permutation_GEN_files()
        self._create_permutation_TENSE_files()
        self._create_permutation_X_files()
        # shuffled permutations:
        self._create_SHUF_files()

class PermSynCreatorRobUnif(PermSynCreatorRob):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "rob_unif"


class PermSynCreatorRobRand1(PermSynCreatorRob):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "rob_rand1"


class PermSynCreatorRobRand2(PermSynCreatorRob):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "rob_rand2"


class PermSynCreatorRobRand3(PermSynCreatorRob):
    def __init__(self, name, file_ending=".tsv"):
        super().__init__(name, file_ending)
        self.lang_type = "rob_rand3"