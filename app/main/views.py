from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_news


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'News-Reel'
    general = get_sources('general')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')
    sports = get_sources('sports')

    return render_template('index.html', title = title, general = general, business = business, technology = technology, sports = sports, entertainment = entertainment, science = science)

@main.route('/source_category/<category>')
def categorized_sources(category):

    '''
    View categorized sources page function that returns sources that are categorized based on news topics.
    Utilizes the source_base_url API endpoint
    '''
    sources = get_sources(category)
    title = f'{sources[0].category}'

    return render_template('categorized-source.html',title = title, sources = sources)


@main.route('/source/<sourceId>')
def source_articles(sourceId):

    '''
    View source page function that returns articles from a particular source
    Utilizes the articles_base url API endpoint

    '''
    news_list = get_news(sourceId)
    title = f'{sourceId}'


    return render_template('source-articles.html', news_list = news_list, title = title)

@main.route('/source/<article_title>')
def article(article_title):

    '''
    View sources page function that returns an article from a particular source
    Utilizes the articles_base url API endpoint
    '''
    article_list = get_news(sourceId)
    article_title = f'{news_list.article_title}'

    return render_template('articles.html',article_title = article_title, article_list = article_list)