data_matrix = [ [2,0,1,2,1,2,2,0],
                [2,0,0,0,1,0,1,1] ]

# first sum x, y, and x*y
mx = my = mxy = 0.0
for x, y in zip(data_matrix[0],data_matrix[1]):
    mx += x
    my += y
    mxy += x * y

n = float(len(data_matrix[0])) # length of row

# turn sums into means
mx /= n
my /= n
mxy /= n

# use equation 10.1
Cxy = mxy - mx*my

print("Cxy:", Cxy)

