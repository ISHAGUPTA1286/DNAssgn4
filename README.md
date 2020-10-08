# DLS
It is a user-interactive populated database created on the model of DLS using MySQL, which specifies many functional requirements through the command-line interface built using python3.

## Overview 
DLS is a futuristic transportation system for the consumer-end goods via drones, set to replace the current courier delivery services. Planned to be completely manless, customers can opt for providing delivery at their doorstep via drones.

## prerequisits
 - mysql-server
 - python3 
 - pretty table 
  use```$ pip install prettytable```
 - pymysql

## Installation and Running Instructions

1. Load and populate the dataset useing following commands repectively within your mysql environment 
```SQL
SOURCE Dls.sql;
SOURCE populate.sql;
```
2. To start cli run 
```python
python3 Dls.py
```
3. Enter the username and password and you are ready to go.

## PROJECT BY: 


YouKnowWho- Anvay Karmore(2019101107), Isha Gupta(2019101111), Kushagra Garg(2019113020).


## Command Tree
- Users(u)
    - All users(u)
    - Add User(a)
    - Delete User(d)
    - Subscriptions(s)
        - Add subscription(a)
        - Show subscription for the user(s)
        - Update Subscription(u)
        - Back(q)
    - InDeliveries(i)
    - OutDeliveries(o)
    - UpdateLocation(l)
    - Station(t)
        - Add Station(a)
        - Update Station Location(u)
        - Back(q)
    - Search for a user(S)
    - Back(q)
- Deliveries(d)
    - All deliveries(d)
    - Add Delivery(a)
    - Remove the Delivery(r)
    - Show time passed for the delivery(t)
    - Back(q)
- Containers(c)
    - All Containers(c)
    - Available containers(a)
    - Dock the container in hive(d)
    - UnDock the container (u)
    - Back(q)
- Bees(b)
    - All Bees(b)
    - Available Bees(a)
    - Find bees in th location(f)
    - Update bee location(l)
    - Back(q)
- Beehives(h)
    - All Hives(h)
    - Hive Capacity(c)
    - Back(q)
- All Commands(a)
    - (1) Add User  
    - (2) Add Station  
    - (3) Show All Users  
    - (4) Show All Bees  
    - (5) show available containers
    - (6) show all containers
    - (7) show available bees
    - (8) show all beehives
    - (9) show all Deliveries
    - (10) Send courier
    - (11) update user location
    - (12) update station location
    - (13) complete delivery
    - (14) dock The Container With ID To Bee Hive With Id
    - (15) undock The Container With ID 
    - (16) Show delivery status 
    - (17) Delete User 
    - (18) Find bees in the location 
    - (19) Find hive capacity
    - (20) Find time passed for the delivery
    - (21) Take Subscription
    - (22) Update Subscription
    - (23) Show USERS Subscriptions  
    - (24) Update BEE Location
    - (25) Filter containers greater than given weight
    - (26) Search the USER 
    - (27) Search Deliveries User is Sending
    - (28) Search Deliveries USer is Receiving
    - (q) back
- Back(q)
