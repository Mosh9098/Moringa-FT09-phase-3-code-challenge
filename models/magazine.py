from database.connection import get_db_connection
from models.article import Article


class Magazine:
    def __init__(self, id, name, category=None):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id=?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT author_id FROM articles WHERE magazine_id=?", (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Article(None, None, None, author["author_id"], None).get_author() for author in authors]

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id=?", (self.id,))
        titles = cursor.fetchall()
        conn.close()
        return [title["title"] for title in titles]

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT author_id, COUNT(*) as count FROM articles WHERE magazine_id=? GROUP BY author_id HAVING count > 2", (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Article(None, None, None, author["author_id"], None).get_author() for author in authors]
