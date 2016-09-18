from PIL import Image
from strings import *
from utils.conf import node_map as nm


class GameNode:
    'Common base class for all employees'


    def __init__(self, prompt="", image="assets/images/lost.gif", button_1="", child_1=None, button_2="", child_2=None, can_progress=True):
        """Creates a new scene w/ image, text, and (optionally) next node"""
        self.prompt = prompt
        self.image = Image.open(image)
        self.button_1 = button_1
        self.child_1 = child_1
        self.button_2 = button_2
        self.child_2 = child_2
        self.prompt = prompt
        self.nexts = {}
        self.can_progress = can_progress

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


    def createTree(self):
        if self.button_1 == "" and self.button_2 == "":
            pass
        print("\n\n\n\n\nnode button 1: {}".format(self.button_1))
        print("node button 2: s{}e".format(self.button_2))

        prompt_1 = eval(nm['{}'.format(self.button_1)]['prompt'])
        print("prompt 1 is: {}".format(prompt_1))
        prompt_2 = eval(nm['{}'.format(self.button_2)]['prompt'])
        print("prompt 2 is: {}".format(prompt_2))
        image_1 = "./assets/images/" + nm['{}'.format(self.button_1)]['image']
        print("IMage 1 is: {}".format(image_1))
        image_2 = "./assets/images/" + nm['{}'.format(self.button_2)]['image']
        print("IMage 2 is: {}".format(image_2))
        child_1_button_1 = eval(nm['{}'.format(self.button_1)]['child_button_name_1'])
        print(child_1_button_1)
        child_1_button_2 = eval(nm['{}'.format(self.button_1)]['child_button_name_2'])
        print(child_1_button_2)
        child_2_button_1 = eval(nm['{}'.format(self.button_2)]['child_button_name_1'])
        print(child_2_button_1)
        child_2_button_2 = eval(nm['{}'.format(self.button_2)]['child_button_name_2'])
        print(child_2_button_2)
        picture_1 = nm['{}'.format(self.button_1)]['take_photo']
        picture_2 = nm['{}'.format(self.button_2)]['take_photo']

        print("creating GameNode for {}".format(prompt_1))
        print("creating GameNode for {}".format(prompt_2))
        child_node_1 = GameNode(prompt=prompt_1, image=image_1, button_1=child_1_button_1, child_1=None, button_2=child_1_button_2, child_2=None, can_progress=picture_1)

        child_node_2 = GameNode(prompt=prompt_2, image=image_2, button_1=child_2_button_1, child_1=None, button_2=child_2_button_2, child_2=None, can_progress=picture_2)

        self.child_1 = child_node_1
        self.child_2 = child_node_2
        self.setChildren()
