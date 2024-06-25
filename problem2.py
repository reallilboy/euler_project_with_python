def Is_Even(FirstNum):
    if FirstNum % 2 == 0:
        return True
    else:
        return False
    break


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
