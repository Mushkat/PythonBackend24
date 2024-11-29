from typing import List

from models.comment import Comment
from models.user import User


def filter_comments_by_author(comments: List[Comment], author: User) -> List[Comment]:
    """
    Отфильтровывает комментарии по айди автора.

    :param comments: Список комментариев, где каждый комментарий — экземпляр класса Comment.
    :param author: Объект пользователя, чьи комментарии нужно отфильтровать.
    :return: Список отфильтрованных комментариев.
    """
    return [comment for comment in comments if comment.author_id == author.id]
