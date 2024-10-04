from django.shortcuts import render
from .models import Project
from contactus_app.models import Footer

# Create your views here.

def home(request):
    projects = Project.objects.all()
    contact = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects':projects, 'contact': contact})
