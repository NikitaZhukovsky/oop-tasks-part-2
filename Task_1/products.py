class Product:
    def __init__(self, name, store, price):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Название товара должно быть строкой")
        if isinstance(store, str):
            self.__store = store
        else:
            raise TypeError("Название магазина должно быть строкой")
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price
        else:
            raise ValueError("Цена должна быть положительным числом.")

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__price = value
        else:
            raise ValueError("Цена должна быть положительным числом.")


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        return self.__products[index]

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def sort_by_name(self):
        self.__products.sort(key=lambda product: product.name)

    def sort_by_store(self):
        self.__products.sort(key=lambda product: product.store)

    def sort_by_price(self):
        self.__products.sort(key=lambda product: product.price)

    def get_products(self):
        return self.__products

    def __add__(self, other):
        total_price = sum([product.price for product in self.__products])
        total_price += sum([product.price for product in other.__products])
        return total_price


product_one = Product("Телефон", "Магазин 1", 10000)
product_two = Product("Ноутбук", "Магазин 2", 50000)
product_three = Product("Машина", "Магазин 3", 2000000)

product_one.price = 12000

warehouse = Warehouse()
warehouse.add_product(product_one)
warehouse.add_product(product_two)
warehouse.add_product(product_three)

print("Список товаров:")
for index, product in enumerate(warehouse.get_products(), start=1):
    print(f"Товар {index}: {product.name}, {product.store}, {product.price} рублей")

state = True
while state:
    index = input("Введите индекс для поиска товара: ")
    if index.isdigit() and (0 <= int(index) < len(warehouse.get_products())):
        index = int(index)
        state = False
    else:
        print("Неверный ввод индекса!")

product = warehouse.get_product_by_index(index)
if product:
    print(f"Товар {index + 1}: {product.name}, {product.store}, {product.price} рублей")
else:
    print("Товар не найден")

state = True
while state:
    name = input("Введите название товара для поиска: ")
    product = warehouse.get_product_by_name(name)
    if product:
        print(f"Товар '{name}': {product.store}, {product.price} рублей")
        state = False
    else:
        print("Товар не найден. Попробуйте ещё раз ввести название товара")


warehouse.sort_by_name()
print("Товары, отсортированные по названию:")
for product in warehouse.get_products():
    print(f"{product.name}, {product.store}, {product.price} рублей")

warehouse.sort_by_store()
print("Товары, отсортированные по магазину:")
for product in warehouse.get_products():
    print(f"{product.name}, {product.store}, {product.price} рублей")

warehouse.sort_by_price()
print("Товары, отсортированные по цене:")
for product in warehouse.get_products():
    print(f"{product.name}, {product.store}, {product.price} рублей")

warehouse_two = Warehouse()
print("Добавлены новые товары: ")
warehouse_two.add_product(Product("Вилка", "Магазин 2", 20))
warehouse_two.add_product(Product("Книга", "Магазин 1", 300))

for index, product in enumerate(warehouse_two.get_products(), start=1):
    print(f"Товар {index}: {product.name}, {product.store}, {product.price} рублей")

total_price = warehouse + warehouse_two
print(f"Общая стоимость товаров на складе: {total_price} рублей")