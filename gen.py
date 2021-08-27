import time
from random import *
import math
import pySic

seed(time.time_ns)

def gen():
    numArray = []
    exists = False

    while len(numArray) < 12:
        r = randint(1, 12)
        for x in numArray:
            if (x == r):
                exists = True

        if (exists):
            exists = False
            continue


        numArray.append(r)
    else:
        s = pySic.scoring(numArray)
        r = ""
        for x in numArray:
            r += str(x) + " "
        return (r + "\n" + str(s))
       

    
