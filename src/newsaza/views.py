from django.shortcuts import render
from .myforms import SignUP


# Create your views here.

def home(request):
    title = "My Title"
    mytitle = {
        "template_title": "hello",
        "template_user": "username",
        "template_sur": "surname",
    }
    context = {
        "template_user": "sahai",
        "template_sur": "srichock",
    }

    data = SignUP()

    #return render(request,"home.html",{})
    #return render(request,"home.html",context=mytitle)
    return render(request,"home.html",{'form': data})
