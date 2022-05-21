import tkinter as tk
import time as t
import threading as th

count = 0
autoClicker = 0
autoClickPrice = 20


def addcookie():
    global count, sent
    count += 1
    sent = "You own " + str(count) + " cookies"
    c['text'] = sent


def addClicker():
    global autoClickPrice, count, autoClicker
    if count >= autoClickPrice:
        count -= autoClickPrice
        autoClickPrice += 10
        autoClicker += 1
        sent = "You own " + str(autoClicker) + " AutoClickers"
        cursor['text'] = sent
        btn2['text'] = "Buy AutoClicker " + "Price:" + str(autoClickPrice)
        sent = "You own " + str(count) + " cookies"
        c['text'] = sent
    else:
        btn2['text'] = "Not enough cookies!"
        t.sleep(1)
        btn2['text'] = "Buy AutoClicker " + "Price:" + str(autoClickPrice)
        sent = "You own " + str(count) + " cookies"
        c['text'] = sent

def Ccheck():
    while True:
        t.sleep(1)
        for i in range(autoClicker):
            addcookie()


t1 = th.Thread(target=Ccheck)
t1.start()

root = tk.Tk()
root.title("Cookie Clicker Clone")
root.geometry('300x300')

btn = tk.Button(root, text="Press for Cookies", width=30, height=2, bg='brown', command=addcookie)
btn.place(x=0, y=0)

btn2 = tk.Button(root, text="Buy AutoClicker " + "Price:20", width=30, height=2, command=addClicker)
btn2.place(x=0, y=0)

c = tk.Label(root, text="You own 0 cookies")
cursor = tk.Label(root, text="You own 0 Autoclickers")
skipline = tk.Label(root, text=" ")

btn.pack()
c.pack()
skipline.pack()
btn2.pack()
cursor.pack()

root.mainloop()