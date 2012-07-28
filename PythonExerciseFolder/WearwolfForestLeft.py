# -*- coding: utf-8 *-*


def wolf_follow():
    print """You stalk the wolf for sometime and you encroach on its dean, the
    wolf was bringing food to her pups, you have a pearfect shot do you
    'take it' or 'let it go'."""

    next = raw_input('> ')
    if next == "take it":
        take_it()
    elif next == "let it go":
        let_it_go()
    else:
        wolf_follow


def take_it():
    print """While you preper to take the shot a white wolf attacks you from
    behinde while you were stalking youre pray a hunter from the mountines had
    been stalking you."""
    exit(0)


def let_it_go():
    print """You turn around and see a white wolf behinde you, it had been
    stalking you, the wolf bows in respect and walks on. You return home and
    think alot about what you had expirienced, finally you decide to talk to
    youre tribes far-seer and after a while he apoints you a shaman of the
    village. After you become a well expirenced shaman you can call the wolf
    and spend many nights talking to him. """
exit(0)
