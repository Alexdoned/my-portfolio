from django.db import DatabaseError
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from projects.models import Project
from blog.models import Blog
from .models import Resume


def home(request):
    try:
        featured_projects = Project.objects.order_by('-created_at')[:4]
        recent_posts = Blog.objects.order_by('-created_at')[:3]
        resume = Resume.objects.order_by('-uploaded_at').first()
    except DatabaseError:
        featured_projects = []
        recent_posts = []
        resume = None

    return render(request, 'core/home.html', {
        'featured_projects': featured_projects,
        'recent_posts': recent_posts,
        'resume': resume,
    })


def about(request):
    return render(request, 'core/about.html')


def resume_download(request):
    try:
        resume = Resume.objects.order_by('-uploaded_at').first()
    except DatabaseError:
        resume = None

    if not resume or not resume.file:
        raise Http404('Resume not available')
    return HttpResponseRedirect(resume.file.url)
