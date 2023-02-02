import sqlite3

class ItemRepository:
    DBPATH = './caffe_service.db'
    # dinesh
    @staticmethod
    def connect_db():
        return sqlite3.connect(ItemRepository.DBPATH)

    @staticmethod
    def display_all_menu_items():
        try:
            conn = ItemRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from menu')
            return rows
        except Exception as e:
            raise Exception('Error: ', e)
    # dinesh
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