from datetime import date
from calendar import monthrange

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

    def reset(self):
        #Resets _rawCD with the Constant RAW_CD (which grabs
        #todays date using date class)
        global _RAW_CD
        global _rawCD
        
        _rawCD = _RAW_CD
        print("This is reset: " + self.getCurrentDate())       

    def getCurrentDate(self) -> date:
        global _rawCD
        return "/".join([str(_rawCD.month), str(_rawCD.day), str(_rawCD.year)])

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
    def getDayRangeForCurrentDate(self) -> tuple: #tuple of int at index 0 & 1!
        #index 0: Enum of day name of first day of month.
        #         (ex. 0-6 -> Mon-Sun)
        #
        #index 1: Total num days in month (based on year and 
        #         month _rawCD is set to).
        global _rawCD
        
        return monthrange(_rawCD.year, _rawCD.month)
                

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

    def getYearlessDateRangeBetweenDates(self, y1, m1, d1, y2, m2, d2) -> list:
        temp = self.getDateRangeBetweenDates(y1, m1, d1, y2, m2, d2)
        outYearlessDateRange = []
        for date in temp:
            mdy = date.split("/")[0:2]
            outYearlessDateRange.append("/".join(mdy))
        return outYearlessDateRange

    def getYearRangeBetweenYears(self, y1, y2) -> list:
        return [str(year) for year in range(y1, (y2 + 1))]
    
    def getMonthRangeBetweenMonths(self, m1, m2) -> list:
        if (m1 < 1 or m1 > 12) or (m2 < 1 or m2 > 12):
            raise ValueError("month inputs cannot be less than 0 or greater than 12.")
        return [str(month) for month in range(m1, (m2 + 1))]
    
    def getDayRangeBetweenDays(self, d1, d2) -> list:
        if (d1 < 1 or d1 > 31) or (d2 < 1 or d2 > 31):
            raise ValueError("month inputs cannot be less than 0 or greater than 12.")
        return [str(day) for day in range(d1, (d2 + 1))]
        
    #Add check for all between methods ensuring that lesser values are passed to 1
    #and higher values are passed to 2.

if __name__ == "__main__":
    cObj = CLCalendar()
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
