from django.conf import settings
from django.conf.urls import include, url
# from django.conf.urls.static import static
from django.contrib import admin
# from django.conf.urls.static import static
# Add this import
from django.contrib.auth import views


from . import views

urlpatterns = [

    # url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^my_post/$', views.my_post, name='my_post'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/prev=(?P<prev>.+)/$', views.post_delete, name='post_delete'),
    url(r'^\?q=(?P<query_search>\w+)$', views.post_list, name='search_result'),
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
