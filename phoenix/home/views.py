from django.shortcuts import render,HttpResponse

# Create your views here.

def landing(request):
    return render(request,'index.html')

