import sqlite3


connection = sqlite3.connect("livestock.db")

cursor = connection.cursor()


cursor.execute("SELECT * FROM livestock")


data = cursor.fetchall()





for animal in data:
    print(animal)


connection.close()