import sys
a=sys.argv[1]
a_file = open(a, "r")
lines = a_file.readlines()
a_file.close()
del lines[0]
del lines[4]
del lines[9:]

new_file = open(a, "w+")
for line in lines:
    new_file.write(line)
new_file.close()