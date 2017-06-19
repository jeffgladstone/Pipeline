# \posts\views.py

from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
import datetime
from django.contrib.auth.models import User

from pipeline.views import sort_posts_recent

def search(request):
    '''sets "q" equal to a user-inputted String literal which is then used to search database for posts and users'''

    now = datetime.datetime.now()
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            unsorted_posts = Post.objects.filter(message__icontains=q)
            posts = sort_posts_recent(unsorted_posts)
            users = User.objects.filter(username__icontains=q)
            return render(request, 'posts/search_results.html', {'posts': posts, 'users': users, 'query': q, 'current_date': now})
    return render(request, 'posts/search_form.html', {'errors': errors})

def add_post(request):
    '''sets "q" equal to a user-inputted String literal which is then appended to database'''

    now = datetime.datetime.now()
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Invalid post. Try again.')
        else:
            Post.objects.create(
                message = q,
                post_date = now,
                user = request.user,
                votes = 0
            )
            unsorted_posts = Post.objects.all()
            sorted_posts = sort_posts_recent(unsorted_posts)
            return render(request, '../templates/success.html', {'current_date': now, 'posts': sorted_posts, 'user': request.user})
    return render(request, 'posts/add_post.html', {'errors': errors})

def delete_todays_post(request):
    '''temporary function to delete all posts with dates equal to current date. Will not be in final version'''

    now = datetime.datetime.now().date()
    Post.objects.filter(post_date__contains = now).delete()
    return render(request, '../templates/success.html',)

def individual_post(request, postid, vote):
    '''acts a profile for an individual post, displaying username, date/time, and votes'''

    postid = int(postid)
    vote = int(vote)
    posts = sort_posts_recent(Post.objects.all())
    if vote == 1:
        for post in posts:
            if (post.id == postid):
                post.votes += 1
                post.save()
    if vote == 2:
        for post in posts:
            if (post.id == postid):
                post.votes -= 1
                post.save()

    return render(request, 'posts/individual_post.html', {'postid': postid, 'posts': posts})

