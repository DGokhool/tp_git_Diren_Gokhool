#!/usr/bin/env python3

import sys
print(sys.argv)

def add(a,b):
    return a+b


#main
x = int(sys.argv[1])
y = int(sys.argv[2])

nbr_arg = len(sys.argv)-1

if(nbr_arg != 2):
  print ("Error")

print(add(x, y))
