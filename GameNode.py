from PIL import Image

class GameNode:
   'Common base class for all employees'

   def __init__(self, text, image, parent=None, key=None, canprogress=True):
      """Creates a new scene w/ image, text, and (optionally) next node"""
      self.image = Image.open(image)
      self.text = text
      self.nexts = {}
      if (parent):
         parent.link(key, self)
      self.canprogress = canprogress

   def getOptions(self):
      """Gets all possible choices that the player can choose"""
      return list(self.nexts.keys())

   def getImage(self):
      return self.image

   def getText(self):
      return self.text

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
