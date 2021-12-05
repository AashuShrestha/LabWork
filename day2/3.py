#Given the integer N - the number of minutes that is passed since midnight - how many
# hours and minutes are displayed on the 24th digital clock?
integer = int(input("enter the integer N :"))
hour = integer // 60
minutes = integer % 60
print (hour,minutes)
