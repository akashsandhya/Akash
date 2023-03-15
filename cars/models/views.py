from django.shortcuts import render
from django.http import HttpResponse
from.models import Models
def index(request):
    models=Models.objects.all()
    return render(request,'index.html',{'models':models})
    #return HttpResponse("<h1>Welcome</h1>")
def about(request):
    return HttpResponse("<h1>Hello</h1>")

# Create your views here.
