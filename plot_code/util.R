library(ggplot2)
library(ggpubr)
library(dplyr)
library(tidyverse)

create_singletype_ib_content_list <- function(lang_type,lang_subtype,lang_list,perm_type) {
  res <- 0
  first <- 0
  for (lang in lang_list$V1) {  
    current <- read.csv(paste(IB_INPUT_DIR,lang_type,"/",lang_subtype,"/ibvalues_",lang,"_",perm_type,".tsv", sep=""),sep="\t", colClasses = c("character","character","character", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "numeric", "character","character","character"))
    if (first == 0) {
      first <- 1
      res <- current
    } else{
      res <- rbind(res, current)
    }
  }
  return (res)
}

#reads in ib_values of the Verbs data for a given perm_type (consisting of SYN,PERM,SHUF,BASE)
create_VERB_ib_df <- function(perm_type) {
  VERB_SEM_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_SEM",sep=""),sep="\t",  header = FALSE)
  VERB_SA_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_SA",sep=""),sep="\t",  header = FALSE)
  VERB_AKK_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_AKK",sep=""),sep="\t",  header = FALSE)
  VERB_ETH_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_ETH",sep=""),sep="\t",  header = FALSE)
  VERB_GER_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_GER",sep=""),sep="\t",  header = FALSE)
  VERB_ROM_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_VERB_ROM",sep=""),sep="\t",  header = FALSE)
  
  res_df <- data.frame(lang_type=character(),
                       lang=character(), 
                       name=character(), 
                       acc=numeric(),
                       compl=numeric(),
                       loss=numeric(),
                       acc_r_base=numeric(),
                       compl_r_base=numeric(),
                       loss_r_base=numeric(),
                       nat=numeric(),
                       var_type=character(),
                       perm_type=character(),
                       feat_cat=character(),
                       stringsAsFactors=FALSE) 
  
  if (grepl("SHUF", perm_type, fixed = TRUE)){
    verb_curr_df_1 <- create_singletype_ib_content_list("VERB","VERB_SEM",VERB_SEM_LIST,"SHUF_SHUF")
    verb_curr_df_2 <- create_singletype_ib_content_list("VERB","VERB_SA",VERB_SA_LIST,"SHUF_SHUF")
    verb_curr_df_3 <- create_singletype_ib_content_list("VERB","VERB_ETH",VERB_ETH_LIST,"SHUF_SHUF")
    verb_curr_df_4 <- create_singletype_ib_content_list("VERB","VERB_AKK",VERB_AKK_LIST,"SHUF_SHUF")
    verb_curr_df_5 <- create_singletype_ib_content_list("VERB","VERB_GER",VERB_GER_LIST,"SHUF_SHUF")
    verb_curr_df_6 <- create_singletype_ib_content_list("VERB","VERB_ROM",VERB_ROM_LIST,"SHUF_SHUF")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (grepl("BASE", perm_type, fixed = TRUE)){
    verb_curr_df_1 <- create_singletype_ib_content_list("VERB","VERB_SEM",VERB_SEM_LIST,"BASE")
    verb_curr_df_2 <- create_singletype_ib_content_list("VERB","VERB_SA",VERB_SA_LIST,"BASE")
    verb_curr_df_3 <- create_singletype_ib_content_list("VERB","VERB_ETH",VERB_ETH_LIST,"BASE")
    verb_curr_df_4 <- create_singletype_ib_content_list("VERB","VERB_AKK",VERB_AKK_LIST,"BASE")
    verb_curr_df_5 <- create_singletype_ib_content_list("VERB","VERB_GER",VERB_GER_LIST,"BASE")
    verb_curr_df_6 <- create_singletype_ib_content_list("VERB","VERB_ROM",VERB_ROM_LIST,"BASE")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (grepl("PERM", perm_type, fixed = TRUE)){
    verb_curr_df_1 <- create_singletype_ib_content_list("VERB","VERB_SEM",VERB_SEM_LIST,"PERM")
    verb_curr_df_2 <- create_singletype_ib_content_list("VERB","VERB_SA",VERB_SA_LIST,"PERM")
    verb_curr_df_3 <- create_singletype_ib_content_list("VERB","VERB_ETH",VERB_ETH_LIST,"PERM")
    verb_curr_df_4 <- create_singletype_ib_content_list("VERB","VERB_AKK",VERB_AKK_LIST,"PERM")
    verb_curr_df_5 <- create_singletype_ib_content_list("VERB","VERB_GER",VERB_GER_LIST,"PERM")
    verb_curr_df_6 <- create_singletype_ib_content_list("VERB","VERB_ROM",VERB_ROM_LIST,"PERM")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (grepl("SYN", perm_type, fixed = TRUE)){
    verb_curr_df_1 <- create_singletype_ib_content_list("VERB","VERB_SEM",VERB_SEM_LIST,"SYN")
    verb_curr_df_2 <- create_singletype_ib_content_list("VERB","VERB_SA",VERB_SA_LIST,"SYN")
    verb_curr_df_3 <- create_singletype_ib_content_list("VERB","VERB_ETH",VERB_ETH_LIST,"SYN")
    verb_curr_df_4 <- create_singletype_ib_content_list("VERB","VERB_AKK",VERB_AKK_LIST,"SYN")
    verb_curr_df_5 <- create_singletype_ib_content_list("VERB","VERB_GER",VERB_GER_LIST,"SYN")
    verb_curr_df_6 <- create_singletype_ib_content_list("VERB","VERB_ROM",VERB_ROM_LIST,"SYN")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  
  verb_res_df <- mutate(res_df, paradigm_type=lang_type)
  
  verb_res_df <- mutate(verb_res_df, lang_family = ifelse(startsWith(lang,"Germanic"), "GER", 
                                                          ifelse(startsWith(lang,"Berber"), "AFRO", 
                                                                 ifelse(startsWith(lang,"Cushitic"), "AFRO", 
                                                                        ifelse(startsWith(lang,"Omotic"), "AFRO", 
                                                                               ifelse(startsWith(lang,"Egyptian"), "AFRO", 
                                                                                      ifelse(startsWith(lang,"Chadic"), "AFRO",
                                                                                             ifelse(startsWith(lang,"Romanic"), "ROM","SEM")
                                                                                      )))))
  ))
  
  verb_res_df <- mutate(verb_res_df, lang_subgroup = ifelse(startsWith(lang,"Germanic"), "Germ", 
                                                            ifelse(startsWith(lang,"Berber"), "Afro", 
                                                                   ifelse(startsWith(lang,"Cushitic"), "Afro", 
                                                                          ifelse(startsWith(lang,"Omotic"), "Afro", 
                                                                                 ifelse(startsWith(lang,"Egyptian"), "Afro", 
                                                                                        ifelse(startsWith(lang,"Chadic"), "Afro",
                                                                                               ifelse(startsWith(lang,"Romanic"), "Rom",
                                                                                                      ifelse(startsWith(lang,"Akkadian"), "EastSem",
                                                                                                             ifelse(startsWith(lang,"Ethiopic"), "SouthSem",
                                                                                                                    ifelse(startsWith(lang,"SouthArabian"), "SouthSem","CentSem") #todo: actually what is ProtoSemitic? (everything else is definitily CentSem, but Protosemitic I'm not sure)
                                                                                                             )))
                                                                                        )))))
  ))
  
  return (verb_res_df)
}


#reads in ib_values of the Pronouns data for a given perm_type (consisting of SYN,PERM,SHUF,BASE)
create_PRON_ib_df <- function(perm_type) {
  PR_TURK_A_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TURK_A",sep=""),sep="\t",  header = FALSE)
  PR_TURK_Ah_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TURK_Ah",sep=""),sep="\t",  header = FALSE)
  PR_TURK_T_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TURK_T",sep=""),sep="\t",  header = FALSE)
  PR_TURK_Th_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TURK_Th",sep=""),sep="\t",  header = FALSE)
  PR_TURK_P_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TURK_P",sep=""),sep="\t",  header = FALSE)
  PR_MONG_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_MONG",sep=""),sep="\t",  header = FALSE)
  PR_TUNG_U_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TUNG_U",sep=""),sep="\t",  header = FALSE)
  PR_TUNG_M_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_TUNG_M",sep=""),sep="\t",  header = FALSE)
  
  PR_KAUK_A_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_KAUK_A",sep=""),sep="\t",  header = FALSE)
  PR_KAUK_G_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_KAUK_G",sep=""),sep="\t",  header = FALSE)
  PR_KAUK_K_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_KAUK_K",sep=""),sep="\t",  header = FALSE)
  PR_KAUK_C_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_KAUK_C",sep=""),sep="\t",  header = FALSE)
  
  PR_INDIRA_U_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_U",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_P_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_P",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_A_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_A",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_B_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_B",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_G_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_G",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_I_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_I",sep=""),sep="\t",  header = FALSE)
  #PR_INDIRA_M_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_PROX_M",sep=""),sep="\t",  header = FALSE)
  PR_INDIRA_S_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_INDIRA_S",sep=""),sep="\t",  header = FALSE)
  
  PR_SLAV_W_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_SLAV_W",sep=""),sep="\t",  header = FALSE)
  PR_SLAV_E_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_SLAV_E",sep=""),sep="\t",  header = FALSE)
  PR_SLAV_S_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_SLAV_S",sep=""),sep="\t",  header = FALSE)
  
  PR_GREEK_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_GREEK",sep=""),sep="\t",  header = FALSE)
  
  PR_GERv_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_GER",sep=""),sep="\t",  header = FALSE)
  PR_GERvh_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_GER_vh",sep=""),sep="\t",  header = FALSE)
  
  PR_ROM_D_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_ROM_D",sep=""),sep="\t",  header = FALSE)
  PR_ROM_F_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_ROM_F",sep=""),sep="\t",  header = FALSE)
  PR_ROM_R_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_ROM_R",sep=""),sep="\t",  header = FALSE)
  PR_ROM_S_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_ROM_S",sep=""),sep="\t",  header = FALSE)
  PR_ROM_L_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_ROM_L",sep=""),sep="\t",  header = FALSE)
  PR_SEM_LIST <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PR_SEM",sep=""),sep="\t",  header = FALSE)
  
  res_df <- data.frame(lang_type=character(),
                       lang=character(), 
                       name=character(), 
                       acc=numeric(),
                       compl=numeric(),
                       loss=numeric(),
                       acc_r_base=numeric(),
                       compl_r_base=numeric(),
                       loss_r_base=numeric(),
                       nat=numeric(),
                       var_type=character(),
                       perm_type=character(),
                       feat_cat=character(),
                       stringsAsFactors=FALSE) 
  
  if (grepl("SHUF", perm_type, fixed = TRUE)){
    turkA <- create_singletype_ib_content_list("PR","PR_TURK_A",PR_TURK_A_LIST,"SHUF_SHUF")
    turkAh <- create_singletype_ib_content_list("PR","PR_TURK_Ah",PR_TURK_Ah_LIST,"SHUF_SHUF")
    turkT <- create_singletype_ib_content_list("PR","PR_TURK_T",PR_TURK_T_LIST,"SHUF_SHUF")
    turkTh <- create_singletype_ib_content_list("PR","PR_TURK_Th",PR_TURK_Th_LIST,"SHUF_SHUF")
    turkP <- create_singletype_ib_content_list("PR","PR_TURK_P",PR_TURK_P_LIST,"SHUF_SHUF")
    mong <- create_singletype_ib_content_list("PR","PR_MONG",PR_MONG_LIST,"SHUF_SHUF")
    tungU <- create_singletype_ib_content_list("PR","PR_TUNG_U",PR_TUNG_U_LIST,"SHUF_SHUF")
    tungM <- create_singletype_ib_content_list("PR","PR_TUNG_M",PR_TUNG_M_LIST,"SHUF_SHUF")
    cur_altai <- rbind(turkA, turkAh, turkT, turkTh, turkP, mong, tungU, tungM)
    kaukA <- create_singletype_ib_content_list("PR","PR_KAUK_A",PR_KAUK_A_LIST, "SHUF_SHUF")
    kaukG <- create_singletype_ib_content_list("PR","PR_KAUK_G",PR_KAUK_G_LIST, "SHUF_SHUF")
    kaukK <- create_singletype_ib_content_list("PR","PR_KAUK_K",PR_KAUK_K_LIST, "SHUF_SHUF")
    kaukC <- create_singletype_ib_content_list("PR","PR_KAUK_C",PR_KAUK_C_LIST, "SHUF_SHUF")
    cur_kauk <- rbind(kaukA, kaukG, kaukK, kaukC)
    indiraU <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_U",PR_INDIRA_U_LIST, "SHUF_SHUF")
    indiraP <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_P",PR_INDIRA_P_LIST, "SHUF_SHUF")
    indiraA <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_A",PR_INDIRA_A_LIST, "SHUF_SHUF")
    indiraB <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_B",PR_INDIRA_B_LIST, "SHUF_SHUF")
    indiraG <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_G",PR_INDIRA_G_LIST, "SHUF_SHUF")
    indiraI <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_I",PR_INDIRA_I_LIST, "SHUF_SHUF")
    #indiraM <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_M",PR_INDIRA_M_LIST, "SHUF_SHUF")
    indiraS <- create_singletype_ib_content_list("PR","PR_INDIRA_S",PR_INDIRA_S_LIST, "SHUF_SHUF")
    cur_indira <- rbind(indiraU, indiraP, indiraA, indiraB, indiraG, indiraI, indiraS)#, indiraM
    slavW <- create_singletype_ib_content_list("PR","PR_SLAV_W",PR_SLAV_W_LIST, "SHUF_SHUF")
    slavE <- create_singletype_ib_content_list("PR","PR_SLAV_E",PR_SLAV_E_LIST, "SHUF_SHUF")
    slavS <- create_singletype_ib_content_list("PR","PR_SLAV_S",PR_SLAV_S_LIST, "SHUF_SHUF")
    cur_slav <- rbind(slavW, slavE, slavS)
    romD <- create_singletype_ib_content_list("PR","PR_ROM_D",PR_ROM_D_LIST, "SHUF_SHUF")
    romF <- create_singletype_ib_content_list("PR","PR_ROM_F",PR_ROM_F_LIST, "SHUF_SHUF")
    romR <- create_singletype_ib_content_list("PR","PR_ROM_R",PR_ROM_R_LIST, "SHUF_SHUF")
    romS <- create_singletype_ib_content_list("PR","PR_ROM_S",PR_ROM_S_LIST, "SHUF_SHUF")
    romL <- create_singletype_ib_content_list("PR","PR_ROM_L",PR_ROM_L_LIST, "SHUF_SHUF")
    cur_rom <- rbind(romD, romF, romR, romS, romL)
    gre <- create_singletype_ib_content_list("PR","PR_GREEK",PR_GREEK_LIST, "SHUF_SHUF")
    ger <- create_singletype_ib_content_list("PR","PR_GER",PR_GERv_LIST, "SHUF_SHUF")
    ger2 <- create_singletype_ib_content_list("PR","PR_GER_vh",PR_GERvh_LIST, "SHUF_SHUF")
    sem <- create_singletype_ib_content_list("PR","PR_SEM",PR_SEM_LIST, "SHUF_SHUF")
    cur_rest <- rbind(gre, ger, ger2, sem)
    pr_curr_df <- rbind(cur_altai,cur_kauk,cur_indira,cur_slav,cur_rom,cur_rest)
    res_df <- rbind(res_df, pr_curr_df)
  }
  if (grepl("BASE", perm_type, fixed = TRUE)){
    turkA <- create_singletype_ib_content_list("PR","PR_TURK_A",PR_TURK_A_LIST,"BASE")
    turkAh <- create_singletype_ib_content_list("PR","PR_TURK_Ah",PR_TURK_Ah_LIST,"BASE")
    turkT <- create_singletype_ib_content_list("PR","PR_TURK_T",PR_TURK_T_LIST,"BASE")
    turkTh <- create_singletype_ib_content_list("PR","PR_TURK_Th",PR_TURK_Th_LIST,"BASE")
    turkP <- create_singletype_ib_content_list("PR","PR_TURK_P",PR_TURK_P_LIST,"BASE")
    mong <- create_singletype_ib_content_list("PR","PR_MONG",PR_MONG_LIST,"BASE")
    tungU <- create_singletype_ib_content_list("PR","PR_TUNG_U",PR_TUNG_U_LIST,"BASE")
    tungM <- create_singletype_ib_content_list("PR","PR_TUNG_M",PR_TUNG_M_LIST,"BASE")
    cur_altai <- rbind(turkA, turkAh, turkT, turkTh, turkP, mong, tungU, tungM)
    kaukA <- create_singletype_ib_content_list("PR","PR_KAUK_A",PR_KAUK_A_LIST, "BASE")
    kaukG <- create_singletype_ib_content_list("PR","PR_KAUK_G",PR_KAUK_G_LIST, "BASE")
    kaukK <- create_singletype_ib_content_list("PR","PR_KAUK_K",PR_KAUK_K_LIST, "BASE")
    kaukC <- create_singletype_ib_content_list("PR","PR_KAUK_C",PR_KAUK_C_LIST, "BASE")
    cur_kauk <- rbind(kaukA, kaukG, kaukK, kaukC)
    indiraU <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_U",PR_INDIRA_U_LIST, "BASE")
    indiraP <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_P",PR_INDIRA_P_LIST, "BASE")
    indiraA <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_A",PR_INDIRA_A_LIST, "BASE")
    indiraB <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_B",PR_INDIRA_B_LIST, "BASE")
    indiraG <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_G",PR_INDIRA_G_LIST, "BASE")
    indiraI <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_I",PR_INDIRA_I_LIST, "BASE")
    #indiraM <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_M",PR_INDIRA_M_LIST, "BASE")
    indiraS <- create_singletype_ib_content_list("PR","PR_INDIRA_S",PR_INDIRA_S_LIST, "BASE")
    cur_indira <- rbind(indiraU, indiraP, indiraA, indiraB, indiraG, indiraI, indiraS)#, indiraM
    slavW <- create_singletype_ib_content_list("PR","PR_SLAV_W",PR_SLAV_W_LIST, "BASE")
    slavE <- create_singletype_ib_content_list("PR","PR_SLAV_E",PR_SLAV_E_LIST, "BASE")
    slavS <- create_singletype_ib_content_list("PR","PR_SLAV_S",PR_SLAV_S_LIST, "BASE")
    cur_slav <- rbind(slavW, slavE, slavS)
    romD <- create_singletype_ib_content_list("PR","PR_ROM_D",PR_ROM_D_LIST, "BASE")
    romF <- create_singletype_ib_content_list("PR","PR_ROM_F",PR_ROM_F_LIST, "BASE")
    romR <- create_singletype_ib_content_list("PR","PR_ROM_R",PR_ROM_R_LIST, "BASE")
    romS <- create_singletype_ib_content_list("PR","PR_ROM_S",PR_ROM_S_LIST, "BASE")
    romL <- create_singletype_ib_content_list("PR","PR_ROM_L",PR_ROM_L_LIST, "BASE")
    cur_rom <- rbind(romD, romF, romR, romS, romL)
    gre <- create_singletype_ib_content_list("PR","PR_GREEK",PR_GREEK_LIST, "BASE")
    ger <- create_singletype_ib_content_list("PR","PR_GER",PR_GERv_LIST, "BASE")
    ger2 <- create_singletype_ib_content_list("PR","PR_GER_vh",PR_GERvh_LIST, "BASE")
    sem <- create_singletype_ib_content_list("PR","PR_SEM",PR_SEM_LIST, "BASE")
    cur_rest <- rbind(gre, ger, ger2, sem)
    pr_curr_df <- rbind(cur_altai,cur_kauk,cur_indira,cur_slav,cur_rom,cur_rest)
    res_df <- rbind(res_df, pr_curr_df)
  }
  if (grepl("PERM", perm_type, fixed = TRUE)){
    turkA <- create_singletype_ib_content_list("PR","PR_TURK_A",PR_TURK_A_LIST,"PERM")
    turkAh <- create_singletype_ib_content_list("PR","PR_TURK_Ah",PR_TURK_Ah_LIST,"PERM")
    turkT <- create_singletype_ib_content_list("PR","PR_TURK_T",PR_TURK_T_LIST,"PERM")
    turkTh <- create_singletype_ib_content_list("PR","PR_TURK_Th",PR_TURK_Th_LIST,"PERM")
    turkP <- create_singletype_ib_content_list("PR","PR_TURK_P",PR_TURK_P_LIST,"PERM")
    mong <- create_singletype_ib_content_list("PR","PR_MONG",PR_MONG_LIST,"PERM")
    tungU <- create_singletype_ib_content_list("PR","PR_TUNG_U",PR_TUNG_U_LIST,"PERM")
    tungM <- create_singletype_ib_content_list("PR","PR_TUNG_M",PR_TUNG_M_LIST,"PERM")
    cur_altai <- rbind(turkA, turkAh, turkT, turkTh, turkP, mong, tungU, tungM)
    kaukA <- create_singletype_ib_content_list("PR","PR_KAUK_A",PR_KAUK_A_LIST, "PERM")
    kaukG <- create_singletype_ib_content_list("PR","PR_KAUK_G",PR_KAUK_G_LIST, "PERM")
    kaukK <- create_singletype_ib_content_list("PR","PR_KAUK_K",PR_KAUK_K_LIST, "PERM")
    kaukC <- create_singletype_ib_content_list("PR","PR_KAUK_C",PR_KAUK_C_LIST, "PERM")
    cur_kauk <- rbind(kaukA, kaukG, kaukK, kaukC)
    indiraU <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_U",PR_INDIRA_U_LIST, "PERM")
    indiraP <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_P",PR_INDIRA_P_LIST, "PERM")
    indiraA <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_A",PR_INDIRA_A_LIST, "PERM")
    indiraB <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_B",PR_INDIRA_B_LIST, "PERM")
    indiraG <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_G",PR_INDIRA_G_LIST, "PERM")
    indiraI <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_I",PR_INDIRA_I_LIST, "PERM")
    #indiraM <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_M",PR_INDIRA_M_LIST, "PERM")
    indiraS <- create_singletype_ib_content_list("PR","PR_INDIRA_S",PR_INDIRA_S_LIST, "PERM")
    cur_indira <- rbind(indiraU, indiraP, indiraA, indiraB, indiraG, indiraI, indiraS)#, indiraM
    slavW <- create_singletype_ib_content_list("PR","PR_SLAV_W",PR_SLAV_W_LIST, "PERM")
    slavE <- create_singletype_ib_content_list("PR","PR_SLAV_E",PR_SLAV_E_LIST, "PERM")
    slavS <- create_singletype_ib_content_list("PR","PR_SLAV_S",PR_SLAV_S_LIST, "PERM")
    cur_slav <- rbind(slavW, slavE, slavS)
    romD <- create_singletype_ib_content_list("PR","PR_ROM_D",PR_ROM_D_LIST, "PERM")
    romF <- create_singletype_ib_content_list("PR","PR_ROM_F",PR_ROM_F_LIST, "PERM")
    romR <- create_singletype_ib_content_list("PR","PR_ROM_R",PR_ROM_R_LIST, "PERM")
    romS <- create_singletype_ib_content_list("PR","PR_ROM_S",PR_ROM_S_LIST, "PERM")
    romL <- create_singletype_ib_content_list("PR","PR_ROM_L",PR_ROM_L_LIST, "PERM")
    cur_rom <- rbind(romD, romF, romR, romS, romL)
    gre <- create_singletype_ib_content_list("PR","PR_GREEK",PR_GREEK_LIST, "PERM")
    ger <- create_singletype_ib_content_list("PR","PR_GER",PR_GERv_LIST, "PERM")
    ger2 <- create_singletype_ib_content_list("PR","PR_GER_vh",PR_GERvh_LIST, "PERM")
    sem <- create_singletype_ib_content_list("PR","PR_SEM",PR_SEM_LIST, "PERM")
    cur_rest <- rbind(gre, ger, ger2, sem)
    pr_curr_df <- rbind(cur_altai,cur_kauk,cur_indira,cur_slav,cur_rom,cur_rest)
    res_df <- rbind(res_df, pr_curr_df)
  }
  if (grepl("SYN", perm_type, fixed = TRUE)){
    turkA <- create_singletype_ib_content_list("PR","PR_TURK_A",PR_TURK_A_LIST,"SYN")
    turkAh <- create_singletype_ib_content_list("PR","PR_TURK_Ah",PR_TURK_Ah_LIST,"SYN")
    turkT <- create_singletype_ib_content_list("PR","PR_TURK_T",PR_TURK_T_LIST,"SYN")
    turkTh <- create_singletype_ib_content_list("PR","PR_TURK_Th",PR_TURK_Th_LIST,"SYN")
    turkP <- create_singletype_ib_content_list("PR","PR_TURK_P",PR_TURK_P_LIST,"SYN")
    mong <- create_singletype_ib_content_list("PR","PR_MONG",PR_MONG_LIST,"SYN")
    tungU <- create_singletype_ib_content_list("PR","PR_TUNG_U",PR_TUNG_U_LIST,"SYN")
    tungM <- create_singletype_ib_content_list("PR","PR_TUNG_M",PR_TUNG_M_LIST,"SYN")
    cur_altai <- rbind(turkA, turkAh, turkT, turkTh, turkP, mong, tungU, tungM)
    kaukA <- create_singletype_ib_content_list("PR","PR_KAUK_A",PR_KAUK_A_LIST, "SYN")
    kaukG <- create_singletype_ib_content_list("PR","PR_KAUK_G",PR_KAUK_G_LIST, "SYN")
    kaukK <- create_singletype_ib_content_list("PR","PR_KAUK_K",PR_KAUK_K_LIST, "SYN")
    kaukC <- create_singletype_ib_content_list("PR","PR_KAUK_C",PR_KAUK_C_LIST, "SYN")
    cur_kauk <- rbind(kaukA, kaukG, kaukK, kaukC)
    indiraU <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_U",PR_INDIRA_U_LIST, "SYN")
    indiraP <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_P",PR_INDIRA_P_LIST, "SYN")
    indiraA <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_A",PR_INDIRA_A_LIST, "SYN")
    indiraB <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_B",PR_INDIRA_B_LIST, "SYN")
    indiraG <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_G",PR_INDIRA_G_LIST, "SYN")
    indiraI <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_I",PR_INDIRA_I_LIST, "SYN")
    #indiraM <- create_singletype_ib_content_list("PR","PR_INDIRA_PROX_M",PR_INDIRA_M_LIST, "SYN")
    indiraS <- create_singletype_ib_content_list("PR","PR_INDIRA_S",PR_INDIRA_S_LIST, "SYN")
    cur_indira <- rbind(indiraU, indiraP, indiraA, indiraB, indiraG, indiraI, indiraS)#, indiraM
    slavW <- create_singletype_ib_content_list("PR","PR_SLAV_W",PR_SLAV_W_LIST, "SYN")
    slavE <- create_singletype_ib_content_list("PR","PR_SLAV_E",PR_SLAV_E_LIST, "SYN")
    slavS <- create_singletype_ib_content_list("PR","PR_SLAV_S",PR_SLAV_S_LIST, "SYN")
    cur_slav <- rbind(slavW, slavE, slavS)
    romD <- create_singletype_ib_content_list("PR","PR_ROM_D",PR_ROM_D_LIST, "SYN")
    romF <- create_singletype_ib_content_list("PR","PR_ROM_F",PR_ROM_F_LIST, "SYN")
    romR <- create_singletype_ib_content_list("PR","PR_ROM_R",PR_ROM_R_LIST, "SYN")
    romS <- create_singletype_ib_content_list("PR","PR_ROM_S",PR_ROM_S_LIST, "SYN")
    romL <- create_singletype_ib_content_list("PR","PR_ROM_L",PR_ROM_L_LIST, "SYN")
    cur_rom <- rbind(romD, romF, romR, romS, romL)
    gre <- create_singletype_ib_content_list("PR","PR_GREEK",PR_GREEK_LIST, "SYN")
    ger <- create_singletype_ib_content_list("PR","PR_GER",PR_GERv_LIST, "SYN")
    ger2 <- create_singletype_ib_content_list("PR","PR_GER_vh",PR_GERvh_LIST, "SYN")
    sem <- create_singletype_ib_content_list("PR","PR_SEM",PR_SEM_LIST, "SYN")
    cur_rest <- rbind(gre, ger, ger2, sem)
    pr_curr_df <- rbind(cur_altai,cur_kauk,cur_indira,cur_slav,cur_rom,cur_rest)
    res_df <- rbind(res_df, pr_curr_df)
  }
  
  pr_res_df <- mutate(res_df, paradigm_type=lang_type)
  
  
  pr_res_df <- mutate(pr_res_df, lang_family = ifelse(startsWith(lang_type,"PR_GER"), "GER", 
                                                             ifelse(startsWith(lang_type,"PR_INDIRA"), "INDIRA", 
                                                                    ifelse(startsWith(lang_type,"PR_KAUK"), "INDIRA", 
                                                                           ifelse(startsWith(lang_type,"PR_MONG"), "ALTAI", 
                                                                                  ifelse(startsWith(lang_type,"PR_SLAV"), "SLAV", 
                                                                                         ifelse(startsWith(lang_type,"PR_TUNG"), "ALTAI",
                                                                                                ifelse(startsWith(lang_type,"PR_TURK"), "ALTAI",
                                                                                                       ifelse(startsWith(lang_type,"PR_GREEK"), "OTHER",
                                                                                                              ifelse(startsWith(lang,"Albanian"), "OTHER",
                                                                                                                     ifelse(startsWith(lang,"Chadic"), "AFRO",
                                                                                                                            ifelse(startsWith(lang,"Cushitic"), "AFRO",
                                                                                                                                   ifelse(startsWith(lang,"Omotic"), "AFRO",
                                                                                                                                          ifelse(startsWith(lang,"Berber"), "AFRO",
                                                                                                                                                 ifelse(startsWith(lang,"Egyptian"), "AFRO",
                                                                                                                                                        ifelse(startsWith(lang_type,"PR_SEM"), "SEM",
                                                                                                                                                               ifelse(startsWith(lang_type,"PR_ROM"), "ROM",
                                                                                                                                                                      ifelse(startsWith(lang,"Ossetian"), "INDIRA",
                                                                                                                                                                             ifelse(startsWith(lang,"Kurdish"), "INDIRA",
                                                                                                                                                                                    ifelse(startsWith(lang_type,"PR_KAUK"), "OTHER",
                                                                                                                                                                                           ifelse(startsWith(lang_type,"PR_ROM"), "ROM",
                                                                                                                                                                                                  ifelse(startsWith(lang_type,"PR_GREEK"), "OTHER",lang_type))
                                                                                                                                                                                           )
                                                                                                                                                                                    )
                                                                                                                                                                             )
                                                                                                                                                                      )
                                                                                                                                                               )
                                                                                                                                                        )))))
                                                                                                              ))))))))
  ))
  
  pr_res_df <- mutate(pr_res_df, lang_subgroup = ifelse(startsWith(lang_type,"PR_GER"), "Germ", 
                                                      ifelse(startsWith(lang_type,"PR_INDIRA"), "Indira", 
                                                                    ifelse(startsWith(lang_type,"PR_MONG"), "Mong", 
                                                                           ifelse(startsWith(lang_type,"PR_SLAV"), "Slav", 
                                                                                  ifelse(startsWith(lang_type,"PR_TUNG"), "Tung",
                                                                                         ifelse(startsWith(lang_type,"PR_TURK"), "Turk",
                                                                                                ifelse(startsWith(lang_type,"PR_GREEK"), "Greek",
                                                                                                       ifelse(startsWith(lang,"Albanian"), "OTHER",
                                                                                                              ifelse(startsWith(lang,"Chadic"), "AfroChadic",
                                                                                                                     ifelse(startsWith(lang,"Cushitic"), "AfroCushitic",
                                                                                                                            ifelse(startsWith(lang,"Omotic"), "AfroOmotic",
                                                                                                                                   ifelse(startsWith(lang,"Berber"), "AfroBerber",
                                                                                                                                          ifelse(startsWith(lang,"Egyptian"), "AfroEgyptian",
                                                                                                                                                 ifelse(startsWith(lang_type,"PR_SEM"), "Semitic",
                                                                                                                                                        ifelse(startsWith(lang_type,"PR_ROM"), "Rom",
                                                                                                                                                               ifelse(startsWith(lang,"Ossetian"), "Indira",
                                                                                                                                                                      ifelse(startsWith(lang,"Kurdish"), "Indira",
                                                                                                                                                                             ifelse(startsWith(lang_type,"PR_KAUK"), "OTHER",
                                                                                                                                                                                    ifelse(startsWith(lang_type,"PR_ROM"), "Rom",
                                                                                                                                                                                           ifelse(startsWith(lang_type,"PR_GREEK"), "Greek",lang_type))
                                                                                                                                                                             )
                                                                                                                                                                      )
                                                                                                                                                               )
                                                                                                                                                        )
                                                                                                                                          )))))
                                                                                                       ))))))))
  ))
  
  #todo: language subfamily
  return (pr_res_df)
}


#reads in ib_values of the PPD data for a given perm_type (consisting of SYN,PERM,SHUF,BASE)
create_PPD_ib_df <- function(perm_type) {
  pron_lang_list <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_PRON",sep=""),sep="\t",  header = FALSE)
  res_df <- data.frame(lang_type=character(),
                       lang=character(), 
                       name=character(), 
                       acc=numeric(),
                       compl=numeric(),
                       loss=numeric(),
                       acc_r_base=numeric(),
                       compl_r_base=numeric(),
                       loss_r_base=numeric(),
                       nat=numeric(),
                       var_type=character(),
                       perm_type=character(),
                       feat_cat=character(),
                       stringsAsFactors=FALSE) 
  if (grepl("SHUF", perm_type, fixed = TRUE)){
    pron_shuf_df <- create_singletype_ib_content_list("PRON","PRON",pron_lang_list,"SHUF_SHUF")
    res_df <- rbind(res_df, pron_shuf_df)
  }
  if (grepl("BASE", perm_type, fixed = TRUE)){
    pron_base_df <- create_singletype_ib_content_list("PRON","PRON",pron_lang_list,"BASE")
    res_df <- rbind(res_df, pron_base_df)
  }
  if (grepl("PERM", perm_type, fixed = TRUE)){
    pron_perm_df <- create_singletype_ib_content_list("PRON","PRON",pron_lang_list,"PERM")
    res_df <- rbind(res_df, pron_perm_df)
  }
  if (grepl("SYN", perm_type, fixed = TRUE)){
    pron_syn_df <- create_singletype_ib_content_list("PRON","PRON",pron_lang_list,"SYN")
    res_df <- rbind(res_df, pron_syn_df)
  }
  
  pron_res_df <- mutate(res_df, lang_family = "PPD", paradigm_type="PPD", lang_subgroup="PPD")
  
  return (pron_res_df)
}


#reads in ib_values of the PPD data for a given perm_type (consisting of SYN,PERM,SHUF,BASE)
create_PPD_CogSci_ib_df <- function(perm_type, type) {
  pron_lang_list <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_",type,sep=""),sep="\t",  header = FALSE)
  res_df <- data.frame(lang_type=character(),
                       lang=character(), 
                       name=character(), 
                       acc=numeric(),
                       compl=numeric(),
                       loss=numeric(),
                       acc_r_base=numeric(),
                       compl_r_base=numeric(),
                       loss_r_base=numeric(),
                       nat=numeric(),
                       var_type=character(),
                       perm_type=character(),
                       feat_cat=character(),
                       stringsAsFactors=FALSE) 
  if (grepl("SHUF", perm_type, fixed = TRUE)){
    pron_shuf_df <- create_singletype_ib_content_list("PRON",type,pron_lang_list,"SHUF_SHUF")
    res_df <- rbind(res_df, pron_shuf_df)
  }
  if (grepl("BASE", perm_type, fixed = TRUE)){
    pron_base_df <- create_singletype_ib_content_list("PRON",type,pron_lang_list,"BASE")
    res_df <- rbind(res_df, pron_base_df)
  }
  if (grepl("PERM", perm_type, fixed = TRUE)){
    pron_perm_df <- create_singletype_ib_content_list("PRON",type,pron_lang_list,"PERM")
    res_df <- rbind(res_df, pron_perm_df)
  }
  if (grepl("SYN", perm_type, fixed = TRUE)){
    pron_syn_df <- create_singletype_ib_content_list("PRON",type,pron_lang_list,"SYN")
    res_df <- rbind(res_df, pron_syn_df)
  }
  
  pron_res_df <- mutate(res_df, lang_family = type, paradigm_type= type, lang_subgroup= type)
  
  return (pron_res_df)
}



#reads in ib_values of the uniform and random freq distributions for a given perm_type (consisting of SYN,PERM,SHUF,BASE)
create_rand_unif_ib_df <- function(perm_type, type) {
  lang_list <- read.csv(paste(LANGLIST_INPUT_DIR,"langlist_",type,sep=""),sep="\t",  header = FALSE)
  res_df <- data.frame(lang_type=character(),
                       lang=character(), 
                       name=character(), 
                       acc=numeric(),
                       compl=numeric(),
                       loss=numeric(),
                       acc_r_base=numeric(),
                       compl_r_base=numeric(),
                       loss_r_base=numeric(),
                       nat=numeric(),
                       var_type=character(),
                       perm_type=character(),
                       feat_cat=character(),
                       stringsAsFactors=FALSE) 
  
  if (grepl("SHUF", perm_type, fixed = TRUE)){
    shuf_df <- create_singletype_ib_content_list("rob",type,lang_list,"SHUF_SHUF")
    res_df <- rbind(res_df, shuf_df)
  }
  if (grepl("BASE", perm_type, fixed = TRUE)){
    base_df <- create_singletype_ib_content_list("rob",type,lang_list,"BASE")
    res_df <- rbind(res_df, base_df)
  }
  if (grepl("PERM", perm_type, fixed = TRUE)){
    perm_df <- create_singletype_ib_content_list("rob",type,lang_list,"PERM")
    res_df <- rbind(res_df, perm_df)
  }
  if (grepl("SYN", perm_type, fixed = TRUE)){
    syn_df <- create_singletype_ib_content_list("rob",type,lang_list,"SYN")
    res_df <- rbind(res_df, syn_df)
  }
  
  res_df <- mutate(res_df, lang_family = type, paradigm_type=type, lang_subgroup=type)
  
  return (res_df)
}







#reads in hitfail_values of the Verbs data for a given perm_type (consisting of SYN,PERM,SHUF)
create_VERB_perform_df <- function(perm_type){
  res_df <- data.frame(lang=character(), 
                       HIT_CETL=numeric(),
                       FAIL_CETL=numeric(),
                       HIT_MI=numeric(),
                       FAIL_MI=numeric(),
                       perm_count=numeric(),
                       better_model=character(),
                       stringsAsFactors=FALSE) 
  
  if (perm_type == "SHUF"){
    verb_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_GER/hitfailvalues_VERB_GER_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ROM/hitfailvalues_VERB_ROM_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SEM/hitfailvalues_VERB_SEM_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SA/hitfailvalues_VERB_SA_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ETH/hitfailvalues_VERB_ETH_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_AKK/hitfailvalues_VERB_AKK_SHUF_SHUF.tsv", sep=""),sep="\t")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (perm_type == "PERM"){
    verb_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_GER/hitfailvalues_VERB_GER_PERM.tsv", sep=""),sep="\t")
    verb_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ROM/hitfailvalues_VERB_ROM_PERM.tsv", sep=""),sep="\t")
    verb_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SEM/hitfailvalues_VERB_SEM_PERM.tsv", sep=""),sep="\t")
    verb_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SA/hitfailvalues_VERB_SA_PERM.tsv", sep=""),sep="\t")
    verb_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ETH/hitfailvalues_VERB_ETH_PERM.tsv", sep=""),sep="\t")
    verb_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_AKK/hitfailvalues_VERB_AKK_PERM.tsv", sep=""),sep="\t")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (perm_type == "ALL" | perm_type == "SHUF_PERM" | perm_type == "PERM_SHUF"){
    verb_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_GER/hitfailvalues_VERB_GER_ALL.tsv", sep=""),sep="\t")
    verb_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ROM/hitfailvalues_VERB_ROM_ALL.tsv", sep=""),sep="\t")
    verb_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SEM/hitfailvalues_VERB_SEM_ALL.tsv", sep=""),sep="\t")
    verb_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_SA/hitfailvalues_VERB_SA_ALL.tsv", sep=""),sep="\t")
    verb_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_ETH/hitfailvalues_VERB_ETH_ALL.tsv", sep=""),sep="\t")
    verb_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"VERB/VERB_AKK/hitfailvalues_VERB_AKK_ALL.tsv", sep=""),sep="\t")
    verb_curr_df <- rbind(verb_curr_df_1, verb_curr_df_2, verb_curr_df_3, verb_curr_df_4, verb_curr_df_5, verb_curr_df_6)
    res_df <- rbind(res_df, verb_curr_df)
  }
  return(res_df)
}

