from tkinter import *
from grid import Grid
#temporary import for testing
from fileManager import FileManager

class GridCellManager:

    def __init__(self, grid, window):
        self._grid = grid
        self._dates = self._grid.getDates()
        self._categories = self._grid.getCategories()

        #Getting column titles, row titles, and cell data.

        self._datFillIns = [None, *self._dates]
        self._catFillIns = [*self._categories]
        self._cellFillIns = self._grid.getAll()

        #Test
        #print(self._datFillIns)
        #print(self._catFillIns)
        #print(self._cellFillIns)

        fillIns = [self._datFillIns]
        for i in range(len(self._catFillIns)):
            temp = [self._catFillIns[i], *self._cellFillIns[i]]
            fillIns.append(temp)

        #print(fillIns)

        #Creating corresponding Entry widgets by column and row.

        self._datEntries = [Entry(window, width = 5) for _ in range((len(self._dates) + 1))]
        self._catEntries = [Entry(window, width = 5) for _ in range(len(self._categories))]
        self._cellEntries = [[Entry(window, width = 5) for _ in range(len(self._dates))] for _ in range(len(self._categories))]

        #Test
        #print(self._datEntries)
        #print(self._catEntries)
        #print(self._cellEntries)

        #Placement list, for placing Entries in window.
        placement = [self._datEntries]
        for i in range(len(self._catEntries)):
            temp = [self._catEntries[i], *self._cellEntries[i]]
            placement.append(temp)

        #Test
        #print(placement)

        for y in range(len(self._catEntries) + 1):
            for x in range(len(self._datEntries)):
                placement[y][x].insert(0, str(fillIns[y][x]))
                placement[y][x].grid(row = y, column = x)

    def getGrid(self) -> Grid:
        outGrid = self._grid
        for y in range(len(self._cellEntries)):
            for x in range(len(self._cellEntries[0])):
                outGrid.setAt(y, x, self._cellEntries[y][x].get())
        return outGrid

if __name__ == "__main__":
    window = Tk()
    window.geometry("800x600")
    gObj = FileManager.getFile("test")
    gcmObj = GridCellManager(gObj, window)
    gridObj = gcmObj.getGrid()
    dummy = Button(window, text = "Save", command = gcmObj.getGrid)
    dummy.place(x = 100, y = 0)
    #print(gridObj)
    window.mainloop()
    

        
