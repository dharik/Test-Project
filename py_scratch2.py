#!/usr/bin/python

import sys

# Random function
def Hello(name):
	print 'Hello ' + name,
	# look at the orientation here
	if name == 'Carlos':
		print '- Hey its you!'


# Define a main() function that prints a little greeting.
def main():
	Hello(sys.argv[1])

# Standard boilerplate that calls the main() function.
if __name__== '__main__':
	main()
