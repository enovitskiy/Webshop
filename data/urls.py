from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.second,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/product/$',
        views.product,
        name='product'),

    url(r'^(?P<category_slug>[-\w]+)/(?P<firstcategory_slug>[-\w]+)/(?P<secondcategory_slug>[-\w]+)/$',
        views.second,
        name='second'),
    url(r'^(?P<category_slug>[-\w]+)/first/$',
        views.first,
        name='first'),

]
app_name = 'shop'