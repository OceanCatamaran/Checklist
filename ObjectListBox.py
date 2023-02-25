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

    def overWriteWith(self, values):
        self._slObj.overWriteWith(values)
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

    def getList(self):
        return self._slObj.getList()

    def pack(self):
        self._LBObj.pack()

    def yview(self):
        return self._LBObj.yview
