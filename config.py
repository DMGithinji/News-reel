import os

class Config:
    '''
    General configuration parent class
    '''
    CATEGORIZED_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&sortBy=popularity&apiKey={}'
    SOURCE_NEWS_BASE_URL = "https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}"
    SEARCH_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&page=1&pageSize=10&apiKey={}'
    API_KEY = os.environ.get('API_KEY')



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


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}