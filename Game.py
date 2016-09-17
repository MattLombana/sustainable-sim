from GameNode import GameNode as gn

class Game:
    start = gn("first thing", "a.gif")
    # second = gn("second thing", "b.gif", start, "tob")
    third = gn("also off the first thing", "c.gif", start, "toc")
    end = gn("rome", "rome.gif")

    fourth = gn("another", "a.gif")
    fifth = gn("asdf", "a.gif")
    sixth = gn("23f3f", "a.gif")
    seventh = gn("anasdfsdfother", "a.gif")
    eighth = gn("gwg23g", "a.gif")

    third.link("3-4", fourth)
    fourth.link("4-5", fifth)
    fifth.link("5-6", sixth)
    sixth.link("6-7", seventh)
    seventh.link("7-8", eighth)

    # second.link( "But all roads lead to", end)
    eighth.link("But all roads lead to", end)

    def __init__(self):
        print("loaded game")