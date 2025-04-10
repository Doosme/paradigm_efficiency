CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")


#read in data
ppd_data_CSg1 <- rbind(create_PPD_CogSci_ib_df("PERM_SHUF_BASE","PRONCogSci21gamma1"))
ppd_data_CSg1 <- ppd_data_CSg1 %>% mutate(LANGFAM = factor(lang_family, levels = c("PRONCogSci21gamma1")))
ppd_data_CSg1 <- ppd_data_CSg1 %>% mutate(LANGFAM = recode(LANGFAM, "PRONCogSci21gamma1" = "PPD gamma1"))

ppd_data_CSg2 <- rbind(create_PPD_CogSci_ib_df("PERM_SHUF_BASE","PRONCogSci21gamma2"))
ppd_data_CSg2 <- ppd_data_CSg2 %>% mutate(LANGFAM = factor(lang_family, levels = c("PRONCogSci21gamma2")))
ppd_data_CSg2 <- ppd_data_CSg2 %>% mutate(LANGFAM = recode(LANGFAM, "PRONCogSci21gamma2" = "PPD gamma2"))

ppd_data_CSg5 <- rbind(create_PPD_CogSci_ib_df("PERM_SHUF_BASE","PRONCogSci21gamma5"))
ppd_data_CSg5 <- ppd_data_CSg5 %>% mutate(LANGFAM = factor(lang_family, levels = c("PRONCogSci21gamma5")))
ppd_data_CSg5 <- ppd_data_CSg5 %>% mutate(LANGFAM = recode(LANGFAM, "PRONCogSci21gamma5" = "PPD gamma5"))


#create corresponding baseline_df
ppd_data_CSg1_bases <- ppd_data_CSg1[grepl("BASE", ppd_data_CSg1$perm_type), ]
ppd_data_CSg2_bases <- ppd_data_CSg2[grepl("BASE", ppd_data_CSg2$perm_type), ]
ppd_data_CSg5_bases <- ppd_data_CSg5[grepl("BASE", ppd_data_CSg5$perm_type), ]

#create corresponding baseline_df
ppd_data_CSg1_shuf <- ppd_data_CSg1[grepl("SHUF", ppd_data_CSg1$perm_type), ]
ppd_data_CSg2_shuf <- ppd_data_CSg2[grepl("SHUF", ppd_data_CSg2$perm_type), ]
ppd_data_CSg5_shuf <- ppd_data_CSg5[grepl("SHUF", ppd_data_CSg5$perm_type), ]

#create corresponding baseline_df
ppd_data_CSg1_perm <- ppd_data_CSg1[grepl("PERM", ppd_data_CSg1$perm_type), ]
ppd_data_CSg2_perm <- ppd_data_CSg2[grepl("PERM", ppd_data_CSg2$perm_type), ]
ppd_data_CSg5_perm <- ppd_data_CSg5[grepl("PERM", ppd_data_CSg5$perm_type), ]




#TODO: 
create_EFF_plot_comb <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  
  ce_plot <- ggplot(data=mutate(data_perm,lang_family = "perms")) 
  ce_plot <- ce_plot + geom_point(aes(x=loss, y=-acc),color='gray', alpha = 1/10, size=0.5) 
  ce_plot <- ce_plot + geom_point(data=data_base,aes(x=loss, y=-acc,color=LANGFAM), alpha = 7/10, size=2)
  ce_plot <- ce_plot + labs(x = "complexity (CETL)", y="accuracy", color="lang family")
  ce_plot <- ce_plot + theme_bw()
  ce_plot <- ce_plot + ggtitle("CETL")
  ce_plot <- ce_plot + theme(
    plot.title = element_text(color="black", size=20, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=18),
    axis.title.y = element_text(color="blue", size=18),
    axis.text.x = element_text(size = 16),
    axis.text.y = element_text(size = 16),
    legend.title = element_text(size = 18, face="bold"),
    legend.text = element_text(size = 16)
  )
  
  co_plot <- ggplot(data=mutate(data_perm,lang_family = "perms")) 
  co_plot <- co_plot + geom_point(aes(x=compl, y=-acc),color='gray', alpha = 1/10, size=0.5) 
  co_plot <- co_plot + geom_point(data=data_base,aes(x=compl, y=-acc,color=LANGFAM), alpha = 7/10, size=2)
  co_plot <- co_plot + labs(x = "complexity (MI)", y="accuracy", color="lang family")
  co_plot <- co_plot + theme_bw()
  co_plot <- co_plot + ggtitle("MI")
  co_plot <- co_plot + theme(
    plot.title = element_text(color="black", size=20, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=18),
    axis.title.y = element_text(color="blue", size=18),
    axis.text.x = element_text(size = 16),
    axis.text.y = element_text(size = 16),
    legend.title = element_text(size = 18, face="bold"),
    legend.text = element_text(size = 16)
  )
  co_plot <- co_plot + theme(legend.text = element_text(size = 10))
  
  res_plot <- ggarrange(ce_plot, co_plot, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  ggsave(paste(OUTPUT_DIR,"EFF_",name,".pdf",sep=""), plot = res_plot, width = 15, height = 6, dpi = 300)
  
  return(res_plot)
}


