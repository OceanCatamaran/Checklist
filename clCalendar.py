from datetime import date
from calendar import monthrange

class CLCalendar:
    def __init__(self):
        #RAW_CD is a constant value(CD stands for CurrentDate).
        #Useful for resetting rawCD.
        
        self._RAW_CD = date.today()
        self._rawCD = self._RAW_CD

    def reset(self):
        #Resets _rawCD with the Constant RAW_CD (which grabs
        #todays date using date class)
        
        self._rawCD = self._RAW_CD
        print("This is reset: " + str(self._rawCD))

    def getDayRangeForCurrentDate(self) -> tuple: #tuple of int at index 0 & 1!
        #index 0: Enum of day name of first day of month.
        #         (ex. 0-6 -> Mon-Sun)
        #
        #index 1: Total num days in month (based on year and 
        #         month _rawCD is set to).
        
        return monthrange(self._rawCD.year, self._rawCD.month)
                

    def getDayRangeBetweenDates(self, y1, m1, d1, y2, m2, d2) -> list:
        #For two specified Dates, (m1/d1/y1 and m2/d2/y2), get all the days in-between both dates (inclusive).
        #All the inclusive dates in-between the two specified dates must be in the form m/d/y as a str.
        currentDay = d1
        currentMonth = m1
        currentYear = y1
        outDayRange = []
        
        while(True):
            try:
                #print(currentMonth)
                if(currentDay > d2 and currentMonth >= m2 and currentYear >= y2):
                    break
                date(currentYear,currentMonth, currentDay)
                outDayRange.append(str(currentMonth) + "/" + str(currentDay) + "/" + str(currentYear))                
                currentDay+=1
            except ValueError:
                currentDay = 1
                if(currentMonth == 12):
                    currentMonth = 1
                    currentYear+=1
                else:
                    currentMonth+=1
        return outDayRange
        

    def getCurrentDate(self) -> date:
        return self._rawCD

    def setCurrentDate(self,
                       year : int = None,
                       month : int = None,
                       day : int = None):
        #Provide the int value for the year, month, and/or day
        #you want to set to _rawCD
        
        if day == None:
            if (month != None) or (year != None):
                day = 1
            else:
                day = self._rawCD.day
        if year == None:
            year = self._rawCD.year
        if month == None:
            month = self._rawCD.month

        temp = self._rawCD.replace(year, month, day)
        print("This is temp: " + str(temp))
        self._rawCD = temp

 
        

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
    #Test 6 getDayRangeBetweenDates
    print()
    print(cObj.getDayRangeBetweenDates(2023, 2, 1, 2023, 3, 1))
    print(cObj.getDayRangeBetweenDates(2024, 2, 1, 2024, 3, 1))
