import random as r
'''
1 is for snake
-1 is for water
0 is for gun
'''
computer = r.randint(-1,1)
youstr = input("enter your choice:s, w or g")
youDict = {"s":1, "w":-1, "g":0}
reverseDict ={1:"snake" , -1:"water", 0:"gun" }
you = youDict[youstr]

print(f"you chose {youstr} \n computer chose {reverseDict[computer]}")
if(computer==-1 and you == 1):
    print("you win!")
elif(computer == -1 and you==0):
    print("you lose!")  
elif(computer==1 and you == -1):
    print("you lose!")      
elif(computer==1 and you == 0):
    print("you win!")  
elif(computer==0 and you == 1):
    print("you lose!")  
elif(computer==0 and you == -1):
    print("you win!")  
else:
    print("match withdraw")        