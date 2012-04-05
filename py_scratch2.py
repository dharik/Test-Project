#!/usr/bin/python
import sys
from sys import stderr,stdout,argv,exit

# Random function
def Hello(name):
	print 'Hello ' + name,
	# look at the orientation here
	if name == 'Carlos':
		print '- Hey its you!'


# Define a main() function that prints a little greeting.
def main():
	if len(argv) != 2:
		stderr.write("Usage: py_scratch2.py STRING\n")
		exit(1)
	Hello(sys.argv[1])

# Standard boilerplate that calls the main() function.
if __name__== '__main__':
	main()
