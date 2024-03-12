import pymongo
import datetime

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['Smriti']
    collection = db['hotel']
    
    print("+----- Hotel Management system ----+\n1. Check in\n2. Show guest list \n3. Check out \n4. Get info of guest \n5. Exit\n+----------------------------------+")
    choice=int(input("Enter the number of the program you desire to run:"))
    total_rooms = list(range(1, 21))

    match choice:
        case 1:
            print("****Check In****")
            name=input("Enter your name: ")
            x = datetime.datetime.now()
            y=int(x.strftime("%H"))
            if (y>=7 and y<12):
                print("Good morning,", name, "!!")
            elif (y>=12 and y<18):
                print("Good afternoon,", name, "!!")
            elif (y>=18 and y<22):
                print("Good evening,", name, "!!")
            else:
                print("Sorry", name, "We are closed!!!\nWe're open from 7:00 AM to 9:59 PM everyday.")
            rooms=collection.find()
            arrayroom=[]
            for item in rooms:
                if 'room_no' in item:
                    arrayroom.append(item['room_no'])
            difference = set(total_rooms) - set(arrayroom)
            print('Available rooms:', difference)
            no_rooms=int(input('How many rooms do you want:'))
            roomslist=[]
            for i in range(1,no_rooms+1):
                room=int(input('Choose any room from the above chart:'))
                roomslist.append(room)
            diff= set(difference) & set(roomslist)
            difflist=list(diff)
            if sorted(roomslist) != sorted(difflist):
                print("Please choose rooms from the chart only")
            else:
                email=input('Enter your email id: ')
                no_of_person=int(input('Enter the no of people: '))
                per=[]
                for i in range (no_of_person):
                    persons=input('Enter the names: ')
                    per.append(persons)
                no_of_days=int(input('Enter the number of days you will be staying: '))
                for item in roomslist:
                    collection.insert_one({'name' : name , 'room_no' : item , 'email' : email , 'persons' : per, 'no_of_days' : no_of_days})
                print("Rooms have been aloted to",name)
        case 2:
            print("****Guest list****\nName\t\t\tRoom no.")
            room=collection.find({}, { 'name': 1, 'room_no' : 1, '_id' : 0 })
            for item in room:
                print(item['name'],item['room_no'],sep='\t\t\t')
        case 3:
            print("****Check out****")
            name=input("Enter your name: ")
            alotedroom=collection.find({'name': name},{'room_no' : 1, '_id':0})
            for item in alotedroom:
                print(item)
            choice2=input('Do you want to check out from all the rooms(y/n)? ')
            if choice2 == 'y':
                collection.delete_many({'name' : name})
            elif choice2 == 'n':
                no_room=int(input('How many room you want to leave? '))                
                for i in range(no_room):
                    room=int(input('Enter the room no.: '))
                    collection.delete_one({'name' : name, 'room_no' : room})
            print("Thank you!! Visit again")
        case 4:
            print("****Guest details****")
            name=input("Enter your name: ")
            email=input("Enter your email: ")
            details = collection.distinct({'name' : name, 'email' : email})
            for items in details:
                print(items)
        case 5:
            print("****Exit****")
        case _:
            print("Input error")
