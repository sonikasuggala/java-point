skmph = int(input("Enter the speed in kmph: "))
smps= skmph * (5/18)
lent = int(input("Enter the length of the train:"))
lenp = int(input("Enter the length of the platform:"))
distance = lent + lenp
time = distance/smps
print("time taken to cross the platform is :", time,"seconds")
