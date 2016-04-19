#!/usr/bin/env python
import datetime
import pprint
#fr=open("/Users/Dorna/Documents/ServerDir/data/stripe/data.csv", "r")
#fw=open("/Users/Dorna/Documents/ServerDir/data/stripe/data_mod.csv", "w")


def fizbuzz2(N):
    for i in range(1,N+1):
        outString = ""
        if i % 3 == 0:
            outString= "Fiz"
        if i%5==0:
            outString+= "Buzz"
        
        print outString or str(i)

fizbuzz2(16)

#pprint.pprint(data)
#fr.close()
#fw.close()

ksjdh kjsh jkg