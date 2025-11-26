duffy <- c(0.037, 0.436, 1.000,0.901)
p <- mean(duffy)
v <- var(duffy)*(3.0/4)
duffyFst <- v/(p*(1-p))
duffyFst

P.locus <- c(0.734,0.496,0.330,0.259)
p <- mean(P.locus)
v <- var(P.locus)*(3.0/4)
P.Fst <- v/(p*(1-p))
P.Fst
