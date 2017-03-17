from django.conf.urls import url
from . import views # . artinya mau ngambil views di folder yang sama kaya folder urls (sama2 di folder poll)

urlpatterns = [
    # /poll/
    url(r'^$', views.index, name='index'),
    # /poll/help_me
    url(r'^help_me/$', views.help_me, name='help_me'),
]
