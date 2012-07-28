# -*- coding: utf-8 *-*

from WearwolfOasisBlueFox import wait_bear


def take_the_shot():

    print"""
    You take the shot and kill the dear. You return to the village
    with a kill but its nothing impresive, you marry and live a deacent life.
    """

    exit(0)


def wait():
    print """
    You wait and the animlas move around, now you have a perfect shot
    lined up for a alpha elk, this is a fine and majestic creature it will
    certinly be respected as a fine kill if it is quick.
    """
    print """So do you want to 'take the shot' or 'wait'?
    """

    next = raw_input('> ')
    if next == "take the shot":
        take_the_shot_elk()
    elif next == "wait":
        wait_elk()
    else:
        wait()

def take_the_shot_elk():
    print """
    You take the shot and hit the elk right in the head, the elk
    simply falls over and dies, the animals scater and you go and colect your
    prize. You return to the vilage with a fine kill and are respected by your
    tribe, the warchife makes blood ties with you and makes you his hunting
    brother, when the warchief dies you will be the next warchief.
    Your life is long and prospures.
    """
    exit(0)


def wait_elk():
    print """The elk moves along you now have a perfect clear shot at a bear
    den mother, this is a very dengerous animal and can only be killed by a
    clean shot to the head.

    Do you want to 'take the shot' or 'wait'?
    """
    next = raw_input('> ')
    if next == "take the shot":
        take_the_shot_bear()
    elif next == "wait":
        wait_bear()
    else:
        wait_elk()


def take_the_shot_bear():
    print """You take the shot and kill the den mother with on shot but her
    cubs and other bears attack you. You take down a few bears but they
    eventualy overwhelm you and kill you."""
    exit(0)
