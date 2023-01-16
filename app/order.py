class Order:
    def __init__(self, id: int, username: str, desc: str, menu_items_ids: list[int]) -> None:
        self.id = id
        self.username = username
        self.desc = desc
        self.menu_items_ids = menu_items_ids