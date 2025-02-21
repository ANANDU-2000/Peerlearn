from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def learner_register(request):  # Add this view
    return render(request, 'learner_register.html')

def mentor_register(request):  # Add this view
    return render(request, 'mentor_register.html')

def login_view(request):
    return render(request, 'login.html')