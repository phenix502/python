#! C:/Python33
import sys
import codecs

def Cat(filename):
	f = codecs.open(filename, 'r','utf-8')
	text = f.read()
	print(text)
	f.close()



# Define a main() function that prints a little greeting.

def main():
	Cat(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()