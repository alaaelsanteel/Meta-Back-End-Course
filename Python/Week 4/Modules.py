
import sys
location= sys.path
print(location) #returns all the possible locations 
#that the interpreter is going to look for when searching for modules, including the current working directory
for i in location:
 print(i) #each in a line

import calendar #to open the calender file hover over calendar and press ctrl and press on it

leap_days= calendar.leapdays(2000,2050)
print(leap_days) #13 leap days in between
leap_year=calendar.isleap(2050) #returns a Boolean value, it tells you if a given year is a leap year.
print(leap_year)

import sample  #py file
import json
json.decoder

import math 
root=math.sqrt(9)
# Instead of importing the entire math module we can directly access the sqrt in better way
from math import sqrt
root =sqrt(9)

import math as m
m.acos
from math import factorial as f
from math import log,sqrt
from  math import * # * means all
f(10)


