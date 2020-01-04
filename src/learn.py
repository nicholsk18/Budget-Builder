from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)
        print(self)
        exitButton = Button(self, text="Button", fg="#ff00ff", command=self.clickExitButton)

        exitButton.place(x=200, y=200)

    def clickExitButton(self):
        exit()


root = Tk()
app = Window(root)

root.wm_title("Tkinter window")
root.geometry("750x750")
root.mainloop()