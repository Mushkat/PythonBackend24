from typing import List

from models.comment import Comment


def get_ordered_comments_by_likes(comments: List[Comment]) -> List[Comment]:
    """
    Сортирует комментарии по количеству лайков в порядке убывания.

    :param comments: Список комментариев, где каждый комментарий — экземпляр класса Comment.
    :return: Отсортированный список комментариев по количеству лайков.
    """
    return sorted(comments, key=lambda comment: comment.like_count, reverse=True)
