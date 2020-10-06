import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable

def Exists(model_name, field_name, field_value):
    checkuserquery = "SELECT COUNT(%s.%s) FROM %s WHERE %s.%s='%d';" % (
        model_name, field_name, model_name, model_name, field_name, field_value)
    cur.execute(checkuserquery)
    count = cur.fetchall()[0]["COUNT(%s.%s)"%(model_name,field_name)]
    if(count==0):
        return False
    return True

def printPretty(dict_list):
    if len(dict_list)==0:
        print("No items in the database")
        return
    x = PrettyTable()
    field_names =[]
    for val in dict_list[0]:
        field_names+=[val]
    x.field_names = field_names
    for val in dict_list:
        y=[]
        for val2 in val:
            y+=[val[val2]]
        x.add_row(y)
    print(x)


def addUser():
    try:
        row = {}
        print("Enter User Details")
        row['first_name'] = input("First Name: ")
        row['user_id'] = int(input("User ID: "))
        row['last_name'] = input("Last Name: ")
        row['latitude'] = float(input("Latitude: "))
        row['longitude'] = float(input("Longitude: "))
        row['address'] = input("Address: ")

        query = "INSERT INTO USER(user_id,first_name,last_name,latitude,longitude,address) VALUES('%d','%s','%s','%f','%f','%s')" % (
            row["user_id"], row["first_name"], row["last_name"], row["latitude"], row["longitude"], row["address"])

        cur.execute(query)
        con.commit()
        print("Succesfully added the user")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def addStation():
    try:
        row = {}
        print("Enter User Details")
        row['station_id'] = int(input("Station ID: "))
        row['user_id'] = int(input("Buy station for the user with User ID: "))
        row['latitude'] = float(input("Latitude: "))
        row['longitude'] = float(input("Longitude: "))

        query = "INSERT INTO STATION(station_id,user_id,latitude,longitude) VALUES('%d','%d','%f','%f')" % (
            row["station_id"], row["user_id"], row["latitude"], row["longitude"])

        cur.execute(query)
        con.commit()
        print("Succesfully added the station")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def addBee():
    pass
    # try:
    #     row = {}
    #     print("Enter BEE Details")
    #     row['bee_id'] = int(input("BEE ID: "))
    #     row['latitude'] = float(input("Location Latitude: "))
    #     row['longitude'] = float(input("Location Longitude: "))
    #     row['bee_class'] = input("BEE CLASS- QUEEN or WORKER: ")
    #     query = "INSERT INTO BEE(bee_id,latitude,longitude,bee_class) VALUES('%d', '%f','%f',,'%s')" %(
    #         row["bee_id"],row["latitude"],row["longitude"],row["bee_class"])
        
    #     cur.execute(query)
    #     con.commit()
    #     print("Successfully added BEE Details")
    # except Exception as e:
    #     con.rollback()
    #     print("Failed to insert BEE Details in Database")
    #     print(">>>>>>>>>>>>>",e)
    
# def addBee():
#     pass


# def addBeehive():
#     pass


# def addBeehiveHole():
#     pass


# def addContainer():
#     pass


def showAllUsers():
    try:
        query = "SELECT * FROM `USER`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    except Exception as e:
        con.rollback()
        print("You are not authorised to see all users")
        print(">>>>>>>>>>>>>", e)



def showAllBees():
    try:
        query = "SELECT * FROM `BEE`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("bee data is private to company")
        print(">>>>>>>>>>>>>", e)


def showAvalableBees():
    try:
        query = "SELECT * FROM `DOCKED_BEE`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("bee data is private to company")
        print(">>>>>>>>>>>>>", e)
    


def showAllBeehives():
    try:
        query = "SELECT * FROM `BEEHIVE`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("beehive data is private to company")
        print(">>>>>>>>>>>>>", e)


def showAllContainers():
    try:
        query = "SELECT * FROM `CONTAINER`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("CONTAINER data is private to company")
        print(">>>>>>>>>>>>>", e)


def showAvailableContaniers():
    pass


def sendCourier():
    pass


def showAllDeliveries():
    try:
        query = "SELECT * FROM `DELIVERY`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("dilivery data is private to company")
        print(">>>>>>>>>>>>>", e)

def showDeliveryStatus():
    pass


def deleteUserWithID():
    pass

def updateUserLocation():
    # take userid, lat, long as input and update the user location
    pass

def updateStationLocation():
    # take station_id, lat, longas input
    pass

def completeDelivery():
    #delete delivery, delivery_status, and container things
    pass

def dockTheBeeWithID():
    #take bee, and dock it, change delivery status to docked, change bee status to docked, delete transit status and transit bee
    pass

def undockTheBeeWithID():
    pass
    # do the opposite of docking the bee

def addUserSubscription():
    #take the userid and wallet amount and add subscription
    try:
        row={}
        print("Add Details for Subsription for User")
        row['wallet_amount'] = float(input("Enter Wallet Amount: "))
        row['user_id'] = int(input("Enter USER ID:")) 

        query = "INSERT INTO SUBSCRIPTION(wallet_amount,user_id) VALUES('%f','%d')" % (
            row["wallet_amount"] , row["user_id"])
        
        cur.execute(query)
        con.commit()
        print("You have successfully subscribed")
    except Exception as e:
        con.rollback()
        print("Subscription Failed")
        print(">>>>>>>>>>>>>", e)
    # pass

