from database.connection import get_db_connection


class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        
    def __repr__(self):
        return f'<Author {self.name}>'

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
        from models.article import Article 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def magazines(self):
        from models.magazine import Magazine 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT magazine_id FROM articles WHERE author_id=?", (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

