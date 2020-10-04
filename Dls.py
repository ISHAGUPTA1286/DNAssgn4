import subprocess as sp
import pymysql
import pymysql.cursors


def Exists(model_name, field_name, field_value):
    checkuserquery = "SELECT COUNT(%s.%s) FROM %s WHERE %s.%s='%d';" % (
        model_name, field_name, model_name, model_name, field_name, field_value)
    cur.execute(checkuserquery)
    count = cur.fetchall()[0]["COUNT(%s.%s)"%(model_name,field_name)]
    if(count==0):
        return False
    return True


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
    pass


def showAllBees():
    pass


def showAvalableBees():
    pass


def showAllBeehives():
    pass


def showAllContainers():
    pass


def showAvailableContaniers():
    pass


def sendCourier():
    pass


def showAllDeliveries():
    pass


def showDeliveryStatus():
    pass


def deleteUserWithID():
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
    # elif(ch == 3):
    #     option3()
    # elif(ch == 4):
    #     option4()
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
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
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
