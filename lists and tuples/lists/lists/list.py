# lists are mutable ,change scan be made in lists.
friends =["akash",5,45.5,False,"Nidhi","apple","orange"]
print(friends[0][3])
friends[0]= "hello!!"
print(friends[0])
print(friends[1:5])
friends.append("World")
print(friends)