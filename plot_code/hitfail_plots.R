CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")

#read in data
ppd_data <- rbind(create_PPD_perform_df("PERM_SHUF"))
verb_data <- rbind(create_VERB_perform_df("PERM_SHUF"))
pron_data <- rbind(create_PRON_perform_df("PERM_SHUF"))

ppd_data_perm <- rbind(create_PPD_perform_df("PERM"))
verb_data_perm <- rbind(create_VERB_perform_df("PERM"))
pron_data_perm <- rbind(create_PRON_perform_df("PERM"))

ppd_data_shuf <- rbind(create_PPD_perform_df("SHUF"))
verb_data_shuf <- rbind(create_VERB_perform_df("SHUF"))
pron_data_shuf <- rbind(create_PRON_perform_df("SHUF"))



performance_comparison_plot <- function(data, name) {
  res_plot <- ggplot(data, aes(better_model, fill=better_model)) 
  res_plot <- res_plot + geom_bar() 
  res_plot <- res_plot + scale_fill_manual(values=c("CETL"="darkgreen",  "MI"="#dd0000", "None"="darkblue"), drop = FALSE)
  res_plot <- res_plot + scale_x_discrete(limits = c("CETL", "MI", "None"))
  res_plot <- res_plot + labs(x = "model", y="# languages", fill="better_model")
  res_plot <- res_plot + theme_bw() 
  res_plot <- res_plot + theme(
    plot.title = element_text(color="black", size=18, face="bold",hjust=0.5),
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

#plot model comparison
g_pron_PERM <- performance_comparison_plot(ppd_data_perm, "PPD")
g_verb_PERM <- performance_comparison_plot(verb_data_perm, "VERB")
g_pr_PERM <- performance_comparison_plot(pron_data_perm, "PRON")
hitfail_plot_PERM <- ggarrange(g_pron_PERM, g_pr_PERM, g_verb_PERM, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL_PERM.pdf", sep=""), plot = hitfail_plot_PERM, width = 8, height = 4, dpi = 300)


g_pron_SHUF <- performance_comparison_plot(ppd_data_shuf, "PPD")
g_verb_SHUF <- performance_comparison_plot(verb_data_shuf, "VERB")
g_pr_SHUF <- performance_comparison_plot(pron_data_shuf, "PRON")
hitfail_plot_SHUF <- ggarrange(g_pron_SHUF, g_pr_SHUF, g_verb_SHUF, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL_SHUF.pdf", sep=""), plot = hitfail_plot_SHUF, width = 8, height = 4, dpi = 300)


g_pron_ALL <- performance_comparison_plot(ppd_data, "PPD")
g_verb_ALL <- performance_comparison_plot(verb_data, "VERB")
g_pr_ALL <- performance_comparison_plot(pron_data, "PRON")
hitfail_plot <- ggarrange(g_pron_ALL, g_pr_ALL, g_verb_ALL, label.x=0, label.y=1.01, common.legend = TRUE, legend = "right", ncol=3, nrow=1)
ggsave(paste(OUTPUT_DIR, "HIT_FAIL.pdf", sep=""), plot = hitfail_plot, width = 8, height = 4, dpi = 300)
