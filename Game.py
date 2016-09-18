from GameNode import GameNode as gn

class Game:
    start = gn("We will ask you to say some things and take some photos along the way.", "./assets/images/a.gif")

    second = gn("Did you know that on average, 10 gallons per day of your water footprint" + 
        " (or 14 percent of your indoor use) is lost to leaks?", "./assets/images/b.gif", 
        start, "Go from start to second!", False)


    end = gn("Thanks for playing our game!", "./assets/images/rome.gif", second, "Exit")
    third = gn("1994 was the year that federally mandated low-flow showerheads, " +
     "faucets, and toilets started to appear on the scene in significant numbers.", 
     "./assets/images/c.gif", start, "Go from start to third. No photo.")


    third.link("Lalalaa", end)

    dummy = gn("nothing here", "./assets/images/lost.gif", end, "Exit")

    # end.link ("But all roads lead to", end)

    def __init__(self):
        print("loaded game")
