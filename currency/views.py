from django.shortcuts import render, HttpResponse,redirect, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article, Comment, Currency
import pyodbc
import psycopg2 as postgre
from django.contrib import messages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
import base64
from io import BytesIO
# Create your views here.


def sqlConnect():
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                       'Server=TUNCERGUREL\SQLEXPRESS01;'
    #                       'Database=AdventureWorks2019;'
    #                       'Trusted_Connection=yes;')
    #
    # cursor = conn.cursor()
    # return cursor

    conn = postgre.connect(
        host="localhost",
        database="etldb",
        user="postgres",
        password="123456")

    # cursor = conn.cursor()
    return conn
@login_required(login_url="user:login")
def Currency(request): #Currency'nin Sql'den alındığı alan
    cur = sqlConnect().cursor()
    query = """select  * from article_currency where exchangedate = (cast(CURRENT_DATE as date)) """
    record = cur.execute(query)
    record = cur.fetchall()

    return render(request, "rates.html", {"records":record})


@login_required(login_url="user:login")
def Cryptos(request): #Currency'nin Mssql'den alındığı alan
    cur = sqlConnect().cursor()
    query2 = """select * from article_cryptocurrency order by last_updated desc, coin_no asc limit 1000"""
    data = cur.execute(query2)
    data = cur.fetchall()

    return render(request, "cryptos.html", {"datas":data})


@login_required(login_url="user:login")
def cryptomoves(request):
    keyword = request.POST.get('keyword')
    print(keyword,"keyword")
    first = keyword.upper() if keyword is not None else "BTC"
    cur = sqlConnect().cursor()
    query = """select * from article_cryptocurrency order by last_updated desc, coin_no asc limit 600"""

    cur.execute(query)
    data = cur.fetchall()


    df = pd.read_sql_query(query, cur.connection)

    crypto = df.loc[df['coin_symbol'] == first]
    # seccrypto = df.loc[df['coin_symbol'] == sec]

    time = crypto['last_updated']
    name = df[(df['coin_symbol'] == first)]['coin_name'][0:1:].values

    last_price = df[(df['coin_symbol'] == first)]['coin_usd_price'][0:1:].values
    last_change_24h = df[(df['coin_symbol'] == first)]['coin_percent_change_24h'][0:1:].values
    last_change_7d = df[(df['coin_symbol'] == first)]['coin_percent_change_7d'][0:1:].values
    last_coin_usd_market_cap = df[(df['coin_symbol'] == first)]['coin_usd_market_cap'][0:1:].values
    last_coin_usd_volume_24h = df[(df['coin_symbol'] == first)]['coin_usd_volume_24h'][0:1:].values
    last_coin_circulating_supply = df[(df['coin_symbol'] == first)]['coin_circulating_supply'][0:1:].values


    values = {"coin_name":name[0],"coin_usd_price":last_price[0],
              "coin_percent_change_24h":last_change_24h[0],
              "coin_percent_change_7d":last_change_7d[0],'coin_usd_market_cap':last_coin_usd_market_cap[0],
              "coin_usd_volume_24h":last_coin_usd_volume_24h[0],"coin_circulating_supply":last_coin_circulating_supply[0]}

    fig = go.Figure(data=go.Scatter(x=time, y=crypto['coin_usd_price'],marker_color="red"))
    fig.update_layout({"title":"{}'s Last 2 Hours".format(name[0].upper()),
                       "xaxis":{"title":"Time (UTC)"},
                       "yaxis":{"title":"Prices (USD)"},
                       "showlegend":False},
                      width=800, height=500)
    graph= plot(fig,output_type='div')


    query2 = """ select coin_symbol from article_cryptocurrency order by last_updated desc limit 20 """

    get_coins = cur.execute(query2)
    get_coins = cur.fetchall()
    coins = []
    for i in get_coins:
        coins.append(i[0])

    return render(request, "cryptomoves.html", {"graphs":graph, "values":values, "get_coins":coins})


def index(request):
    return render(request, "index.html")

@login_required(login_url="user:login")
def rates(request):
    return render(request, "rates.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale Oluşturuldu")
        return redirect("article:dashboard")

    return render(request, "addarticle.html", {"form":form})

def detail(request,id):
    # currency = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, "detail.html", {"currency": article,"comments":comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale Güncellendi")
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request, "Makale Silindi")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail", kwargs={"id": id}))






