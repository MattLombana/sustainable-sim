from GameNode import GameNode as gn

class Game:
    end = gn("Thanks for playing our game!", "./assets/images/rome.gif")
    start = gn("This should be the first panel.", "./assets/images/a.gif")

    second = gn("You are being asked to take a photo right now", "./assets/images/b.gif", start, "Go from statrt to second.", False)
    second.link( "But all roads lead to", end)
    third = gn("The option without the photo", "./assets/images/c.gif", start, "Go from start to third. No photo.")
     

    fourth = gn("another", "./assets/images/a.gif")
    fifth = gn("asdf", "./assets/images/a.gif")
    sixth = gn("23f3f", "./assets/images/a.gif")
    seventh = gn("anasdfsdfother", "./assets/images/a.gif")
    eighth = gn("gwg23g", "./assets/images/a.gif")

    third.link("3-4", fourth)
    fourth.link("4-5", fifth)
    fifth.link("5-6", sixth)
    sixth.link("6-7", seventh)
    seventh.link("7-8", eighth)


    
    
    eighth.link("But all roads lead to", end)
    dummy = gn("nothing here", "./assets/images/lost.gif", end, "Go to the deadone")

    # end.link ("But all roads lead to", end)

    def __init__(self):
        print("loaded game")
