print("|| Welcome to PyCalc ||")
print("1-Add; 2-Subtract; 3-Multiply; 4-Divide; 5-End \n\n")

def check_option():
	while True:
		try:
			option = int(input("Enter your option: "))
			if(type(option) == int and option > 0 and option < 6):
				return option
		except ValueError:
			pass
		print("Enter a valid option. ")

def get_values():
	while True:
		try:
			x = float(input("Enter X: "))
			y = float(input("Enter Y: "))
			if(type(x) == float or type(x) == int):
				if(type(y) == float or type(y) == int):
					return x, y
		except ValueError:
			pass
		print("Enter a valid value. ")


def add(x, y):
	print(f"\n{x} + {y} = {x+y}\n")

def sub(x, y):
	print(f"\n{x} - {y} = {x-y}\n")

def mul(x, y):
	print(f"\n{x} x {y} = {x*y}\n")

def div(x, y):
	if y == 0:
		print("Can't divide by zero.")
	else:
		print(f"\n{x} / {y} = {x/y}\n")


while True:
	choice = check_option()
	if choice == 5:
		break
	a, b = get_values()
	if choice == 1:
		add(a, b)
	elif choice == 2:
		sub(a, b)
	elif choice == 3:
		mul(a, b)
	elif choice == 4:
		div(a, b)