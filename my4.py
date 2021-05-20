import random
import os


randomlist = []
odd_randomlist = []
sum_ = 0

for i in range(0,20):
	n = random.randint(1,20)
	randomlist.append(n)

for y in randomlist:
	if y % 2 != 0:
		odd_randomlist.append(y)
path = os.path.join(os.getcwd(), "file_.txt")
with open(path, 'w') as file_:
	file_.write(str(odd_randomlist))
with open(path, 'r') as file_:
	print(file_.read())

for j in range(0, len(odd_randomlist)):
	sum_ += odd_randomlist[j]
print(sum_)