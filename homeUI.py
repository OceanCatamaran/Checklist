from tkinter import *
from frameSignaler import FrameSignaler
from frameSwitcher import FrameSwitcher
from testUIA import A
from testUIB import B

class HomeUI:
    def __init__(self):
        fsObj = self._getFrameSignaler()
        top = Tk()
        FrameSwitcher.addFrame(A.addFrame(top, fsObj))
        FrameSwitcher.addFrame(B.addFrame(top, fsObj))
        #checkFrameSignaler checks for any flags, if any then
        #it switches to appropriate frame.
        def checkFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            FrameSwitcher.checkFrameSignaler(fsObj)
            top.after(1000, checkFrameSignaler)
        checkFrameSignaler()
        top.mainloop()

    def _getFrameSignaler(self):
        return FrameSignaler

#    def printFrameSignaler(self, top, fsObj):
#       print(fsObj.getFlag())
#       print(fsObj.getData())
#       top.after(top, 1000, self.printFrameSignaler())






if __name__ == "__main__":
    HomeUI()
