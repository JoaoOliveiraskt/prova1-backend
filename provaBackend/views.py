from django.shortcuts import render

def home(request):
    return render(request, "prova/home.html")
