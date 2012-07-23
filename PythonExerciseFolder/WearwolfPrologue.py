# -*- coding: utf-8 *-*

from WearwolfOutTheDoor import steping_out_the_door




def prologue():
    print """You are a hunter of the wild, you live for the hunt, to kill the
    moste elusive animal the the forest would grant you great honor within your
    tribe."""
    print """All of your tribe agrees that the gratest hunter is Anuk,
    not a man but a beast of the hunt, he lives in the high mountins hunting all
    within the forst bellow."""
    print """No one knows what Anuk actualy is, some say hes a troll like
    creature, some say he a wolf and some say a great bird. Each story potrays
    Anuk as a diffrent animal."""
    print """But Anuk is considerd a hunter and not prey he is repected by all
    tribes of Orsinium, but to be the one to kill Anuks long evaded prey would
    be the gratest honor of all, to prove that you are the singal gratest hunter
    in all of Orsinium. This prey is called Hiracian a dark blue fox."""
    print """It is a fine evening as the hunters blessing rises(The Moon) and
    the sun sets you decide that this is a great night for a hunt.
       _________    ___     ___     _________
      /         \  |   |   |   |   |    _____|
      \___   ___/  |   |   |   |   |   |
          |  |     |   |___|   |   |   |____
          |  |     |    ___    |   |    ____|
          |  |     |   |   |   |   |   |
          |  |     |   |   |   |   |   |_____
          |__|     |___|   |___|   |_________|
  ___     ___     ___     ___     ___     ___    _________
 |   |   |   |   |   |   |   |   |   \   |   |  /         \\
 |   |   |   |   |   |   |   |   |    \  |   |  \___   ___/
 |   |___|   |   |   |   |   |   |     \ |   |      |  |
 |    ___    |   |   |   |   |   |      \|   |      |  |
 |   |   |   |   |   |   |   |   |   |\      |      |  |
 |   |   |   |   |   \___/   |   |   | \     |      |  |
 |___|   |___|    \_________/    |___|  \____|      |__|
"""
    start_game()


def start_game():

    print "Do you want to start?"

    next = raw_input('> ')
    if next == "yes":
        steping_out_the_door()
    else:
        start_game()
