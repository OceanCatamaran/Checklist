from tkinter import *
from grid import Grid
#temporary import for testing
from fileManager import FileManager

class GridCellManager:

    def __init__(self, grid, window):
        self._grid = grid
        self._dates = self._grid.getDates()
        self._categories = self._grid.getCategories()

        self._datLabels = [Entry(window, width = 5) for _ in range((len(self._dates) + 1))]
        self._catLabels = [Entry(window, width = 5) for _ in range(len(self._categories))]
        self._cellEntries = [[Entry(window, width = 5) for _ in range(len(self._dates))] for _ in range(len(self._categories))]

        print(self._datLabels)
        print(self._catLabels)
        print(self._cellEntries)

if __name__ == "__main__":
    window = Tk()
    window.geometry("800x600")
    gObj = FileManager.getFile("test")
    gcmObj = GridCellManager(gObj, window)
    

        
