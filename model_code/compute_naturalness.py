from util_directories import NATURALNESS_FOLDERS, VARIATION_FOLDERS
from util_langlists import LANGUAGE_LISTS
from util import read_in_syncretism_classes
from util_permlists import VARIATION_TYPES, get_permlist
import os

def compute_naturalnesses(resdict, language, lang_type):

    baseline_syncclasses = read_in_syncretism_classes(
        VARIATION_FOLDERS[lang_type] + language + "/" + language + "_BASE_BASE1a.tsv")

    baseline_dist_count = 0
    for surface_form, feature_combs in baseline_syncclasses.items():
        baseline_dist_count += dist(feature_combs, lang_type)

    for var_type in VARIATION_TYPES:
        for perm in get_permlist(lang_type, language, var_type):
            current_syncclasses = read_in_syncretism_classes(VARIATION_FOLDERS[lang_type] + language + "/" + language + "_" + perm + "a.tsv")

            current_dist_count = 0
            for surface_form, feature_combs in current_syncclasses.items():
                current_dist_count += dist(feature_combs, lang_type)

            resdict[language][var_type][perm] = current_dist_count - baseline_dist_count

    return resdict


def dist(ls, lang_type):
    if lang_type == "PRON":
        pers_set = list()
        num_set = list()

        for elem in ls:
            if len(elem) == 2:
                pers_set.append(elem[0])
                num_set.append(elem[1])
            elif len(elem) == 3:
                pers_set.append(elem[0:2])
                num_set.append(elem[2])
            else:
                print("ERROR")

        pers_set = set(pers_set)
        num_set = set(num_set)

        return len(pers_set) - 1 + len(num_set) - 1

    elif "VERB" in lang_type or "rob" in lang_type:
        pers_set = list()
        gen_set = list()
        num_set = list()
        ten_set = list()

        for elem in ls:
            elem = elem.replace(" ", "")
            if len(elem) == 4:
                pers_set.append(elem[0])
                num_set.append(elem[1])
                gen_set.append(elem[2])
                ten_set.append(elem[3])
            else:
                raise Exception("ERROR")

        pers_set = set(pers_set)
        num_set = set(num_set)
        gen_set = set(gen_set)
        ten_set = set(ten_set)

        return len(pers_set) - 1 + len(num_set) - 1 + len(gen_set) - 1 + len(ten_set) - 1

    elif "PR_" in lang_type:
        pers_set = list()
        gen_set = list()
        num_set = list()
        ten_set = list()

        for elem in ls:
            elem = elem.replace(" ", "")
            pers_set.append(elem[0])
            num_set.append(elem[1])
            gen_set.append(elem[2])
            ten_set.append(elem[3:])

        pers_set = set(pers_set)
        num_set = set(num_set)
        gen_set = set(gen_set)
        ten_set = set(ten_set)

        return len(pers_set) - 1 + len(num_set) - 1 + len(gen_set) - 1 + len(ten_set) - 1
    else:
        raise Exception("distance function _dist_ for " + lang_type + " not defined")


def write_paradigmcomplexity_values_to_file(var_type, filename, resdict, perm_list):
    res = "lang_name"
    for perm in perm_list:
        res += "\t" + str(perm)

    for lang in resdict.keys():
        res += "\n" + str(lang)
        for perm in perm_list:
            res += "\t" + str(resdict[lang][var_type][perm])

    with open(filename, "w") as g:
        g.write(res)


