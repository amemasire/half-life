__author__ = 'amemasire'

from tkinter import *
# from numpy import *
# from numpy.linalg import *
import cmath


main = Tk()
top = Frame(main); top.pack()
bottom = Frame(main); bottom.pack()

Label(top, text="Initial Mass:").pack(side="left")
IM = Entry(top, width=12)
IM.pack(side='left')

Label(top, text="Final Mass:").pack(side="left")
FM = Entry(top, width=12)
FM.pack(side="left")

Label(top, text="Time Duration:").pack(side="left")
TD = Entry(top, width=12)
TD.pack(side="left")

Label(top, text="Half-Life:").pack(side="left")
HL = Entry(top, width=12)
HL.pack(side="left")


def calc(event=None):
    a = float(IM.get())
    b = float(TD.get())
    c = float(HL.get())
    d = float(FM.get())
    e = float()
    global e
    fm = solve((IM / (TD / HL) ** 2))
    return FM

Label(bottom, text=" Missing Value = ").pack(side="left")
e = Entry(bottom, width=12)
e.pack(side="left")



main.mainloop()