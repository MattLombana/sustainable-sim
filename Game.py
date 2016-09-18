from GameNode import GameNode as gn


class Game:
    end_node = gn("Thanks for playing our game!", "./assets/images/rome.gif")
    bad_ending_node = gn("Unfortunately, that was a bad choice. Better luck next time!", "./assets/images/pme.jpg", "End Game", end_node)

    #after_look_up = gn('after_look_up prompt', "./assets/images/b.gif")

    look_up = gn("Alex: Oh hey, what are you doing after school?", "./assets/images/02-hialex.jpg", "Nothing, I'm free tonight!", None, "I'm hanging out with Eve.", None)

    desk_node = gn("?: Hey, you!", "./assets/images/01-heyyou.jpg", "What?", look_up)

    start_node = gn("Thanks for taking a look at our project.", "./assets/images/00-instr.jpg", "Lets Get Going!", desk_node)



    # second = gn("You are being asked to take a photo right now", "./assets/images/b.gif", start, "Go from statrt to second.", False)
    # second.link("But all roads lead to", end)
    # third = gn("The option without the photo", "./assets/images/c.gif", start, "Go from start to third. No photo.")


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




    # eighth.link("But all roads lead to", end)
    # dummy = gn("nothing here", "./assets/images/lost.gif", end, "Go to the deadone")

    # end.link ("But all roads lead to", end)

    def __init__(self):
        print("loaded game")
