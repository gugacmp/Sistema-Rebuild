from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastrouser(request):
    return render(request, 'cadastrouser.html')

def validaruser(request):
    return render(request, 'validaruser.html')

def menu(request):
    return render(request, 'menu.html')

def rebuild(request):
    return render(request, 'rebuild.html')
