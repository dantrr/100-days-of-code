from tkinter import *

class MyApp:

    def __init__(self, root):
        root.title("My app")

        #normally the window will auto size around the widgets, but we can set a specific size w/
        root.geometry("500x400")
        root.maxsize(1000,800)

        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        label.pack()

        #label["text"] = "new label text" # slow way of config
        #label["font"] = ("Courier", 40)
        
        label.configure(text="new label text", font=("Courier", 40)) #quick way of config
        self.entry_text = StringVar() #string var actively stores text in real time
        entry = Entry(root, textvariable=self.entry_text) # this line passes text from an entry line into our stringvar
        entry.pack() # pack of course, packs a widget from top to bottom in order of packing
        
        #label["textvariable"] = entry_text      #this line originally saved text in entry to label in real time.

        button = Button(root, text="Save Text", command=self.press_button)
        button.pack()
        
        self.listItemStrings = ["Hey", "Hi", "Howdy", "HOWDY BITCH"]
        listItems = StringVar(value=self.listItemStrings)
        listbox = Listbox(root, listvariable=listItems)
        listbox.pack()
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))


    def press_button(self):
        print("Button pressed") #this will only print to terminal
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item(self, index):
        selected_item = self.listItemStrings[index[0]]
        print(selected_item)


root = Tk()
MyApp(root)
root.mainloop()


