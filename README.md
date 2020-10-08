## Overview

It is a user-interactive populated database created on the model of Drone Logistic System using MySQL, which specifies many functional requirements through the command-line interface built using python3.

## Working of the Model
DLS is a futuristic transportation system for the consumer-end goods via drones, set to replace the current courier delivery services. Planned to be completely manless, customers can opt for providing delivery at their doorstep via drones. The drones are called BEES. Bees are of two types: queen and workers, the queen providing intercity logistic facilities, and workers are small drones that work collaboratively, providing delivery and pickup service to the user.   

The bees are docked at HIVE, and the Hive provides charging, maintenance, and loading-unloading services to bees. The packet
to be transported needs to be placed in a user container, which is then picked up by the worker bee and transported to the nearest Hive. The user containers are then

## Installation and Running Instructions

If using the mysql for the first time following commands needs to be followed. To install MySQL server on Ubuntu, run the following commands

```
sudo apt-get update
sudo apt-get install mysql-server
```

When installing the MySQL server for the first time, it will prompt for a root password that you can later login with. 

The start command is
```
mysql -u <user_name> -p <password>
```

As this application involves a login, which can be done using the USER table of the MYSQL database that exists by default. 

To create a new user, the following command can be used in MySQL environment 
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

Granting all the privileges
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```
Above commands needs to be followed by new-users only.

To load and populate the dataset use the following commands repectively within the mysql environment 

```
source Dls.sql;
source populate.sql;
```

To run the user friendly command line interface we fill need PyMySQL for connection to the MySQL server from Python

To install PyMySQL and prettyTables, ignore if already installed  

```
pip3 install PyMySQL
pip3 install PTable
pip3 install pyfiglet
```

To run the code 

```
python3 Dls.py
```

This will prompt for you to enter your username and password. Enter the username and password which we created and you are ready to go.

