def recur_fibo(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(2, n):
        a,b=b, a+b
        print(b)
n=int(input('enter the value of n: '))
recur_fibo(n)