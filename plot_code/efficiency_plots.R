CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")



#read in data
ppd_data <- rbind(create_PPD_ib_df("PERM_SHUF_BASE"))
ppd_data <- ppd_data %>% mutate(LANGFAM = factor(lang_family, levels = c("PPD")))

verb_data <- rbind(create_VERB_ib_df("PERM_SHUF_BASE"))
verb_data <- verb_data %>% mutate(LANGFAM = factor(lang_family, levels = c("SEM", "AFRO","GER", "ROM")))

pron_data <- rbind(create_PRON_ib_df("PERM_SHUF_BASE"))
pron_data <- pron_data %>% mutate(LANGFAM = factor(lang_family, levels = c("SEM", "AFRO","GER", "ROM", "ALTAI", "SLAV","INDIRA","OTHER")))

#create corresponding baseline_df
ppd_data_bases <- ppd_data[grepl("BASE", ppd_data$perm_type), ]
verb_data_bases <- verb_data[grepl("BASE", verb_data$perm_type), ]
pron_data_bases <- pron_data[grepl("BASE", pron_data$perm_type), ]



create_EFF_plot_CETL <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  
  ce_plot <- ggplot(data=mutate(data_perm,lang_family = "perms")) 
  ce_plot <- ce_plot + geom_point(aes(x=loss, y=-acc),color='gray', alpha = 1/10, size=0.5) 
  ce_plot <- ce_plot + geom_point(data=data_base,aes(x=loss, y=-acc,color=LANGFAM), alpha = 7/10, size=2)
  ce_plot <- ce_plot + labs(x = "complexity (CETL)", y="accuracy", color="lang family")
  ce_plot <- ce_plot + theme_bw()
  ce_plot <- ce_plot + ggtitle(name)
  ce_plot <- ce_plot + theme(
    plot.title = element_text(color="black", size=18, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=16),
    axis.title.y = element_text(color="blue", size=16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  
  ggsave(paste(OUTPUT_DIR,"EFF_",name,"_CETL.pdf",sep=""), plot = ce_plot, width = 5, height = 3, dpi = 300)
  
  return(ce_plot)
}


create_EFF_plot_MI <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  
  co_plot <- ggplot(data=mutate(data_perm,lang_family = "perms")) 
  co_plot <- co_plot + geom_point(aes(x=compl, y=-acc),color='gray', alpha = 1/10, size=0.5) 
  co_plot <- co_plot + geom_point(data=data_base,aes(x=compl, y=-acc,color=LANGFAM), alpha = 7/10, size=2)
  co_plot <- co_plot + labs(x = "complexity (MI)", y="accuracy", color="lang family")
  co_plot <- co_plot + theme_bw()
  co_plot <- co_plot + ggtitle(name)
  co_plot <- co_plot + theme(
    plot.title = element_text(color="black", size=18, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=16),
    axis.title.y = element_text(color="blue", size=16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  co_plot <- co_plot + theme(legend.text = element_text(size = 10))
  
  ggsave(paste(OUTPUT_DIR,"EFF_",name,"_MI.pdf",sep=""), plot = co_plot, width = 5, height = 3, dpi = 300)
  
  return(co_plot)
}


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
    plot.title = element_text(color="black", size=18, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=16),
    axis.title.y = element_text(color="blue", size=16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  
  co_plot <- ggplot(data=mutate(data_perm,lang_family = "perms")) 
  co_plot <- co_plot + geom_point(aes(x=compl, y=-acc),color='gray', alpha = 1/10, size=0.5) 
  co_plot <- co_plot + geom_point(data=data_base,aes(x=compl, y=-acc,color=LANGFAM), alpha = 7/10, size=2)
  co_plot <- co_plot + labs(x = "complexity (MI)", y="accuracy", color="lang family")
  co_plot <- co_plot + theme_bw()
  co_plot <- co_plot + ggtitle("MI")
  co_plot <- co_plot + theme(
    plot.title = element_text(color="black", size=18, face="bold",hjust=0.5),,
    axis.title.x = element_text(color="blue", size=16),
    axis.title.y = element_text(color="blue", size=16),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  co_plot <- co_plot + theme(legend.text = element_text(size = 10))
  
  res_plot <- ggarrange(ce_plot, co_plot, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  ggsave(paste(OUTPUT_DIR,"EFF_",name,".pdf",sep=""), plot = res_plot, width = 15, height = 6, dpi = 300)

  return(res_plot)
}


#create CETL plots
ce_plot_VERB <- create_EFF_plot_CETL(verb_data, verb_data_bases,"VERB")
ce_plot_PRON <- create_EFF_plot_CETL(pron_data, pron_data_bases,"PRON")
ce_plot_PPD <- create_EFF_plot_CETL(ppd_data, ppd_data_bases,"PPD") + guides(color = "none", fill = "none")

#create MI plots
co_plot_VERB <- create_EFF_plot_MI(verb_data, verb_data_bases,"VERB")
co_plot_PRON <- create_EFF_plot_MI(pron_data, pron_data_bases,"PRON")
co_plot_PPD <- create_EFF_plot_MI(ppd_data, ppd_data_bases,"PPD") + guides(color = "none", fill = "none")

#create combined plots #todo:
plots_VERB <- create_EFF_plot_comb(verb_data, verb_data_bases,"VERB")
plots_PRON <- create_EFF_plot_comb(pron_data, pron_data_bases,"PRON")
plots_PPD <- create_EFF_plot_comb(ppd_data, ppd_data_bases,"PPD") + guides(color = "none", fill = "none")

#create plot containing CETL for all three domains.
ce_res_plot <- ggarrange(ce_plot_VERB, ce_plot_PRON, ce_plot_PPD, common.legend = FALSE, legend = "right", ncol=3, nrow=1, widths = c(1, 1, 0.75))
ggsave(paste(OUTPUT_DIR,"EFF_ALL_CETL.pdf",sep=""), plot = ce_res_plot, width = 15, height = 3.5, dpi = 300)


