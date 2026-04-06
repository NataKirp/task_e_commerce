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
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products) if products else 0

    def add_product(self, product):
        """Метод для добавления продукта в категорию."""
        product.category = self  # Назначаем категорию продукту
        self.products.append(product)
        Category.product_count += 1
