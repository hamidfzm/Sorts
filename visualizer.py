__author__ = 'Hamid FzM'

# try:
from Tkinter import *
# from ttk import Frame, Button, Checkbutton, Label, Style
# except ImportError:
#     import tkinter


import Sort
from Windows.diagram import Diagram
import pkgutil
root = Tk()

# style = Style()
# style.theme_use('default')
Label(root, text='Select sort algorithms for comparison:').grid(row=1)

frm_sorts = Frame(root)
lst_sorts = Listbox(frm_sorts, selectmode=MULTIPLE)
scl_sorts = Scrollbar(frm_sorts, orient=VERTICAL)

for sort in Sort.__all__:
    lst_sorts.insert(END, sort.replace('_sort', ''))

lst_sorts.config(yscrollcommand=scl_sorts.set)
scl_sorts.config(command=lst_sorts.yview)

scl_sorts.grid(row=0, column=0, sticky=N+S)
lst_sorts.grid(row=0, column=1)
frm_sorts.grid(sticky=W, padx=5, pady=5)


def compare_cmd():
    global root
    Diagram(root, lst_sorts.curselection())

    # canvas.postscript(file="duck.eps")


frame = Frame(root)
Button(frame, text='Compare', command=compare_cmd).grid(row=0, column=0, sticky=W)
Button(frame, text='About', command=compare_cmd).grid(row=0, column=1, sticky=W)
frame.grid(row=3, pady=5)

root.mainloop()


