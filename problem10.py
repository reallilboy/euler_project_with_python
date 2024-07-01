#Find the sum of all the primes below two million.

def is_prime(x):
    prime = True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            prime = False
            break
    return prime
sum = 0
for i in range(2,2000000):
    if is_prime(i):
        sum += i
print(sum)
