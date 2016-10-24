from django.conf.urls import url
from . import views

app_name = 'browse'
urlpatterns = [
    url(r'^$', views.browseIndex, name='index'),
]
