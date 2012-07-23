# -*- coding: utf-8 *-*
from sys import argv

script, one, two, three, four = argv

print "The script", script
print 'says"', one
print "can", two
print "in", three
print "you", four, '".'

thoughts_about_this = raw_input("Who do you think I am?")

print "So you think I am %r!" % (thoughts_about_this)
