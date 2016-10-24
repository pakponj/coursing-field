from django.conf.urls import url
from . import views

app_name = 'course'
urlpatterns = [
    url(r'^create/$', views.createCourse, name='createCourse'),
    url(r'^create/new/$', views.createNewCourse, name='createNewCourse'),
]
