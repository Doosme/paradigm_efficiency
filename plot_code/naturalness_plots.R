CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")


create_NAT_plot_langs <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SHUF", data_perm$perm_type), ]
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  
  g <- ggplot(data=data_perm, aes(group=lang, x=nat, y=loss_r_base)) 
  g <- g + geom_point(aes(color=lang_type), alpha=2/10, size=0.5)  
  g <- g + geom_smooth(aes(color=lang_type), size=0.5, alpha=2/10)  
  g <- g + geom_point(data=data_base, aes(x=nat, y=loss_r_base), size=3, color='red', alpha=2/10) 
  g <- g + labs(x = "naturalness", y="relative complexity (CETL)", color="paradigm type")
  g <- g + ggtitle("CETL")
  g <- g + theme_bw()
  g <- g + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 12),
    legend.title = element_text(size = 14, face="bold"),
    legend.text = element_text(size = 12)
  )
  p <- ggplot(data=data_perm, aes(group=lang, x=nat, y=compl_r_base)) 
  p <- p + geom_point(aes(color=lang_type), alpha=2/10, size=0.5)  
  p <- p + geom_smooth(aes(color=lang_type), size=0.5, alpha=2/10)  
  p <- p + geom_point(data=data_base, aes(x=nat, y=compl_r_base), size=3, color='red', alpha=2/10) 
  p <- p + labs(x = "naturalness", y="relative complexity (MI)", color="paradigm type")
  p <- p + ggtitle("MI")
  p <- p + theme_bw()
  p <- p + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 12),
    legend.title = element_text(size = 14, face="bold"),
    legend.text = element_text(size = 12)
  )
  
  res_plot <- ggarrange(g, p, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  ggsave(paste(OUTPUT_DIR,"NAT_",name,"_langs.pdf", sep = ""), plot = res_plot, width = 12, height = 3, dpi = 300)
  return(res_plot)
}


create_NAT_plot_langfams <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SHUF", data_perm$perm_type), ]
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  g <- ggplot(data=data_perm, aes(group=lang_type, x=nat, y=loss_r_base)) 
  g <- g + geom_point(aes(color=lang_type), alpha=2/10, size=0.5)  
  g <- g + geom_smooth(aes(color=lang_type))  
  g <- g + geom_point(data=data_base, aes(x=nat, y=loss_r_base), size=3, color='red', alpha=2/10) 
  g <- g + labs(x = "naturalness", y="relative complexity (CETL)", color="paradigm type")
  g <- g + ggtitle("CETL")
  g <- g + theme_bw()
  g <- g + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 12),
    legend.title = element_text(size = 14, face="bold"),
    legend.text = element_text(size = 12)
  )
  p <- ggplot(data=data_perm, aes(group=lang_type, x=nat, y=compl_r_base)) 
  p <- p + geom_point(aes(color=lang_type), alpha=2/10, size=0.5)  
  p <- p + geom_smooth(aes(color=lang_type))  
  p <- p + geom_point(data=data_base, aes(x=nat, y=compl_r_base), size=3, color='red', alpha=2/10) 
  p <- p + labs(x = "naturalness", y="relative complexity (MI)", color="paradigm type")
  p <- p + ggtitle("MI")
  p <- p + theme_bw()
  p <- p + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 12),
    legend.title = element_text(size = 14, face="bold"),
    legend.text = element_text(size = 12)
  )
  
  res_plot <- ggarrange(g, p, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  ggsave(paste(OUTPUT_DIR,"NAT_",name,"_langfams.pdf", sep = ""), plot = res_plot, width = 12, height = 3, dpi = 300)
  
  return(res_plot)
}

#read in data
ppd_data <- rbind(create_PPD_ib_df("PERM_BASE"))
verb_data <- rbind(create_VERB_ib_df("PERM_BASE"))
pron_data <- rbind(create_PRON_ib_df("PERM_BASE"))

