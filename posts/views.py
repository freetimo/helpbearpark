from django.shortcuts import render, get_object_or_404
from .models import Directory, Post

def home(request):
	posts = Post.objects.all()[:5].select_related('directory')
	ctx = {
		'posts': posts,
	}
	return render(request, 'index.html', ctx)

def directory(request, choice):
	directories = Directory.objects.filter(choice=choice)
	ctx = {
		'directories': directories,
		'choice': choice,
	}
	return render(request, 'directory.html', ctx)

def post_list(request, choice, slug):
	directory = Directory.objects.get(choice=choice, slug=slug)
	post_list = Post.objects.filter(directory=directory).select_related('directory')
	ctx = {
		'post_list': post_list,
		'choice': choice,
		'slug': slug,
	}
	return render(request, 'post_list.html', ctx)

def post_detail(request, choice, directory_slug, post_slug):
	directory = Directory.objects.get(choice=choice, slug=directory_slug)
	post_detail = get_object_or_404(Post, directory=directory, slug=post_slug)
	ctx = {
		'post_detail': post_detail,
		'directory_slug':directory_slug,
		'choice': choice,
		'post_slug': post_slug,
	}
	return render(request, 'post_detail.html', ctx)

def handler404(request, exception):
	return render(request, '404.html', status=404)

def handler500(request, exception):
	return render(request, '500.html', status=500)