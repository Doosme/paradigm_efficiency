from util_directories import NATURALNESS_FOLDERS
import torch


def read_in_naturalnesses(filename):
    with open(filename) as f:
        data = f.read().split("\n")
        temp_dict = dict()
        for line in data:
            line = line.split("\t")
            if line[0] == "lang_name":
                column_names = line[1:]
            else:
                temp_dict[line[0]] = line[1:]

        data_dict = dict()
        for lang, line in temp_dict.items():
            data_dict[lang] = dict()
            for i in range(len(column_names)):
                data_dict[lang][column_names[i]] = line[i]
    return data_dict


def read_in_all_naturalness_dicts(lang_type):
    pers_perm_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "P-PERM-PERS.tsv")
    ten_perm_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "T-PERM-TEN.tsv")
    gen_perm_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "G-PERM-GEN.tsv")
    num_perm_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "N-PERM-NUM.tsv")
    x_perm_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "X-PERM-XROSS.tsv")
    pers_syn_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "P-SYN-PERS.tsv")
    ten_syn_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "T-SYN-TEN.tsv")
    gen_syn_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "G-SYN-GEN.tsv")
    num_syn_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "N-SYN-NUM.tsv")
    x_syn_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "X-SYN-XROSS.tsv")
    s_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "S-SHUF-SHUF.tsv")
    b_data_dict = read_in_naturalnesses(NATURALNESS_FOLDERS[lang_type] + "B-BASE-BASE.tsv")

    data_dict = {"PERM_XROSS": x_perm_data_dict,
                 "PERM_PERS": pers_perm_data_dict,
                 "PERM_NUM": num_perm_data_dict,
                 "PERM_GEN": gen_perm_data_dict,
                 "PERM_TEN": ten_perm_data_dict,
                 "SYN_XROSS": x_syn_data_dict,
                 "SYN_PERS": pers_syn_data_dict,
                 "SYN_NUM": num_syn_data_dict,
                 "SYN_GEN": gen_syn_data_dict,
                 "SYN_TEN": ten_syn_data_dict,
                 "SHUF_SHUF": s_data_dict,
                 "BASE_BASE": b_data_dict
                 }
    return data_dict


TENSE_DIMENSION_DICT = {"rob_unif":2, "rob_rand1":2, "rob_rand2":2, "rob_rand3":2,
    "VERB_SEM":2, "VERB_GER":2, "VERB_ETH":4, "VERB_AKK":4, "VERB_SA":3, "VERB_ROM":4, "PRON":1,
                           "PR_SLAV_S":6,"PR_SLAV_E":6,"PR_SLAV_W":9,
                          "PR_GER":4,"PR_GER_vh":4,"PR_SEM":2,
                            "PR_ROM_F":5,"PR_ROM_D":3,"PR_ROM_R":6,"PR_ROM_S":6,"PR_ROM_L":6,
                            "PR_TURK_T":6, "PR_TURK_Th":6, "PR_TURK_P":11,"PR_TURK_A":7, "PR_TURK_Ah":7,"PR_MONG":9,"PR_TUNG_U":9,"PR_TUNG_M":5,
                          "PR_INDIRA_PROX_U": 5,"PR_INDIRA_PROX_P": 2,"PR_INDIRA_PROX_A": 5,"PR_INDIRA_PROX_B": 3,"PR_INDIRA_PROX_G":4 ,"PR_INDIRA_PROX_I":3,
                        "PR_GREEK": 4,"PR_INDIRA_S":7,
                      "PR_KAUK_K": 2 ,"PR_KAUK_G": 6,"PR_KAUK_A": 7,"PR_KAUK_C": 4,"PR_KAUK_Ch":8
                        }
PERS_DIMENSION_DICT = {"rob_unif":3, "rob_rand1":3, "rob_rand2":3, "rob_rand3":3,
                       "VERB_SEM":3,"VERB_GER":3, "VERB_ETH":3, "VERB_AKK":3, "VERB_SA":3, "VERB_ROM":3, "PRON":4,
                           "PR_SLAV_S":4,"PR_SLAV_E":4,"PR_SLAV_W":4,
                          "PR_GER":3,"PR_GER_vh":4,"PR_SEM":3,
                            "PR_ROM_F":4,"PR_ROM_D":4,"PR_ROM_R":3,"PR_ROM_S":5,"PR_ROM_L":4,
                            "PR_TURK_T":3, "PR_TURK_Th":4, "PR_TURK_P":3,"PR_TURK_A":3, "PR_TURK_Ah":4,"PR_MONG":5,"PR_TUNG_U":4,"PR_TUNG_M":4,
                          "PR_INDIRA_PROX_U": 7,"PR_INDIRA_PROX_P": 6,"PR_INDIRA_PROX_A": 10,"PR_INDIRA_PROX_B": 10,"PR_INDIRA_PROX_G":9 , "PR_INDIRA_PROX_I":5,
                        "PR_GREEK": 3,"PR_INDIRA_S":3,
                      "PR_KAUK_K": 3 ,"PR_KAUK_G": 3,"PR_KAUK_A": 3,"PR_KAUK_C": 5,"PR_KAUK_Ch":4
                       }