verb_Germanic_data <- verb_data[grepl("Germ", verb_data$lang_subgroup), ]
verb_Romanic_data <- verb_data[grepl("Rom", verb_data$lang_subgroup), ]
verb_CentSem_data <- verb_data[grepl("CentSem", verb_data$lang_subgroup), ]
verb_SouthSem_data <- verb_data[grepl("SouthSem", verb_data$lang_subgroup), ]
verb_EastSem_data <- verb_data[grepl("EastSem", verb_data$lang_subgroup), ]
verb_AfroSem_data <- verb_data[grepl("EastSem|SouthSem|CentSem", verb_data$lang_subgroup), ]

pron_Germanic_data <- pron_data[grepl("Germ", pron_data$lang_subgroup), ]
pron_Romanic_data <- pron_data[grepl("Rom", pron_data$lang_subgroup), ]
pron_Slav_data <- pron_data[grepl("Slav", pron_data$lang_subgroup), ]
pron_Altai_data <- pron_data[grepl("Turk|Mong|Tung", pron_data$lang_subgroup), ]
pron_AfroSem_data <- pron_data[grepl("Semitic|AfroBerber|AfroChadic|AfroCushitic|AfroEgyptian|AfroOmotic", pron_data$lang_subgroup), ]
pron_Indira_data <- pron_data[grepl("Indira", pron_data$lang_subgroup), ]
pron_Other_data <- pron_data[grepl("OTHER|Greek", pron_data$lang_subgroup), ]

#create corresponding baseline_df
ppd_data_bases <- ppd_data[grepl("BASE", ppd_data$perm_type), ]
verb_data_bases <- verb_data[grepl("BASE", verb_data$perm_type), ]
pron_data_bases <- pron_data[grepl("BASE", pron_data$perm_type), ]

verb_Germanic_data_bases <- verb_Germanic_data[grepl("BASE", verb_Germanic_data$perm_type), ]
verb_Romanic_data_bases <- verb_Romanic_data[grepl("BASE", verb_Romanic_data$perm_type), ]
verb_CentSem_data_bases <- verb_CentSem_data[grepl("BASE", verb_CentSem_data$perm_type), ]
verb_SouthSem_data_bases <- verb_SouthSem_data[grepl("BASE", verb_SouthSem_data$perm_type), ]
verb_EastSem_data_bases <- verb_EastSem_data[grepl("BASE", verb_EastSem_data$perm_type), ]
verb_AfroSem_data_bases <- verb_AfroSem_data[grepl("BASE", verb_AfroSem_data$perm_type), ]


pron_Germanic_data_bases <- pron_Germanic_data[grepl("BASE", pron_Germanic_data$perm_type), ]
pron_Romanic_data_bases <- pron_Romanic_data[grepl("BASE", pron_Romanic_data$perm_type), ]
pron_AfroSem_data_bases <- pron_AfroSem_data[grepl("BASE", pron_AfroSem_data$perm_type), ]
pron_Slav_data_bases <- pron_Slav_data[grepl("BASE", pron_Slav_data$perm_type), ]
pron_Altai_data_bases <- pron_Altai_data[grepl("BASE", pron_Altai_data$perm_type), ]
pron_Indira_data_bases <- pron_Indira_data[grepl("BASE", pron_Indira_data$perm_type), ]
pron_Other_data_bases <- pron_Other_data[grepl("BASE", pron_Other_data$perm_type), ]


#renaming paradigm types: #todo
verb_AfroSem_data <- verb_AfroSem_data %>%
  mutate(lang_type = recode(lang_type, "VERB_AKK" = "Type 1", "VERB_ETH" = "Type 2", "VERB_SA" = "Type 3", "VERB_SEM" = "Type 4"))
verb_AfroSem_data_bases <- verb_AfroSem_data_bases %>%
  mutate(lang_type = recode(lang_type, "VERB_AKK" = "Type 1", "VERB_ETH" = "Type 2", "VERB_SA" = "Type 3", "VERB_SEM" = "Type 4"))


