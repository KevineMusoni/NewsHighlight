import unittest
from app.models import Article
from app.requests import get_headlines,get_sources_headlines
class TestArticle(unittest.TestCase):
    def setUp(self):
        self.new_article = Article("1","2","3","4")

    def test_init(self):
        self.assertTrue(self.new_article.author, "3")

    def test_return_articles(self):
        self.assertEqual(type(get_headlines()),list)

    def test_news_source(self):

        new_articles = get_sources_headlines("1234")
        article = new_articles[0]
        self.assertEqual(article.source,"1234")

    
