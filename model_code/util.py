
LANG_TYPES_rob = ["rob_unif","rob_rand1","rob_rand2","rob_rand3"]
LANG_TYPES_VERB = ["VERB_SEM","VERB_SA","VERB_ETH","VERB_AKK","VERB_GER","VERB_ROM"]
LANG_TYPES_PRON = ["PRON"]
LANG_TYPES_PRONCogSci = ["PRONCogSci21gamma1","PRONCogSci21gamma2","PRONCogSci21gamma5"]
LANG_TYPES_PR = ["PR_SLAV_E","PR_SLAV_S","PR_SLAV_W",
              "PR_GER", "PR_GER_vh","PR_SEM",
              "PR_ROM_D","PR_ROM_R","PR_ROM_F","PR_ROM_S","PR_ROM_L",
              "PR_TURK_P", "PR_TURK_T","PR_TURK_Th","PR_TURK_A","PR_TURK_Ah","PR_TUNG_U","PR_TUNG_M","PR_MONG",
                 "PR_INDIRA_PROX_U","PR_INDIRA_PROX_P","PR_INDIRA_PROX_A","PR_INDIRA_PROX_B","PR_INDIRA_PROX_G","PR_INDIRA_S","PR_INDIRA_PROX_I",
                 "PR_KAUK_A","PR_KAUK_G","PR_KAUK_K","PR_KAUK_C","PR_GREEK"]
LANG_TYPES = LANG_TYPES_VERB + LANG_TYPES_PRON + LANG_TYPES_PR + LANG_TYPES_rob


def read_in_paradigm(input_filename):
    content_dict = dict()
    with open(input_filename) as f:
        for line in f:
            line = line.strip().split("\t")
            assert (len(line) == 2)
            content_dict[line[0]] = line[1]
    return content_dict



def read_in_syncretism_classes(input_filename):
    content_dict = dict()
    with open(input_filename) as f:
        for line in f:
            line = line.strip().split("\t")
            assert (len(line) == 2)
            if line[1] in content_dict.keys():
                content_dict[line[1]].append(line[0])
            else:
                content_dict[line[1]] = [line[0]]
    return content_dict

def read_in_ibfile(ibfile):
    firstline = True
    res_dic = dict()
    with open(ibfile) as f:
        for line in f:
            if firstline:
                firstline = False
                continue
            line = line.split()
            res_dic[line[2]] = dict()
            res_dic[line[2]]["lang_type"] = line[0]
            res_dic[line[2]]["lang"] = line[1]
            res_dic[line[2]]["acc"] = line[3]
            res_dic[line[2]]["compl"] = line[4]
            res_dic[line[2]]["loss"] = line[5]
            res_dic[line[2]]["acc_r_base"] = line[6]
            res_dic[line[2]]["compl_r_base"] = line[7]
            res_dic[line[2]]["loss_r_base"] = line[8]
            res_dic[line[2]]["nat"] = line[9]
            res_dic[line[2]]["var_type"] = line[10]
            res_dic[line[2]]["perm_type"] = line[11]
            res_dic[line[2]]["feat_cat"] = line[12]
    return res_dic
            


def read_ibvalues_from_file(ibfile, ib_content_dict):
    with open(ibfile) as f:
        firstline = True
        for line in f:
            if firstline:
                firstline = False
                #lang_type	lang	name	acc	compl	loss	acc_r_base	compl_r_base	loss_r_base	nat	vartype	permtype	featcat
                continue
            line = line.strip().split("\t")
            lang_type, lang, name, acc, compl, loss, acc_r_base, compl_r_base, loss_r_base, nat, vartype, permtype, featcat = line
            if lang_type == "PRONCogSci21gamma1":
                lang = lang + "CogSci21gamma1"
            if lang_type == "PRONCogSci21gamma2":
                lang = lang + "CogSci21gamma2"
            if lang_type == "PRONCogSci21gamma5":
                lang = lang + "CogSci21gamma5"

            if permtype == "SYN":
                continue

            if name not in ib_content_dict[lang_type][lang]:
                ib_content_dict[lang_type][lang][name] = dict()

            ib_content_dict[lang_type][lang][name]["acc"] = float(acc)
            ib_content_dict[lang_type][lang][name]["compl"] = float(compl)
            ib_content_dict[lang_type][lang][name]["loss"] = float(loss)
            ib_content_dict[lang_type][lang][name]["acc_r_base"] = float(acc_r_base)
            ib_content_dict[lang_type][lang][name]["compl_r_base"] = float(compl_r_base)
            ib_content_dict[lang_type][lang][name]["loss_r_base"] = float(loss_r_base)
            ib_content_dict[lang_type][lang][name]["nat"] = int(nat)
            ib_content_dict[lang_type][lang][name]["vartype"] = vartype
            ib_content_dict[lang_type][lang][name]["permtype"] = permtype
            ib_content_dict[lang_type][lang][name]["featcat"] = featcat





def read_weights_from_file(freq_file):
    """
    reads in the weights from a file and creates a dictionary of weights
    :param freq_file: file containing the weights
    :return: dict: feature -> weights
    """
    weights_dict = dict()
    with open(freq_file) as f:
        data = f.read()
        data = data.strip()
        data = data.split("\n")
        for item in data:
            item = item.split("\t")
            feat = item[0]
            weight = float(item[1])
            weights_dict[feat] = weight
    print(weights_dict)
    return weights_dict
