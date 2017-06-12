# \posts\views.py

from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post, Account
import datetime

from pipeline.views import sort_posts_recent

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            posts = Post.objects.filter(message__icontains=q)
            return render(request, 'posts/search_results.html', {'posts': posts, 'query': q})
    return render(request, 'posts/search_form.html', {'errors': errors})

def add_post(request):
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
                account = Account.objects.get(id = 4),  #Change ID number if database is wiped
                votes = 0
            )
            recentposts = sort_posts_recent()
            return render(request, '../templates/success.html', {'current_date': now, 'posts': recentposts})
    return render(request, 'posts/add_post.html', {'errors': errors})

def delete_todays_post(request):
    now = datetime.datetime.now().date()
    Post.objects.filter(post_date__contains = now).delete()
    return render(request, '../templates/success.html',)

def individual_post(request, postid, vote):
    postid = int(postid)
    vote = int(vote)
    posts = Post.objects.all()
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

