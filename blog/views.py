# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post
from blog.forms.delete_post_form import DeletePostForm


def index(request):

    posts = Post.objects.all()

    context = {'posts': posts}

    return render(request, 'index.html', context)


def show_post(request, post_id):


    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = DeletePostForm(request.POST)
        if form.is_valid():
            
            post.delete()
            context = {'message': 'Post {} successfully deleted'.format(post_id)}
           
            response = render(request, 'post_deleted.html', context)
        else:
            context = {'post': post, 'delete_form': form, 'message': 'An error ocurred while deleting the post'}
            response = render(request, 'show_post.html', context)

    else:  # GET method
        form = DeletePostForm()

        context = {'post': post, 'delete_form': form, 'message': None} 

        response = render(request, 'show_post.html', context)

    return response

