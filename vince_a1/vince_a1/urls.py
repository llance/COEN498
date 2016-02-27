"""vince_a1 URL Configuration

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
import vince_animal_game.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_question', vince_animal_game.views.get_question.as_view(), name='get_question'),
    url(r'^json', vince_animal_game.views.json.as_view(), name='jsonAns'),
    url(r'^proto', vince_animal_game.views.proto.as_view(), name='protoAns'),
    url(r'^$', vince_animal_game.views.mainPage, name='mainPage'),

]
