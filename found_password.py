#Who can open the lock?
#One of the numbers is right and in the right place 6,8,2
#One of the correct numbers but wrong somewhere 6,1,4
#Two of the numbers are correct but in the wrong place 2,0,6
#One of the correct numbers but in the wrong place 7,3,8
#all numbers is right 3,8,0

def sit(a,b):
    correct = 0
    found = 0
    br = []
    ar = []
    for i in range(len(a)):
        if a[i] == b[i]:
            correct += 1
        else:
            ar.append(a[i])
            br.append(b[i])

    for c in ar:
        if c in br:
            found += 1
            br.remove(c)

    return correct,found


for i in range(0,1000):
    i = str(i).zfill(3)
    if sit(i,'682') == (1,0)and\
       sit(i,'614') == (0,1)and\
       sit(i,'206') == (0,2)and\
       sit(i,'738') == (0,0)and\
       sit(i,'380') == (0,1):
           print(i)
