from tests.conftest import product


def test_category_init(category_1, category_2):
    assert category_1.name == 'Category 1'
    assert category_1.description == 'Description 1'
    assert len(category_1.products) == 3

    assert category_2.name == 'Category 2'
    assert category_2.description == 'Description 2'
    assert len(category_2.products) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 5
    assert category_2.product_count == 5


def test_add_product(category_1, product):
    category_1.add_product(product)
    assert len(category_1.products) == 4
    assert product.category == category_1
