import math
def Trianlge(a,b,c):
    s=(a+b+c)/2
    if (a+b)>c and (a+c)>b and (b+c)>a:
        area= math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('Area of Triangle: ', area)
    else:
        print('Triangle is not possible')
Trianlge(3,4,5)


