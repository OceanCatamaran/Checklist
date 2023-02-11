from tkinter import *

class EntryReader:

    def __init__(self, entry):
        self._entry = entry

    def getNumber(self) -> int:
        try:
            outInt = int(self._entry.get())
            return outInt if outInt >= 0 else 0
        except Exception:
            print("Please ensure inputted value is a positive whole number.")
            return 0

    @classmethod
    def getCallBack(self, erObj):
        def entryCallBack():
            print(erObj.getNumber())
        return entryCallBack

    

if __name__ == "__main__":
    root = Tk()
    eObj = Entry(root)
    erObj = EntryReader(eObj)
    getButton = Button(root, command = EntryReader.getCallBack(erObj))
    eObj.pack()
    getButton.pack()

    root.mainloop()
    
