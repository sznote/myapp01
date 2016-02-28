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

    data = SignUP()

    context = {
        "form": data,
    }

    if data.is_valid():
        surname = data.cleaned_data['your_surname']
        tel = data.cleaned_data['your_tel']

        context = {
            "form": data,
            "name": surname,
            "tel": tel,
        }
    # return render(request,"home.html",{})
    # return render(request,"home.html",context=mytitle)
    # return render(request,"home.html",{'form': data})
    return render(request, "home.html", context)
