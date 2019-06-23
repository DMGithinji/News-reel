import unittest
from categorized_sources_model import Source

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.categorized_sources = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com", "general", "en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.categorized_sources,Source))

if __name__ == '__main__':
    unittest.main()