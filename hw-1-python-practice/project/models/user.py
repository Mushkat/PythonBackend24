import uuid

class User:
    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str):
        """
        Изменяет имя пользователя.
        """
        self.name = new_name

    def increment_rate(self):
        """
        Увеличивает рейтинг пользователя на 1.
        """
        self.rate += 1

    def ban_user(self):
        """
        Банит пользователя.
        """
        self.is_banned = True

    def unban_user(self):
        """
        Разбанивает пользователя.
        """
        self.is_banned = False

    def __repr__(self) -> str:
        """
        Представляет объект в читаемом виде.
        """
        return (f"<User(id={self.id}, name='{self.name}', rate={self.rate}, "
                f"comments_count={self.comments_count}, banned={self.is_banned})>")