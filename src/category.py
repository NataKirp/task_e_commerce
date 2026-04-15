from src.product import Product


class Category:
    """Класс для создания категорий продуктов."""

    name: str
    description: str
    products: list[Product]  # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self):
        total_category_products = 0
        for product in self.__products:
            total_category_products += product.quantity
        return f"{self.name}, количество продуктов: {total_category_products} шт."

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


    def middle_price(self):
        """Метод для подсчета среднего ценника товаров"""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
