
OUTPUT_DIR <- "/Path/to/R_plots/"
INPUT_DIR <- "/Path/to/freqs/"

frequencies <- read.csv(paste(INPUT_DIR,"calculated_weights_0_DEF.tsv",sep=""),sep="\t", colClasses = c("character","character","character","character","numeric"))
names(frequencies)[1] <- "PERS"
names(frequencies)[2] <- "NUM"
names(frequencies)[3] <- "GEN"
names(frequencies)[4] <- "TEN"
names(frequencies)[5] <- "freq"

frequencies <- frequencies %>%
  mutate(NUM = recode(NUM, "s" = "sg", "p" = "pl", "d" = "du"))

frequencies <- frequencies %>%
  mutate(NUMGEN = factor(paste(NUM, GEN), levels = c("sg m", "sg f","du m", "du f", "pl m", "pl f")))


frequencies <- mutate(frequencies, normed_freq = freq / sum(freq))

g <- ggplot(data=frequencies, aes(y=PERS, x=NUMGEN, fill=log(x=normed_freq, base=exp(1)))) 
g <- g + geom_tile()
g <- g + labs(x = "number & gender", y="person", fill="log prob")



ggsave(paste(OUTPUT_DIR,"FREQ_heatmap.pdf",sep=""), plot = g, width = 3, height = 2, dpi = 300)