#reads in hitfail_values of the Pronouns data for a given perm_type (consisting of SYN,PERM,SHUF)
create_PRON_perform_df <- function(perm_type){
  res_df <- data.frame(lang=character(), 
                       HIT_CETL=numeric(),
                       FAIL_CETL=numeric(),
                       HIT_MI=numeric(),
                       FAIL_MI=numeric(),
                       perm_count=numeric(),
                       better_model=character(),
                       stringsAsFactors=FALSE) 
  
  if (perm_type == "SHUF"){
    pron_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SEM/hitfailvalues_PR_SEM_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER/hitfailvalues_PR_GER_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER_vh/hitfailvalues_PR_GER_vh_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_E/hitfailvalues_PR_SLAV_E_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_W/hitfailvalues_PR_SLAV_W_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_S/hitfailvalues_PR_SLAV_S_SHUF_SHUF.tsv", sep=""),sep="\t")
    
    pron_curr_df_7 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_P/hitfailvalues_PR_TURK_P_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_8 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_T/hitfailvalues_PR_TURK_T_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_9 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Th/hitfailvalues_PR_TURK_Th_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_10 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_A/hitfailvalues_PR_TURK_A_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_11 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Ah/hitfailvalues_PR_TURK_Ah_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_12 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_U/hitfailvalues_PR_TUNG_U_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_13 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_M/hitfailvalues_PR_TUNG_M_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_14 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_MONG/hitfailvalues_PR_MONG_SHUF_SHUF.tsv", sep=""),sep="\t")
    
    pron_curr_df_15 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_A/hitfailvalues_PR_KAUK_A_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_16 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_G/hitfailvalues_PR_KAUK_G_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_17 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_K/hitfailvalues_PR_KAUK_K_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_18 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_C/hitfailvalues_PR_KAUK_C_SHUF_SHUF.tsv", sep=""),sep="\t")
    
    pron_curr_df_19 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_U/hitfailvalues_PR_INDIRA_PROX_U_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_20 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_P/hitfailvalues_PR_INDIRA_PROX_P_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_21 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_A/hitfailvalues_PR_INDIRA_PROX_A_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_22 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_B/hitfailvalues_PR_INDIRA_PROX_B_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_23 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_G/hitfailvalues_PR_INDIRA_PROX_G_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_24 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_I/hitfailvalues_PR_INDIRA_PROX_I_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_25 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_S/hitfailvalues_PR_INDIRA_S_SHUF_SHUF.tsv", sep=""),sep="\t")
    
    pron_curr_df_26 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GREEK/hitfailvalues_PR_GREEK_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_27 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_L/hitfailvalues_PR_ROM_L_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_28 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_S/hitfailvalues_PR_ROM_S_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_29 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_F/hitfailvalues_PR_ROM_F_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_30 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_D/hitfailvalues_PR_ROM_D_SHUF_SHUF.tsv", sep=""),sep="\t")
    pron_curr_df_31 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_R/hitfailvalues_PR_ROM_R_SHUF_SHUF.tsv", sep=""),sep="\t")
    
    pron_curr_df <- rbind(pron_curr_df_1, pron_curr_df_2, pron_curr_df_3, pron_curr_df_4, pron_curr_df_5, pron_curr_df_6, pron_curr_df_7, pron_curr_df_8, pron_curr_df_9, pron_curr_df_10,pron_curr_df_11,  pron_curr_df_12, pron_curr_df_13, pron_curr_df_14, pron_curr_df_15, pron_curr_df_16, pron_curr_df_17, pron_curr_df_18, pron_curr_df_19, pron_curr_df_20, pron_curr_df_21, pron_curr_df_22, pron_curr_df_23, pron_curr_df_24, pron_curr_df_25, pron_curr_df_26, pron_curr_df_27, pron_curr_df_28, pron_curr_df_29, pron_curr_df_30,pron_curr_df_31)
    res_df <- rbind(res_df, pron_curr_df)
  }
  if (perm_type == "PERM"){
    pron_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SEM/hitfailvalues_PR_SEM_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER/hitfailvalues_PR_GER_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER_vh/hitfailvalues_PR_GER_vh_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_E/hitfailvalues_PR_SLAV_E_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_W/hitfailvalues_PR_SLAV_W_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_S/hitfailvalues_PR_SLAV_S_PERM.tsv", sep=""),sep="\t")
    
    pron_curr_df_7 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_P/hitfailvalues_PR_TURK_P_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_8 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_T/hitfailvalues_PR_TURK_T_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_9 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Th/hitfailvalues_PR_TURK_Th_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_10 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_A/hitfailvalues_PR_TURK_A_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_11 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Ah/hitfailvalues_PR_TURK_Ah_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_12 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_U/hitfailvalues_PR_TUNG_U_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_13 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_M/hitfailvalues_PR_TUNG_M_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_14 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_MONG/hitfailvalues_PR_MONG_PERM.tsv", sep=""),sep="\t")
    
    pron_curr_df_15 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_A/hitfailvalues_PR_KAUK_A_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_16 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_G/hitfailvalues_PR_KAUK_G_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_17 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_K/hitfailvalues_PR_KAUK_K_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_18 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_C/hitfailvalues_PR_KAUK_C_PERM.tsv", sep=""),sep="\t")
    
    pron_curr_df_19 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_U/hitfailvalues_PR_INDIRA_PROX_U_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_20 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_P/hitfailvalues_PR_INDIRA_PROX_P_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_21 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_A/hitfailvalues_PR_INDIRA_PROX_A_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_22 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_B/hitfailvalues_PR_INDIRA_PROX_B_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_23 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_G/hitfailvalues_PR_INDIRA_PROX_G_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_24 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_I/hitfailvalues_PR_INDIRA_PROX_I_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_25 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_S/hitfailvalues_PR_INDIRA_S_PERM.tsv", sep=""),sep="\t")
    
    pron_curr_df_26 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GREEK/hitfailvalues_PR_GREEK_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_27 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_L/hitfailvalues_PR_ROM_L_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_28 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_S/hitfailvalues_PR_ROM_S_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_29 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_F/hitfailvalues_PR_ROM_F_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_30 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_D/hitfailvalues_PR_ROM_D_PERM.tsv", sep=""),sep="\t")
    pron_curr_df_31 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_R/hitfailvalues_PR_ROM_R_PERM.tsv", sep=""),sep="\t")
    
    pron_curr_df <- rbind(pron_curr_df_1, pron_curr_df_2, pron_curr_df_3, pron_curr_df_4, pron_curr_df_5, pron_curr_df_6, pron_curr_df_7, pron_curr_df_8, pron_curr_df_9, pron_curr_df_10,pron_curr_df_11,  pron_curr_df_12, pron_curr_df_13, pron_curr_df_14, pron_curr_df_15, pron_curr_df_16, pron_curr_df_17, pron_curr_df_18, pron_curr_df_19, pron_curr_df_20, pron_curr_df_21, pron_curr_df_22, pron_curr_df_23, pron_curr_df_24, pron_curr_df_25, pron_curr_df_26, pron_curr_df_27, pron_curr_df_28, pron_curr_df_29, pron_curr_df_30,pron_curr_df_31)
    res_df <- rbind(res_df, pron_curr_df)
  }
  if (perm_type == "ALL" | perm_type == "SHUF_PERM" | perm_type == "PERM_SHUF"){
    pron_curr_df_1 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SEM/hitfailvalues_PR_SEM_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_2 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER/hitfailvalues_PR_GER_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_3 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GER_vh/hitfailvalues_PR_GER_vh_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_4 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_E/hitfailvalues_PR_SLAV_E_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_5 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_W/hitfailvalues_PR_SLAV_W_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_6 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_SLAV_S/hitfailvalues_PR_SLAV_S_ALL.tsv", sep=""),sep="\t")
    
    pron_curr_df_7 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_P/hitfailvalues_PR_TURK_P_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_8 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_T/hitfailvalues_PR_TURK_T_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_9 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Th/hitfailvalues_PR_TURK_Th_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_10 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_A/hitfailvalues_PR_TURK_A_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_11 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TURK_Ah/hitfailvalues_PR_TURK_Ah_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_12 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_U/hitfailvalues_PR_TUNG_U_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_13 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_TUNG_M/hitfailvalues_PR_TUNG_M_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_14 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_MONG/hitfailvalues_PR_MONG_ALL.tsv", sep=""),sep="\t")
    
    pron_curr_df_15 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_A/hitfailvalues_PR_KAUK_A_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_16 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_G/hitfailvalues_PR_KAUK_G_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_17 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_K/hitfailvalues_PR_KAUK_K_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_18 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_KAUK_C/hitfailvalues_PR_KAUK_C_ALL.tsv", sep=""),sep="\t")
    
    pron_curr_df_19 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_U/hitfailvalues_PR_INDIRA_PROX_U_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_20 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_P/hitfailvalues_PR_INDIRA_PROX_P_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_21 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_A/hitfailvalues_PR_INDIRA_PROX_A_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_22 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_B/hitfailvalues_PR_INDIRA_PROX_B_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_23 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_G/hitfailvalues_PR_INDIRA_PROX_G_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_24 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_PROX_I/hitfailvalues_PR_INDIRA_PROX_I_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_25 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_INDIRA_S/hitfailvalues_PR_INDIRA_S_ALL.tsv", sep=""),sep="\t")
    
    pron_curr_df_26 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_GREEK/hitfailvalues_PR_GREEK_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_27 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_L/hitfailvalues_PR_ROM_L_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_28 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_S/hitfailvalues_PR_ROM_S_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_29 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_F/hitfailvalues_PR_ROM_F_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_30 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_D/hitfailvalues_PR_ROM_D_ALL.tsv", sep=""),sep="\t")
    pron_curr_df_31 <- read.csv(paste(IB_INPUT_DIR,"PR/PR_ROM_R/hitfailvalues_PR_ROM_R_ALL.tsv", sep=""),sep="\t")
    
    pron_curr_df <- rbind(pron_curr_df_1, pron_curr_df_2, pron_curr_df_3, pron_curr_df_4, pron_curr_df_5, pron_curr_df_6, pron_curr_df_7, pron_curr_df_8, pron_curr_df_9, pron_curr_df_10,pron_curr_df_11,  pron_curr_df_12, pron_curr_df_13, pron_curr_df_14, pron_curr_df_15, pron_curr_df_16, pron_curr_df_17, pron_curr_df_18, pron_curr_df_19, pron_curr_df_20, pron_curr_df_21, pron_curr_df_22, pron_curr_df_23, pron_curr_df_24, pron_curr_df_25, pron_curr_df_26, pron_curr_df_27, pron_curr_df_28, pron_curr_df_29, pron_curr_df_30,pron_curr_df_31)
    res_df <- rbind(res_df, pron_curr_df)
  }
  return(res_df)
}