def create_naturalness_files(langtype):
    print("-"*50)
    print(langtype)
    print("-"*50)
    resdict = dict()
    for language in LANGUAGE_LISTS[langtype]:
        resdict[language] = dict()
        for typ in VARIATION_TYPES:
            resdict[language][typ] = dict()

    print("computing\n")
    for language in LANGUAGE_LISTS[langtype]:
        print(language)
        compute_naturalnesses(resdict, language, langtype)


    print("\nwriting")
    if not os.path.exists(NATURALNESS_FOLDERS[langtype]):
        os.makedirs(NATURALNESS_FOLDERS[langtype])
    write_paradigmcomplexity_values_to_file("PERM_NUM", NATURALNESS_FOLDERS[langtype] + "N-PERM-NUM.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["PERM_NUM"])
    write_paradigmcomplexity_values_to_file("PERM_PERS", NATURALNESS_FOLDERS[langtype] + "P-PERM-PERS.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["PERM_PERS"])
    write_paradigmcomplexity_values_to_file("PERM_GEN", NATURALNESS_FOLDERS[langtype] + "G-PERM-GEN.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["PERM_GEN"])
    write_paradigmcomplexity_values_to_file("PERM_TEN", NATURALNESS_FOLDERS[langtype] + "T-PERM-TEN.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["PERM_TEN"])
    write_paradigmcomplexity_values_to_file("PERM_XROSS", NATURALNESS_FOLDERS[langtype] + "X-PERM-XROSS.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["PERM_XROSS"])
    write_paradigmcomplexity_values_to_file("SYN_NUM", NATURALNESS_FOLDERS[langtype] + "N-SYN-NUM.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SYN_NUM"])
    write_paradigmcomplexity_values_to_file("SYN_PERS", NATURALNESS_FOLDERS[langtype] + "P-SYN-PERS.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SYN_PERS"])
    write_paradigmcomplexity_values_to_file("SYN_GEN", NATURALNESS_FOLDERS[langtype] + "G-SYN-GEN.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SYN_GEN"])
    write_paradigmcomplexity_values_to_file("SYN_TEN", NATURALNESS_FOLDERS[langtype] + "T-SYN-TEN.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SYN_TEN"])
    write_paradigmcomplexity_values_to_file("SYN_XROSS", NATURALNESS_FOLDERS[langtype] + "X-SYN-XROSS.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SYN_XROSS"])
    write_paradigmcomplexity_values_to_file("SHUF_SHUF", NATURALNESS_FOLDERS[langtype] + "S-SHUF-SHUF.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["SHUF_SHUF"])
    write_paradigmcomplexity_values_to_file("BASE_BASE", NATURALNESS_FOLDERS[langtype] + "B-BASE-BASE.tsv", resdict, resdict[LANGUAGE_LISTS[langtype][0]]["BASE_BASE"])

if __name__ == "__main__":
    create_naturalness_files("rob_unif")
    create_naturalness_files("rob_rand1")
    create_naturalness_files("rob_rand2")
    create_naturalness_files("rob_rand3")

    create_naturalness_files("VERB_SEM")
    create_naturalness_files("VERB_SA")
    create_naturalness_files("VERB_GER")
    create_naturalness_files("VERB_AKK")
    create_naturalness_files("VERB_ETH")
    create_naturalness_files("VERB_ROM")

    create_naturalness_files("PRON")

    create_naturalness_files("PR_SLAV_E")
    create_naturalness_files("PR_SLAV_W")
    create_naturalness_files("PR_SLAV_S")

    create_naturalness_files("PR_GER")
    create_naturalness_files("PR_GER_vh")

    create_naturalness_files("PR_ROM_S")
    create_naturalness_files("PR_ROM_L")
    create_naturalness_files("PR_ROM_F")
    create_naturalness_files("PR_ROM_D")
    create_naturalness_files("PR_ROM_R")

    create_naturalness_files("PR_TURK_T")
    create_naturalness_files("PR_TURK_Th")
    create_naturalness_files("PR_TURK_A")
    create_naturalness_files("PR_TURK_Ah")
    create_naturalness_files("PR_TURK_P")
    create_naturalness_files("PR_TUNG_U")
    create_naturalness_files("PR_TUNG_M")
    create_naturalness_files("PR_MONG")

    create_naturalness_files("PR_SEM")

    create_naturalness_files("PR_INDIRA_PROX_U")
    create_naturalness_files("PR_INDIRA_PROX_P")
    create_naturalness_files("PR_INDIRA_PROX_A")
    create_naturalness_files("PR_INDIRA_PROX_B")
    create_naturalness_files("PR_INDIRA_PROX_G")
    create_naturalness_files("PR_INDIRA_PROX_I")
    create_naturalness_files("PR_INDIRA_PROX_M")
    create_naturalness_files("PR_INDIRA_S")

    create_naturalness_files("PR_KAUK_A")
    create_naturalness_files("PR_KAUK_G")
    create_naturalness_files("PR_KAUK_K")
    create_naturalness_files("PR_KAUK_C")

    create_naturalness_files("PR_GREEK")
    create_naturalness_files("PR_INDIRA_S")