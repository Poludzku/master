# -*- coding: utf-8 *-*

from WearwolfOasisZone import take_the_shot

from WearwolfOasisZone import wait


def spring_oasis():
    print """The oasis is a big clear pool with many Elks, dears and even none
    hostile bears all shering the same water source, it is prefect harmony.
    you have a perfect shot lined up for a dear do you want to 'take the shot'
    or 'wait'?
    """
    next = raw_input('> ')

    if next == "take the shot":
        take_the_shot()
    elif next == "wait":
        wait()
    else:
        dead("""You are so astaunded by the harmony and beauty you miss your
        chance and return home with no trophy""")

#-----------------------------------------------------------------------------


def mountines():
    print """The mountines are steep and coverd in snow, in the distance you
    can make out what apeers to be a fast moving storm you swear that u can make
    out a voice in the wind but you think its just you imagination."""
    print """Still you need to decide what rout to take, do you go 'furthur up'
    the mountine, walk over to a nerby 'cave' in hope of finding somthing to
    kill or 'give up' on the hunt saying it was stupid to come up here!"""

    next = raw_input('> ')

    if next == "give up":
        give_up()
    elif next == "cave":
        cave()
    elif next == "furthur up":
        up_the_mountine()
    else:
        dead("""You didin't pay attention to your footing, you slip down the
        mountine, cause an avalanche, kill half you village and when you corps
        is found it can bearly be recognised accept for the strange birth mark
        on you ass.""")

#-----------------------------------------------------------------------------


def forest():
    print """The forest is vast and missleading almost like a maze,
    the only way to know where you are is to find key landmarks, you come
    close to the first landmark do you take a right or left?"""

    next = raw_input("> ")

    if next == "left":
        left()
    elif next == "right":
        right()
    else:
        dead("You go of in some strange diraction and cand find your way home")
