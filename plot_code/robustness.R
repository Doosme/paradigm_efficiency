CODE_DIR <- "/Path/to/plot_code/"
IB_INPUT_DIR <- "/Path/to/ibvalues/"
LANGLIST_INPUT_DIR <- "/Path/to/_data_util/"
OUTPUT_DIR <- "/Path/to/R_plots/"

setwd(CODE_DIR) 
source("util.R")


#read in data
unif_data <- create_rand_unif_ib_df("PERM_SHUF_BASE","rob_unif")
rand1_data <- create_rand_unif_ib_df("PERM_SHUF_BASE","rob_rand1")
rand2_data <- create_rand_unif_ib_df("PERM_SHUF_BASE","rob_rand2")
rand3_data <- create_rand_unif_ib_df("PERM_SHUF_BASE","rob_rand3")


unif_data_perm <- unif_data[grepl("PERM", unif_data$perm_type), ]
rand1_data_perm <- rand1_data[grepl("PERM", rand1_data$perm_type), ]
rand2_data_perm <- rand2_data[grepl("PERM", rand2_data$perm_type), ]
rand3_data_perm <- rand3_data[grepl("PERM", rand3_data$perm_type), ]

unif_data_permshuf <- unif_data[grepl("PERM|SHUF", unif_data$perm_type), ]
rand1_data_permshuf <- rand1_data[grepl("PERM|SHUF", rand1_data$perm_type), ]
rand2_data_permshuf <- rand2_data[grepl("PERM|SHUF", rand2_data$perm_type), ]
rand3_data_permshuf <- rand3_data[grepl("PERM|SHUF", rand3_data$perm_type), ]


unif_data_bases <- unif_data[grepl("BASE", unif_data$perm_type), ]
rand1_data_bases <- rand1_data[grepl("BASE", rand1_data$perm_type), ]
rand2_data_bases <- rand2_data[grepl("BASE", rand2_data$perm_type), ]
rand3_data_bases <- rand3_data[grepl("BASE", rand3_data$perm_type), ]




### Efficiency


create_EFF_plot_rob <- function(data, data_base, name) {
  
  ce <- ggplot(data=data) +geom_point(aes(x=loss, y=-acc),color='gray', alpha = 8/10) 
  ce <- ce + geom_point(data=data_base,aes(x=loss, y=-acc), size=2, color="red")
  ce <- ce + labs(x = "complexity (CETL)", y="accuracy") 
  ce <- ce + ggtitle("CETL")
  ce <- ce + theme_bw()
  ce <- ce + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  
  co <- ggplot(data=data) +geom_point(aes(x=compl, y=-acc),color='gray', alpha = 8/10) 
  co <- co + geom_point(data=data_base,aes(x=compl, y=-acc), size=2, color="red")
  co <- co + labs(x = "complexity (CETL)", y="accuracy") 
  co <- co + ggtitle("MI")
  co <- co + theme_bw()
  co <- co + theme(
    plot.title = element_text(color="black", size=16, face="bold",hjust=0.5),
    axis.title.x = element_text(color="blue", size=14),
    axis.title.y = element_text(color="blue", size=14),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face="bold"),
    legend.text = element_text(size = 14)
  )
  res_plot <- ggarrange(ce, co, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  
  ggsave(paste(OUTPUT_DIR,"EFF_",name,".pdf", sep = ""), plot = res_plot, width = 7, height = 3.5, dpi = 300)
  
  return(res_plot)
}

rob_unif_eff <- create_EFF_plot_rob(unif_data, unif_data_bases, "rob_unif")
rob_rand1_eff <- create_EFF_plot_rob(rand1_data, rand1_data_bases, "rob_rand1")
rob_rand2_eff <- create_EFF_plot_rob(rand2_data, rand2_data_bases, "rob_rand2")
rob_rand3_eff <- create_EFF_plot_rob(rand3_data, rand3_data_bases, "rob_rand3")


rob_eff <- ggarrange(rob_unif_eff, rob_rand1_eff, rob_rand2_eff, rob_rand3_eff, labels = c("Uniform","Random1","Random2","Random3"),common.legend = TRUE, legend = "right", ncol=2, nrow=2)
ggsave(paste(OUTPUT_DIR, "EFF_rob_ALL.pdf", sep=""), plot = rob_eff, width = 14, height = 7, dpi = 300)




### Naturalness

