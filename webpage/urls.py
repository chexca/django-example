from django.conf.urls import url
from django.contrib import admin

from blog.views import index, show_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^post/(?P<post_id>\d+)/$', show_post),
]
