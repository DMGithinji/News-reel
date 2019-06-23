class Source:
    '''
    Categorized sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,urlLink,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.urlLink = urlLink
        self.category = category
        self.language = language
        self.country = country
