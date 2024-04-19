# Определяем класс Store для управления магазином
class Store:
    # Конструктор класса Store
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    # Добавление товара в магазин
    def add_item(self, product_name, price):
        self.items[product_name] = price  # Добавление/обновление товара в словарь
        print(f"Добавлен товар: {product_name}, цена: {price}")

    # Удаление товара из магазина
    def remove_item(self, product_name):
        if product_name in self.items:
            del self.items[product_name]  # Удаление товара из словаря
            print(f"Удален товар: {product_name}")
        else:
            print(f"Товар {product_name} не найден")

    # Проверка наличия и цены товара
    def get_price(self, product_name):
        if product_name in self.items:
            return self.items[product_name] # Сообщение о наличии товара и его цена
        # Обработка отсутствия товара
        else:
            print(f"Товар {product_name} не найден") # Сообщение об отсутствии товара и возврат `None`
            return None

    # Обновление цены существующего товара
    def update_price(self, product_name, new_price):
        if product_name in self.items:
            self.items[product_name] = new_price  # Обновление цены товара
            print(f"Цена товара {product_name} обновлена до {new_price}")
        else:
            print(f"Товар {product_name} не найден") # Сообщение об отсутствии товара и возврат `None`


# Создание объектов магазинов
pyaterochka = Store("Пятерочка", "ул. Ленина, 1")
desyatochka = Store("Десяточка", "ул. Гагарина, 5")
maxi = Store("Макси", "пр. Космонавтов, 10")
lenta = Store("Лента", "ш. Энтузиастов, 20")

# Добавление товаров в магазины
print("Добавление товаров в магазин Пятерочка:")
pyaterochka.add_item("Молоко", 50)
pyaterochka.add_item("Хлеб", 20)

print("Добавление товаров в магазин Десяточка:")
desyatochka.add_item("Сахар", 40)
desyatochka.add_item("Соль", 15)

print("Добавление товаров в магазин Макси:")
maxi.add_item("Кофе", 300)
maxi.add_item("Чай", 150)

print("Добавление товаров в магазин Лента:")
lenta.add_item("Мука", 50)
lenta.add_item("Рис", 70)

# Тестирование методов для магазина Пятерочка
print("Тестирование методов для магазина Пятерочка:")
pyaterochka.add_item("Йогурт", 30)
pyaterochka.update_price("Молоко", 55)
pyaterochka.remove_item("Хлеб")

# Запрашиваем и выводим цену существующего товара
print("Запрос цены товара:")
price = pyaterochka.get_price("Молоко")
if price:
    print(f"Цена на 'Молоко': {price}")

# Запрашиваем и выводим цену несуществующего товара
price = pyaterochka.get_price("Хлеб")
if price is None:
    print("Цена на 'Хлеб': Товар не найден")
