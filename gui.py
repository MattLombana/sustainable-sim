from expressiontest import isHappyEnough
from tkinter import Label
from PIL import ImageTk
import capture
import Game as g
import tkinter


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sustainable-Sim")
        self.picCount = 1
        self.camera = capture.start_camera()
        game = g.Game()
        self.current = game.start_node
        self.label = Label(master, text=self.current.getPrompt())
        self.B1 = tkinter.Button(master, text=self.current.button_1, command=lambda: self.update(self.current.child_1))
        self.B2 = tkinter.Button(master, text=self.current.button_2, command=lambda: self.update(self.current.child_2))
        self.img = ImageTk.PhotoImage(self.current.getImage())
        self.panel = Label(master, image=self.img)
        self.panel.image = self.img
        self.label.pack()
        self.B1.pack()
        self.B2.pack()
        self.panel.pack()

        if self.current.button_1 == "":
            self.B1['state'] = 'disabled'
        if self.current.button_2 == "":
            self.B2['state'] = 'disabled'

    def update(self, node):
        """update the image and the buttons to the next node, waiting
        for the camera and happiness judgement to happen if necessary.
        """
        if self.current.getPrompt() == "Thanks for playing our game!":
            capture.stop_camera(self.camera)
            self.master.destroy()

        self.label['text'] = node.getPrompt()
        self.B1['text'] = node.button_1
        self.B2['text'] = node.button_2
        if node.button_1 == "":
            self.B1['state'] = 'disabled'
        else:
            self.B1['state'] = 'normal'
        if node.button_2 == "":
            self.B2['state'] = 'disabled'
        else:
            self.B2['state'] = 'normal'
        self.img = ImageTk.PhotoImage(node.getImage())
        self.panel.configure(image=self.img)
        self.panel.image = self.img
        self.current = node
        node.child_1.createTree()
        node.child_2.createTree()

        # nextnode = self.curr.getNext(key)
        # choices = list(self.curr.nexts.keys())
        # TODO: if cannot progress:
        #   capture.take_photo(camera)

        # is_happy_enough = isHappyEnough(key)

        # # self.curr = nextnode
        # print("something here")
        # print("self.curr.canprogress is " + str(self.curr.canprogress))


        # if (not(self.curr.canprogress)):
            # print("self.curr.canprogress is " + str(self.curr.canprogress))
            # photoname = "Pic" + str(self.picCount) + ".jpg"
            # capture.take_photo(camera, photoname)
            # self.picCount += 1
            # self.curr.canprogress = isHappyEnough(photoname)
            # print("self.curr.canprogress is then " + str(self.curr.canprogress))

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
