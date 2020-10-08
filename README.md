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
