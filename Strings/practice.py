name=input("enter your name")

print(name,"Good afternoon" )
# another waY TO DO the same,using f strings
print(f"Good afternoon {name}")

# problem3
letter = '''dear <|name|>,
                you are selected!
                    <|date|>   '''

print(letter.replace("<|name|>","Nidhi").replace("<|date|>","24 october 2024"))