class News:
    '''
    Categorized news class to define News Objects
    '''

    def __init__(self, sourceName, author,title,description,url,urlToImage,publishedAt,content):
        self.sourceName = sourceName
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content