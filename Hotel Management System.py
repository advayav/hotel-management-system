import pandas as pd
import matplotlib.pyplot as plt 
global d
global df
global total_rs
print("WELCOME TO THE ORCHID")

def menu():
    print("Enter: \n1.  To check in \n2.  To check room availability \n3.  Room Service \n4.  Update Personal Information \n5.  Restaurant \n6.  Cab Service \n7.  Register for Hotel Event")
    print("8.  Booking for Personal Event \n9.  Gift Shop \n10. Payment \n11. Check out \n12. Feedback")
    print("Enter 0 to exit the program")
    c = int(input("Enter your choice: "))
    if c==1:
        checkin()
    elif c==2:
        room_avail()
    elif c==3:
        service()
    elif c==4:
        update()
    elif c==5:
        restaurant()
    elif c==6:
        cab()
    elif c==7:
        h_event()
    elif c==8:
        p_event()
    elif c==9:
        gshop()
    elif c==10:
        payment()
    elif c==11:
        checkout()
    elif c==12:
        feedback()
    elif c==0:
        exit()
    else:
        print("This input is invalid. Please try again")

#Module 1: Adding data
def checkin():
    n = []
    rn = []
    phn = []
    rtype = []
    rcost = []
    index1 = []
    day = []
    x = int(input("Enter the no. of people the data needs to be added for: "))
    for a in range(x):
        index1.append(a)
        r = int(input("Enter Room Number: "))
        rn.append(r)
        name = input("Enter Name: ")
        n.append(name)
        phone = int(input("Enter Phone Number: "))
        phn.append(phone)
        room_type = input("Enter Room Type(Suite/Single/Double): ")
        rtype.append(room_type)
        if room_type=='Suite':
            room_cost = 1000
            rcost.append(room_cost)
        if room_type=='Single':
            room_cost = 500
            rcost.append(room_cost)
        if room_type=='Double':
            room_cost = 750
            rcost.append(room_cost)
        days = int(input("Enter the number of days of stay: "))
        day.append(days)
    d = {'Room_No':rn, 'Name':n, 'Phone_No':phn, 'Room_Type':rtype,
         'Room_Cost':rcost, 'Days_of_Stay':day}
    df = pd.DataFrame(d)
    df = df.set_index('Room_No')
    print(df)
    df['Room_Service'] = 0
    df['Restaurant'] = 0
    df['Cab_Service'] = 0
    df['Hotel_Event'] = 0
    df['Personal_Event'] = 0
    df['Gift_Shop'] = 0
    df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    print("Data stored succefully")
    
    s = 0
    sg = 0
    d = 0

    for i in df['Room_Type']:
        if i=='Suite':
            s+=1
        if i=='Single':
            sg+=1
        if i=='Double':
            d+=1

    num = [s,sg,d]

    pasw=input("Enter y if you want to see a summary of room bookings: ")
    if pasw=='y' or pasw=='Y':
        plt.bar(['Suite','Single','Double'],num)
        plt.xlabel('Room Type')
        plt.ylabel('Number of Rooms Booked')
        plt.title('Room Type vs Number of Rooms Booked')
        plt.show()

    else:
        print('INVALID ENTRY!!')

    menu()

#Module 2: Checking for room availability
def room_avail():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    df = df.set_index('Room_No')
    rn = int(input("Enter the room number to be checked: "))
    
    if rn not in df.index:
        print("Room ",rn," is available for stay")
    else:
        print("Sorry this room is not available for stay")
        
    menu()

