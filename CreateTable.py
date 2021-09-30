import sqlite3
import os

connection = sqlite3.connect("contact.db")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS addressbook(Sno integer primary key autoincrement,
    FirstName varchar(20) not null,LastName varchar(20) null,
    MobileNumber integer unique not null,OfficeNumber integer not null,
    mailid text not null unique,address text not null);""")
connection.commit()
connection.close()
print("Table Created Successfully")