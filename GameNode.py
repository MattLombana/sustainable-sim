from PIL import Image


class GameNode:
    'Common base class for all employees'


    def __init__(self, prompt="", image="assets/images/lost.gif", button_1="", child_1=None, button_2="", child_2=None, canprogress=True):
        """Creates a new scene w/ image, text, and (optionally) next node"""
        self.prompt = prompt
        self.image = Image.open(image)
        self.button_1 = button_1
        self.child_1 = child_1
        self.button_2 = button_2
        self.child_2 = child_2
        self.prompt = prompt
        self.nexts = {}
        self.canprogress = canprogress
        self.setChildren()


    def getOptions(self):
        """Gets all possible choices that the player can choose"""
        return list(self.nexts.keys())


    def getImage(self):
        return self.image


    def getPrompt(self):
        return self.prompt


    def getNext(self, key):
        """Returns next scene, given that the player chose "key" """
        if self.canprogress:
            if key in self.nexts:
                return self.nexts[key]
            else:
                print ("Can't find the next page!")
                return GameNode("Sorry, how did you end up here?", "lost.gif")
        else:
            self.text = self.text + "\nOh no, Player! Are you really sure you mean that? You're not really smiling."
        return self


    def link(self, key, newnode):
        """Links self to point to newnode, if you choose option "key" """
        self.nexts[key] = newnode


    def setChildren(self):
        if ((self.child_1 is not None) and (self.button_1 != "")):
            self.link(self.button_1, self.child_1)
        if ((self.child_2 is not None) and (self.button_2 != "")):
            self.link(self.button_2, self.child_2)
