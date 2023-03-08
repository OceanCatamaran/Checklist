from datetime import date
from calendar import monthrange
from re import match

_RAW_CD = date.today()
_rawCD = _RAW_CD

class CLCalendar:
    '''
    def __init__(self):
        #RAW_CD is a constant value(CD stands for CurrentDate).
        #Useful for resetting rawCD.
        
        self._RAW_CD = date.today()
        self._rawCD = self._RAW_CD
    '''
    @classmethod
    def reset(self):
        #Resets _rawCD with the Constant RAW_CD (which grabs
        #todays date using date class)
        global _RAW_CD
        global _rawCD
        
        _rawCD = _RAW_CD
        print("This is reset: " + self.getCurrentDate())       

    @classmethod
    def getCurrentDate(self) -> date:
        global _rawCD
        return "/".join([str(_rawCD.month), str(_rawCD.day), str(_rawCD.year)])

    @classmethod
    def setCurrentDate(self,
                       year : int = None,
                       month : int = None,
                       day : int = None):
        #Provide the int value for the year, month, and/or day
        #you want to set to _rawCD
        global _rawCD
        
        if day == None:
            if (month != None) or (year != None):
                day = 1
            else:
                day = _rawCD.day
        if year == None:
            year = _rawCD.year
        if month == None:
            month = _rawCD.month

        temp = _rawCD.replace(year, month, day)
        print("This is temp: " + "/".join([str(temp.month), str(temp.day), str(temp.year)]))
        _rawCD = temp

    '''#Rename method for clarity'''
    @classmethod
    def getDayRangeForCurrentDate(self) -> tuple: #tuple of int at index 0 & 1!
        #index 0: Enum of day name of first day of month.
        #         (ex. 0-6 -> Mon-Sun)
        #
        #index 1: Total num days in month (based on year and 
        #         month _rawCD is set to).
        global _rawCD
        
        return monthrange(_rawCD.year, _rawCD.month)
                
    @classmethod
    def getDateRangeBetweenDates(self, y1, m1, d1, y2, m2, d2) -> list:
        #For two specified Dates, (m1/d1/y1 and m2/d2/y2), get all the days in-between both dates (inclusive).
        #All the inclusive dates in-between the two specified dates must be in the form m/d/y as a str.
        currentDay = d1
        currentMonth = m1
        currentYear = y1
        outDateRange = []
        
        while(True):
            try:
                #print(currentMonth)
                if(currentDay > d2 and currentMonth >= m2 and currentYear >= y2):
                    break
                date(currentYear,currentMonth, currentDay)
                outDateRange.append(str(currentMonth) + "/" + str(currentDay) + "/" + str(currentYear))                
                currentDay+=1
            except ValueError:
                currentDay = 1
                if(currentMonth == 12):
                    currentMonth = 1
                    currentYear+=1
                else:
                    currentMonth+=1
        return outDateRange

    @classmethod
    def getYearlessDateRangeBetweenDates(self, y1, m1, d1, y2, m2, d2) -> list:
        temp = self.getDateRangeBetweenDates(y1, m1, d1, y2, m2, d2)
        outYearlessDateRange = []
        for date in temp:
            mdy = date.split("/")[0:2]
            outYearlessDateRange.append("/".join(mdy))
        return outYearlessDateRange

    @classmethod
    def getYearRangeBetweenYears(self, y1, y2) -> list:
        if y1 > y2 : raise ValueError("Beginning number greater than ending number.")
        return [str(year) for year in range(y1, (y2 + 1))]

    @classmethod
    def getMonthRangeBetweenMonths(self, m1, m2) -> list:
        if m1 > m2 : raise ValueError("Beginning number greater than ending number.")
        if (m1 < 1 or m1 > 12) or (m2 < 1 or m2 > 12):
            raise ValueError("month inputs cannot be less than 1 or greater than 12.")
        return [str(month) for month in range(m1, (m2 + 1))]

    @classmethod
    def getDayRangeBetweenDays(self, d1, d2) -> list:
        if d1 > d2 : raise ValueError("Beginning number greater than ending number.")
        if (d1 < 1 or d1 > 31) or (d2 < 1 or d2 > 31):
            raise ValueError("day inputs cannot be less than 1 or greater than 31.")
        return [str(day) for day in range(d1, (d2 + 1))]

    @classmethod
    def getNumRangeBetweenNums(self, n1, n2) -> list:
        if n1 > n2 : raise ValueError("Beginning number greater than ending number.")
        return [str(num) for num in range(n1, (n2 + 1))]
        
    #Add check for all between methods ensuring that lesser values are passed to 1
    #and higher values are passed to 2.

    def _dateFormatter(val_1, val_2):
        date_1 = val_1.split("/")
        if len(date_1) != 3: raise ValueError
        date_1 = [int(num) for num in date_1]
        if date_1[0] < 1 or 12 < date_1[0] : raise ValueError
        if date_1[1] < 1 or 31 < date_1[1] : raise ValueError

        date_2 = val_2.split("/")
        if len(date_2) != 3: raise ValueError
        date_2 = [int(num) for num in date_2]
        if date_2[0] < 1 or 12 < date_2[0] : raise ValueError
        if date_2[1] < 1 or 31 < date_2[1] : raise ValueError

        for i in [2, 0]:
            if date_1[i] > date_2[i] : raise ValueError("Beginning number greater than ending number.")

        if date_1[2] == date_2[2]:
            if date_1[0] == date_2[0]:
                if date_1[1] > date_2[1] : raise ValueError("Beginning number greater than ending number.")

        return [date_1[2], date_1[0], date_1[1], date_2[2], date_2[0], date_2[1]]

    @classmethod
    def getColumns(self, methodSelection, val_1, val_2) -> list:
    #Based on the input a user gives for the dat viewport
    #for values 1 and 2 (top and bottom entry widgets),
    #these values are the bounds used to get the in-between
    #values that will populate the xcolumn of the grid.
        match methodSelection:


        try:
            match methodSelection:
                case 1:
                    inputArgs = self._dateFormatter(val_1, val_2)
                    return self.getDateRangeBetweenDates(*inputArgs)
                
                case 2:
                    inputArgs = self._dateFormatter(val_1, val_2)
                    return self.getYearlessDateRangeBetweenDates(*inputArgs)
                    
                case 3:
                    return self.getYearRangeBetweenYears(int(val_1), int(val_2))

                case 4:
                    return self.getMonthRangeBetweenMonths(int(val_1), int(val_2))

                case 5:
                    return self.getDayRangeBetweenDays(int(val_1), int(val_2))

                case 6:
                    return self.getNumRangeBetweenNums(int(val_1), int(val_2))

                case default:
                    return None
        except:
            return None




