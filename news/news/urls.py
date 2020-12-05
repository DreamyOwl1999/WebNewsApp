
from django.contrib import admin
from django.urls import path, include
from register import views as v1
from main.views import get_profile, get_newsSection, post_newsSection, profile_load
from main.views import title_load, title_load_get, get_articles, post_articles, describe_article
from main.views import like_article, get_likes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v1.registerUser, name="registerUser"),
    path('', include("django.contrib.auth.urls")),
    path('main/ajax/get_profile/', get_profile, name = "get_profile"),
    path('main/ajax/get_newsSection/', get_newsSection, name = "get_newsSection"),
    path('main/ajax/post_newsSection/', post_newsSection, name = "post_newsSection"),
    path('home/', v1.registerUser, name = "profile_load"),
    path('login/main/profile_load/', profile_load, name = "login/main/profile_load"),
    path('profile/title_load/',title_load, name = 'title_load' ),
    path('profile/title_load/get',title_load_get, name = 'title_load_get' ),
    path('profile/title_load/post_aricles',post_articles,   name = 'post_articles'),
    path('profile/title_load/get_aricles', get_articles, name = 'get_articles'),
    path('groot/<article_id>', describe_article, name = 'describe_article'),
    path('grootLike/', like_article, name = 'groot_like'  ),
    path('groot_get_likes/', get_likes, name = 'get_like')
]
