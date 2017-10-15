from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^register/', views.register_view, name='register'),
    url(r'^update/', views.update_view, name='update'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]