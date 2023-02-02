from item_repository import ItemRepository

class ItemActions:
    def __init__(self) -> None:
        self.item_repo = ItemRepository()

    def get_all_cart_items(self, cust_name):
        try:
            items = self.item_repo.get_all_cart_items(cust_name)
            res = []
            for item in items:
                menu_res = self.display_one_menu_item(item[1])
                print(menu_res)
                for menu in menu_res:
                    menu_item_name = menu['menu_item_name']
                res.append({
                    'cart_id': item[0],
                    'menu_item_name': menu_item_name,
                    'order_quantity': item[2],
                    'customer_name': item[3]
                })
            return res
        except Exception as e:
            print(e)
            return {}

    def add_cart_item(self, menu_item_id, order_quantity, customer_name):
        try:
            item = self.item_repo.add_cart_item(menu_item_id, order_quantity, customer_name)
            return item
        except Exception as e:
            print(e)
            return {}

    def delete_a_menu_item(self, menu_item_id):
        try:
            item = self.item_repo.delete_a_menu_item(menu_item_id)
            return item
        except Exception as e:
            print(e)
            return {}
            
    def delete_cart_item(self, cart_id):
        try:
            item = self.item_repo.delete_cart_item(cart_id)
            return item
        except Exception as e:
            print(e)
            return {}

    def update_price(self,item_id, menu_item_price):
        try:
            item = self.item_repo.update_price(item_id, menu_item_price)
            return item
        except Exception as e:
            print(e)
            return {}    

    def update_order_quantity(self, cart_id, order_quantity):
        try:
            item = self.item_repo.update_order_quantity(cart_id, order_quantity)
            return item
        except Exception as e:
            print(e)
            return {}

    def display_all_menu_items(self):
        try:
            items = self.item_repo.display_all_menu_items()
            res = []
            for item in items:
                res.append({
                'menu_item_id': item[0],
                'menu_item_name': item[1],
                'menu_item_description': item[2],
                'menu_item_price': item[3],
                })
            return res
        except Exception as e:
            print(e)
            return {}

    def display_one_menu_item(self,item_id):
        try:
            items = self.item_repo.display_one_menu_item(item_id)
            res = []
            for item in items:
                res.append({
                'menu_item_id': item[0],
                'menu_item_name': item[1],
                'menu_item_description': item[2],
                'menu_item_price': item[3],
                })
            return res
        except Exception as e:
            print(e)
            return {}

    def add_menu_item(self,menu_item_id,menu_item_name, menu_item_description,menu_item_price):
        try:
            item = self.item_repo.add_menu_item(menu_item_id,menu_item_name, menu_item_description,menu_item_price)
            return item
        except Exception as e:
            print(e)
            return {}