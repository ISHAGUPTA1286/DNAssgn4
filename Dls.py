import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
import datetime


def Exists(model_name, field_name, field_value):
    checkuserquery = "SELECT COUNT(%s.%s) FROM %s WHERE %s.%s='%d';" % (
        model_name, field_name, model_name, model_name, field_name, field_value)
    cur.execute(checkuserquery)
    count = cur.fetchall()[0]["COUNT(%s.%s)" % (model_name, field_name)]
    if(count == 0):
        return False
    return True


def printPretty(dict_list):
    if len(dict_list) == 0:
        print("No item returned by the database.\nThis could be due to no matching input.")
        return
    x = PrettyTable()
    field_names = []
    for val in dict_list[0]:
        field_names += [val]
    x.field_names = field_names
    for val in dict_list:
        y = []
        for val2 in val:
            y += [val[val2]]
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
        query = "SELECT * FROM `BEE` where BEE.bee_id not in (SELECT TRANSIT.bee_id from TRANSIT)"
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
    try:
        query = "SELECT CONTAINER.container_id, CONTAINER.weight from CONTAINER WHERE CONTAINER.container_id not in (SELECT DOCKED.container_id from DOCKED) and CONTAINER.container_id not in (SELECT TRANSIT.container_id from TRANSIT);"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)

    except Exception as e:
        con.rollback()
        print("CONTAINER data is private to company")
        print(">>>>>>>>>>>>>", e)


def fetchOneAvailableBee():
    pass
    query = "SELECT * FROM `BEE` where BEE.bee_id not in (SELECT TRANSIT.bee_id from TRANSIT)"
    # query = "SELECT TOP 1"
    cur.execute(query)
    result = cur.fetchall()
    if(len(result) == 0):
        return -1
    else:
        return result[0]['bee_id']


def sendCourier():
    try:
        row = {}
        print("please enter delivery details")
        row['sender_id'] = int(input("Sender ID: "))
        row['receiver_id'] = int(input("Reciever ID: "))
        row['container_id'] = int(input("Container ID: "))

        # do validation for availibility of the container
        #

        # make delivry model
        query = "INSERT INTO DELIVERY VALUES(%d,%d,%d)" % (
            row['sender_id'], row['receiver_id'], row['container_id'])
        cur.execute(query)
        con.commit()

        # make delivery status model
        dt = str(datetime.datetime.now())
        query = "INSERT INTO DELIVERY_STATUS VALUES('%s','%s')" % (
            row['container_id'], dt)
        cur.execute(query)
        con.commit()

        # make delivery status=transit
        bee_id = fetchOneAvailableBee()
        if(bee_id == -1):
            print("No bee available to allocate. Sorry for your inconviniance")
            return
        query = "INSERT INTO TRANSIT VALUES(%d,%d)" % (
            row['container_id'], bee_id)
        cur.execute(query)
        con.commit()
        print('Delivery started')

    except Exception as e:
        con.rollback()
        print("Unable to add delivery")
        print(">>>>>>>>>>>>>", e)


def showAllDeliveries():
    try:
        query = "SELECT * FROM `DELIVERY`"
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)

    except Exception as e:
        con.rollback()
        print("delivery data is private to company")
        print(">>>>>>>>>>>>>", e)


def showDeliveryStatus():
    try:
        container_id = int(input("Enter the container id: "))
        query = "SELECT * from DELIVERY_STATUS where container_id=%d" % container_id
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)

        query = "SELECT * from DOCKED where container_id=%d" % container_id
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            pass
        else:
            print("THe container is docked in beehive with id %d" %
                  result[0]['hive_id'])

        query = "SELECT * from TRANSIT where container_id=%d" % container_id
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 0:
            pass
        else:
            print("THe container is in transit by bee with id %d" %
                  result[0]['bee_id'])

    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


def deleteUserWithID():
    try:
        user_id = int(input("User ID: "))
        query1 = "DELETE from SUBSCRIPTION where user_id=%d" % user_id
        query2 = "DELETE from STATION where user_id=%d" % user_id
        query3 = "DELETE from USER where user_id=%d" % user_id

        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        cur.execute(query3)
        con.commit()

        print("Successfully deleted the user")
    except Exception as e:
        con.rollback()
        print("CANNOT delete user because there might be pending deliveries or:")
        print(">>>>>>>>>>>>>", e)


