from src.category import Category
from src.product import Product


def test_category_init(category_1, category_2):
    assert category_1.name == "Category 1"
    assert category_1.description == "Description 1"

    assert category_2.name == "Category 2"
    assert category_2.description == "Description 2"

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5


def test_add_product():
    category = Category("Test Category", "Category Description")
    product = Product("Test Product", "Product Description", 100.0, 10)
    category.add_product(product)
    assert "Test Product" in category.products


def test_category_str(category_1):
    assert str(category_1) == "Category 1, количество продуктов: 13 шт."


def test_middle_price(category_1, category_without_products):
    assert category_1.middle_price() == 49.99333333333333
    assert category_without_products.middle_price() == 0
