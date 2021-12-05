#find BMI of a person where take mass and height as input from the user
#BMI=mass in kg/ (height in m)2
m=float(input("input mass in kg:"))
h=float(input("input height in m:"))
BMI=m/h**2
print("the BMI is {} kg/ m\u00b2 ." .format(BMI))
