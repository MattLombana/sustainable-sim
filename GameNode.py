from PIL import Image

class GameNode:
   'Common base class for all employees'

   def __init__(self, text, image, parent=None, key=None):
      """Creates a new scene w/ image, text, and (optionally) next node"""
      self.image = Image.open(image)
      self.text = "Alex: The text that will be displayed, M-kun."
      self.nexts = {}
      if (parent):
         parent.link(key, self)

   def getOptions(self):
      """Gets all possible choices that the player can choose"""
      return list(self.nexts.keys())

   def getImage(self):
      return self.image

   def getText(self):
      return self.text

   def getNext(self, key):
      """Returns next scene, given that the player chose "key" """
      if key in self.nexts:
         return self.nexts[key]
      else:
         print ("Can't find the next page!")
         return GameNode("Sorry, how did you end up here?", "lost.gif")

   def link(self, key, newnode):
      """Links self to point to newnode, if you choose option "key" """
      self.nexts[key] = newnode
