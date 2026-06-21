import sqlite3


connection = sqlite3.connect("livestock.db")

cursor = connection.cursor()


health_data = [

(1,1,"Normal",38.2,"Healthy"),

(2,2,"Cold stress",40.1,"Monitor"),

(3,3,"Foot infection",39.8,"Needs treatment"),

(4,4,"Weakness",37.9,"Low energy"),

(5,5,"Normal",38.4,"Healthy")

]


cursor.executemany("""

INSERT INTO health_report
VALUES (?,?,?,?,?)

""", health_data)


connection.commit()

connection.close()


print("Health reports added")