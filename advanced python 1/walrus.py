# it allows to assign values to variable as part of the expression

# using walrus operator
if(n:= len([1,2,3,4,5]))> 3:
    print(f"list is too ,long ({n}elements,expected <=3)")