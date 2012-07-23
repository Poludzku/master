# -*- coding: utf-8 *-*
from sys import exit

def j_joint():
    print """As you walk trough the flames a man in a read and white robe hands
    you a joint and oreos, how many oreos do you take?
    """

    next = raw_input('> ')
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("WTF, how many oreos do you think there are in heaven!")

    if how_much < 20:
        print "You are a true ganja man"
        exit(0)
    else:
        dead("You are a ganja VETERAN!")


def fire_door():
    print """This door is on fire, you hear coughing and strong laughter
    trough the door."""
    print "How are you going to open the door, the door nob is hot as hell."
    fire_door_open = False

    while True:
        next = raw_input("> ")

        if next == "Man up":
            dead("You burned you hand, idot.")
        elif next == "Kick the door open" and not fire_door_open:
            print """The door is open now,
            you can walk trough the fire LIKE A BAUSE."""
            fire_door_open = True
        elif  next == "Kick the door open" and fire_door_open:
            dead("""WTF you kicking the fire for,
            your foot sets a light and you die""")
        elif next == "WALK TROUGH LIKE A BAUSE" and fire_door_open:
            j_joint()
        else:
            print "WTF you doing?"


def gold_door():
    print "This door is made of solid gold and its kinda warm."
    print """As you open the door you se a long tunel with
    a bright light on the end"""
    print "Do you walk to towards the light or close the door?"

    next = raw_input('> ')

    if "close the door" in next:
        dead("Jesus kicks your ass in to hell")
    elif "walk toward the light" in next:
        dead("""You realize that that the light on the end of
        the tunel is hell, as you turn around you see Jesus shuting the door
        behinde you, on this side of the door you see a troll face
        :D = XD = :P""")
    else:
        gold_door()

def dead(why):
    print why, "/sigh, nice work"
    exit(0)

def start():
    print "You are standing and big white room like the matrix."
    print "There are two doors one big gold and one is set on fire."
    print "Which door do you want to open?"

    next = raw_input("> ")

    if next == "Fire door":
        fire_door()
    elif next == "Gold door":
        gold_door()
    else:
        dead("Your to stupid to open doors, you are stuck in purgotory.")

start()
