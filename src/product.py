class Product:
    """Класс для создания продукта."""

    name: str
    description: str
    price: float
    quantity: int

    products_dict = []

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_dict.append(self)

    @classmethod
    def new_product(cls, products_dict):
        """Метод для создания нового объекта класса"""
        name = products_dict.get('name')
        description = products_dict.get('description')
        price = products_dict.get('price')
        quantity = products_dict.get('quantity')
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер возвращает значение приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для проверки на положительное значение новой цены."""
        if new_price < 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price
