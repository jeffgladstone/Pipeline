# pipeline\posts\urls.py

from django.conf.urls import url
from posts import views


urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^addpost/$', views.add_post),
    url(r'^post/(?P<postid>\d{1,2})/(?P<vote>\d{1,2})/$', views.individual_post),
    #url(r'^time/plus/(\d{1,2})/$', hours_ahead),      <------ (example from last project)
    url(r'^delete/$', views.delete_todays_post),
]