create_NAT_plot_rob <- function(data, data_base, name) {
  data_perm <- data
  data_perm <- data_perm[!grepl("SHUF", data_perm$perm_type), ]
  data_perm <- data_perm[!grepl("SYN", data_perm$perm_type), ]
  
  g <- ggplot(data=data_perm, aes(group=lang_type, x=nat, y=loss_r_base)) 
  g <- g + geom_point(aes(color=lang_type), alpha=2/10)  
  g <- g + geom_smooth(aes(color=lang_type))  
  g <- g + geom_point(data=data_base, aes(x=nat, y=loss_r_base), size=3, color='red', alpha=2/10) 
  g <- g + labs(x = "naturalness", y="relative complexity (CETL)") 
  g <- g + ggtitle("CETL")
  g <- g + theme_bw()
  g <- g + theme(
    plot.title = element_text(color="black", size=14, face="bold",hjust=0.5),
    axis.title.x = element_text(color="blue", size=12),
    axis.title.y = element_text(color="blue", size=12),
    axis.text.x = element_text(size = 10),
    axis.text.y = element_text(size = 10),
    legend.title = element_text(size = 12, face="bold"),
    legend.text = element_text(size = 10)
  )
  p <- ggplot(data=data_perm, aes(group=lang_type, x=nat, y=compl_r_base)) 
  p <- p + geom_point(aes(color=lang_type), alpha=2/10) 
  p <- p + geom_smooth(aes(color=lang_type)) 
  p <- p + geom_point(data=data_base,  aes(x=nat, y=compl_r_base), size=3, color='red', alpha=2/10) 
  p <- p + labs(x = "naturalness", y="relative complexity (MI)")
  p <- p + ggtitle("MI")
  p <- p + theme_bw()
  p <- p + theme(
    plot.title = element_text(color="black", size=14, face="bold",hjust=0.5),
    axis.title.x = element_text(color="blue", size=10),
    axis.title.y = element_text(color="blue", size=10),
    axis.text.x = element_text(size = 10),
    axis.text.y = element_text(size = 10),
    legend.title = element_text(size = 12, face="bold"),
    legend.text = element_text(size = 10)
  )
  res_plot <- ggarrange(g, p, common.legend = TRUE, legend = "right", ncol=2, nrow=1)
  ggsave(paste("/Users/do/documents/Uni/0-MA2/pgn-paradigms_DATA/NEW_results/R_plots/NAT_",name,".pdf", sep = ""), plot = res_plot, width = 12, height = 3, dpi = 300)
  
  return(res_plot)
}



rob_unif_nat <- create_NAT_plot_rob(unif_data_perm, unif_data_bases, "rob_unif")
rob_rand1_nat <- create_NAT_plot_rob(rand1_data_perm, rand1_data_bases, "rob_rand1")
rob_rand2_nat <- create_NAT_plot_rob(rand2_data_perm, rand2_data_bases, "rob_rand2")
rob_rand3_nat <- create_NAT_plot_rob(rand3_data_perm, rand3_data_bases, "rob_rand3")


rob_nat <- ggarrange(rob_unif_nat, rob_rand1_nat, rob_rand2_nat, rob_rand3_nat, labels = c("Uniform","Random1","Random2","Random3"),common.legend = TRUE, legend = "right", ncol=1, nrow=4)
ggsave(paste(OUTPUT_DIR,"NAT_rob_ALL.pdf", sep=""), plot = rob_nat, width = 12, height = 12, dpi = 300)













######CORRELATION:


unif_cors_CETL <- unif_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PRON")
avg_cor_unif_CETL <- sum(unif_cors_CETL$cor)/length(unif_cors_CETL$cor)
unif_cors_MI <- unif_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PRON")
avg_cor_unif_MI <- sum(unif_cors_MI$cor)/length(unif_cors_MI$cor)

unif_cors_ALL <- rbind(unif_cors_CETL,unif_cors_MI)

rand1_cors_CETL <- rand1_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PRON")
avg_cor_rand1_CETL <- sum(rand1_cors_CETL$cor)/length(rand1_cors_CETL$cor)
rand1_cors_MI <- rand1_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PRON")
avg_cor_rand1_MI <- sum(rand1_cors_MI$cor)/length(rand1_cors_MI$cor)

rand1_cors_ALL <- rbind(rand1_cors_CETL,rand1_cors_MI)

