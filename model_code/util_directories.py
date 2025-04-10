PROJ_FOLDER = "../"
DATA_UTIL_FOLDER = PROJ_FOLDER + "_data_util/"
RESULTS_FOLDER = PROJ_FOLDER + "../pgn-paradigms_DATA/NEW_results/"

from util import LANG_TYPES_VERB,LANG_TYPES_PRON,LANG_TYPES_PR,LANG_TYPES, LANG_TYPES_rob,LANG_TYPES_PRONCogSci


ORG_PARA_DIR = DATA_UTIL_FOLDER + "paradigms/"

ORG_PARA_FOLDERS = {
                    "VERB_SEM":ORG_PARA_DIR + "paradigms_VERB_SEM/",
                    "VERB_SA":ORG_PARA_DIR + "paradigms_VERB_SA/",
                    "VERB_ETH":ORG_PARA_DIR + "paradigms_VERB_ETH/",
                    "VERB_AKK":ORG_PARA_DIR + "paradigms_VERB_AKK/",
                    "VERB_GER":ORG_PARA_DIR + "paradigms_VERB_GER/",
                    "VERB_ROM":ORG_PARA_DIR + "paradigms_VERB_ROM/",
                     "PRON": ORG_PARA_DIR + "paradigms_PRON/",
                     "PR_SLAV_E" :ORG_PARA_DIR + "paradigms_PR_SLAV/SLAV_E/",
                     "PR_SLAV_S" :ORG_PARA_DIR + "paradigms_PR_SLAV/SLAV_S/",
                     "PR_SLAV_W" :ORG_PARA_DIR + "paradigms_PR_SLAV/SLAV_W/",
                     "PR_GER_vh" :ORG_PARA_DIR + "paradigms_PR_GER/GER_vh/",
                     "PR_GER" :ORG_PARA_DIR + "paradigms_PR_GER/GER/",
                     "PR_SEM" :ORG_PARA_DIR + "paradigms_PR_SEM/SEM/",
                     "PR_ROM_D" :ORG_PARA_DIR + "paradigms_PR_ROM/ROM_D/",
                     "PR_ROM_R" :ORG_PARA_DIR + "paradigms_PR_ROM/ROM_R/",
                     "PR_ROM_F" :ORG_PARA_DIR + "paradigms_PR_ROM/ROM_F/",
                     "PR_ROM_S" :ORG_PARA_DIR + "paradigms_PR_ROM/ROM_S/",
                     "PR_ROM_L" :ORG_PARA_DIR + "paradigms_PR_ROM/ROM_L/",
                     "PR_TURK_P" :ORG_PARA_DIR + "paradigms_PR_TURK/TURK_P/",
                     "PR_TURK_A" :ORG_PARA_DIR + "paradigms_PR_TURK/TURK_A/",
                     "PR_TURK_Ah" :ORG_PARA_DIR + "paradigms_PR_TURK/TURK_Ah/",
                     "PR_TURK_T" :ORG_PARA_DIR + "paradigms_PR_TURK/TURK_T/",
                     "PR_TURK_Th" :ORG_PARA_DIR + "paradigms_PR_TURK/TURK_Th/",
                     "PR_TUNG_U" :ORG_PARA_DIR + "paradigms_PR_TURK/TUNG_U/",
                     "PR_TUNG_M" :ORG_PARA_DIR + "paradigms_PR_TURK/TUNG_M/",
                     "PR_MONG" :ORG_PARA_DIR + "paradigms_PR_TURK/MONG/",
                     "PR_INDIRA_PROX_U" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_U/",
                     "PR_INDIRA_PROX_P" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_P/",
                     "PR_INDIRA_PROX_A" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_A/",
                     "PR_INDIRA_PROX_B" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_B/",
                     "PR_INDIRA_PROX_G" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_G/",
                     "PR_INDIRA_PROX_I" :ORG_PARA_DIR + "paradigms_PR_INDIRA/PROX_I/",
                     "PR_INDIRA_S" :ORG_PARA_DIR + "paradigms_PR_INDIRA/INDIRA_S/",
                     "PR_GREEK" :ORG_PARA_DIR + "paradigms_PR_INDIRA/GREEK/",
                     "PR_KAUK_A" :ORG_PARA_DIR + "paradigms_PR_KAUK/KAUK_A/",
                     "PR_KAUK_G" :ORG_PARA_DIR + "paradigms_PR_KAUK/KAUK_G/",
                     "PR_KAUK_K" :ORG_PARA_DIR + "paradigms_PR_KAUK/KAUK_K/",
                     "PR_KAUK_C" :ORG_PARA_DIR + "paradigms_PR_KAUK/KAUK_C/",
                     "rob_unif" :ORG_PARA_DIR + "paradigms_rob/rob_unif/",
                     "rob_rand1" :ORG_PARA_DIR + "paradigms_rob/rob_rand1/",
                     "rob_rand2" :ORG_PARA_DIR + "paradigms_rob/rob_rand2/",
                     "rob_rand3" :ORG_PARA_DIR + "paradigms_rob/rob_rand3/",
                     }

