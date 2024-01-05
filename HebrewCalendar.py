from pyluach import dates, hebrewcal, parshios
from bidi.algorithm import get_display 
from pyluach.dates import GregorianDate, HebrewDate


year=2023
day=19
month=10

today=dates.GregorianDate(year=1023, month=12,day=31)
print(get_display( today.to_heb().hebrew_year()) )   
print(today.to_heb().year)
print("hebrew day",  today.to_heb().day)
print("hebrew month",  today.to_heb().month)
print("hebrew month",  today.to_heb().month_name())
print("hebrew month",  today.to_heb().month_name(True))

print("-------------------------")


exit()

def calcSum(number):
    res= number
    sum=0
    while res > 0:
            mod=res%10
            sum= sum +mod
            res= int(res/10)
    if sum > 9:
            return calcSum(sum)        
    return sum        
print(" sum = ", calcSum(5774) )

hebrewDate= HebrewDate(6899,1,1)
print("hebrew day",  hebrewDate.day)
print(" hebrew month name ",  hebrewDate.month_name(False))
print(" hebrew month",  hebrewDate.month)
print(" hebrew year ", get_display( hebrewDate.hebrew_year()))
print("year ", hebrewDate.year)


exit()

today=dates.GregorianDate(year=2023, month=10,day=19)
hebDate= today.to_heb().hebrew_date_string() 
print(get_display('טקסט לדוגמא '))
print(" hebrew date = " ,Dir(hebDate))

today=dates.GregorianDate(year=2023, month=9,day=19)
print( today.to_heb().hebrew_year ) 

today=dates.GregorianDate(year=2023, month=12,day=14)
print( today.to_heb().hebrew_date_string() ) 

exit()
today = dates.HebrewDate.today()
lastweek_gregorian = (today - 7).to_greg()
lastweek_gregorian < today
today - lastweek_gregorian

greg = dates.GregorianDate(1986, 3, 21)
heb = dates.HebrewDate(5746, 13, 10)
greg == heb



purim = dates.HebrewDate(5781, 12, 14)
purim.hebrew_day()

purim.hebrew_date_string()
purim.hebrew_date_string(True)

rosh_hashana = dates.HebrewDate(5782, 7, 1)
rosh_hashana.holiday()
rosh_hashana.holiday(hebrew=True)

(rosh_hashana + 3).holiday()
month = hebrewcal.Month(5781, 10)
month.month_name()
month.month_name(True)
for month in hebrewcal.Year(5774).itermonths():
    print(month.month_name())


date = dates.GregorianDate(2010, 10, 6)
parshios.getparsha(date)
parshios.getparsha_string(date, israel=True)
parshios.getparsha_string(date, hebrew=True)
new_date = dates.GregorianDate(2021, 3, 10)
parshios.getparsha_string(new_date)
parshios.getparsha_string(new_date, hebrew=True)