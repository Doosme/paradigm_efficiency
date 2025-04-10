COMBINED_PRON = ["1s","2s","3s",
                 "1p","2p","3p","12p"
                ]

COMBINED_VERB_SEM = COMBINED_VERB_GER = \
            ["1s m G", "1s f G", "2s m G", "2s f G", "3s m G", "3s f G",
            "1p m G", "1p f G", "2p m G", "2p f G", "3p m G", "3p f G",
            "1d m G", "1d f G", "2d m G", "2d f G", "3d m G", "3d f G",
            "1s m V", "1s f V", "2s m V", "2s f V", "3s m V", "3s f V",
            "1p m V", "1p f V", "2p m V", "2p f V", "3p m V", "3p f V",
            "1d m V", "1d f V", "2d m V", "2d f V", "3d m V", "3d f V"
                     ]

#G,V,S
COMBINED_VERB_SA = ["1s m G", "1s f G", "2s m G", "2s f G", "3s m G", "3s f G",
            "1p m G", "1p f G", "2p m G", "2p f G", "3p m G", "3p f G",
            "1d m G", "1d f G", "2d m G", "2d f G", "3d m G", "3d f G",
            "1s m V", "1s f V", "2s m V", "2s f V", "3s m V", "3s f V",
            "1p m V", "1p f V", "2p m V", "2p f V", "3p m V", "3p f V",
            "1d m V", "1d f V", "2d m V", "2d f V", "3d m V", "3d f V",
            "1s m S", "1s f S", "2s m S", "2s f S", "3s m S", "3s f S",
            "1p m S", "1p f S", "2p m S", "2p f S", "3p m S", "3p f S",
            "1d m S", "1d f S", "2d m S", "2d f S", "3d m S", "3d f S"
                    ]

#G,V,S,V
COMBINED_VERB_ETH = COMBINED_VERB_ROM = ["1s m G", "1s f G", "2s m G", "2s f G", "3s m G", "3s f G",
            "1p m G", "1p f G", "2p m G", "2p f G", "3p m G", "3p f G",
            "1d m G", "1d f G", "2d m G", "2d f G", "3d m G", "3d f G",
            "1s m V", "1s f V", "2s m V", "2s f V", "3s m V", "3s f V",
            "1p m V", "1p f V", "2p m V", "2p f V", "3p m V", "3p f V",
            "1d m V", "1d f V", "2d m V", "2d f V", "3d m V", "3d f V",
            "1s m S", "1s f S", "2s m S", "2s f S", "3s m S", "3s f S",
            "1p m S", "1p f S", "2p m S", "2p f S", "3p m S", "3p f S",
            "1d m S", "1d f S", "2d m S", "2d f S", "3d m S", "3d f S",
            "1s m C", "1s f C", "2s m C", "2s f C", "3s m C", "3s f C",
            "1p m C", "1p f C", "2p m C", "2p f C", "3p m C", "3p f C",
                                         "1d m C", "1d f C", "2d m C", "2d f C", "3d m C", "3d f C"
                                         ]



# G,V,S,J
COMBINED_VERB_AKK = ["1s m G", "1s f G", "2s m G", "2s f G", "3s m G", "3s f G",
                "1p m G", "1p f G", "2p m G", "2p f G", "3p m G", "3p f G",
                "1d m G", "1d f G", "2d m G", "2d f G", "3d m G", "3d f G",
                "1s m V", "1s f V", "2s m V", "2s f V", "3s m V", "3s f V",
                "1p m V", "1p f V", "2p m V", "2p f V", "3p m V", "3p f V",
                "1d m V", "1d f V", "2d m V", "2d f V", "3d m V", "3d f V",
                "1s m S", "1s f S", "2s m S", "2s f S", "3s m S", "3s f S",
                "1p m S", "1p f S", "2p m S", "2p f S", "3p m S", "3p f S",
                "1d m S", "1d f S", "2d m S", "2d f S", "3d m S", "3d f S",
                "1s m J", "1s f J", "2s m J", "2s f J", "3s m J", "3s f J",
                "1p m J", "1p f J", "2p m J", "2p f J", "3p m J", "3p f J",
                     "1d m J", "1d f J", "2d m J", "2d f J", "3d m J", "3d f J"
                     ]

_GEN_SLAV_W = ["i", "v", "f", "n"]
_GEN_SLAV_E = _GEN_SLAV_S = _GEN_GER = ["m", "f", "n"]
_PERS_PRON_SLAV = ["1", "2", "3", "r"]
_CASES_SLAV_S = ["NOM", "AKKs", "DATs", "AKK", "DAT", "PROP"]
_CASES_SLAV_E = ["NOM", "AKK", "DAT", "GEN", "INSTR", "LOC"]
_CASES_SLAV_W = ["NOM", "AKK", "DAT", "GEN", "INSTR", "LOC",
                "GENs", "DATs", "AKKs"]
_CASES_GER = ["NOM", "AKK", "DAT", "GEN"]

