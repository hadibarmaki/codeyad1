from django.shortcuts import render
from .models import Project
from contactus_app.models import Footer,Message

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        body = request.POST.get('body')
        Message.objects.create(name=name, email=email, subject=sub, body=body)

    projects = Project.objects.all()
    contact = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects':projects, 'contact': contact})
