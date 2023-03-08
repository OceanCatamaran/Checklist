from tkinter import *
from frameSignaler import FrameSignaler
from fileManager import FileManager
from gridCellManager import GridCellManager

class LogCSheetUI:

    @classmethod
    def addFrame(self, window, fsObj):
        #This method adds the screen to the window from UIManager.
        def frameMaker(display = False):

            if display:
                top = Frame(bg = "white")

                w = 100
                h = 100

                #Creating Frames
                frame = Frame(top, highlightbackground="black")
                notes_frame = Frame(top, relief = "groove", bd = 2, bg = "white")

                #Banner
                bfObj = Frame(window, width = 800, height = 94, bg= "white")
                banner = PhotoImage(file = "BLogCSheet.gif")
                bannerLabel = Label(bfObj, image = banner)
                bannerLabel.image = banner

                bfObj.pack(fill = "both")
                bannerLabel.pack(fill = "both")

                #Initializing Canvas and its Frame?
                canvas = Canvas(frame, width = 600, height = 300, relief = "groove", bd = 2, highlightthickness = 0, bg = "white", scrollregion = [0,0,w,h])
                scrollable_frame = Frame(canvas, width = 400, height = 350)

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
                vertical_scrollbar.pack(side=RIGHT, fill=Y)
                horizontal_scrollbar.pack(side=BOTTOM,fill=X)

                #Adding cells to screen
                print(fsObj.getData().split(",")[0])
                gObjORG = FileManager.getFile(fsObj.getData().split(",")[0])
                gcmObj = GridCellManager(gObjORG, scrollable_frame)

                #Notes Section
                notes_label = Label(notes_frame,text="Notes:",width = 10,height =3, highlightthickness=0, pady=0, borderwidth=1,relief="solid")
                notes_box = Text(notes_frame, width = 50, height = 5)
                notes_box.insert("0.0", gObjORG.getNotes())
                notes_label.pack(side = LEFT, fill = "both", anchor = "nw")
                notes_box.pack(side = BOTTOM, anchor = "n", fill = X, expand = False)
               
                

                #Callbacks
                def destroyScreen():
                    for widget in window.winfo_children():
                        widget.destroy()
                        
                def saveCSheet():
                    gObjNEW = gcmObj.getGrid()
                    gObjNEW.setNotes("".join(notes_box.get("0.0", "end").split("\n")))
                    print(gObjNEW)
                    FileManager.setFile(gObjNEW, fsObj.getData().split(",")[0])

                def back():
                    destroyScreen()
                    screen = fsObj.getData().split(",")[1]
                    fsObj.setFlag(screen)
                    fsObj.setData("")

                #Save Button
                saveB = Button(top, width = 8, height = 2, text = "Save", command = saveCSheet)
                saveB.pack(side = RIGHT, anchor = "nw")


                #Back Button
                backB = Button(top, width = 8, height = 2, text = "Back", command = back)
                backB.pack(side = LEFT, anchor = "ne")

                #Packing widgets
                frame.pack(padx=50,pady=50)
                notes_frame.place(x = 160, y = 400)
                canvas.pack(side="left", fill="both", expand=True)

                #packing top
                top.pack(fill = "both", expand = True)
        frameMaker()
        return ["logCSheetUI", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        #Note, non-home Screens must use this testFrame code
        #as it is different from the testFrame method in the
        #Home Screen class.
        window = Tk()
        window.geometry("800x600")
        fsObj = FrameSignaler
        fsObj.setData("test,selectCSheetUI")
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
