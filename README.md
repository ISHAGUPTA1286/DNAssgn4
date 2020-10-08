# DLS
It is a user-interactive populated database created on the model of DLS using MySQL, which specifies many functional requirements through the command-line interface built using python3.

## Overview 
DLS is a futuristic transportation system for the consumer-end goods via drones, set to replace the current courier delivery services. Planned to be completely manless, customers can opt for providing delivery at their doorstep via drones.

## Prerequisites
 - mysql-server
 - python3 
 - Following modules and libraries which can be installed using requirements.txt 
   * PyMySQL 
   * Pretty Tables
   * pyfiglet  

## Installation and Running Instructions

1. Load and populate the dataset using following commands repectively within your mysql environment:
```
source Dls.sql;
source populate.sql;
```
2. To install required modules and libraries:
```
pip3 install -r requirements.txt
```
3. To start CLI run: 
```
python3 Dls.py
```
4. Enter the username and password and you are ready to go.

## Specifications
1. Atleast five queries
 * Show All Users
 * Show All Bees
 * Show Available Containers
 * Send Courier
 * Show delivery status and many more
2. Atleast three update functions
 * Update Subscription
 * Update User location 
 * Update station location and many more.

## Working of the Model
DLS is a futuristic transportation system for the consumer-end goods via drones, set to replace the current courier delivery services. Planned to be completely manless, customers can opt for providing delivery at their doorstep via drones. The drones are called BEES. Bees are of two types: queen and workers, the queen providing intercity logistic facilities, and workers are small drones that work collaboratively, providing delivery and pickup service to the user.   

The bees are docked at HIVE, and the Hive provides charging, maintenance, and loading-unloading services to bees. The packet
to be transported needs to be placed in a user container, which is then picked up by the worker bee and transported to the nearest Hive. The user containers are then sorted (according to drop location) and are itself filled inside a bigger container which is carried by the queen.

## PROJECT BY


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
