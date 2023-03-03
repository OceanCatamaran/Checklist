class Grid:
    #Assumptions:
    #    1. Data passed to Grid instances are correct.
    #    2. Data passed into dates, categories, and grid
    #       are always going to be strings.
    
    def __init__(self, yRowNum, xColumnNum):
        self._yRowNum = yRowNum
        self._xColumnNum = xColumnNum
        self._dates = []
        self._categories = []
        self._notes = ""
        self._grid = []
        
        for yRow in range(self._yRowNum):
            self._grid.append(["None" for xColumn in range(self._xColumnNum)])

    #Basically a static method constructor to instantiate a...
    #Grid from repr Grid data.
    @classmethod 
    def fromRepr(cls, reprData):
        rawData = reprData.split("\n")
        dates = rawData[0].split(",")
        categories = rawData[1].split(",")
        notes = rawData[2]
        grid = []
        rawData = rawData[3:]
        for yRow in rawData:
            grid.append(yRow.split(","))

        outGrid = cls(len(categories), len(dates))
        outGrid.setDates(dates)
        outGrid.setCategories(categories)
        outGrid.setNotes(notes)
        outGrid._grid = grid

        return outGrid
        
    def setDates(self, dates):
        self._dates = dates

    def setCategories(self, categories):
        self._categories = categories

    def setNotes(self, notes):
        self._notes = notes

    def getDates(self):
        return self._dates

    def getCategories(self):
        return self._categories

    def getNotes(self):
        return self._notes

    def setAt(self, yRow, xColumn, data):
        self._grid[yRow][xColumn] = data

    def getAt(self, yRow, xColumn):
        return self._grid[yRow][xColumn]

    def setAll(self, grid):
        self._grid = grid

    def getAll(self):
        return self._grid

    def __str__(self):
        formattedGrid = []
        for yRow in self._grid:
            formattedGrid.append(str(yRow))
        formattedGrid = "\n".join(formattedGrid)
        
        outString = f"{self._dates}\n{self._categories}\n{self._notes}\n{formattedGrid}"

        return outString

    def __repr__(self):
        formattedDates = ",".join(self._dates)
        formattedCategories = ",".join(self._categories)
        formattedGrid = []
        for yRow in self._grid:
            formattedGrid.append(",".join(yRow))
        formattedGrid = "\n".join(formattedGrid)
        
        outString = f"{formattedDates}\n{formattedCategories}\n{self._notes}\n{formattedGrid}"

        return outString
    
if __name__ == "__main__":
    dates = ["1/1", "1/2"]
    categories = ["A", "B"]
    notes = "Jerry had a something."
    
    #>>>Initializing Grid 1
    print(">>>Initializing Grid 1")
    gObj_1 = Grid(2,2)
    print("\n\n")

    #>>>Setting categories (map to yRows) and dates (map to xColumns)
    print(">>>Setting categories (map to yRows) and dates (map to xColumns)")
    gObj_1.setCategories(categories)
    gObj_1.setDates(dates)
    gObj_1.setNotes(notes)

    print("Dates: " + str(gObj_1.getDates()))
    print("Categories: " + str(gObj_1.getCategories()))
    print("Notes: " + str(gObj_1.getNotes()))
    print("\n\n")

    #>>>Setting data at (0,1) and (1,0)
    print(">>>Setting data at (0,1) and (1,0)")
    gObj_1.setAt(0,1, "X")
    gObj_1.setAt(1,0, "X")

    print("(0,1): " + str(gObj_1.getAt(0,1)))
    print("(1,0): " + str(gObj_1.getAt(1,0)))
    print("\n\n")

    #>>>Testing print Functionality
    print(">>>Testing print Functionality")
    print(">>>__str__")
    print(gObj_1)
    print(">>>__repr__")
    print(repr(gObj_1))
    print("\n\n")

    #>>>Testing Grid instantiation from another Grid (using repr)
    print(">>>Testing Grid instantiation from another Grid (using repr)")
    gObj_1Data = repr(gObj_1)
    gObj_2 = Grid.fromRepr(gObj_1Data)
    print(gObj_2)
    print("\n\n")
    
    
        
