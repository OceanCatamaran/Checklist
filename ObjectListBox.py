from tkinter import *
from sizeableList import SizeableList

class ObjectListBox:

    def __init__(self, root, size = 0, yscrollcommand = None):
        self._root = root
        if yscrollcommand != None:
            self._LBObj = Listbox(self._root, yscrollcommand = yscrollcommand)
        else:
            self._LBObj = Listbox(self._root)
        self._slObj = SizeableList(size)
        if size != 0:
            self._refresh()

            

    def _refresh(self):
        #Refreshes the Listbox widget display
        self._LBObj.delete(0,END)
        self._LBObj.insert(END, *self._slObj.getList())

    def insertAt(self, index, value):
        #Inserts entry at selected spot.
        #Note, you must first type in entry, select line you want to modify,
        #then hit the select button. Otherwise, it will modify the last selected item
        # or the first item in the Listbox.
        self._slObj.insertAt(index, value)
        self._refresh()

    def setSize(self, size):
        self._slObj.setSize(size)
        self._refresh()

    def increment(self):
        incrementedSize = len(self._slObj.getList()) + 1
        self._slObj.setSize(incrementedSize)
        self._refresh()

    def decrement(self):
        decrementedSize = len(self._slObj.getList()) - 1
        self._slObj.setSize(decrementedSize)
        self._refresh()

    #The remaining methods are to facilitate some of Listboxe's built in functionalities.

    def selection(self):
        return self._LBObj.curselection()

    def get(self, index):
        return (self._LBObj.get(index), self._slObj.getList()[index])

    def pack(self):
        self._LBObj.pack()

    def yview(self):
        return self._LBObj.yview

top = Tk()

scrollbar = Scrollbar(top)
scrollbar.pack(side = RIGHT, fill = Y)

OLB1 = ObjectListBox(top, 5, yscrollcommand = scrollbar.set)

entryObj = Entry(top)


def selectCallBack():
    selection = OLB1.selection()
    if len(selection) == 0:
        selection = None
    #.get only retrieves the selected line in the Listbox, and its parallel in
    # the sizeableList object.
    if selection != None:
        OLB1.insertAt(selection[0], entryObj.get())
        print(OLB1.get(selection[0]))

def decrementCallBack():
    OLB1.decrement()

def incrementCallBack():
    OLB1.increment()
    
  
b1 = Button(top, text = "select", command = selectCallBack)

frameObj = Frame(top)
leftB = Button(frameObj, text = "-", command = decrementCallBack)
rightB = Button(frameObj, text = "+", command = incrementCallBack)
leftB.pack(side = LEFT, fill = X)
rightB.pack(side = RIGHT, fill = X)


OLB1.pack()
scrollbar.config(command = OLB1.yview())
b1.pack()
entryObj.pack()
frameObj.pack(fill = X)
top.mainloop()
