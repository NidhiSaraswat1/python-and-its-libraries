import random as r
n = r.randint(0,100)
a = -1
guesses = 0
while(a!=n):
    a = int(input("guess a number"))
    if(a>n):
        guesses += 1
        print("lower number please!!!")
    elif(a<n):
        print("Higher number please")

print(f"you have finally guessedd the number correctly in {guesses} attempt")        

