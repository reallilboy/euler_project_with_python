#Considering a room with 100 people in it
#We want to do a lottery,
#then people randomly give money to each
#other until one person's money reaches 0



import random
random.seed()



#We create 100 people using this loop
people = []
for i in range(50):
    people.append(100)

#we create lottery among people this loop
for x in range(1000):
    for person1 in range(50): 

#Here we choose people randomly
        person2 = random.randrange(50)
        while person2 == 0:
            person2 = random.randrange(50)
#We check people's money
        if people[person1] != 0:
            people[person1] -= 1
            people[person2] += 1

print(people)
