import unittest
from news import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_article = News("ABC News","Reuters Editorial","Foxconn's new chairman says no plan to increase production capacity outside China", "The new chairman of Foxconn said on Friday the Apple Inc supplier had no plan to increase production capacity outside China at the moment.", "https://www.reuters.com/article/us-foxconn-chairman-capacity-idUSKCN1TM0GL","https://s4.reutersmedia.net/resources_v2/images/rcom-default.png","2019-06-21T07:03:52Z","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com." )

    def test_instance(self):
        self.assertTrue(isinstance(self.news_article,News))

    def test_correct_news_init(self):
        '''
        Test  that confirms that the object is instantiated correctly.

        '''
        self.assertEqual(self.news_article.sourceName, "ABC News")
        self.assertEqual(self.news_article.author, "Reuters Editorial")
        self.assertEqual(self.news_article.title, "Foxconn's new chairman says no plan to increase production capacity outside China")
        self.assertEqual(self.news_article.description, "The new chairman of Foxconn said on Friday the Apple Inc supplier had no plan to increase production capacity outside China at the moment.")
        self.assertEqual(self.news_article.url, "https://www.reuters.com/article/us-foxconn-chairman-capacity-idUSKCN1TM0GL")
        self.assertEqual(self.news_article.urlToImage, "https://s4.reutersmedia.net/resources_v2/images/rcom-default.png")
        self.assertEqual(self.news_article.publishedAt, "2019-06-21T07:03:52Z")
        self.assertEqual(self.news_article.content, "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")

if __name__ == '__main__':
    unittest.main()