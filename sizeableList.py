from tkinter import *

class SizeableList:

    def __init__(self, size):
        self._list = []
        if size < 0: raise ValueError("Size value cannot be < 0")
        for i in range(size):
            self._list.append("_")

    def __str__(self):
        return str(self._list)
        
    def __len__(self):
        return len(self._list)

    def setSize(self, size):
        if size > len(self):
            for i in range((size - len(self))):
                self._list.append("_")
        elif size < len(self) and (size >= 0):
            for _ in range(len(self) - size):
                self._list = self._list[:-1]

    def insertAt(self, index, value):
        self._list[index] = value

    def overWriteWith(self, values):
        self._list = values

    def getList(self):
        return self._list




    

if __name__ == "__main__":

    slObj = SizeableList(5)

    print("Initialized slObj object:")
    print(slObj)
    print("len: " + str(len(slObj)))

    print("\nInserting Values into object:")
    slObj.insertAt(0, "A")
    slObj.insertAt(1, "B")
    slObj.insertAt(2, "C")
    slObj.insertAt(3, "D")
    slObj.insertAt(4, "E")
    print(slObj)
    print("len: " + str(len(slObj)))

    print("\nChanging object size:")
    print("Bigger...")
    slObj.setSize(7)
    print(slObj)
    print("len: " + str(len(slObj)))
    print("Smaller...")
    slObj.setSize(3)
    print(slObj)
    print("len: " + str(len(slObj)))
    print("Bigger again...")
    slObj.setSize(7)
    print(slObj)
    print("len: " + str(len(slObj)))
    print("Overwriting with [1,2,3]:")
    slObj.overWriteWith([1,2,3])
    print(slObj)

##    print("\nTriggering value error:")
##    slObj2 = SizeableList(-1)
