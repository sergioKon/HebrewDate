from  Calculator import Calculator
from unittest import TestCase
class HebrewName:

        def __init__(this, firstName,lastName):
            this.firstName= firstName
            this.lastName= lastName
            
        vals = {'א': 1,'ב': 2,'ג': 3, 'ד':4, "ה": 5, "ו": 6, "ז" : 7 , "ח":8, "ט" : 9 , "י":10,
                "כ": 20,  "ך": 20, "ל": 30,  "מ": 40,  "ם": 40, "נ": 50 , "ן": 50, "ס": 60, "ע": 70,  "פ": 80, "צ": 90,
                "ק": 100,  "ר": 200,  "ש": 300 , "ת": 400 }
        
        def fullCalc(this):
             total= this.calcByFirstName()+ this.calcByLastName()
             if total > 9:
                total=Calculator.start(total)
             return total  

        def calcByFirstName(this):
            return this.__calcTotal(this.firstName) 
        
        def calcByLastName(this):
            return this.__calcTotal(this.lastName) 

        def __calcTotal (this,text: str ):
            total = 0 
            for letter in text:
                number = this.vals.get(letter)
                if(number > 99):
                    number= number/100
                elif number>9:
                     number=number/10
                total =  total + number
            if(total > 9): 
                return Calculator.start(int(total))
            return total                 


boris=HebrewName("בוריס","פיין")
test=TestCase()
test.assertEqual(8,boris.calcByFirstName())
test.assertEqual(6,boris.calcByLastName())     
test.assertEqual(5,boris.fullCalc())       

dov=HebrewName("דוב","גרגור")
test.assertEqual(3,dov.calcByFirstName())
test.assertEqual(7,dov.calcByLastName())     
test.assertEqual(1,dov.fullCalc()) 


exit()  

firstName="בוריס"
lastName = "פיין"

hebrewName=HebrewName(firstName, lastName)
print (" first name gematria ", hebrewName.calcByFirstName() )
print (" last name gematria", hebrewName.calcByLastName() )
print (" full gematria = ", hebrewName.fullCalc() )



   

    
         
                  