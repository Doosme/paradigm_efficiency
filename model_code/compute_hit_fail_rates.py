from util_langlists import LANGUAGE_LISTS
from util import read_ibvalues_from_file
from util_directories import IB_FOLDERS

def caluclate_hit_and_fail_rates(lang_type):
    caluclate_hit_and_fail_rates_for_type(lang_type, perm_type="ALL")
    caluclate_hit_and_fail_rates_for_type(lang_type, perm_type="PERM")
    caluclate_hit_and_fail_rates_for_type(lang_type, perm_type="SHUF_SHUF")
    caluclate_hit_and_fail_rates_for_type(lang_type, perm_type="SYN")

def caluclate_hit_and_fail_rates_for_type(lang_type, perm_type):
    #ib_content_dict[lang_type][lang][name]["acc"]
    ib_content_dict = {lang_type:dict()}
    for lang in LANGUAGE_LISTS[lang_type]:
        ib_content_dict[lang_type][lang] = dict()
        filename = IB_FOLDERS[lang_type] + "ibvalues_"+lang+"_"+perm_type+".tsv"
        read_ibvalues_from_file(filename, ib_content_dict)

    res_text = "lang\tHIT_CETL\tFAIL_CETL\tHIT_MI\tFAIL_MI\tperm_count\tbetter_model"
    overall_HIT_CE_count = 0
    overall_FAIL_CE_count = 0
    overall_HIT_CO_count = 0
    overall_FAIL_CO_count = 0
    overall_perm_count = 0
    for lang in LANGUAGE_LISTS[lang_type]:
        HIT_CE_count = 0
        FAIL_CE_count = 0
        HIT_CO_count = 0
        FAIL_CO_count = 0
        perm_count = 0
        for name in ib_content_dict[lang_type][lang]:
            feat_category = ib_content_dict[lang_type][lang][name]["featcat"]
            if "BASE" in feat_category:
                continue

            perm_count += 1
            acc_r_base = ib_content_dict[lang_type][lang][name]["acc_r_base"]
            loss_r_base = ib_content_dict[lang_type][lang][name]["loss_r_base"]
            compl_r_base = ib_content_dict[lang_type][lang][name]["compl_r_base"]
            if acc_r_base >= -0.0001 and loss_r_base > 0.0001\
                or acc_r_base > 0.0001 and loss_r_base >= -0.0001:
                    HIT_CE_count +=1
            if acc_r_base <= 0.0001 and loss_r_base <= 0.0001:
                    FAIL_CE_count +=1

            if acc_r_base >= -0.0001 and compl_r_base > 0.0001\
                or acc_r_base > 0.0001 and compl_r_base >= -0.0001:
                    HIT_CO_count +=1
            if acc_r_base <= 0.0001 and compl_r_base <= 0.0001:
                    FAIL_CO_count +=1

        overall_perm_count += perm_count
        overall_HIT_CE_count += HIT_CE_count
        overall_FAIL_CE_count += FAIL_CE_count
        overall_HIT_CO_count += HIT_CO_count
        overall_FAIL_CO_count += FAIL_CO_count

        add_const = perm_count / 100*5 #5%

        if HIT_CE_count - FAIL_CE_count > HIT_CO_count - FAIL_CO_count + add_const:
            better = "CETL"
        elif HIT_CO_count - FAIL_CO_count > HIT_CE_count - FAIL_CE_count + add_const:
            better = "MI"
        else:
            better = "None"
        res_text += "\n"+ lang + "\t" + str(HIT_CE_count) + "\t" + str(FAIL_CE_count) + "\t" + str(HIT_CO_count) + "\t" + str(FAIL_CO_count) + "\t"+ str(perm_count) + "\t" + better

    write_filename = IB_FOLDERS[lang_type] + "hitfailvalues_" + lang_type + "_"+perm_type+".tsv"
    with open(write_filename, "w") as g:
        g.write(res_text)
    print(res_text)



if __name__ == "__main__":
    caluclate_hit_and_fail_rates("rob_unif")
    caluclate_hit_and_fail_rates("rob_rand1")
    caluclate_hit_and_fail_rates("rob_rand2")
    caluclate_hit_and_fail_rates("rob_rand3")

    caluclate_hit_and_fail_rates("PRON")
    caluclate_hit_and_fail_rates("PRONCogSci21gamma1")
    caluclate_hit_and_fail_rates("PRONCogSci21gamma2")
    caluclate_hit_and_fail_rates("PRONCogSci21gamma5")
    caluclate_hit_and_fail_rates("VERB_SEM")
    caluclate_hit_and_fail_rates("VERB_SA")
    caluclate_hit_and_fail_rates("VERB_ETH")
    caluclate_hit_and_fail_rates("VERB_AKK")
    caluclate_hit_and_fail_rates("VERB_GER")
    caluclate_hit_and_fail_rates("VERB_ROM")


    caluclate_hit_and_fail_rates("PR_SEM")
    caluclate_hit_and_fail_rates("PR_GER")
    caluclate_hit_and_fail_rates("PR_GER_vh")

    caluclate_hit_and_fail_rates("PR_SLAV_E")
    caluclate_hit_and_fail_rates("PR_SLAV_W")
    caluclate_hit_and_fail_rates("PR_SLAV_S")

    caluclate_hit_and_fail_rates("PR_ROM_S")
    caluclate_hit_and_fail_rates("PR_ROM_L")
    caluclate_hit_and_fail_rates("PR_ROM_F")
    caluclate_hit_and_fail_rates("PR_ROM_D")
    caluclate_hit_and_fail_rates("PR_ROM_R")

    caluclate_hit_and_fail_rates("PR_TURK_T")
    caluclate_hit_and_fail_rates("PR_TURK_Th")
    caluclate_hit_and_fail_rates("PR_TURK_A")
    caluclate_hit_and_fail_rates("PR_TURK_Ah")
    caluclate_hit_and_fail_rates("PR_TURK_P")
    caluclate_hit_and_fail_rates("PR_TUNG_M")
    caluclate_hit_and_fail_rates("PR_TUNG_U")
    caluclate_hit_and_fail_rates("PR_MONG")

    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_U")
    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_P")
    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_A")
    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_B")
    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_G")
    caluclate_hit_and_fail_rates("PR_INDIRA_PROX_I")
    caluclate_hit_and_fail_rates("PR_INDIRA_S")

    caluclate_hit_and_fail_rates("PR_GREEK")

    caluclate_hit_and_fail_rates("PR_KAUK_A")
    caluclate_hit_and_fail_rates("PR_KAUK_G")
    caluclate_hit_and_fail_rates("PR_KAUK_K")
    caluclate_hit_and_fail_rates("PR_KAUK_C")
