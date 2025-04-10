import os

from util_directories import PERM_LIST_FOLDER
from util import LANG_TYPES

VARIATION_TYPES = ["PERM_PERS","PERM_NUM","PERM_GEN","PERM_TEN","PERM_XROSS",
            "SYN_PERS","SYN_NUM","SYN_GEN","SYN_TEN","SYN_XROSS",
            "SHUF_SHUF","BASE_BASE"]


permlists_dct = dict()
for lang_type in LANG_TYPES: #todo: auch für TYPES_VERB
    permlists_dct[lang_type] = dict()
    for language in os.listdir(PERM_LIST_FOLDER[lang_type]):
        lang_key = "".join(language.split(".")[:-1]) #strip ".tsv"
        permlists_dct[lang_type][lang_key] = dict()
        with open(PERM_LIST_FOLDER[lang_type]+language) as f:
            for line in f:
                line = line.strip().split("\t")
                permlists_dct[lang_type][lang_key][line[0]] = int(line[1])

def get_permlist(lang_type, language, var_type):
    res_list = []
    for i in range(1,permlists_dct[lang_type][language][var_type]+1):
        res_list.append(var_type+str(i))
    return res_list


def read_in_variations_lists(lang_type, language, perm_typ):
    res_dict = dict()

    with open(PERM_LIST_FOLDER[lang_type]+language+".tsv") as f:
        data = f.read().strip().split("\n")
        for line in data:
            line = line.split("\t")
            res_dict[line[0]] = int(line[1])

    res_list = []

    for key in res_dict.keys():
        if perm_typ in key:
            res_list +=[key.split("_")[-1]+str(i+1) for i in range(res_dict[key])]

    return res_list
