# open is an in built function which takes two parametrs , file address and mode.
# by default mode is read as "r"
f = open("file.txt")
data =f.read()
print(data)
# its important to close a file
f.close()