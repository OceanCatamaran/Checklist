from tkinter import *
from frameSignaler import FrameSignaler

class A:
    @classmethod
    def addFrame(self, top, fsObj):
        #This method adds the screen to the master UI
        def frameMaker(display = False):
            temp = Frame(top, width = 40, height = 20, relief = "groove", borderwidth = 2)

            def next():
                fsObj.setFlag("B")
                fsObj.setData("someFile")
                temp.destroy()

            temp2 = Label(temp, text = "A")
            temp3 = Button(temp, text = "Next", command = next)

            if display:    
                temp.pack()
                temp2.pack()
                temp3.pack()
        #If A is the Home Screen, then pass true to display
        frameMaker(True)
        return ["A", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        top = Tk()
        fsObj = FrameSignaler
        self.addFrame(top, fsObj)

        def printFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            top.after(1000, printFrameSignaler)

        printFrameSignaler()
        
        top.mainloop()

if __name__ == "__main__":
    A.testFrame()
