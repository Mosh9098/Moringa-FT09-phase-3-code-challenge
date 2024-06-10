from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        
    def __repr__(self):
        return f'<Magazine {self.name}>'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id=?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def contributors(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT author_id FROM articles WHERE magazine_id=?", (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Author(author["author_id"], None) for author in authors]

    def article_titles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id=?", (self.id,))
        titles = cursor.fetchall()
        conn.close()
        return [title["title"] for title in titles]

    def contributing_authors(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT author_id, COUNT(*) as count FROM articles WHERE magazine_id=? GROUP BY author_id HAVING count > 2", (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Author(author["author_id"], None) for author in authors]

