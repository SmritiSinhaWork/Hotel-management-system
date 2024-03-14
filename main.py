import pymongo
import datetime


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['Smriti']
    collection = db['hotel']
    
    while True:
        print('+----- Hotel Management system ----+\n1. Check in\n2. Show guest list \n3. Check out \n4. Get info of guest \n5. Exit\n+----------------------------------+')
        choice=int(input('Enter the number of the program you desire to run:'))
        total_rooms = list(range(1, 21))
        match choice:
            case 1:
                print('****Check In****')
                date = datetime.datetime.now()
                hour = date.hour
                
                def greet(name):
                    if 7<= hour <12:
                        return f'Good morning, {name}!!'
                    elif 12<= hour <18:
                        return f'Good afternoon, {name}!!'
                    elif 18<= hour <23:
                        return f'Good evening, {name}!!'
                    else:
                        return f'Good day, {name}!!'
                name=input('Enter your name: ')
                print(greet(name))
            
                def availableroom():
                    global difference
                    rooms=collection.find()
                    arrayroom=[]
                    for item in rooms:
                        if 'room_no' in item:
                            arrayroom.append(item['room_no'])
                    difference = set(total_rooms) - set(arrayroom)
                    return f'Available rooms:, {difference}'
                print(availableroom())
                def checkin(no_rooms):
                    roomslist=[]
                    for i in range(1,no_rooms+1):
                        room=int(input('Choose any room from the above chart:'))
                        roomslist.append(room)
                    difflist=list(set(difference) & set(roomslist))
                    if sorted(roomslist) != sorted(difflist):
                        return 'Please choose rooms from the chart only'
                    else:
                        email=input('Enter your email id: ')
                        no_of_person=int(input('Enter the no of people: '))
                        per=[]
                        for i in range (no_of_person):
                            persons=input('Enter the names: ')
                            per.append(persons)
                        no_of_days=int(input('Enter the number of days you will be staying: '))
                        for item in roomslist:
                            collection.insert_one({'name' : name , 'room_no' : item , 'email' : email , 'persons' : per, 'no_of_days' : no_of_days, 'no_of_person' : no_of_person, 'checkin_time' : date.strftime("%Y-%m-%d %H:%M:%S")})
                        return f'Rooms have been alloted to {name}'
                no_rooms=int(input('How many rooms do you want:'))
                print(checkin(no_rooms))

            case 2:
                print('****Guest list****\nName\t\t\tRoom no.')
                
                def guestlist():
                    room=collection.find({}, { 'name': 1, 'room_no' : 1, '_id' : 0 })
                    for item in room:
                        print(item['name'],item['room_no'],sep='\t\t\t')
                guestlist()
            case 3:
                print('****Check out****')

                def checkout(name,email):
                    
                    room_alloted=collection.find({'name': name, 'email' : email},{'room_no' : 1, '_id':0})
                    for item in room_alloted:
                        return item
                    
                    choice=input('Do you want to check out from all the rooms(y/n)? ')
                    if choice == 'y':
                        collection.delete_many({'name' : name, 'email' : email})
                    elif choice == 'n':
                        room_num=int(input('How many room you want to leave? '))                
                        for i in range(room_num):
                            room=int(input('Enter the room no.: '))
                            collection.delete_one({'name' : name, 'room_no' : room})
                    else:
                        return 'Invalid input'
                    return 'Thank you!! Visit again'
                
                name=input('Enter your name: ')
                email=input('Enter your email: ')
                print(checkout(name,email))
            case 4:
                print('****Guest details****')
                
                def guestdetails(name,email):
                    
                    details=collection.find_one({'name' : name , 'email' : email},{'_id' : 0, 'room_no' : 0, 'no_of_person' : 0, 'no_of_days' : 0})
                    if details == None:
                        return '****No data found****'
                    else:
                        values = details.values()
                        detlist=list()
                        for value in values:
                            detlist.append(value)
                        return detlist
                        
                name=input('Enter your name: ')
                email=input('Enter your email: ')
                print(guestdetails(name,email))
            case 5:
                print('****Exit****')
                break
            case _:
                print('Input error')
client.close()
