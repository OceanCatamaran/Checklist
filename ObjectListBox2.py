from tkinter import *
from sizeableList import SizeableList
from EntryReader import EntryReader

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

    def increment(self, erValue = 1):
        incrementedSize = len(self._slObj.getList()) + erValue
        self._slObj.setSize(incrementedSize)
        self._refresh()

    def decrement(self, erValue = 1):
        decrementedSize = len(self._slObj.getList()) - erValue
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
top.geometry("600x600")

viewport = Frame(top, width = 40, height = 20)


scrollbar = Scrollbar(viewport)
scrollbar.pack(side = RIGHT, fill = Y)

OLB1 = ObjectListBox(viewport, 5, yscrollcommand = scrollbar.set)
OLB1.pack()

entryObj = Entry(top, width = 20)
numEntryObj = Entry(top, width = 5)
erObj = EntryReader(numEntryObj)

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
    OLB1.decrement(erObj.getNumber())

def incrementCallBack():
    OLB1.increment(erObj.getNumber())

#mouseCallback taken from this site...
#Link: https://www.tutorialspoint.com/mouse-position-in-python-tkinter   
def mouseCallBack(e):
#Helps in placement of widget
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
#top.bind('<Motion>',mouseCallBack)  
  
b1 = Button(top, text = "set", command = selectCallBack, width = 5, height = 2)

leftB = Button(top, text = "-", command = decrementCallBack, width = 2, height = 3)
rightB = Button(top, text = "+", command = incrementCallBack, width = 2, height = 3)
leftB.place(x = 0, y = 195)
rightB.place(x = 100, y = 195)

viewport.place(x = 0, y = 0)

scrollbar.config(command = OLB1.yview())
b1.place(x = 125, y = 162)
entryObj.place(x = 0, y = 160)
numEntryObj.place(x = 45, y = 215)
top.mainloop()
