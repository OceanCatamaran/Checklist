from tkinter import *
from frameSignaler import FrameSignaler

class B:
    @classmethod
    def addFrame(self, top, fsObj):
        #This method adds the screen to the master UI
        def frameMaker(display = False):
            #should the display conditional be at this line instead?
            #--Otherwise, would memory leak occur because when addFrame is called...
            #--it is not displayed. Yet when frameMaker function is called, everything is recreated
            #--and then displayed...
            if display:
                temp = Frame(top, width = 40, height = 20, relief = "sunken", borderwidth = 2)

                def back():
                    fsObj.setFlag("A")
                    fsObj.setData("")
                    temp.destroy()

                temp2 = Label(temp, text = "B")
                temp3 = Button(temp, text = "Back", command = back)


                print("B has data: " + fsObj.getData())
                fsObj.setData("")
                temp.pack()
                temp2.pack()
                temp3.pack()
        frameMaker()
        return ["B", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        #Note, non-home Screens must use this testFrame code
        #as it is different from the testFrame method in the
        #Home Screen class.
        top = Tk()
        fsObj = FrameSignaler
        temp = self.addFrame(top, fsObj)
        temp[1](True)
        
        def printFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            top.after(1000, printFrameSignaler)

        printFrameSignaler()
        
        top.mainloop()

if __name__ == "__main__":
    B.testFrame()
