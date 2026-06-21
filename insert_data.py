import sqlite3


connection = sqlite3.connect("livestock.db")

cursor = connection.cursor()


cursor.execute("DELETE FROM livestock")
cursor.execute("DELETE FROM health_report")


animals = [

(1,"Tashi","Yak",5,"Nubra Valley, Ladakh"),

(2,"Dolma","Pashmina Goat",3,"Changthang, Ladakh"),

(3,"Stanzin","Sheep",4,"Leh, Ladakh"),

(4,"Norbu","Goat",2,"Kargil, Ladakh"),

(5,"Lhamo","Yak",7,"Pangong Region, Ladakh")

]


cursor.executemany("""

INSERT INTO livestock
VALUES (?,?,?,?,?)

""", animals)








connection.commit()

connection.close()


print("5 Ladakh animals added")