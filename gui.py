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
        self.choices = self.curr.getOptions()

        self.B = tkinter.Button(master, text=self.choices[0], command=lambda: self.update(self.choices[0]))
        self.B.pack()

        self.img = ImageTk.PhotoImage(self.curr.getImage())
        self.panel = Label(image=self.img)
        self.panel.image = self.img
        self.panel.pack()

    def update(self, key):
        """update the image and the buttons to the next node, waiting
        for the camera and happiness judgement to happen if necessary.
        """
        self.curr = self.curr.getNext(key)
        self.choices = self.curr.getOptions()

        img2 = ImageTk.PhotoImage(self.curr.getImage())
        self.panel.configure(image = img2)
        self.panel.image = self.img

        self.B["text"] = key
        print(key)
        # nextnode = self.curr.getNext(key)
        # choices = list(self.curr.nexts.keys())

        # # self.curr = nextnode
        # print("something here")

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()