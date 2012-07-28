# -*- coding: utf-8 *-*
from WearwolfForestLeft import wolf_follow

from WearwolfForestLeft import deer_follow


def left():
    print """You chose to go left and spoted a white wolf, there are dear
    furthur of in the distance which do  want to stalk, the 'wolf' will be very
    hard to and is likel to be trecking back to the mountin wich will be very
    dangerus. The deer will be a fine kill and should be relativly easy to
    follow."""
    print "Wich do you fillow, 'wolf' or 'deer'."

    next = raw_input('> ')
    if next == "wolf":
        wolf_follow()
    elif next == "deer":
        deer_follow()
    else:
        print "Make your choice."


def right():
    print "In the distance you see the a pack of wolf escorting a blue fox."
    print """You try to get the high ground, you see a little hill that will be
    a great vanteg point, but it is very open, do you want to 'go for it' or 'go
    back' to the village."""

    next = raw_input('> ')
    if next == "go back":
        go_back()
    elif next == "go for it":
        go_for_it()
    else:
        print "So do you want to 'go for it' or 'go back'?"
        right()


def go_back():
    print """You go back to the village and tell all what you had seen. You
    grow old and become an old man who allways tells the story of how he saw
    the blue fox."""
    exit(0)


def go_for_it():
    print """As you walk up to the hill you look back and all you see is a wihte
    flash, that was the last thing you ever sore in this world, that and you
    heard a wolf growl."""