if __name__ == "__main__":
    cObj = CLCalendar
    #Test 1
    print(str(cObj.getCurrentDate()))
    print(str(cObj.getDayRangeForCurrentDate()))
    #Test 2
    cObj.setCurrentDate(2022)
    print(str(cObj.getCurrentDate()))
    print(str(cObj.getDayRangeForCurrentDate()))
    #Test 3
    cObj.setCurrentDate(month=4)
    print(str(cObj.getCurrentDate()))
    print(str(cObj.getDayRangeForCurrentDate()))
    #Test 4
    cObj.setCurrentDate(day=4)
    print(str(cObj.getCurrentDate()))
    print(str(cObj.getDayRangeForCurrentDate()))
    #Test 5
    cObj.reset()
    print(str(cObj.getCurrentDate()))
    print(str(cObj.getDayRangeForCurrentDate()))
    #Test 6 getDateRangeBetweenDates
    print()
    print(cObj.getDateRangeBetweenDates(2023, 2, 1, 2023, 3, 1))
    print(cObj.getDateRangeBetweenDates(2024, 2, 1, 2024, 3, 1))
    #Test 7 getYearlessDateBetweenDates
    print()
    print(cObj.getYearlessDateRangeBetweenDates(2023, 2, 1, 2023, 3, 1))
    print(cObj.getYearlessDateRangeBetweenDates(2024, 2, 1, 2024, 3, 1))
    #Test 8
    print()
    print(cObj.getYearRangeBetweenYears(1900, 2023))
    #Test 9
    print()
    print(cObj.getMonthRangeBetweenMonths(1, 12))
    #Test 10
    print()
    print(cObj.getDayRangeBetweenDays(1, 31))
    print()
    #getColumns Tests
    #Test 1
    print("Method Selection 1:")
    print(cObj.getColumns(1, "2/1/2023", "2/24/2023"))
    #Test 2
    print("Method Selection 2:")
    print(cObj.getColumns(2, "2/1/2023", "2/24/2023"))
    #Test 3
    print("Method Selection 3:")
    print(cObj.getColumns(3, "1900", "2023"))
    #Test 4
    print("Method Selection 4:")
    print(cObj.getColumns(4, "1", "12"))
    #Test 5
    print("Method Selection 5:")
    print(cObj.getColumns(5, "1", "31"))
    #Test 6
    print("Method Selection 6:")
    print(cObj.getColumns(6, "0", "100"))
    
