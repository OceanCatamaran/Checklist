_flag = ""
_data = ""
class FrameSignaler:
    @classmethod
    def setFlag(self, param_flag):
        global _flag
        _flag = param_flag

    @classmethod
    def getFlag(self) -> str:
        global _flag
        return _flag

    @classmethod
    def setData(self, param_data):
        global _data
        _data = param_data

    @classmethod
    def getData(self) -> str:
        global _data
        return _data
        
