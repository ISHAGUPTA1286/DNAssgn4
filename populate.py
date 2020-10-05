import subprocess as sp
import pymysql
import pymysql.cursors

# def populate_users

if __name__ == '__main__':
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
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
