def add(x,y):
    return x+y
def sub(x,y):
    return x-y    
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print('select operation')
print('1.Add')
print('1.sub')
print('1.mul')
print('1.div')
choice=int(input('Enter the choice (1/2/3/4): '))

x=int(input('Enter first number:  '))
y=int(input('Enter second number: '))

if choice == 1:
    print(x , '+', y, '=', add(x,y))
elif choice == 2:
    print(x , '-', y, '=', sub(x,y))
elif choice == 3:
    print(x , '*', y, '=', mul(x,y))
elif choice == 4:
    print(x , '/', y, '=', div(x,y))
else:
    print('invalid input')