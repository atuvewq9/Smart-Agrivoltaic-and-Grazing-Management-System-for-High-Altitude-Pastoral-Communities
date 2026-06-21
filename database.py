import sqlite3


connection = sqlite3.connect("livestock.db")

cursor = connection.cursor()


# create livestock table

cursor.execute("""
CREATE TABLE IF NOT EXISTS livestock(

animal_id INTEGER PRIMARY KEY,

name TEXT,

species TEXT,

age INTEGER,

location TEXT

)

""")


# create health table

cursor.execute("""
CREATE TABLE IF NOT EXISTS health_report(

report_id INTEGER PRIMARY KEY,

animal_id INTEGER,

disease TEXT,

temperature REAL,

status TEXT,


FOREIGN KEY(animal_id)
REFERENCES livestock(animal_id)

)

""")


connection.commit()

connection.close()


print("Tables created")