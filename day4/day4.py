#Write a program to print absolute vlaue of a number entered by user. E.g.-INPUT: 1 OUTPUT: 1INPUT: -1 OUTPUT: 1
x=float(input())
x=abs(x)
if(x%1.0):          #when x is a floating point number
    print(x)
else:
    print(int(x))
    