#reads in hitfail_values of the PPD data for a given perm_type (consisting of SYN,PERM,SHUF)
create_PPD_perform_df <- function(perm_type){
  res_df <- data.frame(lang=character(), 
                       HIT_CETL=numeric(),
                       FAIL_CETL=numeric(),
                       HIT_MI=numeric(),
                       FAIL_MI=numeric(),
                       perm_count=numeric(),
                       better_model=character(),
                       stringsAsFactors=FALSE) 
  
  if (perm_type == "SHUF"){
    verb_curr_df <- read.csv(paste(IB_INPUT_DIR,"PRON/PRON/hitfailvalues_PRON_SHUF_SHUF.tsv", sep=""),sep="\t")
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (perm_type == "PERM"){
    verb_curr_df <- read.csv(paste(IB_INPUT_DIR,"PRON/PRON/hitfailvalues_PRON_PERM.tsv", sep=""),sep="\t")
    res_df <- rbind(res_df, verb_curr_df)
  }
  if (perm_type == "ALL" | perm_type == "SHUF_PERM" | perm_type == "PERM_SHUF"){
    verb_curr_df <- read.csv(paste(IB_INPUT_DIR,"PRON/PRON/hitfailvalues_PRON_ALL.tsv", sep=""),sep="\t")
    res_df <- rbind(res_df, verb_curr_df)
  }
  return(res_df)
}
