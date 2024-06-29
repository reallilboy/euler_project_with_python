sum = 0
sum1 = 0
answer = 0
for i in range(101):
    sum += i ** 2
    sum1 += i
    answer = (sum1 ** 2)-sum
print(answer)

