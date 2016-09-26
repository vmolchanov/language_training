import os
import random


def clear_screen():
	os.system("clear")


def get_path():
	""" Get the file path from the user """

	path = ""

	while True:
		path = input("Enter file name of dictionary: ")
		path = os.getcwd() + "/dictionaries/" + path
		if os.path.isfile(path):
			break
		else:
			print("File is not find!")

	return path


def read_file(path):
	""" Read file in format: word$translation """

	curr_dict = {}	

	with open(path, "r") as fin:
		for line in fin:
			line = line.strip()
			word1 = line[:line.find("$")].lower()
			word2 = line[line.find("$") + 1:].lower()
			curr_dict[word1] = word2

	return curr_dict


def print_dictionary(dictionary):
	counter = 1
	for word in dictionary:
		print(str(counter) + ". " + word + " - " + dictionary[word])
		counter += 1


def get_words(dictionary):
	words_rand = []
	for word in dictionary:
		words_rand.append(word)
	return words_rand


def showAvailableDictionary():
	path = os.getcwd() + "/dictionaries/"
	files = os.listdir(path)
	print("Available dictionaries:")
	for dictionary in files:
		print("\t" + dictionary)
	print()


def training(dictionary, words_rand):
	true_answers = 0
	false_answers = 0
	while True:
		iword = random.randrange(len(words_rand))
		print(dictionary[words_rand[iword]])
		answer = input("> ")

		if answer == "\exit":
			break
		elif answer == "\show":
			print_dictionary(dictionary)
		elif answer == "\stat":
			clear_screen()
			print("Right answers:", true_answers)
			print("Wrong answers:", false_answers)
		elif answer == "\chdict":
			showAvailableDictionary()
			path = get_path()
			clear_screen()
			dictionary = read_file(path)
			print_dictionary(dictionary)			
			words_rand = get_words(dictionary)
		elif answer == "\help":
			print("\\exit - close the application")
			print("\\show - print the dictionary on the screen")
			print("\\stat - print statistic on the screen")
			print("\\chdict - change dictionary")
		elif answer.lower() in dictionary and dictionary[answer.lower()] == dictionary[words_rand[iword]]:
			print("It's right")
			true_answers += 1
		else:
			print("It's wrong")
			print(words_rand[iword])
			false_answers += 1

		input("Press <Enter> to continue")
		clear_screen()


def main():
	""" Basic function """

	showAvailableDictionary()

	path = get_path()
	clear_screen()
	dictionary = read_file(path)
	print_dictionary(dictionary)
	input("Press <Enter> to continue")
	clear_screen()

	# List with the words for random generation from hash-table
	words_rand = get_words(dictionary)

	training(dictionary, words_rand)


if __name__ == "__main__":
	main()
