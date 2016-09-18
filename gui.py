from expressiontest import isHappyEnough
from tkinter import Label
from PIL import ImageTk
import capture
import Game as g
import tkinter


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.camera = capture.start_camera()
        game = g.Game()
        self.curr = game.start
        self.choices = self.curr.getOptions()

        self.B = tkinter.Button(master, text=self.choices[0], command=lambda: self.update(self.choices[0], self.camera))
        self.B.pack()

        self.img = ImageTk.PhotoImage(self.curr.getImage())
        self.panel = Label(master, image=self.img)
        self.panel.image = self.img
        self.panel.pack()


    def update(self, key, camera):
        """update the image and the buttons to the next node, waiting
        for the camera and happiness judgement to happen if necessary.
        """
        self.curr = self.curr.getNext(key)
        self.choices = self.curr.getOptions()

        self.img = ImageTk.PhotoImage(self.curr.getImage())
        self.panel.configure(image=self.img)
        self.panel.image = self.img

        self.B["text"] = key
        print(key)
        # nextnode = self.curr.getNext(key)
        # choices = list(self.curr.nexts.keys())
        # TODO: if cannot progress:
        #   capture.take_photo(camera)
        #if len(choices) == 0:
        #    capture.stop_camera(camera)
        is_happy_enough = isHappyEnough(key)

        # # self.curr = nextnode
        # print("something here")

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
