from app import app
import urllib.request,json
from .models import categorized_sources_model

Source = categorized_sources_model.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
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
            sources_results = process_results(get_sources_response['sources'])


    return sources_results

def process_results(sources_list):
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

