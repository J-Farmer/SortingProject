from random import randint

listNum = []

for i in range(0,1000000):
	listNum.append(randint(0,i))

listNum.sort()
print(listNum)
