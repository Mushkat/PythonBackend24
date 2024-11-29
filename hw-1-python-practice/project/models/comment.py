from datetime import datetime
import uuid

class Comment:
    def __init__(self, author_id: uuid, text: str):
        self.author_id = author_id
        self.text = text
        self.create_date = datetime.now()
        self.update_date = self.create_date
        self.like_count = 0

    def edit_comment(self, new_text: str):
        """
        Редактирует текст комментария и обновляет дату изменения.
        """
        self.text = new_text
        self.update_date = datetime.now()

    def like(self):
        """
        Увеличивает количество лайков на 1.
        """
        self.like_count += 1

    def dislike(self):
        """
        Уменьшает количество лайков на 1, но не опускает ниже 0.
        """
        self.like_count = min(0, self.like_count - 1)

    def __repr__(self) -> str:
        """
        Представляет объект в читаемом виде.
        """
        return (f"<Comment(author_id={self.author_id}, text='{self.text[:15]}...', "
                f"likes={self.like_count}, created={self.create_date}, updated={self.update_date})>")
