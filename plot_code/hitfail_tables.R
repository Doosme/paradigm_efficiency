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


create_hitfail_df <- function(data){
  values <- c(
    round(sum(data$HIT_CETL)/sum(data$perm_count)*100,2),
    round(sum(data$HIT_MI)/sum(data$perm_count)*100,2),
    round(sum(data$FAIL_CETL)/sum(data$perm_count)*100,2),
    round(sum(data$FAIL_MI)/sum(data$perm_count)*100,2),
    round((sum(data$HIT_CETL) - sum(data$FAIL_CETL))/sum(data$perm_count)*100,2),
    round((sum(data$HIT_MI) - sum(data$FAIL_MI))/sum(data$perm_count)*100,2),
    sum(data$perm_count))
  return(values)
}

ppd_perm_values <- create_hitfail_df(ppd_data_perm)
pron_perm_values <- create_hitfail_df(pron_data_perm)
verb_perm_values <- create_hitfail_df(verb_data_perm)
perm_table <- rbind(ppd_perm_values, pron_perm_values, verb_perm_values)
colnames(perm_table) <- c("Hit-CETL","Hit-MI", "Fail-CETL", "Fail-MI", "Eff-CETL", "Eff-MI", "support")
rownames(perm_table) <- c("PPD (PERM)","PRON (PERM)","VERB (PERM)")

ppd_shuf_values <- create_hitfail_df(ppd_data_shuf)
pron_shuf_values <- create_hitfail_df(pron_data_shuf)
verb_shuf_values <- create_hitfail_df(verb_data_shuf)
shuf_table <- rbind(ppd_shuf_values, pron_shuf_values, verb_shuf_values)
colnames(shuf_table) <- c("Hit-CETL","Hit-MI", "Fail-CETL", "Fail-MI", "Eff-CETL", "Eff-MI", "support")
rownames(shuf_table) <- c("PPD (SHUF)","PRON (SHUF)","VERB (SHUF)")


perm_table
shuf_table