#Module 3: Room Service
def service():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    
    rn = int(input("Enter room number: "))
    df = df.set_index('Room_No')

    if rn in df.index:
        print("Enter: \n1. Housekeeping \n2. Extra Bed \n3. Laundry Services")
        x = int(input("Enter your choice: "))
        if x==1:
            t = input("Please enter a convenient time for you: ")
            print("Thank you. Housekeeping will be at your room at",t)
            amt_rs = 0
        elif x==2:
            print("Cost per bed: Rs. 500/day")
            num = int(input("Enter the number of beds you require: "))
            d = int(input("Please enter how many days you want the bed for: "))
            amt_rs = 500*num*d
        elif x==3:
            print("Cost of laundry per load: Rs. 400/day")
            num = int(input("Please enter the number of loads of laundry: "))
            d = int(input("Please enter number of days you want to do laundry: "))
            amt_rs = 400*num*d
        else:
            print("This input is invalid. Please try again.")

        df.loc[rn,'Room_Service'] = df.loc[rn,'Room_Service'] + amt_rs
        df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
        print("Total Cost of Room Service: Rs.",df.loc[rn,'Room_Service'])
        
    else:
        print("Sorry this isn't a valid room number")
        
    menu()

#Module 4: Update Days of Stay
def update():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')

    df = df.set_index('Room_No')
    
    print("To Update the Number of Days of Stay")

    rn = int(input("Enter your room number:"))

    for i, r in df.iterrows():
        if rn in (0, i):
            dos = input("Enter changed number of days:")
            df.loc[rn, 'Days_of_Stay'] = dos
            df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv', index=False)

    print("Data stored successfully!")
    print(df)

    l = []
    #To add Room_No back to the DataFrame
    for x in range(len(df.index)):
        l.append(101 + x)
    
    df['Room_No'] = l
    df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv', index=False)

    menu()


#Module 5: Restaurant
def restaurant():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')

    df = df.set_index('Room_No')
    rn = int(input("Enter room number(0 if no room is booked): "))

    print("Welcome to our Restaurant!")

    print("                 ~**MENU**~                  ")
    inx_item=['Tea','Coffee','Coca Cola','Sprite','Apple Juice','Milkshake',
          'Sweet Corn Soup','Cream of Tomato','Cream of Mushroom','Minestrone',
          'Paneer Masala','Veg Manchurian','Mixed Veggies','Aloo Matar','Pav Bhaji',
          'Biryani','Jeera Rice','Schezwan Rice','Pulao',
          'Butter Naan','Gobi Paratha','Stuffed Kulcha',
          'Ice Cream','Gulab Jamun','Malai Kulfi','Jalebi'] #indexes

    cost=[30,45,35,35,40,20,
        60,50,70,75,
        85,90,100,110,140,
        250,130,160,150,
        65,70,70,
        60,55,90,50] #data

    rest=pd.DataFrame({"Sr No":range(1,27),"Item":inx_item,"Cost":cost}) #Series
    rest.set_index("Sr No",inplace = True)
    print(rest)

    price=0
    for i in rest.index:
        food=int(input("Enter food item you would like to order: "))
        n=int(input("Enter the quantity of the item: "))
        
        price=price+(n*rest.loc[food,"Cost"])
        print(food, rest.loc[food,"Cost"])
        
        end=input("Press X to end your order or C to continue: ")
        
        if end=='C' or end=='c':
            continue
        if end=='X' or end=='x':
            break

    if rn in df.index:
        df.loc[rn,'Restaurant'] = df.loc[rn,'Restaurant']+price
        df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
        print("Total Price: ",df.loc[rn,'Restaurant'])
        print("Thank you for ordering. Enjoy your meal!!")
        
    elif rn==0:
        print("Total Price: ",price)
        print("Thank you for ordering. Enjoy your meal!!")

    else:
        print("Sorry the room number you entered is invalid")

    menu()

#Module 6: Cab Service
def cab():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')

    df = df.set_index('Room_No')
    rn = int(input("Enter room number: "))

    if rn in df.index:
        print("Here are our Cab Service Facilities")
        print("1. Mini Rs 10/km \n2. Sedan Rs 12/km \n3. Prime Sedan(with Movies) Rs 15/km \n4. Minivan Rs 20/km")

        c=int(input("Enter your choice: "))
        km=int(input("Enter distance in kilometers"))

        if(c==1):
            p=km*10
            print("Total Cost: ",p)
        elif(c==2):
            p=km*12
            print("Total Cost: ",p)
        elif(c==3):
            p=km*15
            print("Total Cost: ",p)
        elif(c==4):
            p=km*20
            print("Total Cost: ",p)
        else:
            print("Sorry, this number is not part of our database.")

        df.loc[rn,'Cab_Service'] = df.loc[rn,'Cab_Service']+p
        df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
        
        print("Total Cost of Cab Service: ",df.loc[rn,'Cab_Service'])
      
    menu()

