from typing import List

from models.product import Product


def extract_prices(products: List[Product]) -> List[float]:
    """
    Возвращает массив цен из массива объектов Product.

    :param products: Список продуктов, где каждый продукт — экземпляр класса Product.
    :return: Список цен.
    """
    return [product.get_price() for product in products]
