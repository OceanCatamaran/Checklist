from tkinter import *
from frameSignaler import FrameSignaler
from frameSwitcher import FrameSwitcher
from homepageUI import HomepageUI
from giveFeedbackUI import GiveFeedbackUI
from createCSheetUI import CreateCSheetUI


class uiManager:
    def __init__(self):
        fsObj = self._getFrameSignaler()
        window = Tk()
        window.geometry("800x600")
        window.resizable(False, False)
        FrameSwitcher.addFrame(HomepageUI.addFrame(window, fsObj))
        FrameSwitcher.addFrame(GiveFeedbackUI.addFrame(window, fsObj))
        FrameSwitcher.addFrame(CreateCSheetUI.addFrame(window, fsObj))

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