COMBINED_PR_SLAV_S = []
COMBINED_PR_SLAV_E = []
COMBINED_PR_SLAV_W = []
_pr_slav_help = ["1s", "2s", "3s", "1p", "2p", "3p", "1d", "2d", "3d","rs","rp","rd"]
for elem in _pr_slav_help:
    for g in _GEN_SLAV_W:
        for case in _CASES_SLAV_W:
            COMBINED_PR_SLAV_W.append(elem+" "+g+" "+case)
    for g in _GEN_SLAV_S:
        for case in _CASES_SLAV_S:
            COMBINED_PR_SLAV_S.append(elem+" "+g+" "+case)
    for g in _GEN_SLAV_E:
        for case in _CASES_SLAV_E:
            COMBINED_PR_SLAV_E.append(elem+" "+g+" "+case)


COMBINED_PR_GER_vh = [p+n+" "+g+" "+t
                   for t in ["NOM", "AKK", "DAT", "GEN"]
                   for n in ["s", "d", "p"]
                   for p in ["1", "2v", "3", "2h"]
                   for g in ["m", "f", "n"]]


COMBINED_PR_GER = COMBINED_PR_GREEK = \
                [p+n+" "+g+" "+t
                   for t in ["NOM", "AKK", "DAT", "GEN"]
                   for n in ["s", "d", "p"]
                   for p in ["1", "2", "3"]
                   for g in ["m", "f", "n"]]


COMBINED_PR_INDIRA_PROX_U = [p + n + " " + g + " " + t for t in ["NOM", "INDIR", "ERG", "GEN", "DAT"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "2h", "2j", "3e", "3x", "3w"]
                             for g in ["m", "f"]]


COMBINED_PR_INDIRA_PROX_P = [p + n + " " + g + " " + t for t in ["NOM","OBJ"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "2h", "3e", "3x", "3w"]
                             for g in ["m", "f"]]

COMBINED_PR_INDIRA_PROX_I = [p + n + " " + g + " " + t for t in ["NOM","OBL","GEN"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3e", "3x", "3w"]
                             for g in ["m", "f"]]

COMBINED_PR_INDIRA_PROX_A = [p + n + " " + g + " " + t for t in ["NOM", "AKK", "DAT", "GEN", "LOC"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "2h", "2j", "3ev", "3ej", "3eh", "3xv", "3xj", "3xh"]
                             for g in ["m", "f", "n"]]


COMBINED_PR_INDIRA_PROX_B = [p + n + " " + g + " " + t for t in ["NOM", "OBJ", "GEN"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "2h", "2j", "3ev", "3ej", "3xv", "3xj", "3wv", "3wj"]
                             for g in ["c"]]

COMBINED_PR_INDIRA_PROX_G = [p + n + " " + g + " " + t for t in ["NOM", "ERG", "DAT", "GEN"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3ev", "3eh", "3xv", "3xh", "rv", "rh"]
                             for g in ["c"]] \
                            + ["12p " + g + " " + t for t in ["NOM", "ERG", "DAT", "GEN"] for g in ["c"]]

COMBINED_PR_INDIRA_PROX_M = [p + n + " " + g + " " + t for t in ["NOM","AKK","INSTR","GEN"]
                             for n in ["s", "p"]
                             for p in ["1", "2v","2h","2j", "3v", "3h"]
                             for g in ["m","f","n"]] \
                            + ["12p " + g + " " + t for t in ["NOM","AKK","INSTR","GEN"] for g in ["m","f","n"]]

COMBINED_PR_INDIRA_S = [p + n + " " + g + " " + t for t in ["NOM", "AKK", "INSTR", "DAT", "ABL", "GEN", "LOC"]
                             for n in ["s", "p","d"]
                             for p in ["1", "2", "3"]
                             for g in ["m","f","n"]]




COMBINED_PR_TURK_A = [p + n + " " + g + " " + t for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC", "INSTR"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["c"]]
COMBINED_PR_TURK_Ah = [p + n + " " + g + " " + t for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC", "INSTR"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "3", "2h"]
                             for g in ["c"]]
COMBINED_PR_TURK_P = [p + n + " " + g + " " + t for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC", "INSTR", "ALLA", "EQUA", "SIMI", "COM"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["c"]]


COMBINED_PR_TURK_T = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["c"]]

COMBINED_PR_TURK_Th = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "3", "2h"]
                             for g in ["c"]]


COMBINED_PR_TUNG_M = [p + n + " " + g + " " + t
                             for t in ["NOM","AKK","GEN","DAT","ABL"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["c"]]\
                     +["12p c " + t for t in ["NOM","AKK","GEN","DAT","ABL"]]


COMBINED_PR_TUNG_U = [p + n + " " + g + " " + t
                             for t in ["NOM","AKK","GEN","DAT","ABL","LOC","INSTR","PROL","DIR"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["c"]]\
                     +["12p c " + t for t in ["NOM","AKK","GEN","DAT","ABL","LOC","INSTR","PROL","DIR"]]

COMBINED_PR_MONG = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC", "INSTR", "COM", "DIR"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "2h", "3"]
                             for g in ["c"]]\
                     +["12p c " + t for t in ["NOM", "AKK", "DAT", "GEN", "ABL", "LOC", "INSTR", "COM", "DIR"]]



COMBINED_PR_ROM_S = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "DISJ", "CON"]
                             for n in ["s", "p"]
                             for p in ["1", "2v", "3", "r", "2h"]
                             for g in ["m", "f"]]

