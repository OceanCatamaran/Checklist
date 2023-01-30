import os
import glob
from pathlib import Path
from grid import Grid
from clCalendar import CLCalendar
class FileIO:
    @classmethod
    def writeDataTo(self, reprData, fileName) -> None:
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        with open(filePath, "w") as cSheet:
            cSheet.write(reprData)

    @classmethod
    def readDataFrom(self, fileName) -> str:
        outReprData = ""
        filePath = Path.cwd() / "SavedData" / (fileName + ".cSheet")
        if not(filePath.is_file()):
            raise ValueError("filePath does not exist or is not a file.")
        with open(filePath, "r") as cSheet:
            for line in cSheet:
                outReprData += line
        return outReprData
    
    @classmethod
    def _pathFormatter(self, filePath) -> str:
        return repr(filePath)[15:-2]

    @classmethod
    def getFileNames(self) -> list:
        outFileNames = []
        filePath = (Path.cwd() / "SavedData" / "*.cSheet")
        filePath = FileIO._pathFormatter(filePath)
        for name in glob.glob(filePath):
            outFileNames.append(str(os.path.basename(name))[:-7])
        return outFileNames
        
if __name__ == "__main__":
    #gObj = Grid.fromRepr("1/1,1/2\nA,B\nNone,X\nX,None")
    #FileIO.writeDataTo(repr(gObj), "test")
    #print(FileIO.readDataFrom("test"))
    print(FileIO.getFileNames())
