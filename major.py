import datetime
print("+----Hotel Management System----+\n|1. Check in                    |\n|2. Show guest list             |\n|3. Check out                   |\n|4. Get info of any guest       |\n|5. Exit                        |\n+-------------------------------+")
a=int(input("Enter the number of the program you desired to run:"))
match a:
    case 1:
        print("****Check In****")
        name=input("Enter your name: ")
        x = datetime.datetime.now()
        y=int(x.strftime("%H"))
        if (y>=7 and y<12):
	        print("Good morning,", name, "!!")
        elif (y>=12 and y<18):
	        print("Good afternoon,", name, "!!")
        elif (y>=18 and y<23):
	        print("Good night,", name, "!!")
    case 2:
        print("****Guest list****")
        print(name,",",room)
    case 3:
        print("****Check out****")
        name=input("Enter your name: ")
        print("Thank you!! Visit again")
    case 4:
        print("****Guest details****")
        name=input("Enter your name: ")
    case 5:
        print("****Exit****")
    case _:
        print("Input error")