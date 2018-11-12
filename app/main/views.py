from ..requests import get_headlines,get_sources,get_sources_headlines
from flask import render_template,request,url_for,redirect
from . import main

@main.route("/")
def index():
    headlines = get_headlines() 
    title = "Cosmos News"
    return render_template("index.html", headlines=headlines,title=title)

@main.route("/sources/<category>")
def sources(category):
    sources = get_sources(category)
    title = category.capitalize()
    header = category.capitalize()
    return render_template("news_source.html",sources = sources,title = title,header = header)

@main.route("/sources/articles/<id>")
def news_source(id):
    articles = get_sources_headlines(id)
    header = id.split("-")
    new_head = []
    for head in header:
        new_head.append(head.upper())
    final_header = " ".join(new_head)

    return render_template("articles.html",articles = articles,header = final_header,title=final_header)
