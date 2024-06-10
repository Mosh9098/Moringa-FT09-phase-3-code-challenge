from database.connection import get_db_connection
from models.author import Author 
from models.magazine import Magazine 


class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    def get_author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id=?", (self.author_id,))
        author = cursor.fetchone()
        conn.close()
        return Author(author["id"], author["name"])

    def get_magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id=?", (self.magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        return Magazine(magazine["id"], magazine["name"], magazine["category"])