COMBINED_PR_ROM_D = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3", "r"]
                             for g in ["m", "f"]]

COMBINED_PR_ROM_R = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "AKKl", "DATl"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3"]
                             for g in ["m", "f"]]

COMBINED_PR_ROM_F = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "DISJ", "CON"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3", "r"]
                             for g in ["m", "f"]]

COMBINED_PR_ROM_L = [p + n + " " + g + " " + t
                             for t in ["NOM", "AKK", "DAT", "GEN", "DISJ", "CON"]
                             for n in ["s", "p"]
                             for p in ["1", "2", "3", "r"]
                             for g in ["m", "f", "n"]]


COMBINED_PR_SEM = [p + n + " " + g + " " + t
                     for t in ["NOM", "SUFF"]
                     for n in ["s", "d", "p"]
                     for p in ["1", "2", "3"]
                     for g in ["m", "f"]]



COMBINED_PR_KAUK_A = [p + n + " " + g + " " + t
                     for t in ["NOM", "AKK", "INSTR", "DAT", "ABL", "GEN", "LOC"]
                     for n in ["s", "p"]
                     for p in ["1", "2", "3"]
                     for g in ["c"]]

COMBINED_PR_KAUK_G = [p + n + " " + g + " " + t
                     for t in ["NOM","ERG","INSTR","DAT","ADV","GEN"]
                     for n in ["s", "p"]
                     for p in ["1", "2", "3"]
                     for g in ["c"]]


COMBINED_PR_KAUK_K = [p + n + " " + g + " " + t
                     for t in ["NOM", "OBL"]
                     for n in ["s", "p"]
                     for p in ["1", "2", "3"]
                     for g in ["c"]]

COMBINED_PR_KAUK_C = [p + n + " " + g + " " + t
                     for t in ["NOM", "ERG", "INSTR", "ADV"]
                     for n in ["s", "p"]
                     for p in ["1", "2", "3e", "3x", "3w"]
                     for g in ["c"]]


COMBINED = {
    "VERB_SEM": COMBINED_VERB_SEM,
    "VERB_SA": COMBINED_VERB_SA,
    "VERB_ETH": COMBINED_VERB_ETH,
    "VERB_AKK": COMBINED_VERB_AKK,
    "VERB_GER": COMBINED_VERB_GER,
    "VERB_ROM": COMBINED_VERB_ROM,
    "PRON": COMBINED_PRON,
    "PR_SLAV_E": COMBINED_PR_SLAV_E,
    "PR_SLAV_S": COMBINED_PR_SLAV_S,
    "PR_SLAV_W": COMBINED_PR_SLAV_W,
    "PR_GER_vh": COMBINED_PR_GER_vh,
    "PR_GER": COMBINED_PR_GER,
    "PR_SEM": COMBINED_PR_SEM,
    "PR_ROM_D": COMBINED_PR_ROM_D,
    "PR_ROM_R": COMBINED_PR_ROM_R,
    "PR_ROM_F": COMBINED_PR_ROM_F,
    "PR_ROM_S": COMBINED_PR_ROM_S,
    "PR_ROM_L": COMBINED_PR_ROM_L,
    "PR_TURK_P": COMBINED_PR_TURK_T,
    "PR_TURK_A": COMBINED_PR_TURK_A,
    "PR_TURK_Ah": COMBINED_PR_TURK_Ah,
    "PR_TURK_T": COMBINED_PR_TURK_T,
    "PR_TURK_Th": COMBINED_PR_TURK_Th,
    "PR_TUNG_U": COMBINED_PR_TUNG_U,
    "PR_TUNG_M": COMBINED_PR_TUNG_M,
    "PR_MONG": COMBINED_PR_MONG,
    "PR_INDIRA_PROX_U": COMBINED_PR_INDIRA_PROX_U,
    "PR_INDIRA_PROX_P": COMBINED_PR_INDIRA_PROX_P,
    "PR_INDIRA_PROX_A": COMBINED_PR_INDIRA_PROX_A,
    "PR_INDIRA_PROX_B": COMBINED_PR_INDIRA_PROX_B,
    "PR_INDIRA_PROX_G": COMBINED_PR_INDIRA_PROX_G,
    "PR_INDIRA_PROX_I": COMBINED_PR_INDIRA_PROX_I,
    "PR_INDIRA_S": COMBINED_PR_INDIRA_S,
    "PR_GREEK": COMBINED_PR_GREEK,
    "PR_KAUK_A": COMBINED_PR_KAUK_A,
    "PR_KAUK_G": COMBINED_PR_KAUK_G,
    "PR_KAUK_K": COMBINED_PR_KAUK_K,
    "PR_KAUK_C": COMBINED_PR_KAUK_C,
    "rob_unif": COMBINED_VERB_SEM,
    "rob_rand1": COMBINED_VERB_SEM,
    "rob_rand2": COMBINED_VERB_SEM,
    "rob_rand3": COMBINED_VERB_SEM,
}