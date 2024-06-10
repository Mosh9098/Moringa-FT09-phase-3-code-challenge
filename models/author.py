from database.connection import get_db_connection
from models.article import Article

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    def _execute_query(self, query, params=()):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result

    def articles(self):
        query = "SELECT * FROM articles WHERE author_id=?"
        articles = self._execute_query(query, (self.id,))
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def magazines(self):
        query = "SELECT DISTINCT magazine_id FROM articles WHERE author_id=?"
        magazines = self._execute_query(query, (self.id,))
        return [Article(None, None, None, None, magazine["magazine_id"]).get_magazine() for magazine in magazines]
