# -*- coding: utf-8 *-*

from WearwolfZones import mountines

from WearwolfZones import spring_oasis

from WearwolfZones import forest

def steping_out_the_door():
    print """As you take a step out the door the fresh air fills your lungs,
    you can feel that tonight it will be a good kill, but where will you hunt?
    In the mountines which Anuk calls his home and the moste elite predators
    reside, the well spring oasis where many fine elks make there wattering hole
    or the forest benethe the mountines where old hunters claim they have seen
    the mystical blue fox"""

    next = raw_input('> ')
    if next == "mountines":
        mountines()
    elif next == "spring oasis":
        spring_oasis()
    elif next == "forest":
        forest()
    else:
        print """You can go hunt in the 'mountines', the great forest or the
        spring_oasis"""
        steping_out_the_door()

