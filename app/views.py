from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm
from .models import Category, News


@app.route('/')
def index():
    news_list = News.query.all()
    categories = Category.query.all()
    return render_template('index.html',
                           news=news_list,
                           categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    categories = Category.query.all()
    return render_template('news_detail.html',
                           news=news,
                           categories=categories)


@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template('category.html',
                           news=news,
                           category_name=category_name,
                           categories=categories)
