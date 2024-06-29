# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

num = 2
while True:
    if all(num % n == 0 for n in range(1,21)):
        print(num)
        break
    else:
        num += 2
