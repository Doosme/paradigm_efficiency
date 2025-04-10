CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"


setwd(CODE_DIR) 
source("util.R")

#read in data
ppd_data <- rbind(create_PPD_ib_df("PERM"))
ppd_data <- ppd_data %>% mutate(LANGFAM = factor(lang_family, levels = c("PPD")))

verb_data <- rbind(create_VERB_ib_df("PERM"))
verb_data <- verb_data %>% mutate(LANGFAM = factor(lang_family, levels = c("SEM", "AFRO","GER", "ROM")))

pron_data <- rbind(create_PRON_ib_df("PERM"))
pron_data <- pron_data %>% mutate(LANGFAM = factor(lang_family, levels = c("SEM", "AFRO","GER", "ROM", "ALTAI", "SLAV","INDIRA","OTHER")))


#create corresponding baseline_df
verb_data_SEM <- verb_data[grepl("SEM", verb_data$LANGFAM), ]
verb_data_AFRO <- verb_data[grepl("AFRO", verb_data$LANGFAM), ]
verb_data_GER <- verb_data[grepl("GER", verb_data$LANGFAM), ]
verb_data_ROM <- verb_data[grepl("ROM", verb_data$LANGFAM), ]

pron_data_SEM <- pron_data[grepl("SEM", pron_data$LANGFAM), ]
pron_data_AFRO <- pron_data[grepl("AFRO", pron_data$LANGFAM), ]
pron_data_GER <- pron_data[grepl("GER", pron_data$LANGFAM), ]
pron_data_ROM <- pron_data[grepl("ROM", pron_data$LANGFAM), ]
pron_data_ALTAI <- pron_data[grepl("ALTAI", pron_data$LANGFAM), ]
pron_data_SLAV <- pron_data[grepl("SLAV", pron_data$LANGFAM), ]
pron_data_INDIRA <- pron_data[grepl("INDIRA", pron_data$LANGFAM), ]
pron_data_OTHER <- pron_data[grepl("OTHER", pron_data$LANGFAM), ]




#######COR plots
cor_list <- function(lang_list,expr_type){
  cors_CETL <- lang_list %>%
    group_by(lang) %>%
    summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr=expr_type)
  cors_MI <- lang_list %>%
    group_by(lang) %>%
    summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr=expr_type)
  res_list <- rbind(cors_CETL,cors_MI)
  
  return(res_list)
}

cor_plot <- function(data,name){
  plot <- ggplot(data=data, aes(x=model, y=cor, color=model)) 
  plot <- plot + geom_jitter(alpha=0.4, size=1) 
  plot <- plot + ylim(-1,1) 
  plot <- plot + geom_boxplot(alpha=0) 
  #plot <- plot + geom_line(aes(group=lang), size=0.1, color="#AAAAAA") 
  plot <- plot + labs(x = "model", y="correlation (per language)")
  plot <- plot + ggtitle(name)
  plot <- plot + theme_bw()
  plot <- plot + theme(
    plot.title = element_text(color="black", size=14, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=12),
    axis.title.y = element_text(color="blue", size=12),
    axis.text.x = element_text(size = 12),
    axis.text.y = element_text(size = 12),
    legend.title = element_text(size = 14, face="bold"),
    legend.text = element_text(size = 12)
  )
  return(plot)
}

VERB_Sem_cors_ALL <- cor_list(verb_data_SEM, "VERB")
VERB_Afro_cors_ALL <- cor_list(verb_data_AFRO, "VERB")
VERB_Rom_cors_ALL <- cor_list(verb_data_ROM, "VERB")
VERB_Ger_cors_ALL <- cor_list(verb_data_GER, "VERB")

plot_VERB_Rom_cors_jitter <- cor_plot(VERB_Rom_cors_ALL, "Romanic VERB")
plot_VERB_Ger_cors_jitter <- cor_plot(VERB_Ger_cors_ALL, "Germanic VERB")
plot_VERB_Sem_cors_jitter <- cor_plot(VERB_Sem_cors_ALL, "Semitic VERB")
plot_VERB_Afro_cors_jitter <- cor_plot(VERB_Afro_cors_ALL, "Afroasiatic VERB")

PRON_Sem_cors_ALL <- cor_list(pron_data_SEM, "PRON")
PRON_Afro_cors_ALL <- cor_list(pron_data_AFRO, "PRON")
PRON_Rom_cors_ALL <- cor_list(pron_data_ROM, "PRON")
PRON_Ger_cors_ALL <- cor_list(pron_data_GER, "PRON")
PRON_Altai_cors_ALL <- cor_list(pron_data_ALTAI, "PRON")
PRON_Slav_cors_ALL <- cor_list(pron_data_SLAV, "PRON")
PRON_Indira_cors_ALL <- cor_list(pron_data_INDIRA, "PRON")
PRON_Other_cors_ALL <- cor_list(pron_data_OTHER, "PRON")

