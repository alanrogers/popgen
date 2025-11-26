from pgen import Tabulator

# A dummy data set consisting of numbers between 0.0 and 1.0.

data = [0.33236342968786442, 0.73055958580640823, 0.34100448055922677, 
        0.93062544008569004, 0.57670398113446419, 0.51266858597089471]

tab = Tabulator()     # construct a new tabulator
for x in data:        # tabulate the data
    tab += x

print(tab)             # print the tabulation
