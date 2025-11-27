library(ggplot2)
dat <- read.table("inbredmort.txt", header=T)

# Adjust text size. Default is 11
mytheme = theme_get()
mytheme$text$size = 20
theme_set(mytheme)

# The range of the combined data.
r <- with(dat, range(c(outbred, cousin)))

# Add a little to both ends so that the points don't fall on the axes.
dr <- diff(r)/20
mylim <- c( r[1]-dr, r[2]+dr)

# Plot data
plt <- ggplot(dat, aes(outbred, cousin)) +
  geom_point(shape=1, size=2) +
  xlim(mylim) + ylim(mylim) +
  coord_fixed(ratio=1) +
  geom_abline(slope=1, intercept=0) +
  geom_text(x=43, y=0, label="(Bittles and Neel, 1994)") +
  ggtitle("Offspring mortality: inbred versus outbred") +
  xlab("Outbred") +
  ylab("Cousin marriage")
ggsave("inbredmort.pdf", plot=plt)

