# -*- coding: utf-8 *-*
def anuks_gift():
    print """Well met hunter, I see that you have taken my kill. Well done,
    you have proved that you are a great hunter and worthy of my gift!
    Now preaper to feel my gift in your vains. To feel my blood in you and
    bask in the thrill of the blood moon!"""
    print"""Do you accept Anuks gift?"""

    next = raw_input('> ')
    if next == "yes":
        anuks_gift_yes()
    elif next == "no":
        anuks_gift_no()
    else:
        anuks_gift()


def anuks_gift_yes():
    print """Preper hunter.
    'Anuk morphs into a wolf and charges at you, starteld you cower as Anuk
    charges at you then leeps and bites you on the sholder, he then runs of
    in the direction of the mountines and howls to the moon.
    As you look up at the moon you feel as if it is pulsing with the same rythem
    as your heart, the moon then starts to bleed from the center as you feel a
    burst of adrenalin. You feel youre muscels expand and you jaw extend as you
    begin to hunger. The moon now is compleatly red and you have stoped growing,
    you look at the reflection of youre new gift in the pool next to the blue
    foxes body. You howl at the blood moon as you know it is time to hunt.'"""
