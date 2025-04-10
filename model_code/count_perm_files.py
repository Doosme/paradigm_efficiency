import os

from util_directories import IB_FOLDERS
from util import LANG_TYPES_VERB, LANG_TYPES_PR, read_in_ibfile

Afro_count = 0
Sem_count = 0
Ger_count = 0
Rom_count = 0


for lang_type in LANG_TYPES_VERB:
    for file in os.listdir(IB_FOLDERS[lang_type]):
        if file.startswith("ibvalues") and "_ALL.tsv" in file:
            #print(file)
            ib_dic = read_in_ibfile(IB_FOLDERS[lang_type] + file)
            for perm in ib_dic.keys():
                if "PERM" in ib_dic[perm]["perm_type"] or "SHUF" in ib_dic[perm]["perm_type"]:
                    if "Germanic" in perm:
                        Ger_count += 1
                    elif "Berber" in perm or "Cushitic" in perm or "Egyptian" in perm or "Chadic" in perm or "Omotic" in perm:
                        Afro_count += 1
                    elif "Romanic" in perm:
                        Rom_count +=1
                    else:
                        Sem_count +=1
                        
print("VERBs:")
print("AFRO: " + str(Afro_count))
print("SEM: " + str(Sem_count))
print("GER: " + str(Ger_count))
print("ROM: " + str(Rom_count))


print()

Afro_count = 0
Sem_count = 0
Ger_count = 0
Rom_count = 0
Slav_count = 0
Altaic_count = 0
Indira_count = 0 #indo-iranian
Other_IE_count = 0


for lang_type in LANG_TYPES_PR:
    for file in os.listdir(IB_FOLDERS[lang_type]):
        if file.startswith("ibvalues") and "_ALL.tsv" in file:
            ib_dic = read_in_ibfile(IB_FOLDERS[lang_type] + file)
            for perm in ib_dic.keys():
                if "PERM" in ib_dic[perm]["perm_type"] or "SHUF" in ib_dic[perm]["perm_type"]:
                    if "GER" in lang_type:
                        Ger_count += 1
                    elif "SEM" in lang_type:
                        if "Berber" in perm or "Cushitic" in perm or perm.startswith("Egyptian") or "Chadic" in perm or "Omotic" in perm:
                            Afro_count += 1
                        else:
                            Sem_count += 1
                    elif "TURK" in lang_type or "TUNG" in lang_type or "MONG" in lang_type:
                        Altaic_count += 1
                    elif "SLAV" in lang_type:
                        Slav_count += 1
                    elif "ROM" in lang_type:
                        if perm.startswith("Albanian"):
                            Other_IE_count += 1
                        else:
                            Rom_count += 1
                    elif "GREEK" in lang_type:
                        Other_IE_count += 1
                    elif "KAUK" in lang_type:
                        if "KAUK_K" in lang_type:
                            Indira_count += 1
                        else:
                            Other_IE_count += 1
                    elif "INDIRA" in lang_type:
                        if perm.startswith("ProtoIndoEuro"):
                            Other_IE_count += 1
                        else:
                            Indira_count += 1


print("PR:")
print("AFRO: " + str(Afro_count))
print("SEM: " + str(Sem_count))
print("GER: " + str(Ger_count))
print("ROM: " + str(Rom_count))
print("SLAV: " + str(Slav_count))
print("ALTAIC: " + str(Altaic_count))
print("INDIRA: " + str(Indira_count))
print("OTHER_IE: " + str(Other_IE_count))



print()
Pron_count = 0

for lang_type in LANG_TYPES_PR:
    for file in os.listdir(IB_FOLDERS[lang_type]):
        if file.startswith("ibvalues") and "_ALL.tsv" in file:
            ib_dic = read_in_ibfile(IB_FOLDERS[lang_type] + file)
            for perm in ib_dic.keys():
                if "PERM" in ib_dic[perm]["perm_type"] or "SHUF" in ib_dic[perm]["perm_type"]:
                    Pron_count += 1

print("PRON:")
print("PRON: " + str(Pron_count))



print()


Afro_count = 0
Sem_count = 0
Ger_count = 0
Rom_count = 0
Slav_count = 0
Altaic_count = 0
Indira_count = 0 #indo-iranian
Other_IE_count = 0


for lang_type in LANG_TYPES_PR:
    for file in os.listdir(IB_FOLDERS[lang_type]):
        if file.startswith("ibvalues") and "_ALL.tsv" in file:
            if "GER" in lang_type:
                Ger_count += 1
            elif "SEM" in lang_type:
                if "Berber" in file or "Cushitic" in file or file.startswith("Egyptian") or "Chadic" in file or "Omotic" in file:
                    Afro_count += 1
                else:
                    Sem_count += 1
            elif "TURK" in lang_type or "TUNG" in lang_type or "MONG" in lang_type:
                Altaic_count += 1
            elif "SLAV" in lang_type:
                Slav_count += 1
            elif "ROM" in lang_type:
                if file.startswith("Albanian"):
                    Other_IE_count += 1
                else:
                    Rom_count += 1
            elif "GREEK" in lang_type:
                Other_IE_count += 1
            elif "KAUK" in lang_type:
                if "KAUK_K" in lang_type:
                    Indira_count += 1
                else:
                    Other_IE_count += 1
            elif "INDIRA" in lang_type:
                if file.startswith("ProtoIndoEuro"):
                    Other_IE_count += 1
                else:
                    Indira_count +=1


print("PR #languages :")
print("AFRO: " + str(Afro_count))
print("SEM: " + str(Sem_count))
print("GER: " + str(Ger_count))
print("ROM: " + str(Rom_count))
print("SLAV: " + str(Slav_count))
print("ALTAIC: " + str(Altaic_count))
print("INDIRA: " + str(Indira_count))
print("OTHER_IE: " + str(Other_IE_count))
