# -*- coding: utf-8 *-*


def wait_bear():
    print """You wait for the bear to pass and it seems like you missed your
    best chance but you notice how all the animals stop drinkig simotaniusly.
    A pack of wolves apear and aproach the spring, the other animals step aside
    but i apears its more out of respect then fear or hostilty.
    The wolves make clear path from the forest and escort a small animal.

    ITS HIRACIAN! The legandary blue fox, there is no time to think do you want
    to take the shot as he drinks from the spring? Or let him pass?
    """
    next = raw_input('> ')
    if next == "take the shot":
        take_the_shot_bluefox()
    elif next == "let him pass":
        let_bluefox_pass()
    else:
        print "Quick make your choice you dont have long"
        wait_bear()


def let_bluefox_pass():
    print """You return home with no kill and the faint image of Hiracian
    the blue fox, you regret not taking that shot but seeing him has brought you
    great luck with you other hunts."""
    exit(0)


def take_the_shot_bluefox():
    print """As you take the shot and let go of the bowstring you notice that
    just at the last second Hiracian was not drinking but bowing his head
    towards you out of respect, time feals like it has slown down and you hear
    a voice in your head "Well done hunter!".
    You are not sure how but you are scertine that it was Hiracian himself
    congratulating you.
    In a flash the animals scatter in fear and the spring becomes empty but for
    the dead body of the blue fox. Sudenly you hear a hawk screech in the air
    above and a great black brid swoops down from the sky.
    The bird lands over the body of the blue fox and investigates it, as the
    the bird raises his head to look at you it lets out a deffening screech and
    begines to change slowly becoming a bear. The transformation is horifc but
    facinating, the screech that first sounded like a bird became a bears growl.
    The bear sits down on it behinde nad is siting upright almost like a normal
    person.
    All you can do is stand and watch as you are convinced that this is the end
    for you. You hear a voice in your head "Greatings great hunter! I am Anuk"

    Do you flee? or respond "Greatings great Anuk"?
    """

    next = raw_input()
    if next == "flee":
        flee()
    elif next == "Greatings great Anuk!":
        anuks_gift()
    else:
        print "You are so astounded by Anuks greatness you cant think properly!"
        anuks_gift()
