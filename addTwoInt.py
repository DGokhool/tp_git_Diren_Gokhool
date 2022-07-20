#!/usr/bin/env python3

import sys
print(sys.argv)

def add(a,b):
    return a+b


#main
nbr_arg = len(sys.argv)-1

if(nbr_arg < 2):
    print ("Input again")
    x =int(input("Entrez la premiere valeur:"))
    y =int(input("Entrez la deuxieme valeur:"))
elif(nbr_arg > 2):
    print ("Error too many numbers entered")

else: 
    x = int(sys.argv[1])
    y = int(sys.argv[2])

print(add(x, y))
