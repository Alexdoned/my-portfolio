from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Blog


def blog_list(request):
    paginator = Paginator(Blog.objects.all(), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})
