"""shelved URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import shelvedApp.views
import shelvedApp.amazonQuery
import shelvedApp.discogs
import shelvedApp.getFromMongo
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^register/', shelvedApp.views.register, name='register'),

    url(r'^login/', shelvedApp.views.login, name='login'),

    url(r'^books/', shelvedApp.views.addBook, name='getBooks'),

    url(r'^getbooks/', shelvedApp.getFromMongo.getBooks, name='getBooks'),

    url(r'^movies/', shelvedApp.views.addMovie, name='getMovies'),

    url(r'^library/', shelvedApp.views.delete, name='delete'),

    url(r'^getmovies/', shelvedApp.getFromMongo.getMovies, name='getMovies'),

    # url(r'^musics/', shelvedApp.views.musics.as_view(), name='getMusics'),

    # url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    # url(r'^api-token-auth/', views.obtain_auth_token),
]

