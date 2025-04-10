from compute_accuracy import compute_accuracy
from compute_accuracy_CogSci21 import compute_accuracy_CogSci21
from compute_complexity import compute_complexity
from util_naturalness import read_in_all_naturalness_dicts, _read_in_paradigm_tensor, _read_in_frequency_tensor
from util_permlists import get_permlist, VARIATION_TYPES
from util_langlists import LANGUAGE_LISTS
from util_directories import VARIATION_FOLDERS, FREQ_FILES, IB_FOLDERS, LOSSES_FOLDERS
from util import read_in_paradigm

import os
import torch

def calculate_result_values(lang_type, lang, perm_name, cluster_name):
    base_paradigm_file = VARIATION_FOLDERS[lang_type] + lang + "/" + lang + "_BASE_BASE1a.tsv"
    base_paradigm = _read_in_paradigm_tensor(lang_type, base_paradigm_file)

    paradigm_file = VARIATION_FOLDERS[lang_type] + lang + "/" + lang + "_" + perm_name + "a.tsv"
    paradigm = _read_in_paradigm_tensor(lang_type, paradigm_file)
    frequencies = _read_in_frequency_tensor(lang_type, FREQ_FILES[lang_type])




    #paradigm, frequencies = read_in_paradigm_for_accuracy_computation()
    accuracy = compute_accuracy(paradigm, frequencies)
    if "PRON" in lang_type:
        accuracy_CogSci21_gamma1 = compute_accuracy_CogSci21(paradigm, frequencies, gamma=1)
        accuracy_CogSci21_gamma2 = compute_accuracy_CogSci21(paradigm, frequencies, gamma=2)
        accuracy_CogSci21_gamma5 = compute_accuracy_CogSci21(paradigm, frequencies, gamma=5)
    complexity = compute_complexity(paradigm, frequencies)

    if "BASE" in cluster_name:
        i_list = "abcdefghjk"
    else:
        i_list = "abcde"
    loss_list = []
    for i in i_list:
        loss_file_i = LOSSES_FOLDERS[lang_type] + lang + "/" + lang + "_" + perm_name + i + "_losses.tsv"
        with open(loss_file_i) as f:
            text = f.read().strip().split("\n")
            for line in text:
                if "total" in line:
                    losses = [float(value) for value in line.split("\t")[1:]]
                    loss_i = sum(losses) / len(losses)
                    loss_list.append(loss_i)
    loss_avg = sum(loss_list) / len(loss_list)

    equal_to_shuf = torch.equal(base_paradigm, paradigm) if "BASE" not in cluster_name else False

    base_cont_dict = read_in_paradigm(base_paradigm_file)
    perm_cont_dict = read_in_paradigm(paradigm_file)

    equal_to_base = base_cont_dict == perm_cont_dict if "BASE" not in cluster_name else False

    if "PRON" in lang_type:
        return accuracy, complexity, loss_avg, equal_to_shuf, equal_to_base, accuracy_CogSci21_gamma1, accuracy_CogSci21_gamma2, accuracy_CogSci21_gamma5
    return accuracy, complexity, loss_avg, equal_to_shuf, equal_to_base


