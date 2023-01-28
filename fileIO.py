from pathlib import Path
from grid import Grid
from clCalendar import CLCalendar
class FileIO:
    @classmethod
    def writeDataTo(self, reprData, fileName):
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        with open(filePath, "w") as cSheet:
            cSheet.write(reprData)

    @classmethod
    def readDataFrom(self, fileName):
        outReprData = ""
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        if not(filePath.is_file()):
            raise ValueError("filePath does not exist or is not a file.")
        with open(filePath, "r") as cSheet:
            for line in cSheet:
                outReprData += line
        return outReprData
        
if __name__ == "__main__":
    gObj = Grid.fromRepr("1/1,1/2\nA,B\nNone,X\nX,None")
    FileIO.writeDataTo(repr(gObj), "test")
    print(FileIO.readDataFrom("test"))
