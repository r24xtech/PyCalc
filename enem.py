print("|| Welcome to ENEM_Calculator ||\n")

all_weights = {}
all_grades = {}
counter = 0
total_weight = 0

def get_weights(topic):
	global counter, total_weight
	while True:
		try:
			weight = float(input(f"Enter weight for {topic}: "))
			all_weights[topic] = weight
			counter += 1
			total_weight += weight
			return
		except ValueError:
			print("Please enter a valid weight.")

def get_grades(topic):
	while True:
		try:
			grade = float(input(f"Enter {topic} grade: "))
			if grade > 0 and grade <= 1000:
				all_grades[topic] = grade
				return
		except ValueError:
			pass
		print("Please enter a grade between 0 and 1000.")

def do_the_math():
	total = 0
	total += all_weights["reda"] * all_grades["reda"]
	total += all_weights["math"] * all_grades["math"]
	total += all_weights["ling"] * all_grades["ling"]
	total += all_weights["huma"] * all_grades["huma"]
	total += all_weights["natu"] * all_grades["natu"]
	total = total/10
	return total

def main():
	global counter, total_weight
	while True:
		get_weights("reda")
		get_weights("math")
		get_weights("ling")
		get_weights("huma")
		get_weights("natu")
		if counter == 5 and total_weight == 10:
			break
		elif counter == 5 and total_weight != 10:
			print("Invalid sum of weights. Sum must be 10.")
			#all_weights.clear() ## removes all keys from dictionary
			counter = 0
			total_weight = 0
		else:
			pass
	print("\n")
	get_grades("reda")
	get_grades("math")
	get_grades("ling")
	get_grades("huma")
	get_grades("natu")

main()
final_grade = do_the_math()
print(f"\nYour final grade is: {final_grade}")
