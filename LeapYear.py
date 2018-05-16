year = input("Input Leap Year: ")
if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            print(year + " is a leap year")
        else:
            print(year + " is not a leap year")
    elif int(year) < 100:
        print(year + " is a leap year")
    else:
        print(year + " is not a leap year")
else:
    print(year + " is not a leap year")
