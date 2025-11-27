# This is not the code used to construct dmyhist.eps. I got started
# here on an effort to reproduce that and then quit. I want to make
# the bars narrower but haven't the patience.
library(latticeExtra)
x <- c(0, 1, 0, 0, 1, 1, 1, 0, 0, 2)

histogram(x, type="count")
