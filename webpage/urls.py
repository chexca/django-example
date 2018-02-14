from django.conf.urls import url
from django.contrib import admin

from blog.views import index, show_post, create_post, delete_post, publish_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^post/(?P<post_id>\d+)/$', show_post),
    url(r'^post/create/$', create_post),
    url(r'^post/delete/(?P<post_id>\d+)/$', delete_post),
    url(r'^post/publish/(?P<post_id>\d+)/$', publish_post),
]
