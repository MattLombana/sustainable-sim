from GameNode import GameNode as gn

class Game:
    start = gn("first thing", "./assets/images/a.gif")
    second = gn("second thing", "./assets/images/b.gif", start, "tob", False)
    # third = gn("also off the first thing", "./assets/images/c.gif", start, "toc")
    end = gn("rome", "./assets/images/rome.gif")

    # fourth = gn("another", "./assets/images/a.gif")
    # fifth = gn("asdf", "./assets/images/a.gif")
    # sixth = gn("23f3f", "./assets/images/a.gif")
    # seventh = gn("anasdfsdfother", "./assets/images/a.gif")
    # eighth = gn("gwg23g", "./assets/images/a.gif")

    # third.link("3-4", fourth)
    # fourth.link("4-5", fifth)
    # fifth.link("5-6", sixth)
    # sixth.link("6-7", seventh)
    # seventh.link("7-8", eighth)

    second.link( "But all roads lead to", end)
    # eighth.link("But all roads lead to", end)
    # end.link ("But all roads lead to", end)

    def __init__(self):
        print("loaded game")
