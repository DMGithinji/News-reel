from flask import render_template
from app import app
from .requests import get_sources


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'There are various examples of sources-based-on-category on this page'
    general = get_sources('general')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')
    health = get_sources('health')
    sports = get_sources('sports')

    return render_template('index.html', title = title, general = general, business = business, technology = technology, sports = sports, health = health, entertainment = entertainment, science = science)

@app.route('/source_category/<category>')
def categorized_sources(category):

    '''
    View categorized sources page function that returns sources that are categorized based on news topics.
    Utilizes the source_base_url API endpoint
    '''

    return render_template('categorized-source.html',category = category)


@app.route('/source/<sourceName>')
def source_articles(sourceName):

    '''
    View source page function that returns articles from a particular source
    Utilizes the articles_base url API endpoint

    '''

    return render_template('source-articles.html', sourceName = sourceName)

@app.route('/source/<sourceName>/<title>')
def article(sourceName,title):

    '''
    View sources page function that returns an article from a particular source
    Utilizes the articles_base url API endpoint
    '''

    return render_template('articles.html',title = title, sourceName = sourceName)