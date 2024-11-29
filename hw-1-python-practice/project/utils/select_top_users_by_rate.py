from typing import List

from models.user import User


def select_top_users_by_rate(users: List[User], top_size: int) -> List[User]:
    """
    Выбирает топ пользователей с максимальным рейтингом.

    :param users: Список пользователей, где каждый пользователь — экземпляр класса User.
    :param top_size: Количество пользователей, которых нужно выбрать.
    :return: Список пользователей с наибольшим рейтингом.
    """
    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]
