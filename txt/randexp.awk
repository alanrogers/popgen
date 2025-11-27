BEGIN {
  srand();   # initialize random number generator
  h = 0.001;  # set the value of the hazard to whatever you want
  K = 1000;  # number of random variates to generate
  for(i=0; i<K; i++)
  {
    u = rand();     # random number between 0 and 1
    t = -log(u)/h;  # exponential variate with hazard h
    s = s+t;        # sum of t values
    s2 = s2 + t*t;  # sum of squared t values
  }
  mean = s/K;
  variance = s2/K - mean*mean;
  print "mean = ", mean, " SD = ", sqrt(variance);
}

