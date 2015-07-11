__author__ = 'amemasire'

from tkinter import *

swagbase = Tk()
up = Frame(swagbase); up.pack()
down = Frame(swagbase); down.pack()

Label(up, text="What Do You Want To Find Today?").pack(side="left")
HalfLife = Button(down, width=12, text="The Half-Life")
HalfLife.pack(side='left')

InitialMass = Button(down, width=12, text="The Initial Mass")
InitialMass.pack(side='left')

FinalMass = Button(down, width=12, text="The Final Mass")
FinalMass.pack(side='left')

TimePeriod = Button(down, width=12, text="The Time Period")
TimePeriod.pack(side='left')

swagbase.mainloop()