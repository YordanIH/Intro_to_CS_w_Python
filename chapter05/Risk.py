age=int(input("Please enter you age :"))
bmi=int(input("Please enter your bodymass index :"))
young = age < 45
slim = bmi < 22.0
if young:
    if slim:
        print("risk is low")
    else:
        print("risk is medium")
else:
    if slim:
        print("risk is medium")
    else:
        print("risk is high")
        
