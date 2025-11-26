function rnorm()
{
  do{
    /* form uniform variates on [-1,1] */
    v1 = 2.0*rand() - 1.0;
    v2 = 2.0*rand() - 1.0;
    s = v1*v1 + v2*v2;
  }while(s > 1.0);
  /* we now have a random point (v1,v2) in the unit circle */
  y = sqrt(-2.0*log(s)/s);
  /* now x1 and x2 are uniform random variates */
  x1 = v1*y;
  return(x1);
}

BEGIN {
    srand();
    m = 100;
    Va = 100;  # Additive genetic variance
    Ve = 100;  # environmental variance
    fa = sqrt(Va/2);
    fe = sqrt(Ve);
    for(i=0; i < 1000; ++i) {
	w = fa*rnorm();  # dummy
	x = fa*rnorm();  # genetic contributions
	y = fa*rnorm();
	z = fa*rnorm();
	e1 = fe*rnorm();  # environmental contributions
	e2 = fe*rnorm();
	#printf("%10.3f & %10.3f \\\\\n", m+x+y+e1, m+x+z+e2);
	printf("%10.3f %10.3f\n", m+x+y+e1, m+x+z+e2);
    }
#    printf("Parameters: Va=%f Ve = %f heritability = %f\n",
#	   Va, Ve, Va/(Va+Ve));
}