verb_Germanic_data <- verb_Germanic_data %>%
  mutate(lang_type = recode(lang_type, "VERB_GER" = "Type 1"))
verb_Germanic_data_bases <- verb_Germanic_data_bases %>%
  mutate(lang_type = recode(lang_type, "VERB_GER" = "Type 1"))

verb_Romanic_data <- verb_Romanic_data %>%
  mutate(lang_type = recode(lang_type, "VERB_ROM" = "Type 1"))
verb_Romanic_data_bases <- verb_Romanic_data_bases %>%
  mutate(lang_type = recode(lang_type, "VERB_ROM" = "Type 1"))



pron_AfroSem_data <- pron_AfroSem_data %>%
  mutate(lang_type = recode(lang_type, "PR_SEM" = "Type 1"))
pron_AfroSem_data_bases <- pron_AfroSem_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_SEM" = "Type 1"))

pron_Germanic_data <- pron_Germanic_data %>%
  mutate(lang_type = recode(lang_type, "PR_GER" = "Type 1", "PR_GER_vh" = "Type 2"))
pron_Germanic_data_bases <- pron_Germanic_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_GER" = "Type 1", "PR_GER_vh" = "Type 2"))

pron_Romanic_data <- pron_Romanic_data %>%
  mutate(lang_type = recode(lang_type, "PR_ROM_D" = "Type 1", "PR_ROM_F" = "Type 2", "PR_ROM_R" = "Type 3", "PR_ROM_S" = "Type 4", "PR_ROM_L" = "Type 5"))
pron_Romanic_data_bases <- pron_Romanic_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_ROM_D" = "Type 1", "PR_ROM_F" = "Type 2", "PR_ROM_R" = "Type 3", "PR_ROM_S" = "Type 4", "PR_ROM_L" = "Type 5"))

pron_Slav_data <- pron_Slav_data %>%
  mutate(lang_type = recode(lang_type, "PR_SLAV_W" = "Type 1", "PR_SLAV_E" = "Type 2", "PR_SLAV_S" = "Type 3"))
pron_Slav_data_bases <- pron_Slav_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_SLAV_W" = "Type 1", "PR_SLAV_E" = "Type 2", "PR_SLAV_S" = "Type 3"))

pron_Altai_data <- pron_Altai_data %>%
  mutate(lang_type = recode(lang_type, "PR_TURK_A" = "Type Turk1", "PR_TURK_Ah" = "Type Turk2", "PR_TURK_T" = "Type Turk3", "PR_TURK_Th" = "Type Turk4", "PR_TURK_P" = "Type Turk5", "PR_MONG" = "Type Mong", "PR_TUNG_U" = "Type Tung1", "PR_TUNG_M" = "Type Tung2"))
pron_Altai_data_bases <- pron_Altai_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_TURK_A" = "Type Turk1", "PR_TURK_Ah" = "Type Turk2", "PR_TURK_T" = "Type Turk3", "PR_TURK_Th" = "Type Turk4", "PR_TURK_P" = "Type Turk5", "PR_MONG" = "Type Mong", "PR_TUNG_U" = "Type Tung1", "PR_TUNG_M" = "Type Tung2"))


pron_Indira_data <- pron_Indira_data %>%
  mutate(lang_type = recode(lang_type, "PR_KAUK_K" = "Type 1", "PR_INDIRA_PROX_U" = "Type 2", "PR_INDIRA_PROX_P" = "Type 3", "PR_INDIRA_PROX_A" = "Type 4", "PR_INDIRA_PROX_B" = "Type 5", "PR_INDIRA_PROX_G" = "Type 6", "PR_INDIRA_PROX_I" = "Type 7", "PR_INDIRA_S" = "Type 8"))
pron_Indira_data_bases <- pron_Indira_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_KAUK_K" = "Type 1", "PR_INDIRA_PROX_U" = "Type 2", "PR_INDIRA_PROX_P" = "Type 3", "PR_INDIRA_PROX_A" = "Type 4", "PR_INDIRA_PROX_B" = "Type 5", "PR_INDIRA_PROX_G" = "Type 6", "PR_INDIRA_PROX_I" = "Type 7", "PR_INDIRA_S" = "Type 8"))

