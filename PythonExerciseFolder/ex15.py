# -*- coding: utf-8 *-*
# This imports dickhead
from sys import argv

# This is the argument
script, filename = argv

# Command to open the specifice file of you choice
txt = open(filename)

# The print that prompts and asks the qoestion
print "Here's your file %r:" % filename
# Printing of the file of choice
print txt.read()

# Print reasking to opne the file agien
print "Type the filename agein:"
# The raw input that lets you specify the file you want open
file_agein = ("> ")

# Reopening the same file
txt_agein = open(file_agein)

# The txt from inside the file printed.
print txt_agein.read()
