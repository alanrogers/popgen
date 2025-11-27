#set output "lddecay.svg"     # for print output
#set terminal svg dynamic font "Arial,20"
set terminal latex
set output "lddecay.tex"     # for print output
set size 2.8/5., 2.5/3.
#set terminal pdfcairo color font "Arial,20"
set xlabel "Time (t) in Generations"
set ylabel "\\Large$\\frac{D_t}{D_0}$"
set style line 1 linetype 1
set style line 2 linetype 2
set style line 3 linetype 6
set yrange [0.0:1.0]
set xrange [0:300]
set dummy t
set key on
set ytics 0.25, 0.25, 1
plot (1-0.2)**t title "c = 0.2" ls 1, (1-0.02)**t title "c = 0.02" ls 2, \
  (1-0.002)**t title "c = 0.002" ls 3

#pause mouse
