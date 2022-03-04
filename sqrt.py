#Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50.
#H is 30.
#D is a variable whose values should be input to your program in a comma-separated sequence.

#here not clear about giving input in comma seperated sequence

from cmath import sqrt
import math

C=50
H=30

def sqr(D=int(input("enter the value of D\n"))):
   
     Q=(2*C*D)/H
     print(sqrt(Q))
sqr()

    


