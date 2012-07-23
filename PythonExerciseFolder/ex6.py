# -*- coding: utf-8 *-*
# Setting up the strings.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Using strings to make the senteces reapetable and easy to use.
print x
print y

# Printing the string with a Print in front of it.
print "I said: %r." % x
print "I also said: '%s'." % y

# New string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing the new string one after the other.
print joke_evaluation % hilarious

# New string
w = "This is the left side of..."
e = "a string with a right side."

# Printing the new string one after the other.
print w + e

# Using the + combines/adds things together, things like string can be added.
