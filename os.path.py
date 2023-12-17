import os
import sys
PATH = 1


def check_path(givenPath):
	return os.path.exists(givenPath)

def main():
	myPath = sys.argv[PATH]
	check = check_path(myPath)
	if not check:
		print("Directory not found")
	else:
		print("Hi {}".format(myPath))
main()