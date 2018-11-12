import os

class Config():
    SEARCH_API = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    API_KEY = os.environ.get("API_KEY")
    HEADLINES_API  = "https://newsapi.org/v2/top-headlines?country=us&country=gb&country=au&apiKey={}"
    SOURCES_API = "https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"
    NEWS_SOURCE_API = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}
