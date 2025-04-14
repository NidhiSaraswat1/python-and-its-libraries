num = int(input("enter a number to check palindrome"))
dup = num
pal =0

while(num>0):
     
    pal =  pal*10 + num%10
    num = num//10
if(pal == dup):
    print("number is palindrome")    
else:
    print("number is not palindrome")    