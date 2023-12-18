# page 151 in the book
import random
CONTROL_TOWER_LOCATION = (4, 4)

class Plane:
	def __init__(self):
		self.__x = 0
		self.__y = 0

	def __str__(self):
		return "Plane position: {}".format(self.get_position())

	def update_position(self):
		self.__x += random.randint(-1, 1)
		self.__y += random.randint(-1, 1)

	def get_position(self):
		return self.__x, self.__y

	def set_position(self, x, y):
		if (x, y) == CONTROL_TOWER_LOCATION:
			print("Location of the tower")
		elif x < 0 or y < 0:
			print("illegal location")
		else:
			self.__x = x
			self.__y = y


class Boat:
	def __init__(self):
		self.__x = 0
		self.__y = 0

def main():
	print("This main function is not reached if the file is imported")

if __name__ == "__main__":
	main()