pron_Other_data <- pron_Other_data %>%
  mutate(lang_type = recode(lang_type, "PR_KAUK_A" = "Type 1", "PR_KAUK_G" = "Type 2", "PR_KAUK_C" = "Type 3", "PR_ROM_R" = "Type 4", "PR_GREEK" = "Type 5"))
pron_Other_data_bases <- pron_Other_data_bases %>%
  mutate(lang_type = recode(lang_type, "PR_KAUK_A" = "Type 1", "PR_KAUK_G" = "Type 2", "PR_KAUK_C" = "Type 3", "PR_ROM_R" = "Type 4", "PR_GREEK" = "Type 5"))


ppd_data <- ppd_data %>%
  mutate(lang_type = recode(lang_type, "PRON" = "Type 1"))
ppd_data_bases <- ppd_data_bases %>%
  mutate(lang_type = recode(lang_type, "PRON" = "Type 1"))


#create plots
create_NAT_plot_langs(verb_AfroSem_data, verb_AfroSem_data_bases,"VERB_SemAfro")
create_NAT_plot_langfams(verb_AfroSem_data, verb_AfroSem_data_bases,"VERB_SemAfro")

create_NAT_plot_langs(verb_Germanic_data, verb_Germanic_data_bases,"VERB_Germanic")
create_NAT_plot_langfams(verb_Germanic_data, verb_Germanic_data_bases,"VERB_Germanic")

create_NAT_plot_langs(verb_Romanic_data, verb_Romanic_data_bases,"VERB_Romanic")
create_NAT_plot_langfams(verb_Romanic_data, verb_Romanic_data_bases,"VERB_Romanic")


create_NAT_plot_langs(verb_data, verb_data_bases,"VERB_ALL")
create_NAT_plot_langfams(verb_data, verb_data_bases,"VERB_ALL")



create_NAT_plot_langs(ppd_data, ppd_data_bases,"PPD")
create_NAT_plot_langfams(ppd_data, ppd_data_bases,"PPD")


#todo!
create_NAT_plot_langs(pron_Romanic_data, pron_Romanic_data_bases,"PRON_Romanic")
create_NAT_plot_langfams(pron_Romanic_data, pron_Romanic_data_bases,"PRON_Romanic")

create_NAT_plot_langs(pron_Germanic_data, pron_Germanic_data_bases,"PRON_Germanic")
create_NAT_plot_langfams(pron_Germanic_data, pron_Germanic_data_bases,"PRON_Germanic")

create_NAT_plot_langs(pron_AfroSem_data, pron_AfroSem_data_bases,"PRON_AfroSem")
create_NAT_plot_langfams(pron_AfroSem_data, pron_AfroSem_data_bases,"PRON_AfroSem")

create_NAT_plot_langs(pron_Slav_data, pron_Slav_data_bases,"PRON_Slavic")
create_NAT_plot_langfams(pron_Slav_data, pron_Slav_data_bases,"PRON_Slavic")

create_NAT_plot_langs(pron_Altai_data, pron_Altai_data_bases,"PRON_Altaic")
create_NAT_plot_langfams(pron_Altai_data, pron_Altai_data_bases,"PRON_Altaic")

create_NAT_plot_langs(pron_Indira_data, pron_Indira_data_bases,"PRON_Indoiranian")
create_NAT_plot_langfams(pron_Indira_data, pron_Indira_data_bases,"PRON_Indoiranian")

create_NAT_plot_langs(pron_data, pron_data_bases,"PRON_ALL")
create_NAT_plot_langfams(pron_data, pron_data_bases,"PRON_ALL")

create_NAT_plot_langs(pron_Other_data, pron_Other_data_bases,"PRON_Other")
create_NAT_plot_langfams(pron_Other_data, pron_Other_data_bases,"PRON_Other")

