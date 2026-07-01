from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'github_url', 'live_demo_url')
    search_fields = ('title', 'description', 'technologies_used')
    list_filter = ('created_at',)