#todo:
NUM_DIMENSION_DICT = {"rob_unif":3, "rob_rand1":3, "rob_rand2":3, "rob_rand3":3,
                      "VERB_SEM":3, "VERB_GER":3, "VERB_ETH":3, "VERB_AKK":3, "VERB_SA":3, "VERB_ROM":3, "PRON":2,
                           "PR_SLAV_S":3,"PR_SLAV_E":3,"PR_SLAV_W":3,
                          "PR_GER":3,"PR_GER_vh":3, "PR_SEM":3,
                            "PR_ROM_F":2,"PR_ROM_D":2,"PR_ROM_R":2,"PR_ROM_S":2,"PR_ROM_L":2,
                            "PR_TURK_T":2, "PR_TURK_Th":2, "PR_TURK_P":2,"PR_TURK_A":2, "PR_TURK_Ah":2,"PR_MONG":2,"PR_TUNG_U":2,"PR_TUNG_M":2,
                          "PR_INDIRA_PROX_U": 2,"PR_INDIRA_PROX_P": 2,"PR_INDIRA_PROX_A": 2,"PR_INDIRA_PROX_B": 2,"PR_INDIRA_PROX_G":2 ,"PR_INDIRA_PROX_I":2 ,
                      "PR_GREEK": 3,"PR_INDIRA_S":3,
                      "PR_KAUK_K": 2,"PR_KAUK_G": 2,"PR_KAUK_A": 2,"PR_KAUK_C": 2,"PR_KAUK_Ch":2
                        }
GEN_DIMENSION_DICT = {"rob_unif":2, "rob_rand1":2, "rob_rand2":2, "rob_rand3":2,
                      "VERB_SEM":2, "VERB_GER":2, "VERB_ETH":2, "VERB_AKK":2, "VERB_SA":2, "VERB_ROM":2, "PRON":1,
                           "PR_SLAV_S":3,"PR_SLAV_E":3,"PR_SLAV_W":4,
                          "PR_GER":3,"PR_GER_vh":3,"PR_SEM":2,
                            "PR_ROM_F":2,"PR_ROM_D":2,"PR_ROM_R":2,"PR_ROM_S":2,"PR_ROM_L":3,
                            "PR_TURK_T":1, "PR_TURK_Th":1, "PR_TURK_P":1,"PR_TURK_A":1, "PR_TURK_Ah":1,"PR_MONG":1,"PR_TUNG_U":1,"PR_TUNG_M":1,
                          "PR_INDIRA_PROX_U": 2,"PR_INDIRA_PROX_P": 2,"PR_INDIRA_PROX_A": 3,"PR_INDIRA_PROX_B": 1,"PR_INDIRA_PROX_G":1 ,"PR_INDIRA_PROX_I":2 ,
                        "PR_GREEK": 3,"PR_INDIRA_S":3,
                      "PR_KAUK_K": 1,"PR_KAUK_G": 1,"PR_KAUK_A": 1,"PR_KAUK_C": 1,"PR_KAUK_Ch":1
                      }

def _get_feat_values(lang_type,feat_str):
    feats = feat_str.split(" ")
    if lang_type == "PRON": assert len(feats) == 1
    else: assert len(feats) == 3

    if len(feats) == 1:
        person = feats[0][:-1]
        number = feats[0][-1]
        gender = ""
        tense = ""
    else:
        person = feats[0][:-1]
        number = feats[0][-1]
        gender = feats[1]
        tense = feats[2]

    return person, number, gender, tense

def _read_in_paradigm_tensor(lang_type, paradigm_file):
    conj_idx_dict = dict()
    last_value = 0
    num_dim = NUM_DIMENSION_DICT[lang_type]
    gen_dim = GEN_DIMENSION_DICT[lang_type]
    pers_dim = PERS_DIMENSION_DICT[lang_type]
    ten_dim = TENSE_DIMENSION_DICT[lang_type]

    paradigm = torch.zeros(ten_dim, num_dim, pers_dim, gen_dim, dtype=torch.int64)


    with open(paradigm_file) as f:
        for line in f:
            feat, conj = line.split("\t")
            person,number,gender,tense = _get_feat_values(lang_type,feat)

            pers_digit, num_digit, gen_digit, temp_digit = create_feat_digits(lang_type, person, number, gender, tense)

            if conj in conj_idx_dict.keys():
                value = conj_idx_dict[conj]
            else:
                value = last_value + 1
                last_value += 1
                conj_idx_dict[conj] = value

            paradigm[temp_digit, num_digit, pers_digit, gen_digit] = value
    return paradigm

