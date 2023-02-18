_frames = {}
class FrameSwitcher:
    @classmethod
    def addFrame(self, frameData):
        global _frames
        _frames[frameData[0]] = frameData[1]
        
    @classmethod
    def checkFrameSignaler(self, fsObj):
        global _frames
        flag = fsObj.getFlag()
        fsObj.setFlag("")
        if flag != "":
            _frames[flag](True)
            
