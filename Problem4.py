#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_ok(answer):
    if answer[0] == answer[5]and\
       answer[1] == answer[4]and\
       answer[2] == answer[3]and\
       answer[0] == '9':
       print(answer)

for i in range(1000):
    for n in range(1000):
       is_ok(answer=str(i*n).zfill(6))
