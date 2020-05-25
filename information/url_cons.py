from django.urls import re_path

from information.views import main

urlpatterns = [
    re_path(r'(?P<slug>[^/]+)/$', main),
]