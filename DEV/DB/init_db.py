import sqlite3

connection = sqlite3.connect('caffe_service.db')

with open('DB/schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO menu (id, name, description, price) VALUES (?,?,?,?)",
    ("M1", "Java Chip Frappuccino", "Tall,Indian Espresso Roast (regular) - Default,With Whipped Cream", 50))

cursor.execute("INSERT INTO cart (mid, order_quantity, name) VALUES (?,?,?)",
    ("M1", 3, "Dinesh"))

connection.commit()
connection.close()