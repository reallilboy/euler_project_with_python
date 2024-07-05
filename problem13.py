#What is the10001 st prime number?





def is_prime(x):
    prime = True
    for i in range(2,x):
        if x % i ==0:
            prime = False
            break
    return prime

count = 0
for i in range(2,100000000000):
    if is_prime(i):
        count += 1 
        if count == 10001:
            print(i)
            break
