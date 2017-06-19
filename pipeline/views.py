from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
from posts.models import Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def sort_posts_recent(posts_data):
    '''sorts list of posts in order by date created'''

    # This line creates a list of tuples (Post Date, Post Object)
    post_tuples = [(single_post.post_date, single_post) for single_post in posts_data] 

    # This line sorts (descending) the list of tuples by date
    sorted_posts = [item[1] for item in sorted(post_tuples, key=lambda tup: tup[0], reverse=True)]
    
    return sorted_posts
    
def homepage(request):
    '''provides user with name and date, along with plenty of links for different features'''

    first_name = 'guest'
    now = datetime.datetime.now()
    posts = sort_posts_recent(Post.objects.all())
    if request.user.username:
        username = request.user.username
        first_name = request.user.first_name
    else:
        username = 'guest'
    return render(request, 'homepage.html', {'current_date': now, 'posts': posts, 'username': username, 'first_name': first_name})

def profile(request, user_id):
    '''displays user information in detail, only if user is logged in. Also displays list of user's posts'''

    now = datetime.datetime.now()
    if not request.user.is_authenticated():
        user_id = 0
        return render(request, 'profile.html', {'user_id': user_id})
    users = User.objects.all()
    user_id = int(user_id)
    unsorted_posts = Post.objects.filter(user = user_id)
    recent_posts = sort_posts_recent(unsorted_posts)
    return render(request, 'profile.html', {'users': users, 'you': request.user, 'user_id': user_id, 'posts': recent_posts, 'current_date': now})

def success(request):
    '''simple "success" page'''

    return render(request, 'success.html')

def about(request):
    '''simple "about" page. Displays one paragraph on Pipeline background'''

    return render(request, 'about.html')