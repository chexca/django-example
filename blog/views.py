# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post
from blog.forms.create_post_form import CreatePostForm


def index(request):

    published_posts = Post.objects.filter(published_date__isnull=False)
    not_published_posts = Post.objects.filter(published_date__isnull=True)

    context = {'published_posts': published_posts, 'not_published_posts': not_published_posts}

    return render(request, 'blog/index.html', context)


def show_post(request, post_id):

    post = Post.objects.get(id=post_id)

    context = {'post': post, 'message': None}

    response = render(request, 'blog/show_post.html', context)

    return response


def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.execute()
            context = {'post': post}

            response = render(request, 'blog/post_created.html', context)

        else:
            context = {'response_status': 'error', 'errors': form.errors, 'form': form}

            response = render(request, 'blog/create_post.html', context)

    else:
        form = CreatePostForm()
        context = {'response_status': 'success', 'form': form}

        response = render(request, 'blog/create_post.html', context)

    return response


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    context = {'post_id': post_id}

    return render(request, 'blog/post_deleted.html', context)


def publish_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.publish()
    context = {'post_id': post_id}

    return render(request, 'blog/post_published.html', context)
