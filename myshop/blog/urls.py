from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.glavnaya, name='glavnaya'),
    url(r'^index', views.index, name='index'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^news', views.news, name='news'),
    url(r'^novosti/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),
]