class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        return self.__products[index]

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return product
        return None

    def sort_by_name(self):
        self.__products.sort(key=lambda product: product.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda product: product.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda product: product.get_price())

    def get_products(self):
        return self.__products

    def __add__(self, other):
        total_price = sum([product.get_price() for product in self.__products])
        total_price += sum([product.get_price() for product in other.__products])
        return total_price


product_one = Product("Телефон", "Магазин 1", 10000)
product_two = Product("Ноутбук", "Магазин 2", 50000)
product_three = Product("Машина", "Магазин 3", 2000000)


warehouse = Warehouse()
warehouse.add_product(product_one)
warehouse.add_product(product_two)
warehouse.add_product(product_three)

# Вывод информации о товарах
print("Список товаров:")
for index, product in enumerate(warehouse.get_products(), start=1):
    print(f"Товар {index}: {product.get_name()}, {product.get_store()}, {product.get_price()} рублей")

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
    print(f"Товар {index + 1}: {product.get_name()}, {product.get_store()}, {product.get_price()} рублей")
else:
    print("Товар не найден")

state = True
while state:
    name = input("Введите название товара для поиска: ")
    product = warehouse.get_product_by_name(name)
    if product:
        print(f"Товар '{name}': {product.get_store()}, {product.get_price()} рублей")
        state = False
    else:
        print("Товар не найден. Попробуйте ещё раз ввести название товара")


warehouse.sort_by_name()
print("Товары, отсортированные по названию:")
for product in warehouse.get_products():
    print(f"{product.get_name()}, {product.get_store()}, {product.get_price()} рублей")

warehouse.sort_by_store()
print("Товары, отсортированные по магазину:")
for product in warehouse.get_products():
    print(f"{product.get_name()}, {product.get_store()}, {product.get_price()} рублей")

warehouse.sort_by_price()
print("Товары, отсортированные по цене:")
for product in warehouse.get_products():
    print(f"{product.get_name()}, {product.get_store()}, {product.get_price()} рублей")

warehouse_two = Warehouse()
print("Добавлены новые товары: ")
warehouse_two.add_product(Product("Вилка", "Магазин 2", 20))
warehouse_two.add_product(Product("Книга", "Магазин 1", 300))

for index, product in enumerate(warehouse_two.get_products(), start=1):
    print(f"Товар {index}: {product.get_name()}, {product.get_store()}, {product.get_price()} рублей")

total_price = warehouse + warehouse_two
print(f"Общая стоимость товаров на складе: {total_price} рублей")