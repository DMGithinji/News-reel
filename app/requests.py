import urllib.request,json
from .models import Source
from .models import News

# Getting api key
api_key = None

# Getting the base urls

sources_base_url = None
news_base_url = None

def configure_request(app):
    global api_key, sources_base_url, news_base_url
    api_key = app.config['API_KEY']
    sources_base_url = app.config["CATEGORIZED_SOURCE_BASE_URL"]
    news_base_url = app.config["SOURCE_NEWS_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_source_results(get_sources_response['sources'])


    return sources_results

def process_source_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        urlLink = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        
        sources_object = Source(id,name,description,urlLink,category,language, country)
        sources_results.append(sources_object)

    return sources_results




def get_news(sourceId):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_base_url.format(sourceId,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_lists = process_news_results(get_news_response['articles'])


    return news_lists

def process_news_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        sourceName = news_item.get("source['name']")
        author = news_item.get('author')
        article_title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:    
            news_object = News(sourceName,author,article_title,description, url, urlToImage,publishedAt, content)
            news_results.append(news_object)

    return news_results