def updateUserLocation():
    try:
        user_id = int(input("User Id: "))
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))
        query = "UPDATE USER SET latitude=%f, longitude=%f where user_id=%d" % (
            latitude, longitude, user_id)
        cur.execute(query)
        con.commit()
        print("Successfully updated the user location")

    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


def updateStationLocation():
    try:
        station_id = int(input("STATION Id: "))
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))
        query = "UPDATE STATION SET latitude=%f, longitude=%f where station_id=%d" % (
            latitude, longitude, station_id)
        cur.execute(query)
        con.commit()
        print("Successfully updated the station location")

    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


def completeDelivery():
    # delete delivery, delivery_status, and container things
    try:
        container_id = int(input("Enter Container ID: "))
        query4 = "DELETE from DELIVERY where container_id=%d" % container_id
        query3 = "DELETE from DELIVERY_STATUS where container_id=%d" % container_id
        query1 = "DELETE from DOCKED where container_id=%d" % container_id
        query2 = "DELETE from TRANSIT where container_id=%d" % container_id
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()
        cur.execute(query3)
        con.commit()
        cur.execute(query4)
        con.commit()

        print("Delivery completed")
    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


def dockTheContainerWithIDToBeeHiveWithId():
    try:
        container_id = int(input("Container ID: "))
        hive_id = int(input("Hive ID: "))

        # validate if container is in transit
        query = "SELECT * from TRANSIT where container_id=%d" % container_id
        cur.execute(query)
        if(len(cur.fetchall()) == 0):
            raise("The container ID is not valid")
        query = "DELETE from TRANSIT where container_id=%d" % container_id
        cur.execute(query)
        con.commit()

        query = "INSERT INTO DOCKED VALUES(%d,%d)" % (container_id, hive_id)
        cur.execute(query)
        con.commit()
        print("Succesfully docked the container")
    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


def undockTheContainerWithID():
    try:
        container_id = int(input("Container ID: "))
        # hive_id = int(input("Hive ID: "))

        # validate if container is docked
        query = "SELECT * from DOCKED where container_id=%d" % container_id
        cur.execute(query)
        if(len(cur.fetchall()) == 0):
            raise("The container ID is not valid")
        query = "DELETE from DOCKED where container_id=%d" % container_id
        cur.execute(query)
        con.commit()

        bee_id = fetchOneAvailableBee()
        if(bee_id == -1):
            raise("No available BEE")
        query = "INSERT INTO TRANSIT VALUES(%d,%d)" % (container_id, bee_id)
        cur.execute(query)
        con.commit()

        print("Succesfully undocked the container")

    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


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
    # take the userid and wallet amount and add subscription
    pass


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
    # take the subscription_id and added amount and update the wallet
    pass


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
    # show all the user subsriptions for the given user_id
    pass


def findBees():
    try:
        lat = float(input("Latitude: "))
        dlat = float(input("+/-latitude: "))
        lng = float(input("Longitude: "))
        dlng = float(input("+/-longitude: "))
    

        query = "SELECT * from BEE where BEE.latitude >%d AND BEE.latitude<%d AND BEE.longitude>%d AND BEE.longitude<%d" % (
            lat-dlat, lat+dlat, lng- dlng, lng+ dlng)
        cur.execute(query)
        result = cur.fetchall()
        printPretty(result)
    except Exception as e:
        con.rollback()
        print("ERROr")
        print(">>>>>>>>>>>>>", e)


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
    pass
    # take the given bee_id, lat and long and update


def findHiveCapacity():
    try:
        hive_id = int(input('Hive ID: '))
        
        query = "SELECT COUNT(hive_id) from BEEHIVE_HOLE where hive_id=%d"%hive_id
        
        cur.execute(query)

        printPretty(cur.fetchall())
    except Exception as e:
        print(">>>>>>>>>>>>>>>",e)

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
    # take weight as input and find all the containers with weight aboove the given weight
    pass


