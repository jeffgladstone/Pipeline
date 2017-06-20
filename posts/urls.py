# pipeline\posts\urls.py

from django.conf.urls import url
from posts import views


urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^addpost/$', views.add_post),
    url(r'^post/(?P<postid>\d{1,3})/(?P<vote>\d{1})/$', views.individual_post), # \d{1,3} means any number with 1 - 3 digits
    url(r'^browse/(?P<postfilter>.+)/$', views.browse),
    url(r'^delete/$', views.delete_todays_post),
]