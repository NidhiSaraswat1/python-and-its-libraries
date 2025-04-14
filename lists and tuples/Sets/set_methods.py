# cannot contgain duplicate values and can't use index feature
s ={1,2,3,4,5,"Nidhi"}

print(s, type(s))
s.add("ridjima")
print(s)
print(len(s))
s.remove(4)
s.pop()

# union and intrersection
s1={78,68} 
s2={78,68,879}
# prints the value of bith sets wothout repeating 
# print(s1.union(s2))

# prints value which are common in both sets
print(s1.intersection(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))

