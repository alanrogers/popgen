set output "twolocsim.ps"     # for print output
set terminal postscript color linewidth 8 enhanced font "Vera" 24
set xlabel "Generations"
set xtics out
set ytics out
#set ylabel "D"
set yrange [-0.5:1.0]
set xrange [0:800]
set key on
plot "twolocsim.dat" using 1:2 title "p_A" with lines, \
  "twolocsim.dat" using 1:3 title "p_B" with lines, \
  "twolocsim.dat" using 1:(5*$4) title "5*D" with lines, \
  "twolocsim.dat" using 1:5 title "d" with lines
#pause mouse
