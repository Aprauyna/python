# A module is a file containing Python definitions and statements that can be used in other Python programs
# Similar to code library
# Python has a library of ready-made modules (e.g. datetime, math, etc), and we can also create our own custom modules
# A module is a single .py file
# Using a module: import math or from math import pi

import datetime
curr=datetime.datetime.now()
print(curr)

from datetime import date
currr=date.today()
print(currr)

import time
print(time.ctime())