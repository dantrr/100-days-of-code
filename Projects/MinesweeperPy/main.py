from tkinter import* #imports libraries
import settings
import utils

root = Tk() #runs main window
root.configure(bg="black") #sets background
root.geometry(f"{settings.width}x{settings.height}") #window size width x height, imported from settings file
root.title("Minesweeper Clone") #window title
root.resizable(False, False) #disables resizing if false, for width and height

top_frame = Frame(
    root,
    bg="red",
    width=1440,
    height=180,
) 
top_frame.place(x=0, y=0) #places item at defined pixel location

left_frame = Frame(
    root,
    bg="blue", 
    width=360,
    height=540,
)
left_frame.place(x=0, y=180)

root.mainloop() #all code will be between these root lines.
