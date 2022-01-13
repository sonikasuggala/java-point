stkmph = int(input("Enter the speed of train in kmph: "))
smkmph = int(input("Enter the speed of man in kmph: "))
rs=stkmph-smkmph
rsmps=rs * (5/18)
dl=int(input("Enter Distance covered to cross the man /length of the train:"))
time=dl/rsmps
print("Time taken by train to cross the man walking is :", time , "seconds")
