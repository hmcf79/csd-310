# Group 4 - Brittany Kyncl, Holly McFarland, Riese Bohnak, Mark Witt
# CSD 310 - Module 11 - Milestone 3
# 12/11/2022

import mysql.connector
from mysql.connector import errorcode

#Display the average assets from all clients.
def averageAssets(cursor):
    cursor.execute("select count(client_ID), avg(assets) from assets")
    selection = cursor.fetchall()

    for i in selection:
        print("\n{} accounts found with an average of ${:.2f} in possession.".format((i[0],i[1])))

#Display the amount of new clients in the last x months.
def monthlyNewUsers(cursor, months):
    #multiple by the average amount of days in a month
    days = months * 30.417
    cursor.execute(f"select sum(datediff(curdate(), initialization_date) <= {days}) from clients")
    selection = cursor.fetchall()

    for i in selection:
        print("\n{} accounts have been created in the last {} months.".format(i[0], months))

#Display how many clients have had over x amount of transactions in a month
def userTransactions(cursor,transactions):
    cursor.execute(f"select client_id,COUNT(*) >= {transactions} as count, extract(year from transaction_date) as year, extract(month from transaction_date) as month from transactions group by client_id, month(transaction_date), year(transaction_date)")
    selection = cursor.fetchall()
    x = 0

    for i in selection:
        x += i[1]

    print(f"\n{x} clients have had atleast {transactions} transactions in a month.")

config = {
    "user": "root",
    "password": "Maverick01!!",
    "host": "127.0.0.1",
    "database": "wilson_financial",
    "port": "3006",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    myCursor = db.cursor()

    #Averages the assets of all clients
    averageAssets(myCursor)
    
    #Input is months
    monthlyNewUsers(myCursor, 6)

    #Input is transactions per month
    userTransactions(myCursor, 2)




    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()


