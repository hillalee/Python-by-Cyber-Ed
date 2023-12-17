
char = input("Insert an upper case letter A-Z: \n")
size = int(input("Insert an odd number 1-21: \n"))
iteration = 0
upper = size
lower = 1


while upper >=1:
	print(" " * iteration, char * upper)
	iteration += 1
	upper -= 2

iteration -=1
char = chr(ord(char) + 32)

while lower <=size:
	print(" " * iteration, char * lower)
	iteration -= 1
	lower += 2
