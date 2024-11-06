import sqlite3 as sql
import os

db = sql.connect("tennisvereniging.sqlite")

cursor = db.cursor()

with open("code.txt", "r") as file:
    cursor.execute(file.read())

result = cursor.fetchall()

db.close()

if os.path.exists("output.txt"):
    os.remove("output.txt")

with open("output.txt", "w") as file:
    for item in result:
        file.write(str(item) + "\n")

    file.close()
