class Config:
    '''
    General configuration parent class
    '''
    CATEGORIZED_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SOURCE_ARTICLES_BASE_URL = "https://newsapi.org/v2/top-headlines?language=en&sources={}&apiKey={}"
    SEARCH_ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&page=1&pageSize=10&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True