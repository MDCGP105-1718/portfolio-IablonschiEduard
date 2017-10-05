Name = input("Insert name here: ")
Age = input("Insert age here: ")
Height = input("Insert height, please specify inches or cm on paper ")
Weight = input("Insert weight, please specify pounds or kilograms on paper: ")
Eyes = input("Insert eye colour: ")
Hair = input("Insert hair colour: ")

if int(Age)<=60:
    print("You are young")
else:
    print("You are still young")

if int(Height)>=180: #height measured in cm
    print("You should go pro!")

if int(Weight)>=120: #weight measured in kilograms
    print("You should try exercising a bit more!")
    