#Module 7: Hotel Events
def h_event():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    
    df = df.set_index('Room_No')
    
    print("Upcoming Hotel Events:")
    print("1. Bose Launch Event             19-05-2022    1900hrs    Rs.300")
    print("2. Cancer Awareness Marathon     23-04-2022    0800hrs    Rs.100")
    print("3. Summer Ball                   04-05-2022    2000hrs    Rs.500")

    r_no=int(input("Enter room no.(0 if no room is booked): "))
    
    ev=int(input("Enter the serial number of the event you would like to attend: "))

    if ev<4 and ev>0:
        t=int(input("Enter number of tickets to be bought: "))
        if(ev==1):
            tp=t*300
        if(ev==2):
            tp=t*100
        if(ev==3):
            tp=t*500

        if r_no in df.index:
            df.loc[r_no,'Hotel_Event'] = df.loc[r_no,'Hotel_Event']+tp
            df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
            print("Total Cost for Hotel Events: Rs.",df.loc[r_no,'Hotel_Event'])

        elif r_no==0:
            print("Total Cost for Hotel Event: Rs.", tp)

        else:
            print("Sorry the room number you entered is invalid")
            
    else:
        print("Sorry this is not one of our options")
     
    menu()

#Module 8: Personal Events    
def p_event():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    
    df = df.set_index('Room_No')
    
    r_no=int(input("Enter room no.(0 if no room is booked): "))

    ev=int(input("Enter \n1. To host a birthday party \n2. To host a marriage ceremony \n3. To host other events: "))
    v=int(input("Enter \n1. To choose banquet hall as venue\n2. To choose lawn as venue: "))
    h=int(input("Enter the number of hours you want to book the venue for: "))

    if ev>0 and ev<4 and v>0 and v<3:
        if(ev+v==2):
            tpr=1500*h
        if(ev+v==3):
            tpr=2000*h
        if(ev+v==4):
            tpr=2500*h
        if(ev+v==5):
            tpr=2000*h

        if r_no in df.index:
            df.loc[r_no,'Personal_Event'] = df.loc[r_no,'Personal_Event']+tpr
            df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
            print("Total Cost for Personal Events: Rs.",df.loc[r_no,'Personal_Event'])

        elif r_no==0:
            print("Total Cost for Personal Events: Rs.",tpr)

        else:
            print("Sorry the room number you have entered is invalid")

    else:
        print("Sorry this is not one of our options")
    
    menu()

#Module 9: Gift Shop
def gshop():

    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    
    df = df.set_index('Room_No')
    rn = int(input("Enter room no.(0 if no room is booked): "))
    
    g=int(input("Enter \n1. To buy a purse (Rs. 150)\n2. To buy a t-shirt(Rs. 200)\n3. To buy a fridge magnet(Rs. 250) \n4. To buy handicrafts(Rs. 200): "))

    q=int(input("Enter the quantity of the item you would like to buy: "))

    if g>0 and g<5:
        if(g==1):
            tpr=150*q
        if(g==2):
            tpr=200*q
        if(g==3):
            tpr=250*q
        if(g==4):
            tpr=200*q

        if rn in df.index:
            df.loc[rn,'Gift_Shop'] = df.loc[rn,'Gift_Shop']+tpr
            df.to_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
            print("Total Cost for Gift Shop: Rs.",df.loc[rn,'Gift_Shop'])

        elif rn==0:
            print("Total Cost for Gift Shop: Rs.",tpr)

        else:
            print("Sorry the room number you entered is invalid")

    else:
        print("Sorry this is not one of our options")

    menu()

