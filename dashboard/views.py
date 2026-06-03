from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aws(request):
    return render(request, 'aws.html')    

def docker(request):
    return render(request, 'docker.html')

def jenkins(request):
    return render(request, 'jenkins.html')

def kubernetes(request):
    return render(request, 'kubernetes.html')

def monitoring(request):
    return render(request, 'monitoring.html')

def ai_assistant(request):
    return render(request, 'ai_assistant.html')

def security(request):
    return render(request, 'security.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


