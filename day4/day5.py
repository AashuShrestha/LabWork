#A student will not be allowed to sit in exam if his/her attendence is less than 75%.Take following input from userNumber of classes held
#Number of classes attended.And print percentage of class attendedIs student is allowed to sit in exam or not.
Utsav Thapa
h=int(input("Number of classes held"))
a=int(input("Number of class attended"))
p=a/h*100
print(f"Percentage of class attended is {p}%.")
if p>=75:
    print("Student is allowed to sit in exam .")
else:
    print("Student is not allowed to sit in exam")
