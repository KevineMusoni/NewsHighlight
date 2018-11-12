import urllib.request,json
from .models import Article,Source
# api initialise

api_key = None
sources_api = None
news_source_api = None
search_api = None
headlines_api = None

def configure_request(app):

    global api_key,sources_api,news_source_api,headlines_api
    api_key = app.config["API_KEY"]
    sources_api = app.config["SOURCES_API"]
    headlines_api = app.config["HEADLINES_API"]
    news_source_api  = app.config["NEWS_SOURCE_API"]
    search_api = app.config["SEARCH_API"]

def get_articles(articles):
    
    results =  []
    for article in articles:
        author = article.get("author")
        description = article.get("description")
        url = article.get("url")
        image_url = article.get("urlToImage")
        publish_date = article.get("publishedAt")[0:10]
        content = article.get("content")
        title = article.get("title")
        source = article.get("source")["id"]
        if image_url and content and author:
            new_article = Article(author,title,description,url,image_url,publish_date,content,source)
            results.append(new_article)

    return results

def news_sources(sources):
    results = []

    for source in sources:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        category = source.get("category")
        if description:
            new_source = Source(id,name,description,category)
            results.append(new_source)

    return results

def get_headlines():

    headlines_url = headlines_api.format(api_key)

    with urllib.request.urlopen(headlines_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        headlines = None
        if headlines_response["articles"]:
            headlines_list = headlines_response["articles"]
            headlines = get_articles(headlines_list)

    return headlines

def get_sources(category):

    sources_url = sources_api.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
    
        sources = None
        if sources_response["sources"]:
            sources_list = sources_response["sources"]
            sources = news_sources(sources_list)

    return sources

def get_sources_headlines(id):

    news_source_url = news_source_api.format(id,api_key)

    with urllib.request.urlopen(news_source_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        headlines = None
        if headlines_response["articles"]:
            headlines_list = headlines_response["articles"]
            headlines = get_articles(headlines_list)

    return headlines
        
def search_articles(search_name):

    search_url = search_api.format(search_name,api_key)

    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        results = None
        if search_response["articles"]:
            search_list = search_response["articles"]
            results = get_articles(search_list)

    return results