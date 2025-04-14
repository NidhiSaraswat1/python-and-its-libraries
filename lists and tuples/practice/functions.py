def dist_list(l1):
   length = len(l1)
   x =[]
   for i in range(0,length):
      b = l1[i]
      if b not in x:
         x.append(b)
   return x     
    

n = int(input("enter the number of items for the list "))
l1 =[]
for i in range(n):
   a = int(input("enter the items for list"))
   l1.append(a)

print(dist_list(l1))   



