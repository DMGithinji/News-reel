from app import app
import urllib.request,json
from .models import categorized_sources_model

# Getting api key
api_key = app.config['API_KEY']

# Getting the movie base url
sources_base_url = app.config["CATEGORIZED_SOURCE_BASE_URL"]
news_base_url = app.config["SOURCE_NEWS_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)


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
    for sources_item in sources_list:
        id = sources_item.get('id]')
        name = sources_item.get('name')
        description = sources_item.get('description')
        urlLink = sources_item.get('urlLink')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        if id:
            sources_object = Sources(id,name,description,urlLink,category,language, country)
            sources_results.append(sources_object)

    return sources_results

