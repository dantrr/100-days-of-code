from tkinter import *

class MyApp:

    def __init__(self, root):
        root.title("My app")

        #normally the window will auto size around the widgets, but we can set a specific size w/
        root.geometry("500x400")
        root.maxsize(1000,800)

        label = Label(root, text="Some label text")
        label.pack()

        #label["text"] = "new label text"
        #label["font"] = ("Courier", 40)
        
        label.configure(text="new label text", font=("Courier", 40))
        entry_text = StringVar()
        entry = Entry(root, textvariable=entry_text) 
        entry.pack()

        label["textvariable"] = entry_text      


root = Tk()
MyApp(root)
root.mainloop()


