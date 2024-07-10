#a < b < c = 100
#found a , b , c

for c in range(334,500):
    for a in range(1,int(1000-c)):
        b = (1000 - c ) - a
        if a**2 + b**2 == c**2:
            print(a,b,c)
