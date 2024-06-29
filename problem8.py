#n! mean n *(n-1)
#for example 10! = 3628800
#find the sum of the digits in number 100!



def is_ok(answer):
    sum = 0
    for i in answer:
        sum += int(i)
    print(sum)



answer = 1
for i in range(1,101):
    answer *= i
is_ok(str(answer))
