import sqlite3 as sql
import os

db = sql.connect("tennisvereniging.sqlite")

cursor = db.cursor()

with open("code.txt", "r") as file:
    cursor.execute(file.read())

result = cursor.fetchall()

db.close()

i=0
for item in result:
    i += 1
    print(f"{i}. " + str(item) + "\n")

file.close()
