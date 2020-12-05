from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . forms import newsForm
from . models import Profile, Article
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from . models import newsSection

from django.contrib.auth.models import User
import json


def get_profile(request):
    if request.is_ajax and request.method == "GET":
        current_user = request.user
        profile = user.Profile
        serialized = serializers.serialize('json', profile)
    return JsonResponse({"Profile": serialized}, status =200)

def get_newsSection(request):
    if request.is_ajax and request.method == "GET":
        current_user = request.user
        sect = request.user.Profile.newsSection
        serialized = serializers.serialize('json', sect)
    return JsonResponse({"Sect": serialized}, status =200)

def post_newsSection(request):
    if request.is_ajax and request.method == "POST":
        if hasattr(request.user.profile, "newssection"):
            print("true")
            form = newsForm(request.POST or None, instance = request.user.profile.newssection)
            if form.is_valid():
                news = form.save()
        else:
            print("false")
            form = newsForm(request.POST or None)
            if form.is_valid():
                news = form.save()
                print("valid")
            news.profile = request.user.profile

    return JsonResponse({}, status =200)

def profile_load(request):
    context = {}
    context['form'] = newsForm()
    user = request.user.username
    return render(request, "main.html", {"form": newsForm, "name": user})

def title_load(request):
    return render(request, "titles.html", {})

def title_load_get(request):
    sections = request.user.profile.newssection.choices
    sections = sections.replace("'", "")
    sections = sections.replace(" ", "")
    sections = sections.replace("[", "")
    sections = sections.replace("]", ",")
    return JsonResponse({"choices": sections}, status =200)


def post_articles(request):
    if request.is_ajax and request.method == "POST":
        choice = request.POST.get("choice")
        print(choice)
    sections = request.user.profile.newssection.choices
    global artList
    artList = []
    for article in Article.objects.all():
        print(article.section)
        if article.section == choice:
            artList.append(article)
    articleList = artList
    print(artList)
    return JsonResponse({}, status =200)


def get_articles(request):
    print("new art", artList)
    if request.is_ajax and request.method == "GET":
        articles = serializers.serialize('json', artList)
    return JsonResponse({"articles": articles}, status =200)

def describe_article(request, article_id):
    global art
    art = Article.objects.get(pk=article_id)
    return render (request, "articles.html", {"article":art})

def like_article(request):
    if request.is_ajax and request.method == "POST":
        art.likes = art.likes + 1
        art.save()
    return JsonResponse({}, status =200)

def get_likes(request):
    if request.is_ajax and request.method == "GET":
        likes = art.likes
        print(likes)
    return JsonResponse({"likes": likes}, status =200)
