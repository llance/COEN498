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
from django.conf.urls import url
from django.contrib import admin
import shelvedApp.views
import shelvedApp.amazonQuery
import shelvedApp.discogs
import shelvedApp.getFromMongo


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^register/', shelvedApp.views.register, name='register'),
    url(r'^login/', shelvedApp.views.login, name='login'),

    url(r'^addIbsn/', shelvedApp.views.addIbsn, name='addIbsn'),

    url(r'^books/', shelvedApp.getFromMongo.getBooks, name='getBooks'),


    url(r'^set/', shelvedApp.views.set),
    url(r'^test/', shelvedApp.amazonQuery.getBookByISBN),
]
