from tkinter import *
from frameSignaler import FrameSignaler


class HomepageUI:
    @classmethod
    def addFrame(self, window, fsObj):
        #This method adds the screen to the window from UIManager.
        def frameMaker(display = False):
            if display:
                # initialize home page window
                home_page = Frame(window, width = 800, height = 600, bg = "white")

                # create frame for options
                page_frame = Frame(home_page, bg = "white")

                #Banner
                bfObj = Frame(window, width = 800, height = 94, bg= "white")
                banner = PhotoImage(file = "Bhomepage.gif")
                bannerLabel = Label(bfObj, image = banner)
                bannerLabel.image = banner

                bfObj.place(x = 0, y = 0)
                bannerLabel.pack(fill = "both")                


                # callbacks
                def destroyScreen():
                    for widget in window.winfo_children():
                            widget.destroy()
                
                def createCSheet():
                    destroyScreen()
                    fsObj.setFlag("createCSheetUI")
                    fsObj.setData("")

                def selectCSheet():
                    destroyScreen()
                    fsObj.setFlag("selectCSheetUI")
                    fsObj.setData("")

                def feedback():
                    destroyScreen()
                    fsObj.setFlag("feedbackUI")
                    fsObj.setData("")

                # create options buttons for frame
                create_page = Button(page_frame, text="Create", width="50", command = createCSheet, borderwidth = 2)
                select_page = Button(page_frame, text="Select", width="50", command = selectCSheet, borderwidth = 2)
                create_page.pack(pady=20)
                select_page.pack()

                page_frame.place(anchor="s")
                page_frame.pack(padx=5, pady=20)


                # create feedback button
                feedback_button = Button(page_frame, text="?", width="3", command = feedback, borderwidth = 2,)
                feedback_button.pack(anchor="w", padx=0, pady=(25, 0))

                #Grid.rowconfigure(option_frame, 0, weight=1)
                #Grid.columnconfigure(option_frame, 0, weight=1)


                #create_page.grid(row=0, column=0, sticky="NSEW")
                #select_page.grid(row=1, column=0, sticky="NSEW")

                #create_page.grid # Should this line be here?

                page_frame.place(in_=home_page, anchor="c", relx=0.5, rely=0.5)
                home_page.pack()

        frameMaker(True)
        return ["homepageUI", frameMaker]

    @classmethod
    def testFrame(self):
        #This method is for testing the screen by itself
        window = Tk()
        window.geometry("800x600")
        fsObj = FrameSignaler
        self.addFrame(window, fsObj)

        def printFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            window.after(1000, printFrameSignaler)

        printFrameSignaler()
        
        window.mainloop()

if __name__ == "__main__":
    HomepageUI.testFrame()
