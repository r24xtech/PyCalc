print("HW03 \n\n")

go = True

op_choices = ["+", "-", "*", "/", "//", "^", "**", "%"]

def do_the_math(i, a, b):
	if(i == 0):
		return a + b
	elif(i == 1):
		return a - b
	elif(i == 2):
		return a * b
	elif(i == 3):
		return a/b
	elif(i == 4):
		a = int(a)
		b = int(b)
		return a//b
	elif(i == 5 or i == 6):
		return a**b
	elif(i == 7):
		return a%b
	else:
		print("Invalid input..")


while (go == True):

	op_counter = 0
	operator = str(input("Enter operator (+, -, *, /, //, ^, **, %): "))
	
	while True:
		try:
			x = float(input("Enter X: "))
			break
		except ValueError:
			print("(Enter a number X)")

	while True:
		try:
			y = float(input("Enter Y: "))
			break
		except ValueError:
			print("(Enter a number Y)")
		


	for i in range(0, 8):
		if(operator == op_choices[i]):
			print("{} {} {} = {}".format(x, operator, y, do_the_math(i, x, y)))
			break
		op_counter = op_counter + 1
		if(op_counter == 7 and operator != op_choices[i]):
			print("Invalid operator: ", operator)

	foo = str(input("\n\n Go again? Y - yes, anything else - no:_"))
	if(foo == "y" or foo == "Y"):
		go = True
	else:
		go = False