def create_ib_files(lang_type):
    #read in naturalnesses
    syncompl_dict = read_in_all_naturalness_dicts(lang_type)

    #create empty dictionary
    #dct["ArabicCA"]["SYN_XROSS"]["XROSS70"]
    #dct[lang][cluster][perm]
    dct = dict()
    for lang in LANGUAGE_LISTS[lang_type]:
        dct[lang] = {var:dict() for var in VARIATION_TYPES}
        for cluster_name in VARIATION_TYPES:
            perm_list = get_permlist(language=lang, lang_type=lang_type, var_type=cluster_name)
            for perm in perm_list:
                dct[lang][cluster_name][perm] = dict()

    print("calculating...")
    l = len(LANGUAGE_LISTS[lang_type])
    i = 0
    #calculate accuracies and complexities
    for lang in LANGUAGE_LISTS[lang_type]:
        i += 1
        #print(lang, lang_type, cluster_name)
        print(str(i)+" of "+str(l), lang)
        for cluster_name in VARIATION_TYPES:
            perm_list = get_permlist(language=lang, lang_type=lang_type, var_type=cluster_name)
            for perm_name in perm_list:
                if "PRON" in lang_type:
                    acc, compl, crossent, equal_to_shuf, equal_to_base, accuracy_CogSci21_gamma1, accuracy_CogSci21_gamma2, accuracy_CogSci21_gamma5 = calculate_result_values(lang_type, lang, perm_name, cluster_name)
                else:
                    acc, compl, crossent, equal_to_shuf, equal_to_base = calculate_result_values(lang_type, lang, perm_name, cluster_name)
                dct[lang][cluster_name][perm_name]["complexities"] = compl
                dct[lang][cluster_name][perm_name]["accuracies"] = acc
                dct[lang][cluster_name][perm_name]["crossentropies"] = crossent
                dct[lang][cluster_name][perm_name]["equal_to_shuf"] = equal_to_shuf
                dct[lang][cluster_name][perm_name]["equal_to_base"] = equal_to_base
                if "PRON" in lang_type:
                    dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma1"] = accuracy_CogSci21_gamma1
                    dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma2"] = accuracy_CogSci21_gamma2
                    dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma5"] = accuracy_CogSci21_gamma5



        base_acc = dct[lang]["BASE_BASE"]["BASE_BASE1"]["accuracies"]
        if "PRON" in lang_type:
            base_acc_CS1 = dct[lang]["BASE_BASE"]["BASE_BASE1"]["accuracy_CogSci21_gamma1"]
            base_acc_CS2 = dct[lang]["BASE_BASE"]["BASE_BASE1"]["accuracy_CogSci21_gamma2"]
            base_acc_CS5 = dct[lang]["BASE_BASE"]["BASE_BASE1"]["accuracy_CogSci21_gamma5"]
        base_compl = dct[lang]["BASE_BASE"]["BASE_BASE1"]["complexities"]
        base_loss = dct[lang]["BASE_BASE"]["BASE_BASE1"]["crossentropies"]
        for cluster_name in VARIATION_TYPES:
            perm_list = get_permlist(language=lang, lang_type=lang_type, var_type=cluster_name)
            for perm_name in perm_list:
                acc = dct[lang][cluster_name][perm_name]["accuracies"]
                compl = dct[lang][cluster_name][perm_name]["complexities"]
                loss = dct[lang][cluster_name][perm_name]["crossentropies"]
                if "PRON" in lang_type:
                    accCS1 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma1"]
                    accCS2 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma2"]
                    accCS5 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma5"]

                dct[lang][cluster_name][perm_name]["complexities_resp_base"] = compl - base_compl
                dct[lang][cluster_name][perm_name]["accuracies_resp_base"] = acc - base_acc
                dct[lang][cluster_name][perm_name]["crossentropies_resp_base"] = loss - base_loss

                if "PRON" in lang_type:
                    dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma1"] = accCS1 - base_acc_CS1
                    dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma2"] = accCS2 - base_acc_CS2
                    dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma5"] = accCS5 - base_acc_CS5

    # file: name, acc, compl, loss, sync_compl
    print("writing results...")
    for lang in LANGUAGE_LISTS[lang_type]:
        if "PRON" in lang_type:
            res_dict_CogSci21_gamma1 = {var: "lang_type\tlang\tname\tacc\tcompl\tloss\tacc_r_base\tcompl_r_base\tloss_r_base\tnat\tvar_type\tperm_type\tfeat_cat" for var in VARIATION_TYPES + ["PERM","SYN","BASE"] + ["ALL"] + ["BASELIKE_BASELIKE"]}
            res_dict_CogSci21_gamma2 = {var: "lang_type\tlang\tname\tacc\tcompl\tloss\tacc_r_base\tcompl_r_base\tloss_r_base\tnat\tvar_type\tperm_type\tfeat_cat" for var in VARIATION_TYPES + ["PERM","SYN","BASE"] + ["ALL"] + ["BASELIKE_BASELIKE"]}
            res_dict_CogSci21_gamma5 = {var: "lang_type\tlang\tname\tacc\tcompl\tloss\tacc_r_base\tcompl_r_base\tloss_r_base\tnat\tvar_type\tperm_type\tfeat_cat" for var in VARIATION_TYPES + ["PERM","SYN","BASE"] + ["ALL"] + ["BASELIKE_BASELIKE"]}
        res_dict = {var: "lang_type\tlang\tname\tacc\tcompl\tloss\tacc_r_base\tcompl_r_base\tloss_r_base\tnat\tvar_type\tperm_type\tfeat_cat" for var in VARIATION_TYPES + ["PERM","SYN","BASE"] + ["ALL"] + ["BASELIKE_BASELIKE"]}

        #print(res_dict.keys())

        for cluster_name in VARIATION_TYPES:
            perm_list = get_permlist(language=lang, lang_type=lang_type, var_type=cluster_name)
            for perm_name in perm_list:
                acc = dct[lang][cluster_name][perm_name]["accuracies"]
                loss = dct[lang][cluster_name][perm_name]["crossentropies"]
                compl = dct[lang][cluster_name][perm_name]["complexities"]
                naturalness = syncompl_dict[cluster_name][lang][perm_name]
                acc_r_base = dct[lang][cluster_name][perm_name]["accuracies_resp_base"]
                compl_r_base = dct[lang][cluster_name][perm_name]["complexities_resp_base"]
                loss_r_base = dct[lang][cluster_name][perm_name]["crossentropies_resp_base"]
                if "PRON" in lang_type:
                    accCS1 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma1"]
                    accCS2 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma2"]
                    accCS5 = dct[lang][cluster_name][perm_name]["accuracy_CogSci21_gamma5"]
                    acc_r_baseCS1 = dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma1"]
                    acc_r_baseCS2 = dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma2"]
                    acc_r_baseCS5 = dct[lang][cluster_name][perm_name]["accuracies_resp_base_CogSci21_gamma5"]


                #change permutations to shuf if equal
                if dct[lang][cluster_name][perm_name]["equal_to_base"]:
                    type_name = "BASELIKE_BASELIKE"
                elif dct[lang][cluster_name][perm_name]["equal_to_shuf"]:
                    type_name = "SHUF_SHUF"
                else:
                    type_name = cluster_name

                cur_string = "\n"+lang_type  + "\t" + lang + "\t" + lang + "_" + perm_name + "\t" + str(acc) + "\t" + str(compl) + "\t" + str(loss) + "\t" + str(acc_r_base) + "\t" + str(compl_r_base) + "\t" + str(loss_r_base) + "\t" + str(naturalness) + "\t" + str(type_name) + "\t" + str(type_name.split("_")[0]) + "\t" + str(type_name.split("_")[1])
                res_dict[type_name] += cur_string
                if "PERM" in type_name:
                    res_dict["PERM"] += cur_string
                if "SYN" in type_name:
                    res_dict["SYN"] += cur_string
                if "BASE" in type_name and not "BASELIKE" in type_name:
                    res_dict["BASE"] += cur_string
                res_dict["ALL"] += cur_string

                if "PRON" in lang_type:
                    cur_string_CogSci21_gamma1 = "\n"+lang_type+"CogSci21gamma1"  + "\t" + lang + "\t" + lang + "_" + perm_name + "\t" + str(accCS1) + "\t" + str(compl) + "\t" + str(loss) + "\t" + str(acc_r_baseCS1) + "\t" + str(compl_r_base) + "\t" + str(loss_r_base) + "\t" + str(naturalness) + "\t" + str(type_name) + "\t" + str(type_name.split("_")[0]) + "\t" + str(type_name.split("_")[1])
                    cur_string_CogSci21_gamma2 = "\n"+lang_type+"CogSci21gamma2"  + "\t" + lang + "\t" + lang + "_" + perm_name + "\t" + str(accCS2) + "\t" + str(compl) + "\t" + str(loss) + "\t" + str(acc_r_baseCS2) + "\t" + str(compl_r_base) + "\t" + str(loss_r_base) + "\t" + str(naturalness) + "\t" + str(type_name) + "\t" + str(type_name.split("_")[0]) + "\t" + str(type_name.split("_")[1])
                    cur_string_CogSci21_gamma5 = "\n"+lang_type+"CogSci21gamma5"  + "\t" + lang + "\t" + lang + "_" + perm_name + "\t" + str(accCS5) + "\t" + str(compl) + "\t" + str(loss) + "\t" + str(acc_r_baseCS5) + "\t" + str(compl_r_base) + "\t" + str(loss_r_base) + "\t" + str(naturalness) + "\t" + str(type_name) + "\t" + str(type_name.split("_")[0]) + "\t" + str(type_name.split("_")[1])


                    res_dict_CogSci21_gamma1[type_name] += cur_string_CogSci21_gamma1
                    if "PERM" in type_name:
                        res_dict_CogSci21_gamma1["PERM"] += cur_string_CogSci21_gamma1
                    if "SYN" in type_name:
                        res_dict_CogSci21_gamma1["SYN"] += cur_string_CogSci21_gamma1
                    if "BASE" in type_name and not "BASELIKE" in type_name:
                        res_dict_CogSci21_gamma1["BASE"] += cur_string_CogSci21_gamma1
                    res_dict_CogSci21_gamma1["ALL"] += cur_string_CogSci21_gamma1

                    res_dict_CogSci21_gamma2[type_name] += cur_string_CogSci21_gamma2
                    if "PERM" in type_name:
                        res_dict_CogSci21_gamma2["PERM"] += cur_string_CogSci21_gamma2
                    if "SYN" in type_name:
                        res_dict_CogSci21_gamma2["SYN"] += cur_string_CogSci21_gamma2
                    if "BASE" in type_name and not "BASELIKE" in type_name:
                        res_dict_CogSci21_gamma2["BASE"] += cur_string_CogSci21_gamma2
                    res_dict_CogSci21_gamma2["ALL"] += cur_string_CogSci21_gamma2

                    res_dict_CogSci21_gamma5[type_name] += cur_string_CogSci21_gamma5
                    if "PERM" in type_name:
                        res_dict_CogSci21_gamma5["PERM"] += cur_string_CogSci21_gamma5
                    if "SYN" in type_name:
                        res_dict_CogSci21_gamma5["SYN"] += cur_string_CogSci21_gamma5
                    if "BASE" in type_name and not "BASELIKE" in type_name:
                        res_dict_CogSci21_gamma5["BASE"] += cur_string_CogSci21_gamma5
                    res_dict_CogSci21_gamma5["ALL"] += cur_string_CogSci21_gamma5


        for cluster_name, res_str in res_dict.items():
            if not os.path.exists(IB_FOLDERS[lang_type]):
                os.makedirs(IB_FOLDERS[lang_type])
            with open(IB_FOLDERS[lang_type] + "ibvalues_" + lang + "_" + cluster_name + ".tsv", "w") as g:
                g.write(res_str+"\n")

        if "PRON" in lang_type:
            p1 = "/".join(IB_FOLDERS[lang_type].split("/")[:-2])+"/"+"PRONCogSci21gamma1/"
            p2 = "/".join(IB_FOLDERS[lang_type].split("/")[:-2])+"/"+"PRONCogSci21gamma2/"
            p5 = "/".join(IB_FOLDERS[lang_type].split("/")[:-2])+"/"+"PRONCogSci21gamma5/"
            for p in [p1,p2,p5]:
                if not os.path.exists(p):
                   os.makedirs(p)


            for cluster_name, res_str_CogSci21_gamma1 in res_dict_CogSci21_gamma1.items():
                with open(p1 + "ibvalues_" + lang +"CogSci21gamma1_" + cluster_name + ".tsv", "w") as g:
                    g.write(res_str_CogSci21_gamma1+"\n")
            for cluster_name, res_str_CogSci21_gamma2 in res_dict_CogSci21_gamma2.items():
                with open(p2 + "ibvalues_" + lang +"CogSci21gamma2_" + cluster_name + ".tsv", "w") as g:
                    g.write(res_str_CogSci21_gamma2+"\n")
            for cluster_name, res_str_CogSci21_gamma5 in res_dict_CogSci21_gamma5.items():
                with open(p5 + "ibvalues_" + lang +"CogSci21gamma5_" + cluster_name + ".tsv", "w") as g:
                    g.write(res_str_CogSci21_gamma5+"\n")

    print(50*"-")
    print("DONE " + str(lang_type))
    print(50*"-")



