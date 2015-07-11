from tkinter import *
from math import *

root = Tk()
top = Frame(root); top.pack()
Label(top, text='Define f(x):').pack(side='left')

f_entry = Entry(top, width=12)
f_entry.pack(side='left')
f_entry.insert('end', 'x')

Label(top, text='  x =').pack(side='left')
x_entry = Entry(top, width=6)
x_entry.pack(side='left')
x_entry.insert('end', '0')

s_label = Label(top, width=9)

def calc(event=None):
    f_txt = f_entry.get()
    x = float(x_entry.get())
    res = eval(f_txt)
    global s_label
    s_label.configure(text='%g' % res)   # display f(x) value

x_entry.bind('<Return>', calc)
Button(top, text='  f = ', relief='flat',command=calc).pack(side='left')
s_label.pack(side='left')

def quit(event=None): root.quit()
root.bind('<q>', quit)
root.mainloop()