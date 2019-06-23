from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source = 'BBC News'

    return render_template('index.html', source = source)

@app.route('/source/<category>')
def categorized_sources(category):

    '''
    View categorized sources page function that returns sources that are categorized based on news topics
    '''

    return render_template('categorized-source.html',category = category)


@app.route('/source/<category>/<source>')
def source_articles(category, source):

    '''
    View sources page function that returns articles from a particular source
    '''

    return render_template('source-articles.html',category = category, source = source)