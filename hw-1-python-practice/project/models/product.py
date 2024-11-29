class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0  # Скидка в процентах

    def edit_category(self, new_category: str):
        """
        Изменяет категорию продукта.
        """
        self.category = new_category

    def edit_price(self, new_price: float):
        """
        Изменяет цену продукта.
        """
        self.price = new_price

    def set_sale(self, sale: int):
        """
        Устанавливает скидку на продукт.
        :param sale: Процент скидки (0-100).
        """
        if 0 <= sale <= 100:
            self.sale = sale
        else:
            raise ValueError("Скидка должна быть в пределах от 0 до 100.")

    def cancel_sale(self):
        """
        Отменяет текущую скидку.
        """
        self.sale = 0

    def get_price(self) -> float:
        """
        Возвращает цену продукта с учетом скидки.
        """
        return self.price * (1 - self.sale / 100)

    def __repr__(self) -> str:
        """
        Представляет объект в читаемом виде.
        """
        return (f"<Product(name='{self.name}', category='{self.category}', price={self.price}, "
                f"sale={self.sale}%)>")