create_EFF_plot_comb(ppd_data_CSg1, ppd_data_CSg1_bases,"PRONCogSci21gamma1")
create_EFF_plot_comb(ppd_data_CSg2, ppd_data_CSg2_bases,"PRONCogSci21gamma2")
create_EFF_plot_comb(ppd_data_CSg5, ppd_data_CSg5_bases,"PRONCogSci21gamma5")



######HITFAIL:

PronCogSci21gamma1_ALL <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma1/hitfailvalues_PRONCogSci21gamma1_ALL.tsv", sep=""),sep="\t")
PronCogSci21gamma2_ALL <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma2/hitfailvalues_PRONCogSci21gamma2_ALL.tsv", sep=""),sep="\t")
PronCogSci21gamma5_ALL <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma5/hitfailvalues_PRONCogSci21gamma5_ALL.tsv", sep=""),sep="\t")

PronCogSci21g1_PERM <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma1/hitfailvalues_PRONCogSci21gamma1_PERM.tsv", sep=""),sep="\t")
PronCogSci21g2_PERM <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma2/hitfailvalues_PRONCogSci21gamma2_PERM.tsv", sep=""),sep="\t")
PronCogSci21g5_PERM <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma5/hitfailvalues_PRONCogSci21gamma5_PERM.tsv", sep=""),sep="\t")
PronCogSci21g1_SHUF <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma1/hitfailvalues_PRONCogSci21gamma1_SHUF_SHUF.tsv", sep=""),sep="\t")
PronCogSci21g2_SHUF <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma2/hitfailvalues_PRONCogSci21gamma2_SHUF_SHUF.tsv", sep=""),sep="\t")
PronCogSci21g5_SHUF <- read.csv(paste(IB_INPUT_DIR,"PRON/PRONCogSci21gamma5/hitfailvalues_PRONCogSci21gamma5_SHUF_SHUF.tsv", sep=""),sep="\t")



performance_comparison_plot <- function(data, name) {
  res_plot <- ggplot(data, aes(better_model, fill=better_model)) 
  res_plot <- res_plot + geom_bar() 
  res_plot <- res_plot + scale_fill_manual(values=c("CETL"="darkgreen",  "MI"="#dd0000", "None"="darkblue"), drop = FALSE)
  res_plot <- res_plot + scale_x_discrete(limits = c("CETL", "MI", "None"))
  res_plot <- res_plot + labs(x = "model", y="# languages", fill="better model")
  res_plot <- res_plot + theme_bw() 
  res_plot <- res_plot + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),
    axis.title.x = element_text(color="blue", size=16),
    axis.title.y = element_text(color="blue", size=16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  res_plot <- res_plot + ggtitle(name)
  
  return(res_plot)
}






g_pron_CogSci21gamma1_PERM <- performance_comparison_plot(PronCogSci21g1_PERM, "PPD gamma1")
g_pron_CogSci21gamma2_PERM <- performance_comparison_plot(PronCogSci21g2_PERM, "PPD gamma2")
g_pron_CogSci21gamma5_PERM <- performance_comparison_plot(PronCogSci21g5_PERM, "PPD gamma5")
hitfail_plot_CogSci21_PERM <- ggarrange(g_pron_CogSci21gamma1_PERM, g_pron_CogSci21gamma2_PERM, g_pron_CogSci21gamma5_PERM, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL_CogSci21_PERM.pdf", sep=""), plot = hitfail_plot_CogSci21_PERM, width = 8, height = 4, dpi = 300)

g_pron_CogSci21gamma1_SHUF <- performance_comparison_plot(PronCogSci21g1_SHUF, "PPD gamma1")
g_pron_CogSci21gamma2_SHUF <- performance_comparison_plot(PronCogSci21g2_SHUF, "PPD gamma2")
g_pron_CogSci21gamma5_SHUF <- performance_comparison_plot(PronCogSci21g5_SHUF, "PPD gamma5")
hitfail_plot_CogSci21_SHUF <- ggarrange(g_pron_CogSci21gamma1_SHUF, g_pron_CogSci21gamma2_SHUF, g_pron_CogSci21gamma5_SHUF, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL_CogSci21_SHUF.pdf", sep=""), plot = hitfail_plot_CogSci21_SHUF, width = 8, height = 4, dpi = 300)

g_pron_CogSci21gamma1_ALL <- performance_comparison_plot(PronCogSci21gamma1_ALL, "PPD gamma1")
g_pron_CogSci21gamma2_ALL <- performance_comparison_plot(PronCogSci21gamma2_ALL, "PPD gamma2")
g_pron_CogSci21gamma5_ALL <- performance_comparison_plot(PronCogSci21gamma5_ALL, "PPD gamma5")
hitfail_plot_CogSci21 <- ggarrange(g_pron_CogSci21gamma1_ALL, g_pron_CogSci21gamma2_ALL, g_pron_CogSci21gamma5_ALL, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL_CogSci21.pdf", sep=""), plot = hitfail_plot_CogSci21, width = 8, height = 4, dpi = 300)

