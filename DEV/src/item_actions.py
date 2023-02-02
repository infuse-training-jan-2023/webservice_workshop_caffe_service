from item_repository import ItemRepository

class ItemActions:
    def __init__(self) -> None:
        self.item_repo = ItemRepository()

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