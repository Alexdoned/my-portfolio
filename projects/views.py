from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Project


def project_list(request):
    search_query = request.GET.get('search', '')
    technology_filter = request.GET.get('technology', '')
    projects = Project.objects.order_by('-created_at')

    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies_used__icontains=search_query)
        )

    if technology_filter:
        projects = projects.filter(technologies_used__icontains=technology_filter)

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_technologies = set(
        tech.strip() for project in Project.objects.all() for tech in project.technology_list()
    )

    return render(request, 'projects/project_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'technology_filter': technology_filter,
        'all_technologies': sorted(all_technologies),
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {
        'project': project,
    })
