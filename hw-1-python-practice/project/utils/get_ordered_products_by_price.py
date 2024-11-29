from typing import List

from models.product import Product


def get_ordered_products_by_price(products: List[Product]) -> List[Product]:
    """
    Сортирует продукты по цене в порядке убывания.

    :param products: Список продуктов, где каждый продукт — экземпляр класса Product.
    :return: Отсортированный список продуктов по цене.
    """
    return sorted(products, key=lambda product: product.get_price(), reverse=True)
