# \posts\views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from posts.models import Post
import datetime
from django.contrib.auth.models import User

from pipeline.views import sort_posts_recent, sort_posts_popular, sort_posts_unpopular

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
            #unsorted_posts = Post.objects.all()
            #sorted_posts = sort_posts_recent(unsorted_posts)
            return redirect('/')
    return render(request, 'posts/add_post.html', {'errors': errors})

def delete_todays_post(request):
    '''temporary function to delete all posts with dates equal to current date. Will not be in final version'''

    now = datetime.datetime.now().date()
    Post.objects.filter(post_date__contains = now).delete()
    return render(request, '../templates/success.html',)

def individual_post(request, postid):
    '''acts a profile for an individual post, displaying username, date/time, and votes'''
    
    try:
        postid = int(postid)
    except ValueError:
        raise Http404()
    posts = sort_posts_recent(Post.objects.all())
    kwargs = {"posts": posts, 'postid': postid}
    if 'q' in request.GET:
        q = request.GET['q']
        if (q == 'Upvote'):
            for post in posts:
                if (post.id == postid):
                    post.votes += 1
                    post.save()
            return redirect('/post/' + str(postid), **kwargs)
        elif (q == 'Downvote'):
            for post in posts:
                if (post.id == postid):
                    post.votes -= 1
                    post.save()
            return redirect('/post/' + str(postid), )
        elif (q == 'Delete'):
            for post in posts:
                if (post.id == postid):
                    post.delete()
            return redirect('/success/') 

    return render(request, 'posts/individual_post.html', {'posts': posts, 'postid': postid})


def browse(request, postfilter):
    '''browses through posts with various filters'''
    
    now = datetime.datetime.now()
    unsorted_posts = Post.objects.all()
    if (postfilter == 'new'):
        sorted_posts = sort_posts_recent(unsorted_posts)
    elif (postfilter == 'trending'):
        sorted_posts = sort_posts_popular(unsorted_posts)
    elif (postfilter == 'worst'):
        sorted_posts = sort_posts_unpopular(unsorted_posts)

    return render(request, 'posts/browse.html', {'posts': sorted_posts, 'current_date': now})


