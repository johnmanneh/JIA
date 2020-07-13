from django.shortcuts import render

# Create your views here.
def test(request,*args,**kwargs):
    return render(request,'layout.html',{})

def home(request,*args,**kwargs):
    return render(request,'home.html',{})