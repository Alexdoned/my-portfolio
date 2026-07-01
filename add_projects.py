#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from projects.models import Project

projects_data = [
    {
        'title': 'Cyon Jalingo',
        'description': 'A web application project showcasing full-stack development skills.',
        'technologies_used': 'JavaScript, React, Node.js, MongoDB',
        'github_url': 'https://github.com/Alexdoned/cyon-jalingo',
        'live_demo_url': '',
    },
    {
        'title': 'CCRN',
        'description': 'A comprehensive project demonstrating advanced development practices.',
        'technologies_used': 'Python, Django, PostgreSQL',
        'github_url': 'https://github.com/Alexdoned/CCRN',
        'live_demo_url': '',
    },
    {
        'title': 'MERN Crash',
        'description': 'A full-stack MERN application built from scratch as a learning project.',
        'technologies_used': 'MongoDB, Express, React, Node.js',
        'github_url': 'https://github.com/Alexdoned/mern-crash',
        'live_demo_url': '',
    },
    {
        'title': 'Cybersecurity',
        'description': 'Security-focused project exploring cybersecurity concepts and implementations.',
        'technologies_used': 'Python, Security, Networking',
        'github_url': 'https://github.com/Alexdoned/Cybersecurity',
        'live_demo_url': '',
    },
]

for project_data in projects_data:
    project, created = Project.objects.get_or_create(
        title=project_data['title'],
        defaults={
            'description': project_data['description'],
            'technologies_used': project_data['technologies_used'],
            'github_url': project_data['github_url'],
            'live_demo_url': project_data['live_demo_url'],
        }
    )
    if created:
        print(f"✅ Created: {project.title}")
    else:
        print(f"⏭️  Already exists: {project.title}")

print("\nAll projects added successfully!")
