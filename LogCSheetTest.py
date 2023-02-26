from tkinter import *
from frameSignaler import FrameSignaler

class LogCSheetUI:

    @classmethod
    def addFrame(self, window, fsObj):
        #This method adds the screen to the window from UIManager.
        def frameMaker(display = False):

            if display:
                top = Frame()

                w = 100
                h = 100

                #Creating Frames
                frame = Frame(top, highlightbackground="black")
                frame2 = Frame(top)

                #Initializing Canvas and its Frame?
                canvas = Canvas(frame, width = 600, height = 300, bd = 0, highlightthickness = 0, bg = "white", scrollregion = [0,0,w,h])
                scrollable_frame = Frame(canvas)

                #Some Scrollbar related settings?
                vertical_scrollbar = Scrollbar(frame,orient="vertical",command=canvas.yview)
                horizontal_scrollbar = Scrollbar(frame,orient="horizontal",command=canvas.xview)
                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )
                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=vertical_scrollbar.set)
                canvas.configure(xscrollcommand=horizontal_scrollbar.set)

                #Adding cells to screen
                for i in range(20):
                    for j in range(20):
                        Entry(scrollable_frame,width=5).grid(row=i,column=j)

                #Notes Section
                notes_label = Label(frame2,text="Notes:",width = 10,height =3,borderwidth=1,relief="solid").grid(row=0,column=50,padx=40,sticky='E')
                notes_box = Entry(frame2,width=30)
                notes_box.grid(row=0,column=100,ipady=30,sticky='W')
                vertical_scrollbar.pack(side=RIGHT, fill=Y)
                horizontal_scrollbar.pack(side=BOTTOM,fill=X)

                #Packing widgets
                frame.pack(padx=100,pady=100)
                frame2.pack()
                canvas.pack(side="left", fill="both", expand=True)

                #packing top
                top.pack()
        frameMaker()
        return ["LogCSheetUI", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        #Note, non-home Screens must use this testFrame code
        #as it is different from the testFrame method in the
        #Home Screen class.
        window = Tk()
        window.geometry("600x600")
        fsObj = FrameSignaler
        temp = self.addFrame(window, fsObj)
        temp[1](True)

        def printFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            window.after(1000, printFrameSignaler)

        printFrameSignaler()

        window.mainloop()

if __name__ == "__main__":
    LogCSheetUI.testFrame()
