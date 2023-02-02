import sqlite3

class ItemRepository:
    DBPATH = "./caffe_service.db"

    @staticmethod
    def connect_db():
        return sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def get_all_cart_items(cust_name):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from cart where customer_name=?', (cust_name,))
            return rows
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def add_cart_item(menu_item_id, order_quantity, customer_name):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            insert_cursor = c.execute("INSERT INTO cart (menu_item_id, order_quantity, customer_name) VALUES (?,?,?)",
            (menu_item_id, order_quantity, customer_name))
            conn.commit()
            conn.close()
            return {
                'cart_id': insert_cursor.lastrowid,
                'menu_item_id': menu_item_id,
                'order_quantity': order_quantity,
                'customer_name': customer_name
            }
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def delete_a_menu_item(menu_item_id):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            c.execute("DELETE FROM menu WHERE menu_item_id=?",(menu_item_id,))
            conn.commit()
            conn.close()
            return {
                'Message': f'Menu item {menu_item_id} deleted successfully'
            }
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def delete_cart_item(cart_id):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            c.execute("DELETE FROM cart WHERE cart_id=?",(cart_id,))
            conn.commit()
            conn.close()
            return {
                'Message': f'Cart item {cart_id} deleted successfully'
            }
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def update_order_quantity(cart_id, order_quantity):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            c.execute("update cart set order_quantity=? where cart_id=?", (order_quantity, cart_id,))
            conn.commit()
            conn.close()
            return {
                # 'cart_id': cart_id,
                # 'order_quantity': order_quantity,
                'Message': f'Order quantity updated as {order_quantity}'
            }
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def update_price(item_id, menu_item_price):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            c.execute("update menu set menu_item_price=? where menu_item_id=?", (menu_item_price, item_id,))
            conn.commit()
            conn.close()
            return {
                'menu_item_id': item_id,
                'menu_item_price': menu_item_price,
            }
        except Exception as e:
            raise Exception("Errors: ", e)

    @staticmethod
    def display_all_menu_items():
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from menu')
            return rows
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def display_one_menu_item(item_id):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from menu where menu_item_id=?', (item_id,))
            return rows
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def add_menu_item(menu_item_id,menu_item_name, menu_item_description,menu_item_price):
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            c.execute('insert into menu(menu_item_id,menu_item_name, menu_item_description, menu_item_price) values(?,?,?,?)', 
            (menu_item_id, menu_item_name, menu_item_description,menu_item_price))
            conn.commit()
            return {
                'menu_item_id': menu_item_id,
                'menu_item_name': menu_item_name,
                'menu_item_description': menu_item_description,
                'menu_item_price': menu_item_price
          }
        except Exception as e:
          raise Exception('Error: ', e)

