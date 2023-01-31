import glob
from grid import Grid
from clCalendar import CLCalendar
from fileIO import FileIO

class FileManager:

    @classmethod
    def getFileNames(self) -> list:
        return FileIO.getFileNames()

    @classmethod    
    def createFile(self, grid, fileName) -> None:
        FileIO.writeDataTo(repr(grid), fileName)

    @classmethod
    def copyFile(self, copyName, selectedFileName) -> None:
        #This method copies the content from the selectedFileName,
        #then writes that data into a new cSheet with the argument
        #passed into the fileName parameter for this method.
        copiedData = FileIO.readDataFrom(selectedFileName)
        FileIO.writeDataTo(copiedData, copyName)

    @classmethod
    def getFile(self, selectedFileName) -> Grid:
        #This method returns raw cSheet data to be modified or logged.
        return Grid.fromRepr(FileIO.readDataFrom(selectedFileName))

    @classmethod
    def setFile(self, updatedGrid, selectedFileName) -> None:
        #This method is given raw cSheet data to modify or log a particular
        #cSheet file.
        FileIO.writeDataTo(repr(updatedGrid), selectedFileName)

    @classmethod
    def deleteFile(self, selectedFileName) -> None:
        FileIO.deleteFile(selectedFileName)

if __name__ == "__main__":
    #Testing getFileNames method
    fileNames = FileManager.getFileNames()
    
    #Testing getFile method
    gObj = FileManager.getFile(fileNames[0])

    #Testing setFile method
    FileManager.setFile(gObj, fileNames[0])

    #Testing createFile method
    FileManager.createFile(gObj, "test2")

    #Testing copyFile method
    fileNames = FileManager.getFileNames()
    FileManager.copyFile("test2-copy", fileNames[1])

    #Testing deleteFile method ~ deleting test2-copy.cSheet
    fileNames = FileManager.getFileNames()
    FileManager.deleteFile(fileNames[1])
    
