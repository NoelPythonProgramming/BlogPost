from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
	return render(request, 'blog_posts/index.html')

def topics(request):
	topics = Topic.objects.all()
	context = {'topics': topics}
	return render(request, 'blog_posts/topics.html', context)