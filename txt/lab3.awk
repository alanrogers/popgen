BEGIN {
  # Exercise 3-1
  print "Exercise 3-1"
  n = 123
  print "F20 = ", 1 - (1 - 1/(2*n))^20
  print ""
  # Exercise 3-2
  print "Exercise 3-2"
  # let g = 1-f
  g = 1
  for(i=1; i<=20; i++)
  {
    g = g * (1 - 1/(2*n))
    n = n * 1.01
  }
  f = 1 - g
  print "F20 = ",  f
  print ""
  # Exercise 3-3
  print "Exercise 3-3"
  Ne = 4*1000*1 / (1000 + 1)
  print "Ne = ", Ne
}

#############  output ###########################
#Exercise 3-1
#F20 =  0.0782364
#
#Exercise 3-2
#F20 =  0.0715395
#
#Exercise 3-3
#Ne =  3.996
