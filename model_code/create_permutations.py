import random

from PermSynCreatorVERB import PermSynCreatorAKK, PermSynCreatorETH, PermSynCreatorGER, PermSynCreatorSA, PermSynCreatorSEM, PermSynCreatorROM, PermSynCreatorRobUnif,PermSynCreatorRobRand1,PermSynCreatorRobRand2,PermSynCreatorRobRand3
from PermSynCreatorPRON import PermSynCreatorPRON
from PermSynCreatorPR_SLAV import PermSynCreatorPR_SLAV_E,PermSynCreatorPR_SLAV_W,PermSynCreatorPR_SLAV_S
from PermSynCreatorPR_GER import PermSynCreatorPR_GER, PermSynCreatorPR_GER_vh, PermSynCreatorPR_GREEK, PermSynCreatorPR_INDIRA_S
from PermSynCreatorPR_ROM import PermSynCreatorPR_ROM_S,PermSynCreatorPR_ROM_L, PermSynCreatorPR_ROM_D, PermSynCreatorPR_ROM_F, PermSynCreatorPR_ROM_R
from PermSynCreatorPR_TURK import PermSynCreatorPR_TURK_T, PermSynCreatorPR_TURK_Th, PermSynCreatorPR_TURK_A, PermSynCreatorPR_TURK_Ah, PermSynCreatorPR_TURK_P, PermSynCreatorPR_TUNG_U, PermSynCreatorPR_TUNG_M,PermSynCreatorPR_MONG
from PermSynCreatorPR_SEM import PermSynCreatorPR_SEM, PermSynCreatorPR_SEM_h
from PermSynCreatorPR_IND import PermSynCreatorPR_INDIRA_PROX_U,PermSynCreatorPR_INDIRA_PROX_P,PermSynCreatorPR_INDIRA_PROX_A,PermSynCreatorPR_INDIRA_PROX_B,PermSynCreatorPR_INDIRA_PROX_G,PermSynCreatorPR_INDIRA_PROX_I
from PermSynCreatorPR_KAUK import PermSynCreatorPR_KAUK_A,PermSynCreatorPR_KAUK_G,PermSynCreatorPR_KAUK_K, PermSynCreatorPR_KAUK_C

random.seed(1234)



from util_directories import ORG_PARA_FOLDERS, VARIATION_FOLDERS, PERM_LIST_FOLDER
from util_langlists import LANGUAGE_LISTS





