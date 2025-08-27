import math
import sys
import random as rd #example of what to call it to shorten it when using it often
from enum import Enum
from math import pi
import London # can import another file as a module, then use any functions you created in that file
from FStrings import rock_paper_scissors   #importing a specific function from another file
print(math.pi)

# for item in dir(rd):
#     print(item) #also says it all in the python docs
#     #you can also use help(rd) for more information
#     # help(rd)

#print(London.Bird)
#print(London.randomfacts())

print(__name__)
print(London.__name__) #if you run this file it will say __main__ but if you run London.py it will say London

if __name__ == "__main__":
    London.randomfacts() 
    print("This script is being run directly")
else:
    print("This script is being imported")



rock_paper_scissors()   