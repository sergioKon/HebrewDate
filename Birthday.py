from  Calculator import Calculator
from pyluach import dates, hebrewcal
from bidi.algorithm import get_display  as RightToLeft

class Bitrhday:
    def __init__(this, englishDate):
        this.englishDate= englishDate
        year, month,day = this.parseDate()
        date=dates.GregorianDate(year, month,day)
        this.hebrewDate = date.to_heb()
    
  
    def caclEnglish(this):
        year, month,day = this.parseDate() 
        total=Calculator.start(year)+ Calculator.start(month) + Calculator.start(day)
        sum= Calculator.start(total) 
        return sum   
    
    def parseDate(this):
        date= this.englishDate
        return  int(date[6:10]), int(date[3:5]), int(date[0:2])
    
    def calcHebrew(this):
        hebrewDate= this.hebrewDate
        dict=hebrewDate.dict()
        year=dict.get("year")
        month= dict.get("month")
        day= dict.get("day")
        
        hebDate= RightToLeft(this.hebrewDate.hebrew_date_string() )
        
        total=Calculator.start(year)+ Calculator.start(month) + Calculator.start(day)
        
        sum= Calculator.start(total) 
        return sum
        
    def calcEnglish(this):
            pass

boris= Bitrhday("11/01/1970")
print(boris.calcHebrew())
print(boris.caclEnglish())

