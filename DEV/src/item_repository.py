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
            c.execute("INSERT INTO cart (menu_item_id, order_quantity, customer_name) VALUES (?,?,?)",
            (menu_item_id, order_quantity, customer_name))
            conn.commit()
            conn.close()
            return {
                'cart_id': c.lastrowid,
                'menu_item_id': menu_item_id,
                'order_quantity': order_quantity,
                'customer_name': customer_name
            }
        except Exception as e:
            raise Exception("Errors: ", e)