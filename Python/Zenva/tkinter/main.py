from tkinter import *

class MyApp:

    def __init__(self, root):
        root.title("My app")

        #normally the window will auto size around the widgets, but we can set a specific size w/
        root.geometry("500x400")
        root.maxsize(1000,800)

root = Tk()
MyApp(root)
root.mainloop()


