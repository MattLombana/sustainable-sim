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
        self.picCount = 1;

        self.camera = capture.start_camera()
        game = g.Game()
        self.curr = game.start
        self.choices = self.curr.getOptions()

        self.label = Label(master, text=self.curr.getText())
        self.label.pack()

        self.B = tkinter.Button(master, text=self.choices[0], command=lambda: self.update(self.choices[0], self.camera))
        self.B.pack()
        self.B2 = tkinter.Button(master, text="Hmm...", command=print("button 2"))
        if (len(self.choices) > 1):
            self.B2 = tkinter.Button(master, text=self.choices[1], command=lambda: self.update(self.choices[1], self.camera))

        self.B2.pack()

        self.img = ImageTk.PhotoImage(self.curr.getImage())
        self.panel = Label(master, image=self.img)
        self.panel.image = self.img
        self.panel.pack()


    def update(self, key, camera):
        """update the image and the buttons to the next node, waiting
        for the camera and happiness judgement to happen if necessary.
        """
        if len(self.choices) == 0:
           capture.stop_camera(camera)
           self.master.destroy()
        if self.label['text'] == "Thanks for playing our game!":
           capture.stop_camera(camera)
           self.master.destroy()

        if (self.B2):
            self.B2['text'] = "Hmm..."
            self.B2['state'] = 'disabled'

        # string: fielname pass into capture
        # also pass it into expression test

        # if canprogress == fasle, the node is expecting a picanalysis
        # runs picanalysis, creates new node. This is run again when getNext returns
        #    self.curr later on.
        print("self.curr.canprogress is " + str(self.curr.canprogress))
        if (not(self.curr.canprogress)):
            print("self.curr.canprogress is " + str(self.curr.canprogress))
            photoname = "Pic" + str(self.picCount) + ".jpg"
            capture.take_photo(camera, photoname)
            self.picCount += 1       
            self.curr.canprogress = isHappyEnough(photoname)
            print("self.curr.canprogress is then " + str(self.curr.canprogress))

        self.curr = self.curr.getNext(key)
        self.choices = self.curr.getOptions()

        self.img = ImageTk.PhotoImage(self.curr.getImage())
        self.panel.configure(image=self.img)
        self.panel.image = self.img

        self.label["text"] = self.curr.getText()


        self.B["text"] = key
        print(key)
        # nextnode = self.curr.getNext(key)
        # choices = list(self.curr.nexts.keys())
        # TODO: if cannot progress:
        #   capture.take_photo(camera)
        
        # is_happy_enough = isHappyEnough(key)

        # # self.curr = nextnode
        # print("something here")

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
