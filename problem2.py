#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2 , the first 10 terms will be: 
1,2,3,5,8,13,21,34,55
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def Is_Even(FirstNum):
    if FirstNum % 2 == 0:
        return True
    else:
        return False


FirstNum = 1
SecondNum = 2
sum = 0
while FirstNum < 4000000:
    NewNum = FirstNum + SecondNum
    FirstNum = SecondNum
    SecondNum = NewNum
    if (Is_Even(FirstNum)):
        sum += FirstNum
print(sum)
