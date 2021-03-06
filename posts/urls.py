from django.conf.urls import url
from posts import views


urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="detail"),
    url(r'^update/(?P<id>\d+)/$', views.post_update, name="update"),
    url(r'^delete/(?P<id>\d+)/$', views.post_delete, name="delete"),
]