VARIATION_FOLDERS = {}
for lang_type in LANG_TYPES_PR:
    VARIATION_FOLDERS[lang_type] = RESULTS_FOLDER + "perms/PR/" + lang_type + "/"
for lang_type in LANG_TYPES_VERB:
    VARIATION_FOLDERS[lang_type] = RESULTS_FOLDER + "perms/VERB/" + lang_type + "/"
for lang_type in LANG_TYPES_PRON:
    VARIATION_FOLDERS[lang_type] = RESULTS_FOLDER + "perms/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_rob:
    VARIATION_FOLDERS[lang_type] = RESULTS_FOLDER + "perms/rob/" + lang_type + "/"


PERM_DIR = RESULTS_FOLDER + "perms/"

LOSSES_DIR = RESULTS_FOLDER + "losses/"
LOSSES_FOLDERS = {}
for lang_type in LANG_TYPES_PR:
    LOSSES_FOLDERS[lang_type] = RESULTS_FOLDER + "losses/PR/" + lang_type + "/"
for lang_type in LANG_TYPES_VERB:
    LOSSES_FOLDERS[lang_type] = RESULTS_FOLDER + "losses/VERB/" + lang_type + "/"
for lang_type in LANG_TYPES_PRON:
    LOSSES_FOLDERS[lang_type] = RESULTS_FOLDER + "losses/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_rob:
    LOSSES_FOLDERS[lang_type] = RESULTS_FOLDER + "losses/rob/" + lang_type + "/"


NATURALNESS_DIR = RESULTS_FOLDER + "naturalness/"
NATURALNESS_FOLDERS = {}
for lang_type in LANG_TYPES_PR:
    NATURALNESS_FOLDERS[lang_type] = RESULTS_FOLDER + "naturalness/PR/" + lang_type + "/"
for lang_type in LANG_TYPES_VERB:
    NATURALNESS_FOLDERS[lang_type] = RESULTS_FOLDER + "naturalness/VERB/" + lang_type + "/"
for lang_type in LANG_TYPES_PRON:
    NATURALNESS_FOLDERS[lang_type] = RESULTS_FOLDER + "naturalness/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_rob:
    NATURALNESS_FOLDERS[lang_type] = RESULTS_FOLDER + "naturalness/rob/" + lang_type + "/"

PERM_LIST_DIR = RESULTS_FOLDER + "permlists/"
PERM_LIST_FOLDER = {}
for lang_type in LANG_TYPES_PR:
    PERM_LIST_FOLDER[lang_type] = RESULTS_FOLDER + "permlists/PR/" + lang_type + "/"
for lang_type in LANG_TYPES_VERB:
    PERM_LIST_FOLDER[lang_type] = RESULTS_FOLDER + "permlists/VERB/" + lang_type + "/"
for lang_type in LANG_TYPES_PRON:
    PERM_LIST_FOLDER[lang_type] = RESULTS_FOLDER + "permlists/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_rob:
    PERM_LIST_FOLDER[lang_type] = RESULTS_FOLDER + "permlists/rob/" + lang_type + "/"


IB_FOLDERS = {}
for lang_type in LANG_TYPES_PR:
    IB_FOLDERS[lang_type] = RESULTS_FOLDER + "ibvalues/PR/" + lang_type + "/"
for lang_type in LANG_TYPES_VERB:
    IB_FOLDERS[lang_type] = RESULTS_FOLDER + "ibvalues/VERB/" + lang_type + "/"
for lang_type in LANG_TYPES_PRON:
    IB_FOLDERS[lang_type] = RESULTS_FOLDER + "ibvalues/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_PRONCogSci:
    IB_FOLDERS[lang_type] = RESULTS_FOLDER + "ibvalues/PRON/" + lang_type + "/"
for lang_type in LANG_TYPES_rob:
    IB_FOLDERS[lang_type] = RESULTS_FOLDER + "ibvalues/rob/" + lang_type + "/"


DATA_LANGLIST_FOLDER = DATA_UTIL_FOLDER +"langlists/"

FREQ_DIR = DATA_UTIL_FOLDER + "freqs/"
FREQ_FILES = {lang_type: DATA_UTIL_FOLDER + "calculated_weights_" + lang_type + ".tsv" for lang_type in LANG_TYPES}
