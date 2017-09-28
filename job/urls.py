from django.conf.urls import url

from . import views

app_name = "job"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.one_service, name='one_service'),
    url(r'^service/profile$', views.profile, name='profile'),
]