def findTimePassed():
    try:
        container_id = int(input("Container ID: "))

        query = "SELECT * from DELIVERY_STATUS where container_id=%d"%container_id
        cur.execute(query)
        result = cur.fetchall()
        if(len(result)==0):
            raise("No such delivery")
        current_time = datetime.datetime.now()
        bg_time = str(result[0]['bg_time'])
        print("Beginning time is: ",bg_time)
        bg_t = datetime.datetime.strptime(bg_time,'%Y-%m-%d %H:%M:%S')
        timedelta =str(current_time - bg_t)
        print("Time passed is: ",timedelta, " hours")
        
    except Exception as e:
        print(">>>>>>>>>>>>>>",e)


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
    # take firstname as input and give info about the user
    pass


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
    # give all the deliveries pending for the user as sender
    pass


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
        showAvailableContaniers()
    elif(ch == 6):
        showAllContainers()
    elif(ch == 7):
        showAvalableBees()
    elif(ch == 8):
        showAllBeehives()
    elif(ch == 9):
        showAllDeliveries()
    elif(ch == 10):
        sendCourier()
    elif(ch == 11):
        updateUserLocation()
    elif(ch == 12):
        updateStationLocation()
    elif(ch == 13):
        completeDelivery()
    elif(ch == 14):
        dockTheContainerWithIDToBeeHiveWithId()
    elif(ch == 15):
        undockTheContainerWithID()
    elif(ch == 16):
        showDeliveryStatus()
    elif(ch == 17):
        deleteUserWithID()
    elif(ch == 18):
        findBees()
    elif(ch==19):
        findHiveCapacity()
    elif(ch==20):
        findTimePassed()
    elif(ch == 21):
        addUserSubscription()
    elif(ch == 22):
        updateSubscription()
    elif (ch==23):
        showUserSubscriptions()
    elif (ch == 24):
        updateBeeLocation()
    elif(ch==25):
        findCont()
    elif (ch==26):
        searchUserWithFirstName()
    elif (ch==27):
        searchDeliveriesUserIsSending()
    elif(ch==28):
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
        tmp = sp.call('clear', shell=True)

        with con.cursor() as cur:
            while(1):
                # tmp = sp.call('clear', shell=True)
                print("Users(u)", end="\t")
                print("Containers(c)", end="\t")
                print("Deliveries(d)", end="\t")
                print("Bees(b)", end="\t")
                print("Beehives(h)", end="\t")
                print("Quit(q)")
                # print("1. Add User")  
                # print("2. Add Station")  
                # print("3. Show All Users")  
                # print("4. Show All Bees")  
                # print("5. show available containers")
                # print("6. show all containers")
                # print("7. show available bees")
                # print("8. show all beehives")
                # print("9. show all Deliveries")
                # print("10. Send courier")
                # print("11. update user location")
                # print("12. update station location")
                # print("13. complete delivery")
                # print("14. dock The Container With ID To Bee Hive With Id")
                # print("15. undock The Container With ID ")
                # print("16. Show delivery status ")
                # print("17. Delete User ")
                # print("18. Find bees in the location ")
                # print("19. Find hive capacity")
                # print("20. Find time passed for the delivery")
                # print("21. Take Subscription") # Apply for subscription
                # print("22. Update Subscription") # Updating subscription details
                # print("23. Show USERS Subscriptions ") # Show all users with subscription
                # print("24. Update BEE Location") # updates bee location
                # print("25. Filter containers greater than given weight") #filter containers greater than given weight
                # print("26. Search the USER") # Search the user with first name
                # print("27. Search Deliveries User is Sending") #SEarch deliveries which user is sending
                # print("28. Search Deliveries USer is Receiving") #SEarch deliveries which user is recieving
                ch = input("Enter choice> ")
                # tmp = sp.call('clear', shell=True)
                if ch == "q":
                    break
                elif ch=="u":
                    print("All users(u)",end="\t")
                    print("Add User(a)",end="\t")
                    print("Delete User(d)",end="\t")
                    print("Subscriptions(s)",end="\t")
                    print("InDeliveries(i)",end="\t")
                    print("OutDeliveries(o)",end="\t")
                    print("UpdateLocation(l)",end="\t")
                    print("Station(t)",end="\t")
                    print("Search for a user(S)",end="\t")
                    print("Quit(q)")

                    c = input("Enter choice> ")
                    # tmp = sp.call('clear', shell=True)
                    if c=="u":
                        showAllUsers()
                    elif c=="q":
                        continue
                    elif c=="a":
                        addUser()
                    elif c=="d":
                        deleteUserWithID()
                    elif c=="s":
                        print("Add subscription(a)",end="\t")
                        print("Show subscription for the user(s)",end="\t")
                        print("Update Subscription(u)",end="\t")
                        print("Quit(q)")

                        chr = input("Enter choice> ")
                        # tmp = sp.call('clear', shell=True)

                        if(chr=="a"):
                            addUserSubscription()
                        elif chr=="q":
                            continue
                        elif chr=="s":
                            showUserSubscriptions()
                        elif chr=="u":
                            updateSubscription()
                        else:
                            print("Command Not found!!")
                    elif c=="i":
                        searchAllDeliveriesUserIsReceiving()
                    elif c=="o":
                        searchDeliveriesUserIsSending()
                    elif c=="l":
                        updateUserLocation()
                    elif c=="t":
                        
                        print("Add Station(a)",end="\t")
                        print("Update Station Location(u)",end="\t")
                        print("Quit(q)")

                        chr = input("Enter choice> ")
                        # tmp=sp.call('clear',shell=True)

                        if(chr=="a"):
                            addStation()
                        elif chr=="q":
                            continue
                        elif chr=="u":
                            updateStationLocation()
                        else:
                            print("Command not found!!!")
                    elif c=="S":
                        searchUserWithFirstName()
                    else:
                        print("Command not found!!")

                elif ch=="c":
                    print("All Containers(c)",end="\t")
                    print("Available containers(a)",end="\t")
                    print("Dock the container in hive(d)",end="\t")
                    print("UnDock the container (u)",end="\t")
                    print("Quit(q)")

                    c = input("Enter choice> ")
                    # tmp = sp.call('clear', shell=True)

                    if c=="c":
                        showAllContainers()
                    elif c=="q":
                        continue
                    elif c=="a":
                        showAvailableContaniers()
                    elif c=="d":
                        dockTheContainerWithIDToBeeHiveWithId()
                    elif c=="u":
                        undockTheContainerWithID()
                    else:
                        print("Command not found!!")

                elif ch=="d":
                    print("All deliveries(d)",end="\t")
                    print("Add Delivery(a)",end="\t")
                    print("Remove the Delivery(r)",end="\t")
                    print("Show time passed for the delivery(t)",end="\t")
                    print("Quit(q)")
                    c = input("Enter choice> ")
                    # tmp = sp.call('clear', shell=True)

                    if c=="d":
                        showAllDeliveries()
                    if c=="q":
                        continue
                    elif c=="a":
                        sendCourier()
                    elif c=="r":
                        completeDelivery()
                    elif c=="t":
                        findTimePassed()
                    else:
                        print("Command not found!!")

                elif ch=="b":
                    print("All Bees(b)",end="\t")
                    print("Available Bees(a)",end="\t")
                    print("Find bees in th location(f)",end="\t")
                    print("Update bee location(l)",end="\t")
                    print("Quit(q)")

                    c = input("Enter choice> ")
                    # tmp = sp.call('clear', shell=True)

                    if c=="b":
                        showAllBees()
                    elif c=="q":
                        continue
                    elif c=="a":
                        showAvalableBees()
                    elif c=="f":
                        findBees()
                    elif c=="l":
                        updateBeeLocation()
                    else:
                        print("Command not found")


                elif ch=="h":
                    print("All Hives(h)",end="\t")
                    print("Hive Capacity(c)",end="\t")
                    print("Quit(q)")

                    c = input("Enter choice> ")
                    # tmp = sp.call('clear', shell=True)

                    if c=="h":
                        showAllBeehives()
                    elif c=="q":
                        continue
                    elif c=="c":
                        findHiveCapacity()
                    else:
                        print("Command not found!!!")

                else:
                    print("Command not recognized!!! Try Again.")
                    # if(ch=="u")
                    # dispatch(ch)
                tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
