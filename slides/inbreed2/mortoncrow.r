# I think these data are from Morton, Crow, and Muller, 1956.
library(ggplot2)
df <- read.table("mortoncrow.txt", header=T)

# Adjust text size. Default is 11
mytheme = theme_get()
mytheme$text$size = 20
theme_set(mytheme)

df$lns <- with(df, log(s/n))
ggplot(df, aes(f, lns)) + geom_point() +
    xlab("Inbreeding Coefficient") +
    ylab("log Survival")
ggsave("mortoncrow.pdf")
