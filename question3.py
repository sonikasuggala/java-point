skmph = int(input("Enter the speed in kmph: "))
time = int(input("Enter the time in seconds: "))
lt = int(input("Enter the length of train :"))
smps= skmph * (5/18)
lb = (smps*time)-lt
print("The lenghth of the bridge is:", lb , "meters")
