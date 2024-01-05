from dateutil import parser as Parser
from pyluach import dates

class Calculator:
    def __init__(self, date):
        self.validate(date)
        self.date= date
        self.day=date[0:2]  
        self.month= date[3:5]
        self.year=date[6:10]
    
    def validate(self,date):
       try:
          Parser.parse(date)          
       except ValueError:
            raise Exception("Sorry, Wrong date format")
 

    def hebStart(self):
        year=int(self.year)
        month=int(self.month)
        day=int(self.day)
        currentDate=dates.GregorianDate(year,month, day )           
        hebrewDate= currentDate.to_heb()
        hebrewYear=hebrewDate.year
        hebreWDay= hebrewDate.day
        hebrewMonth= hebrewDate.month
        total= Calculator.start(hebrewYear)+ Calculator.start(hebreWDay)+ Calculator.start(hebrewMonth)
      #  values.hebDate=total
        return total

    def startByFirstName(self, firstName):
        pass

    def startByLastName(self):
        pass

    def gregStart(self):
        total=0
       
        total= Calculator.start(self.day)+ Calculator.start(self.month)+ Calculator.start(self.year)
       # values.gregDate=total
        return total
    
    @staticmethod
    def start( number: int):
        sum=0      
        for digit in str(number):
         sum= sum + int(digit)
        if(sum > 9):
           return Calculator.start(sum)
        return sum
       

calculator = Calculator("11.01.1970") 

#print(calculator.gregStart())  
#print(calculator.hebStart())

      
