import sys
import codecs

def Cat(filename):
	f = codecs.open(filename, 'r','utf-8')
	for line in f:
		print(line)

	f.close()
# Define a main() function that prints a little greeting.

def Hello(name):
	name = name + "!!!!!!!"
	print('Hello',name)
def main():
	#Cat(sys.argv[1])
	Hello(sys.argv[1])
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()