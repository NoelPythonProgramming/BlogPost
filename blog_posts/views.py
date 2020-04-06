from django.shortcuts import render

from .models import BlogPost
# Create your views here.

def index(request):
	return render(request, 'blog_posts/index.html')
