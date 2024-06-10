import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_article_creation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title")
        self.assertEqual(article.title, "Test Title")

    def test_author_articles(self):
        author = Author(1, "John Doe")
        author_articles = author.articles()
        self.assertEqual(author_articles, [])

    def test_magazine_articles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine_articles = magazine.articles()
        self.assertEqual(magazine_articles, [])

    def test_magazine_contributors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine_contributors = magazine.contributors()
        self.assertEqual(magazine_contributors, [])

    def test_magazine_article_titles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article_titles = magazine.article_titles()
        self.assertEqual(article_titles, [])

    def test_magazine_contributing_authors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        contributing_authors = magazine.contributing_authors()
        self.assertEqual(contributing_authors, [])

if __name__ == "__main__":
    unittest.main()
