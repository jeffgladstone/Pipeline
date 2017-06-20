"""pipeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from pipeline.views import homepage, profile, success, about, signup, update_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'), #{'next_page': '/'} redirects home
    url(r'^$', homepage),
    url(r'^profile/(?P<user_id>\d{1,3})/$', profile),
    url(r'^profile/(?P<user_id>\d{1,3})/update/$', update_profile),
    url(r'^success/$', success), #hasn't been used yet
    url(r'^about/$', about),
    url(r'^signup/$', signup, name='signup'),
    url(r'^', include('posts.urls')),
]