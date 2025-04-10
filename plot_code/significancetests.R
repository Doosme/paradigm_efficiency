CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")


ppd_data <- rbind(create_PPD_ib_df("PERM_SHUF_BASE"))
verb_data <- rbind(create_VERB_ib_df("PERM_SHUF_BASE"))
pron_data <- rbind(create_PRON_ib_df("PERM_SHUF_BASE"))

ppd_data_permshuf <- ppd_data[grepl("SHUF|PERM", ppd_data$perm_type), ]
verb_data_permshuf <- verb_data[grepl("SHUF|PERM", verb_data$perm_type), ]
pron_data_permshuf <- pron_data[grepl("SHUF|PERM", pron_data$perm_type), ]

ppd_data_shuf <- ppd_data[grepl("SHUF", ppd_data$perm_type), ]
verb_data_shuf <- verb_data[grepl("SHUF", verb_data$perm_type), ]
pron_data_shuf <- pron_data[grepl("SHUF", pron_data$perm_type), ]

ppd_data_perm <- ppd_data[grepl("PERM", ppd_data$perm_type), ]
verb_data_perm <- verb_data[grepl("PERM", verb_data$perm_type), ]
pron_data_perm <- pron_data[grepl("PERM", pron_data$perm_type), ]

ppd_data_bases <- ppd_data[grepl("BASE", ppd_data$perm_type), ]
verb_data_bases <- verb_data[grepl("BASE", verb_data$perm_type), ]
pron_data_bases <- pron_data[grepl("BASE", pron_data$perm_type), ]




#perm
t.test(ppd_data_bases$loss, ppd_data_perm$loss, alternative = "two.sided")
t.test(pron_data_bases$loss, pron_data_perm$loss, alternative = "two.sided")
t.test(verb_data_bases$loss, verb_data_perm$loss, alternative = "two.sided")

t.test(ppd_data_bases$acc, ppd_data_perm$acc, alternative = "two.sided")
t.test(pron_data_bases$acc, pron_data_perm$acc, alternative = "two.sided")
t.test(verb_data_bases$acc, verb_data_perm$acc, alternative = "two.sided")

#shuf
t.test(ppd_data_bases$loss, ppd_data_shuf$loss, alternative = "two.sided")
t.test(pron_data_bases$loss, pron_data_shuf$loss, alternative = "two.sided")
t.test(verb_data_bases$loss, verb_data_shuf$loss, alternative = "two.sided")

t.test(ppd_data_bases$acc, ppd_data_shuf$acc, alternative = "two.sided")
t.test(pron_data_bases$acc, pron_data_shuf$acc, alternative = "two.sided")
t.test(verb_data_bases$acc, verb_data_shuf$acc, alternative = "two.sided")



#perm-shuf
permshuf_PPD_CE_ttest <- t.test(ppd_data_bases$loss, ppd_data_permshuf$loss, alternative = "two.sided")
permshuf_PRON_CE_ttest <- t.test(pron_data_bases$loss, pron_data_permshuf$loss, alternative = "two.sided")
permshuf_VERB_CE_ttest <- t.test(verb_data_bases$loss, verb_data_permshuf$loss, alternative = "two.sided")

permshuf_PPD_ACC_ttest <- t.test(ppd_data_bases$acc, ppd_data_permshuf$acc, alternative = "two.sided")
permshuf_PRON_ACC_ttest <- t.test(pron_data_bases$acc, pron_data_permshuf$acc, alternative = "two.sided")
permshuf_VERB_ACC_ttest <- t.test(verb_data_bases$acc, verb_data_permshuf$acc, alternative = "two.sided")

res_table <- rbind(
  c(permshuf_PPD_CE_ttest$statistic, permshuf_PPD_CE_ttest$p.value),
  c(permshuf_PPD_ACC_ttest$statistic, permshuf_PPD_ACC_ttest$p.value),
  c(permshuf_PRON_CE_ttest$statistic, permshuf_PRON_CE_ttest$p.value),
  c(permshuf_PRON_ACC_ttest$statistic, permshuf_PRON_ACC_ttest$p.value),
  c(permshuf_VERB_CE_ttest$statistic, permshuf_VERB_CE_ttest$p.value),
  c(permshuf_VERB_ACC_ttest$statistic, permshuf_VERB_ACC_ttest$p.value)
)
colnames(res_table) <- c("t-value", "p-value")
rownames(res_table) <- c("PPD (CETL)", "PPD (ACC)",
              "PRON (CETL)", "PRON (ACC)",
              "VERB (CETL)", "VERB (ACC)")

res_table