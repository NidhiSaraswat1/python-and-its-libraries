f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
line = f.readline()
while(line != " "):
    print(line)
    line = f.readline()

# print( type(line1))
f.close()