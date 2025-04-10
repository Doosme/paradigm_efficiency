CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")



#read in data
ppd_data <- rbind(create_PPD_ib_df("PERM_SHUF_BASE"))
verb_data <- rbind(create_VERB_ib_df("PERM_SHUF_BASE"))
pron_data <- rbind(create_PRON_ib_df("PERM_SHUF_BASE"))

ppd_data_shuf <- ppd_data[grepl("SHUF", ppd_data$perm_type), ]
verb_data_shuf <- verb_data[grepl("SHUF", verb_data$perm_type), ]
pron_data_shuf <- pron_data[grepl("SHUF", pron_data$perm_type), ]

ppd_data_perm <- ppd_data[grepl("PERM", ppd_data$perm_type), ]
verb_data_perm <- verb_data[grepl("PERM", verb_data$perm_type), ]
pron_data_perm <- pron_data[grepl("PERM", pron_data$perm_type), ]


verb_AfroSem_data <- verb_data[grepl("EastSem|SouthSem|CentSem", verb_data$lang_subgroup), ]
#correlation tests for plotted SemAfro:
verb_afrosem_cor <- cor.test(verb_AfroSem_data$nat, verb_AfroSem_data$loss, method="spearman")

VERB_cors_CETL <- verb_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="VERB")
avg_cor_VERB_CETL <- sum(VERB_cors_CETL$cor)/length(VERB_cors_CETL$cor)

VERB_cors_MI <- verb_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="VERB")
avg_cor_VERB_MI <- sum(VERB_cors_MI$cor)/length(VERB_cors_MI$cor)

VERB_cors_ALL <- rbind(VERB_cors_CETL,VERB_cors_MI)

PR_cors_CETL <- pron_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PR")
avg_cor_PR_CETL <- sum(PR_cors_CETL$cor)/length(PR_cors_CETL$cor)

PR_cors_MI <- pron_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PR")
avg_cor_PR_MI <- sum(PR_cors_MI$cor)/length(PR_cors_MI$cor)

PR_cors_ALL <- rbind(PR_cors_CETL,PR_cors_MI)


PRON_cors_CETL <- pron_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PRON")
avg_cor_PRON_CETL <- sum(PRON_cors_CETL$cor)/length(PRON_cors_CETL$cor)

PRON_cors_MI <- pron_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PRON")
avg_cor_PRON_MI <- sum(PRON_cors_MI$cor)/length(PRON_cors_MI$cor)

PRON_cors_ALL <- rbind(PRON_cors_CETL,PRON_cors_MI)


cor_values_table <- 
  rbind(c(avg_cor_PRON_CETL, avg_cor_PRON_MI),
        c(avg_cor_PR_CETL, avg_cor_PR_MI),
        c(avg_cor_VERB_CETL, avg_cor_VERB_MI))
colnames(cor_values_table) <- c("CETL", "MI")
rownames(cor_values_table) <- c("PPD","PRON","VERB")




#correlation tests for plotted SemAfro:
verb_afrosem_cor

#correlation table
cor_values_table


