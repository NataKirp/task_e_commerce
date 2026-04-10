from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000
    assert product.quantity == 5


def test_new_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    new_product.name = 'Samsung Galaxy S23 Ultra'
    new_product.description = '256GB, Серый цвет, 200MP камера'
    new_product.price = 180000
    new_product.quantity = 5
