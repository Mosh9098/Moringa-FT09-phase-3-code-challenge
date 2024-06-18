from database.connection import get_db_connection
from models.article import Article

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
    def __repr__(self):
        return f'<Author {self._name}>'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(self, None, article["title"], article["content"]) for article in articles]
