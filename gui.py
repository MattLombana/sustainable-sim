import tkinter
from tkinter import Label
from PIL import ImageTk
import Game as g

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        game = g.Game()
        self.curr = game.start
        choices = list(self.curr.nexts.keys())

        B = tkinter.Button(master, text = choices[0], command = self.update(choices[0]))
        B.pack()
        pic = self.curr.getImage()
        img = ImageTk.PhotoImage(pic)
        label = Label(image=img)
        label.image = img
        label.pack()

    def update(self, key):
        """update the image and the buttons to the next node, waiting
        for the camera and happiness judgement to happen if necessary.
        """

        print("at least i tried")
        nextnode = self.curr.getNext(key)
        choices = list(self.curr.nexts.keys())

        # self.curr = nextnode
        print("something here")

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()