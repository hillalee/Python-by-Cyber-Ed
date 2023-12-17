# python book by Cyber Ed, page 109

def check_input(user_input):
	"""checks if 5 digit input is not alpha
		if it's the desired input, returns True"""
	if (not user_input.isdecimal()) or len(user_input) != 5:
		return False
	return True


def divided(user_input):
	"""takes care of the 2nd task, returns each
	digit, divided by commas"""
	list_of_digits = []
	for num in user_input:
		list_of_digits.append(num)
	return list_of_digits


def sum_of_digits(list_of_digits):
	"""sums up every digit"""
	user_sum = 0
	for num in list_of_digits:
		user_sum += int(num)
	return user_sum


def main():
	assert divided("123") == ["1", "2", "3"]
	assert check_input("abc") == False
	assert check_input("12344") == True
	assert check_input("123") == False
	assert sum_of_digits([1,2,3,4,5]) == 15
	user_input = input("Please insert a 5 digit number: \n")
	while not check_input(user_input):
		user_input = input("Illegal input. \n"
						   "Please insert a 5 digit number: \n")

	devided_list = divided(user_input)

	print("You entered the number: {} \nThe digits of the number are: {} \n"
		  "The sum of the number is: {}".format(user_input, ", ".join(devided_list), sum_of_digits(devided_list)))

if __name__ == "__main__":
	main()
