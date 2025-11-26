BEGIN{
    n = 0;
    mX = 0;
    mY = 0;
    mXsq = 0;
    mYsq = 0;
    mXY = 0;
}
NF==2 {
    mX += $1;
    mY += $2;
    mXsq += $1 * $1;
    mYsq += $2 * $2;
    mXY += $1 * $2;
    ++n;
}
END{
    mX /= n;
    mY /= n;
    mXsq /= n;
    mYsq /= n;
    mXY /= n;
	
    vX = (mXsq - mX^2);
    vY = (mYsq - mY^2);
    c  = (mXY - mX * mY);

    printf("n = %d\n", n);
    printf("mX = %f mY = %f\n", mX, mY);
    printf("mXsq = %f mYsq = %f mXY = %f\n", mXsq, mYsq, mXY);
    printf("vX = %f vY = %f cov = %f\n", vX, vY, c);
    printf("regression of y on x: %f\n", c/vX);
    printf("heritability        : %f\n", 2.0 * c/vX);
}
