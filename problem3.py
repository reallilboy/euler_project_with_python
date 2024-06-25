#a simple algorithm for prime factor calculation
#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of the number 600851475134?


number = 600851475143
answer = 1
for i in range(2,number):
    if number % i == 0:
        answer *= i
    if answer == number: 
        print(i)
        break
