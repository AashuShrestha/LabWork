#2. WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
e=int(input("enter the subject"))
s=int(input("enter the second subject"))
m=int(input("enter the third subject:"))
h=int(input("enter the fourth subject"))
totalmarks = e+s+m+h
print("total score is", totalmarks)
percentage = (totalmarks / 400) * 100
print("total percent is" , percentage, "%")
if percentage  > 70:
    print("he got distinction")
elif percentage > 60:
    print("he got division")   
elif percentage > 40:
    print("he passed the exam")
elif percentage < 40:
    print("you are failed try again good luck")
    
