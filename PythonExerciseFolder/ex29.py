# -*- coding: utf-8 *-*
people = 20
cats = 30
dogs = 15


if people < cats:
    print "To many cats the world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater then or equal to dogs."

if people <= dogs:
    print "People are less then or equal to dogs"


if people == dogs:
    print "People are dogs"
