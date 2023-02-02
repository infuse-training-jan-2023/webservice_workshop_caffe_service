from item_repository import ItemRepository

class ItemActions:
    def __init__(self) -> None:
        self.item_repo = ItemRepository()

    def get_all_cart_items(self, cust_name):
        try:
            items = self.item_repo.get_all_cart_items(cust_name)
            res = []
            for item in items:
                res.append({
                    'cart_id': item[0],
                    'menu_item_id': item[1],
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