rand2_cors_CETL <- rand2_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PRON")
avg_cor_rand2_CETL <- sum(rand2_cors_CETL$cor)/length(rand2_cors_CETL$cor)
rand2_cors_MI <- rand2_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PRON")
avg_cor_rand2_MI <- sum(rand2_cors_MI$cor)/length(rand2_cors_MI$cor)

PRON_CS21g5_cors_ALL <- rbind(rand2_cors_CETL,rand2_cors_MI)

rand3_cors_CETL <- rand3_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, loss), p=round(cor.test(nat,loss)$p.value,4), model="CETL", expr="PRON")
avg_cor_rand3_CETL <- sum(rand3_cors_CETL$cor)/length(rand3_cors_CETL$cor)
rand3_cors_MI <- rand3_data_perm %>%
  group_by(lang) %>%
  summarize(cor=cor(nat, compl), p=round(cor.test(nat,compl)$p.value,4), model="MI", expr="PRON")
avg_cor_rand3_MI <- sum(rand3_cors_MI$cor)/length(rand3_cors_MI$cor)

rand3_cors_ALL <- rbind(rand3_cors_CETL,rand3_cors_MI)

#
cor_values_table <-
  rbind(c(round(avg_cor_unif_CETL,2), round(avg_cor_unif_MI,2)),
        c(round(avg_cor_rand1_CETL,2), round(avg_cor_rand1_MI,2)),
        c(round(avg_cor_rand2_CETL,2), round(avg_cor_rand2_MI,2)),
        c(round(avg_cor_rand3_CETL,2), round(avg_cor_rand3_MI,2)))
colnames(cor_values_table) <- c("CETL", "MI")
rownames(cor_values_table) <- c("uniform","random1","random2", "random3")

cor_values_table








########TODO: wird das gebraucht?

#perm-shuf
permshuf_unif_CE_ttest <- t.test(mu=unif_data_bases$loss, x=unif_data_permshuf$loss, alternative = "two.sided")
permshuf_rand1_CE_ttest <- t.test(mu=rand1_data_bases$loss, x=rand1_data_permshuf$loss, alternative = "two.sided")
permshuf_rand2_CE_ttest <- t.test(mu=rand2_data_bases$loss, x=rand1_data_permshuf$loss, alternative = "two.sided")
permshuf_rand3_CE_ttest <- t.test(mu=rand3_data_bases$loss, x=rand1_data_permshuf$loss, alternative = "two.sided")

permshuf_unif_ACC_ttest <- t.test(mu=unif_data_bases$acc, x=unif_data_permshuf$acc, alternative = "two.sided")
permshuf_rand1_ACC_ttest <- t.test(mu=rand1_data_bases$acc, x=rand1_data_permshuf$acc, alternative = "two.sided")
permshuf_rand2_ACC_ttest <- t.test(mu=rand2_data_bases$acc, x=rand2_data_permshuf$acc, alternative = "two.sided")
permshuf_rand3_ACC_ttest <- t.test(mu=rand3_data_bases$acc, x=rand3_data_permshuf$acc, alternative = "two.sided")


res_table <- rbind(
  c(permshuf_unif_CE_ttest$statistic, permshuf_unif_CE_ttest$p.value),
  c(permshuf_unif_ACC_ttest$statistic, permshuf_unif_ACC_ttest$p.value),
  c(permshuf_rand1_CE_ttest$statistic, permshuf_rand1_CE_ttest$p.value),
  c(permshuf_rand1_ACC_ttest$statistic, permshuf_rand1_ACC_ttest$p.value),
  c(permshuf_rand2_CE_ttest$statistic, permshuf_rand2_CE_ttest$p.value),
  c(permshuf_rand2_ACC_ttest$statistic, permshuf_rand2_ACC_ttest$p.value),
  c(permshuf_rand3_CE_ttest$statistic, permshuf_rand3_CE_ttest$p.value),
  c(permshuf_rand3_ACC_ttest$statistic, permshuf_rand3_ACC_ttest$p.value)
)
colnames(res_table) <- c("t-value", "p-value")
rownames(res_table) <- c("Uniform (CETL)", "Uniform (ACC)",
                         "Random1 (CETL)", "Random1 (ACC)",
                         "Random2 (CETL)", "Random2 (ACC)",
                         "Random3 (CETL)", "Random3 (ACC)")

res_table

