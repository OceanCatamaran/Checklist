from tkinter import *
from frameSignaler import FrameSignaler
from frameSwitcher import FrameSwitcher
from homepageUI import HomepageUI
from giveFeedbackUI import GiveFeedbackUI
from selectCSheetUI import SelectCSheetUI
from createCSheetUI import CreateCSheetUI


class uiManager:
    def __init__(self):
        #Setting up Window
        fsObj = self._getFrameSignaler()
        window = Tk()
        window.geometry("800x600")
        window.iconbitmap("favicon.ico")
        window.title("Checklist")
        window.resizable(False, False)

        #Setting up Screens
        FrameSwitcher.addFrame(HomepageUI.addFrame(window, fsObj))
        FrameSwitcher.addFrame(GiveFeedbackUI.addFrame(window, fsObj))
        FrameSwitcher.addFrame(CreateCSheetUI.addFrame(window, fsObj))
        FrameSwitcher.addFrame(SelectCSheetUI.addFrame(window, fsObj))

        # checkFrameSignaler checks for any flags, if any then
        # it switches to appropriate frame.
        def checkFrameSignaler():
            print(fsObj.getFlag())
            print(fsObj.getData())
            FrameSwitcher.checkFrameSignaler(fsObj)
            window.after(1000, checkFrameSignaler)

        checkFrameSignaler()
        window.mainloop()

    def _getFrameSignaler(self):
        return FrameSignaler


if __name__ == "__main__":
    uiManager()
