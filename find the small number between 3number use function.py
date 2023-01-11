def smallest(x,y,z):
    if x<y and x<z:
        return x
    elif y<z:
        return y
    else:
        return z
print(smallest(10,12,14))