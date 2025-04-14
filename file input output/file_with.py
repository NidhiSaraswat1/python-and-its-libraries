f = open("file.txt")
print(f.read())
f.close()

# the same can be done using with statement where u dont need to close the file
with open("file.txt") as f:
    print(f.read())