#Module 10: Payment    
def payment():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    df = df.set_index('Room_No')
    rn = int(input("Please enter your room number: "))
    if rn in df.index:
        rcost = df.Room_Cost[rn]*df.Days_of_Stay[rn]
        print("Room cost is: ", rcost)
        rscost = df.Room_Service[rn]
        print("Room service cost is: ", rscost)
        rescost = df.Restaurant[rn]
        print("Restaurant cost is: ", rescost)
        cscost = df.Cab_Service[rn]
        print("Cab Service cost is: ", cscost)
        hecost = df.Hotel_Event[rn]
        print("Hotel Events cost is: ", hecost)
        pecost = df.Personal_Event[rn]
        print("Personal Events cost is: ", pecost)
        gscost = df.Gift_Shop[rn]
        print("Gift Shop products cost is: ", gscost)
        tcost = rcost + rscost + rescost + cscost + hecost + pecost + gscost
        fcost = 1.18*tcost
        print("Final cost of stay including GST is: ", fcost)
    else:
        print("Invalid Room Number. Kindly try again. ")
    
    menu()
    
#Module 11 : Checkout
def checkout():
    df = pd.read_csv('C:\\Users\\advay\\Desktop\\Project_Final.csv')
    df = df.set_index('Room_No')
    rn = int(input("Please enter your Room Number: "))
    if rn in df.index:
        df.drop(rn, axis = 0)
        print("You have successfully checked out!")
    else:
        print("Invalid Room Number. Kindly try again. ")

    menu()
    
#Module 12: Feedback
def feedback():
    rate1 = int(input("Please rate the room service from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate1 == 1 :
        print("Not Satisfied")
    if rate1 == 2 :
        print("Mediocre")
    if rate1 == 3 :
        print("Acceptable")
    if rate1 == 4 :
        print("Good")
    if rate1 == 5 :
        print("Outstanding")

    rate2 = int(input("Please rate the hotel transport service from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate2 == 1 :
        print("Not Satisfied")
    if rate2 == 2 :
        print("Mediocre")
    if rate2 == 3 :
        print("Acceptable")
    if rate2 == 4 :
        print("Good")
    if rate2 == 5 :
        print("Outstanding")

    rate3 = int(input("Please rate the restaurant service from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate3 == 1 :
        print("Not Satisfied")
    if rate3 == 2 :
        print("Mediocre")
    if rate3 == 3 :
        print("Acceptable")
    if rate3 == 4 :
        print("Good")
    if rate3 == 5 :
        print("Outstanding")

    rate4 = int(input("Please rate the hotel events service from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate4 == 1 :
        print("Not Satisfied")
    if rate4 == 2 :
        print("Mediocre")
    if rate4 == 3 :
        print("Acceptable")
    if rate4 == 4 :
        print("Good")
    if rate4 == 5 :
        print("Outstanding")

    rate5 = int(input("Please rate the gift shop service from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate5 == 1 :
        print("Not Satisfied")
    if rate5 == 2 :
        print("Mediocre")
    if rate5 == 3 :
        print("Acceptable")
    if rate5 == 4 :
        print("Good")
    if rate5 == 5 :
        print("Outstanding")

    rate6 = int(input("Please rate the friendliness of the hotel personnel from 1 to 5 stars, where 5 stars is the best possible rating and 1 star is the worst possible rating: "))
    if rate6 == 1 :
        print("Not Satisfied")
    if rate6 == 2 :
        print("Mediocre")
    if rate6 == 3 :
        print("Acceptable")
    if rate6 == 4 :
        print("Good")
    if rate6 == 5 :
        print("Outstanding")

    feedback = input("Kindly provide some feedback on how we can improve our service and make this hotel a better getaway destination: ")
    print("***** THANK YOU FOR CHOOSING THE ORCHID. WE HOPE YOU ENJOYED YOUR STAY *****")


menu()
