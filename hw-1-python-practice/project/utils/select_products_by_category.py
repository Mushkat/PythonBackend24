from typing import List

from models.product import Product


def select_products_by_category(products: List[Product], category: str) -> List[Product]:
    """
    Фильтрует продукты по заданной категории.

    :param products: Список продуктов, где каждый продукт — экземпляр класса Product.
    :param category: Категория для фильтрации.
    :return: Список продуктов, принадлежащих к заданной категории.
    """
    return [product for product in products if product.category == category]
