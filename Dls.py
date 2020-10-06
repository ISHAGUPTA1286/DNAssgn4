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
    # take the userid and wallet amount and add subscription
    pass


def updateSubscription():
    # take the subscription_id and added amount and update the wallet
    pass


def showUserSubscriptions():
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
    # take firstname as input and give info about the user
    pass


def searchDeliveriesUserIsSending():
    # give all the deliveries pending for the user as sender
    pass


def searchAllDeliveriesUserIsReceiving():
    pass


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
                print("5. show available containers")
                print("6. show all containers")
                print("7. show available bees")
                print("8. show all beehives")
                print("9. show all Deliveries")
                print("10. Send courier")
                print("11. update user location")
                print("12. update station location")
                print("13. complete delivery")
                print("14. dock The Container With ID To Bee Hive With Id")
                print("15. undock The Container With ID ")
                print("16. Show delivery status ")
                print("17. Delete User ")
                print("18. Find bees in the location ")
                print("19. Find hive capacity")
                print("20. Find time passed for the delivery")
                # print("9. show all Deliveries")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 25:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
