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

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        product.category = self  # Назначаем категорию продукту
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода списка товаров"""
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str
