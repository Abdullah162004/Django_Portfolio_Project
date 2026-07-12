from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'skills': skills})


def projects(request):
    project_list = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': project_list})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
