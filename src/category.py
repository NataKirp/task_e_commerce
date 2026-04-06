from src.product import Product


class Category:
    """Класс для создания категорий продуктов."""
    name: str
    description: str
    products: list[Product]   # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.products) if products else 0

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        product.category = self  # Назначаем категорию продукту
        self.products.append(product)
        Category.product_count += 1



if __name__ == '__main__':
    prod = [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
    categories_data = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', prod)

    print(categories_data.name)
    print(categories_data.description)
    print(categories_data.products)
    print(Category.category_count)
    print(Category.product_count)