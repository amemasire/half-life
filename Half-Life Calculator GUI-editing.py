__author__ = 'amemasire'

from tkinter import *
 from numpy import *
# from numpy.linalg import *
from cmath import *
from scipy import *


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

missing = Label(bottom, width=12)


def calc():
    a = float(IM.get())
    b = float(TD.get())
    c = float(HL.get())
    d = float(FM.get())
    missing = float()
    res = eval
    return FM

Label(bottom, text=" Missing Value = ").pack(side="left")
missing = Entry(bottom, width=12)
missing.pack(side="left")

main.mainloop()