plot_PRON_Rom_cors_jitter <- cor_plot(PRON_Rom_cors_ALL, "Romanic PRON")
plot_PRON_Ger_cors_jitter <- cor_plot(PRON_Ger_cors_ALL, "Germanic PRON")
plot_PRON_Sem_cors_jitter <- cor_plot(PRON_Sem_cors_ALL, "Semitic PRON")
plot_PRON_Afro_cors_jitter <- cor_plot(PRON_Afro_cors_ALL, "Afroasiatic PRON")
plot_PRON_Altai_cors_jitter <- cor_plot(PRON_Altai_cors_ALL, "Altaic PRON")
plot_PRON_Slav_cors_jitter <- cor_plot(PRON_Slav_cors_ALL, "Slavic PRON")
plot_PRON_Indira_cors_jitter <- cor_plot(PRON_Indira_cors_ALL, "Indoiranian PRON")
plot_PRON_Other_cors_jitter <- cor_plot(PRON_Other_cors_ALL, "Other PRON")

PPD_cors_ALL <- cor_list(ppd_data, "PPD")
plot_PPD_cors_jitter <- cor_plot(PPD_cors_ALL, "PPD")




plot_PPDs <- ggarrange(plot_PPD_cors_jitter, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=1, nrow=1)
ggsave(paste(OUTPUT_DIR, "COR_PPD.pdf",sep=""), plot = plot_PPDs, width = 3.5, height = 3, dpi = 300)

plot_VERBs <- ggarrange(plot_VERB_Sem_cors_jitter,plot_VERB_Afro_cors_jitter,plot_VERB_Ger_cors_jitter, plot_VERB_Rom_cors_jitter, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=2, nrow=2)
ggsave(paste(OUTPUT_DIR, "COR_VERB.pdf",sep=""), plot = plot_VERBs, width = 6, height = 6, dpi = 300)

plot_PRONs <- ggarrange(plot_PRON_Sem_cors_jitter,plot_PRON_Afro_cors_jitter,plot_PRON_Ger_cors_jitter, plot_PRON_Rom_cors_jitter, plot_PRON_Slav_cors_jitter, plot_PRON_Altai_cors_jitter, plot_PRON_Indira_cors_jitter, plot_PRON_Other_cors_jitter, label.x=-0.05, label.y=1.02, common.legend = TRUE, legend = "right", ncol=2, nrow=4)
ggsave(paste(OUTPUT_DIR, "COR_PRON.pdf",sep=""), plot = plot_PRONs, width = 6, height = 12, dpi = 300)



VERB_cors_ALL <- rbind(VERB_Sem_cors_ALL, VERB_Afro_cors_ALL, VERB_Rom_cors_ALL, VERB_Ger_cors_ALL)
PRON_cors_ALL <- rbind(PRON_Sem_cors_ALL, PRON_Afro_cors_ALL, PRON_Rom_cors_ALL, PRON_Ger_cors_ALL, PRON_Altai_cors_ALL, PRON_Slav_cors_ALL, PRON_Indira_cors_ALL, PRON_Other_cors_ALL)
ALL_cors_ALL <- rbind(PPD_cors_ALL, PRON_cors_ALL, VERB_cors_ALL)

ALL_cors_ALL <- ALL_cors_ALL %>%
  mutate(EXPR_MODEL = factor(paste(expr, model), levels = c("PPD CETL", "PPD MI","PRON CETL", "PRON MI", "VERB CETL", "VERB MI")))


plot_cors_all_box <- ggplot(data=ALL_cors_ALL, aes(x=EXPR_MODEL, y=cor, color=model)) + geom_boxplot() + ylim(-1,1)
plot_cors_all_box <- plot_cors_all_box + facet_grid(. ~ expr, scales = "free", space = "free")
plot_cors_all_box <- plot_cors_all_box + labs(x = "model & domain", y="correlation (per language)")
plot_cors_all_box <- plot_cors_all_box + theme_bw()
plot_cors_all_box <- plot_cors_all_box + theme(
  axis.title.x = element_text(color="blue", size=12),
  axis.title.y = element_text(color="blue", size=12),
  axis.text.x = element_text(size = 12),
  axis.text.y = element_text(size = 12),
  legend.title = element_text(size = 14, face="bold"),
  legend.text = element_text(size = 12)
)
plot_cors_all_box <- plot_cors_all_box + scale_x_discrete(labels = c(
  "PPD CETL" = "CETL",
  "PPD MI" = "MI",
  "PRON CETL" = "CETL",
  "PRON MI" = "MI",
  "VERB CETL" = "CETL",
  "VERB MI" = "MI"
))

ggsave(paste(OUTPUT_DIR, "COR_all_box.pdf", sep=""), plot = plot_cors_all_box, width = 7, height = 6, dpi = 300)
