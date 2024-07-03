#The following iterative sequence is defined for the set of positive integers:
#n -> n/2(even)
#n -> n3 + 1(odd)
#Which starting number, under one million, produces the longest chain?

def is_ok(x):
    count = 1
    while x > 1:
        if x % 2 ==0:
            x //= 2
            count += 1
        else:
            x = x * 3 + 1
            count += 1
    return count

answer = 0
for i in range(1,1000000):
    if answer < is_ok(i):
        answer = is_ok(i)
        print(i,answer)
