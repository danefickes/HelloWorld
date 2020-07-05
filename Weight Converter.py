weight = input('Weight: ')
units = input("Pounds or kilograms (Lbs/Kg): ")

if units.lower() == "lbs":
    print(float(weight) / 2.2)

elif units.lower() == "kg":
    print(float(weight) * 2.2)

elif units.lower() != "lbs" or "kg":
    print("Please enter 'Lbs' or 'Kg'")