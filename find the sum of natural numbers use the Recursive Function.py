def recur_func(x):
    if x==1:
        return 1
    else:
        return x + recur_func(x-1)
   

y=int(input('Enter the value of x: '))
print(recur_func(y))
 
