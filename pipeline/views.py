from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
from posts.models import Post
from django.contrib.auth import authenticate, login

def sort_posts_recent():
    
    # This line gathers the posts from the server
    posts_data = Post.objects.all()

    # This line creates a list of tuples (Post Date, Post Object)
    post_tuples = [(single_post.post_date, single_post) for single_post in posts_data] 

    # This line sorts (descending) the list of tuples by date
    sorted_posts = [item[1] for item in sorted(post_tuples, key=lambda tup: tup[0], reverse=True)]
    
    return sorted_posts
    
def homepage(request):

    now = datetime.datetime.now()
    posts = sort_posts_recent()
    if request.user.username:
        username = request.user.username
    else:
        username = 'guest'
    return render(request, 'homepage.html', {'current_date': now, 'posts': posts, 'username': username})

def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')