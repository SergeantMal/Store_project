# Программа для хранения информации о товарах в магазине


# Класс магазина

class Store:
    # Инициализация магазина
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = self.items = items if items is not None else {}  # Устанавливаем словарь по умолчанию, если не передан

    # Метод добавления товара
    def add_item(self, name, price):
        self.items[name] = price

    # Метод удаления товара
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    # Метод получения цены товара
    def get_item_price(self, name):
        return self.items.get(name)

    # Метод изменения цены товара
    def change_item_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price

    # Метод вывода списка товаров
    def show_store_items(self, flag=True):
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")
        print("Список товаров:")
        for index, (name, price) in enumerate(self.items.items(), start=1):  # start=1 задаёт начало нумерации с 1
            if flag:
                print(f"{index}. {name}: {price} руб.")
            else:
                print(f"{index}. {name}")

store_list = []

# Функция добавления магазина
def add_store():
    name = input("Введите название магазина: ")
    address = input("Введите адрес магазина: ")
    return Store(name, address)

# Функции работы с магазином

# Функция добавления товара
def add_item_to_store(store):
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    store.add_item(name, price)

# Функция удаления товара
def remove_item_from_store(store):
    show_store_items(store)
    name = input("Введите название товара, который хотите удалить: ")
    try:
        store.remove_item(name)
    except KeyError:
        print(f"Товар {name} не найден в магазине.")

# Функция получения цены товара
def get_item_price_from_store(store):
    show_store_items(store, False)
    name = input("Введите название товара, цену которого хотите узнать: ")
    price = store.get_item_price(name)
    if price is not None:
        print(f"Цена товара {name}: {price} руб.")
    else:
        print(f"Товар {name} не найден в магазине.")

# Функция изменения цены товара
def change_item_price_in_store(store):
    show_store_items(store, False)
    name = input("Введите название товара, цену которого хотите изменить: ")
    new_price = float(input("Введите новую цену товара: "))
    store.change_item_price(name, new_price)

# Функция вывода списка товаров
def show_store_items(store, flag=True):
    store.show_store_items(flag)

# Функция вывода списка магазинов
def show_store_list():
    print("Список магазинов:")
    for i, store in enumerate(store_list, 1):
        print(f"{i}. {store.name}")


# Главная программа
while True:
    print("Выберите действие:")
    print("")
    print("1. Добавить магазин")
    print("2. Добавить товар в магазин")
    print("3. Удалить товар из магазина")
    print("4. Получить цену товара в магазине")
    print("5. Изменить цену товара в магазине")
    print("6. Показать список товаров в магазине")
    print("7. Показать список магазинов")
    print("0. Выход")
    print("")
    choice = input("Введите номер действия: ")
    if choice == "1":
        store = add_store()
        store_list.append(store)
    elif choice == "2":
        show_store_list()
        choice_store = int(input("Введите номер магазина, в который хотите добавить товар: "))
        store = store_list[choice_store - 1]
        add_item_to_store(store)
    elif choice == "3":
        show_store_list()
        choice_store = int(input("Введите номер магазина, в котором хотите удалить товар: "))
        store = store_list[choice_store - 1]
        remove_item_from_store(store)
    elif choice == "4":
        show_store_list()
        choice_store = int(input("Введите номер магазина, в котором хотите узнать цену товара: "))
        store = store_list[choice_store - 1]
        get_item_price_from_store(store)
    elif choice == "5":
        show_store_list()
        choice_store = int(input("Введите номер магазина, в котором хотите изменить цену товара: "))
        store = store_list[choice_store - 1]
        change_item_price_in_store(store)
    elif choice == "6":
        show_store_list()
        choice_store = int(input("Введите номер магазина, в котором хотите узнать список товаров: "))
        store = store_list[choice_store - 1]
        show_store_items(store)
    elif choice == "7":
        show_store_list()
    elif choice == "0":
        break

