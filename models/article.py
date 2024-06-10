class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        
    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

