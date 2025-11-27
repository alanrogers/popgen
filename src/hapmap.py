# This program reads a file containing hapmap genotype data and
# prints each line

# Open data file and read it into a list of lines.
list_of_lines = open("encode-chr7-1kbp.dat").readlines()

# Operate on the lines in the list, one at a time.
for line in list_of_lines:
	# Get rid of white space at beginning and end
	line = line.strip()

        # Skip comments
	if line[0] == '#':
		continue

	# Turn line into a list of fields.
	line = line.split()

	# Skip header
	if line[0] == "rs#":
		continue

	# Data begins with field 11
	data = line[11:]

	# Print data
	print(data)



