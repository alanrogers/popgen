BEGIN {
  srand();   # initialize random number generator
  K = 1000;  # number of random variates to generate
  G = 1000;  # number of genes in population
  for(i=0; i<K; i++)
  {
    T = 0;
    # sum over coalescent intervals
    for(n=10; n>=2; n--)
    {
      h = n*(n-1)/(2*G); # hazard
      u = rand();        # random number between 0 and 1
      t = -log(u)/h;     # exponential variate for this interval
      T = T + t;         # add to sum
    }
    s = s+T;        # sum of t values
    s2 = s2 + T*T;  # sum of squared t values
  }
  mean = s/K;
  variance = s2/K - mean*mean;
  print "mean = ", mean, " SD = ", sqrt(variance);
}

