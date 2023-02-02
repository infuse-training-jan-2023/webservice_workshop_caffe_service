import sqlite3

connection = sqlite3.connect('caffe_service.db')

with open('DB/schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO menu (menu_item_id, menu_item_name, menu_item_description, menu_item_price) VALUES (?,?,?)",
    ("M1", "Java Chip Frappuccino", "Tall,Indian Espresso Roast (regular) - Default,With Whipped Cream", 50))

cursor.execute("INSERT INTO cart (menu_item_id, order_quantity, customer_name) VALUES (?,?,?)",
    ("M1", 3, "Dinesh"))

connection.commit()
connection.close()