if __name__ == "__main__":
    create_ib_files("PRON")

    create_ib_files("rob_unif")
    create_ib_files("rob_rand1")
    create_ib_files("rob_rand2")
    create_ib_files("rob_rand3")


    create_ib_files("VERB_SEM")
    create_ib_files("VERB_SA")
    create_ib_files("VERB_GER")
    create_ib_files("VERB_AKK")
    create_ib_files("VERB_ETH")
    create_ib_files("VERB_ROM")
    create_ib_files("PRON")


    create_ib_files("PR_GER")
    create_ib_files("PR_GER_vh")

    create_ib_files("PR_GREEK")

    create_ib_files("PR_SLAV_S")
    create_ib_files("PR_SLAV_E")
    create_ib_files("PR_SLAV_W")

    create_ib_files("PR_ROM_S")
    create_ib_files("PR_ROM_L")
    create_ib_files("PR_ROM_F")
    create_ib_files("PR_ROM_D")
    create_ib_files("PR_ROM_R")

    create_ib_files("PR_TURK_T")
    create_ib_files("PR_TURK_Th")
    create_ib_files("PR_TURK_A")
    create_ib_files("PR_TURK_Ah")
    create_ib_files("PR_TURK_P")
    create_ib_files("PR_MONG")
    create_ib_files("PR_TUNG_M")
    create_ib_files("PR_TUNG_U")

    create_ib_files("PR_SEM")

    create_ib_files("PR_INDIRA_PROX_U")
    create_ib_files("PR_INDIRA_PROX_P")
    create_ib_files("PR_INDIRA_PROX_A")
    create_ib_files("PR_INDIRA_PROX_B")
    create_ib_files("PR_INDIRA_PROX_G")
    create_ib_files("PR_INDIRA_PROX_I")
    create_ib_files("PR_INDIRA_PROX_M")
    create_ib_files("PR_INDIRA_S")

    create_ib_files("PR_KAUK_A")
    create_ib_files("PR_KAUK_G")
    create_ib_files("PR_KAUK_K")
    create_ib_files("PR_KAUK_C")