def updateSubscription():
    #take the subscription_id and added amount and update the wallet
    try:
        row = {}
        print("UPDATING SUBSCRIPTION DETAILS")
        row['user_id'] = int(input("ENTER USER ID: "))
        row['wallet_amount'] = float(input("ENTER AMOUNT TO BE ADDED: "))
        query = "UPDATE 'SUBSCRIPTION' SET wallet_amount = wallet_amount + '%d' WHERE user_id = '%d'" %(
            row['wallet_amount'],row['user_id'])

        cur.execute(query)
        con.commit()
        print("Successfully Updated")
    except Exception as e:
        con.rollback()
        print("Couldn't Update")
        print(">>>>>>>>>>>>>", e)

def showUserSubscriptions():
    #show all the user subsriptions for the given user_id
    try:
        row = {}
        print("Enter USER-ID for which you want to see SUBSCRIPTIONS")
        row['user_id'] = int(input("USER ID: "))
        query = "SELECT * FROM `SUBSCRIPTION` WHERE user_id = %d" % (row["user_id"])

        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    except Exception as e:
        con.rollback()
        print("Data is private to company")
        print(">>>>>>>>>>>>>", e)
    # pass

def findBees():
    pass
    #take lat and long and radius and find the bees in the given radius of that point

def updateBeeLocation():
    #take the given bee_id, lat and long and update
    try:
        row = {}
        print("Enter given BEE_ID and its updated location details")
        row['bee_id'] = int(input("BEE_ID: "))
        row['latitude'] = float(input("Updated Location's Latitude: "))
        row['longitude'] = float(input("Updated Location's Longitude: "))

        query = "UPDATE `BEE` SET latitude = '%f', longitude = '%f' WHERE bee_id = '%d'" % (
            row["latitude"],row["longitude"],row["bee_id"])
        
        cur.execute(query)
        con.commit()
        print(" BEE Location details updated successfully")
    except Exception as e:
        con.rollback()
        print("Could not Update location")
        print(">>>>>>>>>>>>>", e)

def findHives():
    #take the capacity as parameter and filter all the hives with capacity above given
    pass

def findCont():
    #take weight as input and find all the containers with weight aboove the given weight
    try:
        row = {}
        print("Filter containers greater than given weight ")
        row['weight'] = float(input("ENTER weight of container: "))

        query = "SELECT * FROM CONTAINER WHERE `weight`>='%f'" % (row['weight'])
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    except Exception as e:
        con.rollback()
        print("SEARCH FAILED")
        print(">>>>>>>>>>>>>", e)

def findTimePassed():
    #take delivery id as input and find the time passed from the bg_time.
    pass

def searchUserWithFirstName():
    #take firstname as input and give info about the user
    try:
       row = {}
       print("SEARCH THE USER")
       row['first_name'] = input("Enter FIRST NAME of USER: ")
       
       query = "SELECT * FROM USER WHERE first_name = '%s'" % (row['first_name']) 

       cur.execute(query)
       result = cur.fetchall()
       printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("Data is private to company")
        print(">>>>>>>>>>>>>", e)

def searchDeliveriesUserIsSending():
    #give all the deliveries pending for the user as sender
    try:
        row = {}
        print("SEARCH DELIVERIES USER IS SENDING")
        row['user_id'] = int(input("ENTER USER ID: "))
        query = "SELECT * FROM DELIVERY WHERE sender_id ='%d'" % (row['user_id'])

        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)

    except Exception as e: 
        con.rollback()
        print("Data is private to company")
        print(">>>>>>>>>>>>>", e)

def searchAllDeliveriesUserIsReceiving():
    try:
        row = {}
        print("SEARCH DELIVERIES USER IS RECEIVING")
        row['user_id'] = int(input("ENTER USER ID: "))
        query = "SELECT * FROM DELIVERY WHERE receiver_id ='%d'" % (row['user_id'])

        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    
    except Exception as e:
        con.rollback()
        print("Data is private to company")
        print(">>>>>>>>>>>>>", e)
    

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        addUser()
    elif(ch == 2):
        addStation()
    elif(ch == 3):
        showAllUsers()
    elif(ch == 4):
        showAllBees()
    elif(ch == 5):
        addStation()
    elif(ch == 6):
        showAllUsers()
    elif(ch == 7):
        showAllBees()
    elif(ch == 8):
        addStation()
    elif(ch == 9):
        showAllUsers()
    elif(ch == 10):
        showAllBees()
    elif(ch == 11):
        addStation()
    elif(ch == 12):
        showAllUsers()
    elif(ch == 13):
        showAllBees()
    elif(ch == 14):
        addStation()
    elif(ch == 15):
        showAllUsers()
    elif(ch == 16):
        showAllBees()
    elif(ch == 17):
        addUserSubscription()
    elif(ch == 18):
        updateSubscription()
    elif (ch==19):
        showUserSubscriptions()
    elif (ch == 20):
        updateBeeLocation()
    elif(ch==21):
        findCont()
    elif (ch==22):
        searchUserWithFirstName()
    elif (ch==23):
        searchDeliveriesUserIsSending()
    elif(ch==24):
        searchAllDeliveriesUserIsReceiving()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='DLS',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Add User")  # Hire an Employee
                print("2. Add Station")  # Fire an Employee
                print("3. Show All Users")  # Promote Employee
                print("4. Show All Bees")  # Employee Statistics
                
              
                print("17. Take Subscription") # Apply for subscription
                print("18. Update Subscription") # Updating subscription details
                print("19. Show USERS Subscriptions ") # Show all users with subscription
                print("20. Update BEE Location") # updates bee location
                print("21. Filter containers greater than given weight") #filter containers greater than given weight
                print("22. Search the USER") # Search the user with first name
                print("23. Search Deliveries User is Sending") #SEarch deliveries which user is sending
                print("23. Search Deliveries USer is Receiving") #SEarch deliveries which user is recieving
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

# connection = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()