def _read_in_frequency_tensor(lang_type, frequency_file):
    num_dim = NUM_DIMENSION_DICT[lang_type]
    gen_dim = GEN_DIMENSION_DICT[lang_type]
    pers_dim = PERS_DIMENSION_DICT[lang_type]
    ten_dim = TENSE_DIMENSION_DICT[lang_type]

    frequencies = torch.zeros(ten_dim, num_dim, pers_dim, gen_dim, dtype=torch.float)

    with open(frequency_file) as f:
        for line in f:
            feat, freq = line.split("\t")
            person, number, gender, tense = _get_feat_values(lang_type, feat)

            pers_digit, num_digit, gen_digit, temp_digit = create_feat_digits(lang_type, person, number, gender, tense)

            num_tenses = TENSE_DIMENSION_DICT[lang_type]
            frequencies[temp_digit, num_digit, pers_digit, gen_digit] = float(freq) / num_tenses / 98.17  # normed by 98.17 because the values were not exact percentages, normed by 2 because V and G were same values

    return frequencies


def create_feat_digits(lang_type, pers, num, gen, temp):
    if "VERB" in lang_type or "PR_SEM" in lang_type or "rob" in lang_type:
        num_digit = {"s":0,"p":1,"d":2}[num]
        pers_digit = {"1":0,"2":1,"3":2}[pers]
        ten_digit = {"G":0,"V":1,"S":2,"J":3,"C":3}[temp]
        gen_digit = {"m":0,"f":1}[gen]

    elif "PRON" in lang_type:
        num_digit = {"s":0,"p":1}[num]
        pers_digit = {"1":0,"2":1,"3":2,"12":3}[pers]
        gen_digit = 0
        ten_digit = 0

    elif "PR_GER" in lang_type or "PR_GREEK" == lang_type:
        num_digit = {"s":0,"p":1,"d":2}[num]
        pers_digit = {"1":0,"2":1,"2v":1,"3":2,"2h":3}[pers]
        ten_digit = {"NOM":0,"AKK":1,"DAT":2,"GEN":3}[temp]
        gen_digit = {"m":0,"f":1,"n":2}[gen]

    elif "PR_SLAV" in lang_type:
        num_digit = {"s":0,"p":1,"d":2}[num]
        pers_digit = {"1":0,"2":1,"3":2,"r":3}[pers]
        if lang_type == "PR_SLAV_W" or lang_type == "PR_SLAV_E":
            ten_digit = {"NOM":0,"AKK":1,"DAT":2,"GEN":3,"INSTR":4,"LOC":5,"GENs":6,"DATs":7,"AKKs":8}[temp]
        elif lang_type == "PR_SLAV_S":
            ten_digit = {"NOM": 0, "AKK": 1, "DAT": 2,  "PROP": 3, "AKKs": 4, "DATs": 5}[temp]
        else:
            raise Exception("ERROR: create_feat_digits not implemented")
        gen_digit = {"m":0,"i":0,"f":1,"n":2,"v":3}[gen]

    elif "PR_TURK" in lang_type or "PR_TUNG" in lang_type:
        num_digit = {"s":0,"p":1}[num]
        pers_digit = {"1":0,"2":1,"2v":1,"3":2,"2h":3, "12":3}[pers]
        ten_digit = {"NOM":0,"AKK":1,"DAT":2,"GEN":3, "ABL":4, "LOC":5, "INSTR":6,
                     "ALLA":7, "EQUA":8, "SIMI":9, "COM":10,
                     "PROL":7, "DIR":8}[temp]
        gen_digit = {"c":0}[gen]
    elif "PR_MONG" in lang_type:
        num_digit = {"s":0,"p":1}[num]
        pers_digit = {"1":0,"2v":1,"3":2,"2h":3, "12":4}[pers]
        ten_digit = {"NOM":0,"AKK":1,"DAT":2,"GEN":3, "ABL":4, "LOC":5, "INSTR":6,
                     "COM":7, "DIR":8}[temp]
        gen_digit = {"c":0}[gen]



    elif "PR_ROM" in lang_type:
        num_digit = {"s": 0, "p": 1}[num]
        pers_digit = {"1": 0, "2": 1, "2v":1, "3": 2,"r":3,"2h":4}[pers]
        if "PR_ROM_R" == lang_type:
            ten_digit = {"NOM": 0, "AKK": 1, "DAT": 2, "GEN": 3, "AKKl": 4, "DATl": 5,}[temp]
        elif "PR_ROM_D" == lang_type  or  "PR_ROM_F" == lang_type:
            ten_digit = {"NOM": 0, "AKK": 1, "DAT": 2, "DISJ": 3, "CON": 4}[temp]
        elif "PR_ROM_S" == lang_type or "PR_ROM_L" == lang_type:
            ten_digit = {"NOM": 0, "AKK": 1, "DAT": 2, "GEN": 3, "DISJ": 4, "CON": 5}[temp]
        else:
            raise Exception("ERROR: create_feat_digits not implemented")
        gen_digit = {"m":0,"f":1, "n":2}[gen]

    elif "INDIRA_S" == lang_type:
        num_digit = {"s": 0, "p": 1,"d":2}[num]
        pers_digit = {"1": 0, "2": 1, "3": 2}[pers]
        ten_digit = {"NOM": 0, "AKK": 1, "INSTR": 2, "DAT": 3, "ABL": 4, "GEN": 5, "LOC": 6}[temp]
        gen_digit = {"m": 1, "f":2, "n":3}[gen]

    elif "PR_INDIRA" in lang_type:
        num_digit = {"s":0,"p":1, "d":2}[num]
        if "PR_INDIRA_PROX_U" == lang_type:
            pers_digit = {"1":0, "2v":1,"2h":2,"2j":3, "3e":4,"3x":5,"3w":6}[pers]
            ten_digit = {"NOM":0,"INDIR":1,"ERG":2,"GEN":3,"DAT":4}[temp]
        elif "PR_INDIRA_PROX_P" == lang_type:
            pers_digit = {"1":0, "2v":1, "2h":2, "3e":3, "3x":4,"3w":5}[pers]
            ten_digit = {"NOM":0, "OBJ":1}[temp]
        elif "PR_INDIRA_PROX_A" == lang_type:
            pers_digit = {"1":0, "2v":1, "2h":2, "2j":3, "3ev":4, "3ej":5, "3eh":6, "3xv":7, "3xj":8, "3xh":9}[pers]
            ten_digit = {"NOM":0, "AKK":1, "DAT":2, "GEN":3, "LOC":4}[temp]
        elif "PR_INDIRA_PROX_B" == lang_type:
            pers_digit = {"1":0, "2v":1, "2h":2, "2j":3, "3ev":4, "3ej":5, "3xv":6, "3xj":7, "3wv":8, "3wj":9}[pers]
            ten_digit = {"NOM":0, "OBJ":1, "GEN":2}[temp]
        elif "PR_INDIRA_PROX_G" == lang_type:
            pers_digit = {"1":0, "2":1,"3ev":2, "3eh":3, "3xv":4, "3xh":5, "rv":6, "rh":7, "12":8}[pers]
            ten_digit = {"NOM":0, "ERG":1, "DAT":2, "GEN":3}[temp]
        elif "PR_INDIRA_PROX_I" == lang_type:
            pers_digit = {"1":0, "2":1,"3e":2, "3x":3, "3w":4}[pers]
            ten_digit = {"NOM":0, "OBL":1, "GEN":2}[temp]
        elif lang_type == "PR_INDIRA_S":
            pers_digit = {"1":0, "2":1,"3":2}[pers]
            ten_digit = {"NOM":0, "AKK":1, "INSTR":2, "DAT":3, "ABL":4, "GEN":5, "LOC":6}[temp]
        else:
            raise Exception("ERROR: create_feat_digits not implemented")
        gen_digit = {"c":0, "m":0,"f":1,"n":2}[gen]

    elif "PR_KAUK" in lang_type:
        num_digit = {"s": 0, "p": 1}[num]
        if "PR_KAUK_A" == lang_type or "PR_KAUK_G" == lang_type or "PR_KAUK_K" == lang_type:
            pers_digit = {"1": 0, "2": 1, "3": 2}[pers]
            ten_digit = {"NOM": 0, "AKK": 1, "INSTR": 2, "DAT": 3, "ABL": 4, "GEN": 5, "LOC": 6,"ERG":1, "OBL":1, "ADV":4}[temp]
        elif "PR_KAUK_Ch" == lang_type:
            pers_digit = {"1": 0, "2": 1, "3": 2, "12":3}[pers]
            ten_digit = {"NOM": 0, "GEN": 1, "DAT": 2, "ERG": 3, "ALLA": 4, "INSTR": 5, "LOC": 6,"COMP": 1}[temp]
        elif "PR_KAUK_C" == lang_type:
            pers_digit = {"1": 0, "2": 1, "3e":2,"3x":3,"3w":4,"r":5}[pers]
            ten_digit = {"NOM": 0, "ERG": 1, "INSTR": 2, "ADV": 3}[temp]
        else:
            raise Exception("ERROR: create_feat_digits not implemented")
        gen_digit = {"c": 0}[gen]
    else:
        raise Exception("ERROR: create_feat_digits not implemented")

    return pers_digit, num_digit, gen_digit, ten_digit


