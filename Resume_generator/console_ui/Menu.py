from .MenuItems import MenuItem

class Menu:
    def __init__(self, items: list[MenuItem]):
        self.items = items

    def display(self):
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item.name}")
        print("0. Back")

    def select_item(self, index: int):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def get_selection(self):
        choice = input("Select an option: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(self.items):
                return index
        return -1

    def get_menu_items(self):
        return self.items
   