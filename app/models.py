class Article:
    def __init__(self,author,title,description,url,image_url,publish_date,content,source):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publish_date = publish_date
        self.content = content
        self.source = source
class Source:   
    def __init__(self,id,name,description,category):
        self.id = id
        self.name = name
        self.description = description  
        self.category  = category
        