def create_permutation_files(lang_type):
    print("-"*50)
    print(lang_type)
    print("-" * 50)
    for lang in LANGUAGE_LISTS[lang_type]:
        print(lang)
        if lang_type == "VERB_SEM":
            var_creator = PermSynCreatorSEM(lang, file_ending=".tsv")
        elif lang_type == "VERB_GER":
            var_creator = PermSynCreatorGER(lang, file_ending=".tsv")
        elif lang_type == "VERB_SA":
            var_creator = PermSynCreatorSA(lang, file_ending=".tsv")
        elif lang_type == "VERB_AKK":
            var_creator = PermSynCreatorAKK(lang, file_ending=".tsv")
        elif lang_type == "VERB_ETH":
            var_creator = PermSynCreatorETH(lang, file_ending=".tsv")
        elif lang_type == "VERB_ROM":
            var_creator = PermSynCreatorROM(lang, file_ending=".tsv")

        elif lang_type == "PRON":
            var_creator = PermSynCreatorPRON(lang, file_ending=".tsv")

        elif lang_type == "PR_SLAV_E":
            var_creator = PermSynCreatorPR_SLAV_E(lang, file_ending=".tsv")
        elif lang_type == "PR_SLAV_W":
            var_creator = PermSynCreatorPR_SLAV_W(lang, file_ending=".tsv")
        elif lang_type == "PR_SLAV_S":
            var_creator = PermSynCreatorPR_SLAV_S(lang, file_ending=".tsv")
        elif lang_type == "PR_GER":
            var_creator = PermSynCreatorPR_GER(lang, file_ending=".tsv")
        elif lang_type == "PR_GER_vh":
            var_creator = PermSynCreatorPR_GER_vh(lang, file_ending=".tsv")
        elif lang_type == "PR_ROM_D":
            var_creator = PermSynCreatorPR_ROM_D(lang, file_ending=".tsv")
        elif lang_type == "PR_ROM_R":
            var_creator = PermSynCreatorPR_ROM_R(lang, file_ending=".tsv")
        elif lang_type == "PR_ROM_F":
            var_creator = PermSynCreatorPR_ROM_F(lang, file_ending=".tsv")
        elif lang_type == "PR_ROM_S":
            var_creator = PermSynCreatorPR_ROM_S(lang, file_ending=".tsv")
        elif lang_type == "PR_ROM_L":
            var_creator = PermSynCreatorPR_ROM_L(lang, file_ending=".tsv")
        elif lang_type == "PR_TURK_T":
            var_creator = PermSynCreatorPR_TURK_T(lang, file_ending=".tsv")
        elif lang_type == "PR_TURK_Th":
            var_creator = PermSynCreatorPR_TURK_Th(lang, file_ending=".tsv")
        elif lang_type == "PR_TURK_P":
            var_creator = PermSynCreatorPR_TURK_P(lang, file_ending=".tsv")
        elif lang_type == "PR_TURK_A":
            var_creator = PermSynCreatorPR_TURK_A(lang, file_ending=".tsv")
        elif lang_type == "PR_TURK_Ah":
            var_creator = PermSynCreatorPR_TURK_Ah(lang, file_ending=".tsv")
        elif lang_type == "PR_TUNG_U":
            var_creator = PermSynCreatorPR_TUNG_U(lang, file_ending=".tsv")
        elif lang_type == "PR_TUNG_M":
            var_creator = PermSynCreatorPR_TUNG_M(lang, file_ending=".tsv")
        elif lang_type == "PR_MONG":
            var_creator = PermSynCreatorPR_MONG(lang, file_ending=".tsv")
        elif lang_type == "PR_SEM":
            var_creator = PermSynCreatorPR_SEM(lang, file_ending=".tsv")
        elif lang_type == "PR_SEM_h":
            var_creator = PermSynCreatorPR_SEM_h(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_U":
            var_creator = PermSynCreatorPR_INDIRA_PROX_U(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_P":
            var_creator = PermSynCreatorPR_INDIRA_PROX_P(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_A":
            var_creator = PermSynCreatorPR_INDIRA_PROX_A(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_B":
            var_creator = PermSynCreatorPR_INDIRA_PROX_B(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_G":
            var_creator = PermSynCreatorPR_INDIRA_PROX_G(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_I":
            var_creator = PermSynCreatorPR_INDIRA_PROX_I(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_PROX_M":
            var_creator = PermSynCreatorPR_INDIRA_PROX_M(lang, file_ending=".tsv")
        elif lang_type == "PR_INDIRA_S":
            var_creator = PermSynCreatorPR_INDIRA_S(lang, file_ending=".tsv")
        elif lang_type == "PR_KAUK_A":
            var_creator = PermSynCreatorPR_KAUK_A(lang, file_ending=".tsv")
        elif lang_type == "PR_KAUK_G":
            var_creator = PermSynCreatorPR_KAUK_G(lang, file_ending=".tsv")
        elif lang_type == "PR_KAUK_K":
            var_creator = PermSynCreatorPR_KAUK_K(lang, file_ending=".tsv")
        elif lang_type == "PR_KAUK_C":
            var_creator = PermSynCreatorPR_KAUK_C(lang, file_ending=".tsv")
        elif lang_type == "PR_GREEK":
            var_creator = PermSynCreatorPR_GREEK(lang, file_ending=".tsv")

        elif lang_type == "rob_unif":
            var_creator = PermSynCreatorRobUnif(lang, file_ending=".tsv")
        elif lang_type == "rob_rand1":
            var_creator = PermSynCreatorRobRand1(lang, file_ending=".tsv")
        elif lang_type == "rob_rand2":
            var_creator = PermSynCreatorRobRand2(lang, file_ending=".tsv")
        elif lang_type == "rob_rand3":
            var_creator = PermSynCreatorRobRand3(lang, file_ending=".tsv")
        else:
            raise Exception("ERROR: language type unknown" + str(lang_type))

        var_creator.create_permutations_and_syncretisms(ORG_PARA_FOLDERS[lang_type])
        var_creator.write_permutations_to_files(VARIATION_FOLDERS[lang_type], PERM_LIST_FOLDER[lang_type])


if __name__ == "__main__":
    create_permutation_files("rob_unif")
    create_permutation_files("rob_rand1")
    create_permutation_files("rob_rand2")
    create_permutation_files("rob_rand3")


    create_permutation_files("VERB_SEM")
    create_permutation_files("VERB_SA")
    create_permutation_files("VERB_GER")
    create_permutation_files("VERB_AKK")
    create_permutation_files("VERB_ETH")
    create_permutation_files("VERB_ROM")

    create_permutation_files("PRON")

    create_permutation_files("PR_SLAV_S")
    create_permutation_files("PR_SLAV_E")
    create_permutation_files("PR_SLAV_W")

    create_permutation_files("PR_GER")
    create_permutation_files("PR_GER_vh")

    create_permutation_files("PR_ROM_S")
    create_permutation_files("PR_ROM_L")
    create_permutation_files("PR_ROM_F")
    create_permutation_files("PR_ROM_D")
    create_permutation_files("PR_ROM_R")

    create_permutation_files("PR_TURK_T")
    create_permutation_files("PR_TURK_Th")
    create_permutation_files("PR_TURK_A")
    create_permutation_files("PR_TURK_Ah")
    create_permutation_files("PR_TURK_P")
    create_permutation_files("PR_TUNG_M")
    create_permutation_files("PR_TUNG_U")
    create_permutation_files("PR_MONG")


    create_permutation_files("PR_SEM")


    create_permutation_files("PR_INDIRA_PROX_U")
    create_permutation_files("PR_INDIRA_PROX_P")
    create_permutation_files("PR_INDIRA_PROX_A")
    create_permutation_files("PR_INDIRA_PROX_B")
    create_permutation_files("PR_INDIRA_PROX_G")
    create_permutation_files("PR_INDIRA_PROX_I")
    create_permutation_files("PR_INDIRA_PROX_M")
    create_permutation_files("PR_INDIRA_S")

    create_permutation_files("PR_KAUK_A")
    create_permutation_files("PR_KAUK_G")
    create_permutation_files("PR_KAUK_K")
    create_permutation_files("PR_KAUK_C")

    create_permutation_files("PR_GREEK")
