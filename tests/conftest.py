import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
# Функция, которая будет возвращать объект класса Category
def category_1():
    return Category(
        name="Category 1",
        description="Description 1",
        products=[
            Product("Product 1", "Product description 1", 100.00, 1),
            Product("Product 2", "Product description 2", 9.99, 9),
            Product("Product 3", "Product description 3", 39.99, 3),
        ],
    )


@pytest.fixture
# Функция, которая будет возвращать объект класса Category
def category_2():
    return Category(
        name="Category 2",
        description="Description 2",
        products=[
            Product("Product 1", "Product description 1", 1000.0, 10),
            Product("Product 2", "Product description 2", 99.99, 90),
        ],
    )


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def smartphone_1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
