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


def addBeehive():
    pass


def addBeehiveHole():
    pass


def addContainer():
    pass


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
    pass

def updateSubscription():
    #take the subscription_id and added amount and update the wallet
    pass

def showUserSubscriptions():
    #show all the user subsriptions for the given user_id
    pass

def findBees():
    pass
    #take lat and long and radius and find the bees in the given radius of that point

def updateBeeLocation():
    pass
    #take the given bee_id, lat and long and update

def findHives():
    #take the capacity as parameter and filter all the hives with capacity above given
    pass

def findCont():
    #take weight as input and find all the containers with weight aboove the given weight
    pass

def findTimePassed():
    #take delivery id as input and find the time passed from the bg_time.
    pass

def searchUserWithFirstName():
    #take firstname as input and give info about the user
    pass

def searchDeliveriesUserIsSending():
    #give all the deliveries pending for the user as sender
    pass

def searchAllDeliveriesUserIsReceiving():
    pass
# def hireAnEmployee():
#     """
#     This is a sample function implemented for the refrence.
#     This example is related to the Employee Database.
#     In addition to taking input, you are required to handle domain errors as well
#     For example: the SSN should be only 9 characters long
#     Sex should be only M or F
#     If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
#     HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
#     """
#     try:
#         # Takes emplyee details as input
#         row = {}
#         print("Enter new employee's details: ")
#         name = (input("Name (Fname Minit Lname): ")).split(' ')
#         row["Fname"] = name[0]
#         row["Minit"] = name[1]
#         row["Lname"] = name[2]
#         row["Ssn"] = input("SSN: ")
#         row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
#         row["Address"] = input("Address: ")
#         row["Sex"] = input("Sex: ")
#         row["Salary"] = float(input("Salary: "))
#         row["Dno"] = int(input("Dno: "))

#         query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
#             row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

#         print(query)
#         cur.execute(query)
#         con.commit()

#         print("Inserted Into Database")

#     except Exception as e:
#         con.rollback()
#         print("Failed to insert into database")
#         print(">>>>>>>>>>>>>", e)

#     return


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