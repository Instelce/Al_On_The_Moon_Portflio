from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import *


def home(request):
    projects = Projects.objects.order_by('-date')[:2]
    about = About.objects.get()
    contacts = Contact.objects.order_by('name')

    context = {
        'projects': projects,
        'about': about,
        'contacts': contacts
    }

    if request.method == 'POST':
        messages = Messages()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        messages.name = name
        messages.email = email
        messages.subject = subject
        messages.content = content
        messages.save()
        return redirect('merci/')

    return render(request, 'portfolio/home.html', context)


def project_detail(request, project_id, project_name):
    project = get_object_or_404(Projects, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'portfolio/project_detail.html', context)


def all_projects(request):
    projects = Projects.objects.order_by('-date')
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/all_projects.html', context)


def thanks_messages(request):
    return render(request, 'portfolio/message_redirect.html')
    