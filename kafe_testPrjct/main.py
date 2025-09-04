import sys
sys.stdout.reconfigure(encoding='utf-8')
from classes.product import Product
from classes.order import Order
drinks =[ Product("Latte", 5.5),
            Product("Cappuccino", 3.6),
            Product("Espresso", 2.5),
            Product("Tea", 1.5),
            Product("Mocha", 4.0),
            Product("Americano", 3.0),
            Product("Macchiato", 4.5),
            Product("Hot Chocolate", 4.2),
            Product("Iced Coffee", 3.8),]

# make cicle for display menu chuse number of drink
userOrder = Order()
def display_menu(Order, drinks): # if qantity =0 just show menu else show menu with qantity
    print("\nМеню:")
    for idx, drink in enumerate(drinks, start=1):
        quantity = Order.exist_in_order(drink.get_name())
        if quantity > 0:
            print(f"{idx}. {drink.display_info()}     (В заказе: {quantity})")
        else:
            print(f"{idx}. {drink.display_info()}")
    print(f"{len(drinks)+1}. Просмотреть заказ")
    print(f"{len(drinks)+2}. Очистить заказ")
    print(f"{len(drinks)+3}. Выйти")

def chuse_drink():
    while True:
        # cleer screen
      
        display_menu(userOrder, drinks)
        choice = input("Выберите напиток по номеру (или действие): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(drinks):
               userOrder.add_item(drinks[choice - 1].get_name(), drinks[choice - 1].get_price(), 1)
                
            elif choice == len(drinks) + 1:
                if userOrder.is_empty():
                    print("Ваш заказ пуст.")
                else:
                    print("\nВаш заказ:")
                    userOrder.display_order()
            elif choice == len(drinks) + 2:
                userOrder.clear_order()
                print("Заказ очищен.")
            elif choice == len(drinks) + 3:
                print("Спасибо за визит! До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
        else:
            print("Пожалуйста, введите номер.")
    
   
chuse_drink()