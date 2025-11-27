from tabulator import Tabulator  # module for tabulating data

# A dummy data set consisting of numbers between 0.0 and 1.0.
data = [0.39760402926232336, 0.38844722349063998, 0.15828823308128848,
        0.21675307512013373, 0.67759054634129579, 0.63336008432108437,
        0.7791838758913473, 0.11329205659594056, 0.088616376501101851,
        0.27797955173023731]

# tabulate numbers in range [0,1] into 5 bins        
tab = Tabulator(-0.00001, 1.00001, 5) 
for x in data:
    tab += x

print(tab)
