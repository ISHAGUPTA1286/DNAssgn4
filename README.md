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
2. Atleast three update functions
 * 

## Working of the Model
DLS is a futuristic transportation system for the consumer-end goods via drones, set to replace the current courier delivery services. Planned to be completely manless, customers can opt for providing delivery at their doorstep via drones. The drones are called BEES. Bees are of two types: queen and workers, the queen providing intercity logistic facilities, and workers are small drones that work collaboratively, providing delivery and pickup service to the user.   

The bees are docked at HIVE, and the Hive provides charging, maintenance, and loading-unloading services to bees. The packet
to be transported needs to be placed in a user container, which is then picked up by the worker bee and transported to the nearest Hive. The user containers are then sorted (according to drop location) and are itself filled inside a bigger container which is carried by the queen.

## PROJECT BY

YouKnowWho- Anvay Karmore(2019101107), Isha Gupta(2019101111), Kushagra Garg(2019113020).
