from django.urls import path

from . import views
app_name = 'blog_posts'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
]