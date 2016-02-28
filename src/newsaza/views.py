from django.shortcuts import render
from .myforms import SignUpForm
from .myforms import SazaForm

# Create your views here.

def home(request):
    title = "My Title"
    mytitle = {
        "template_title": "hello",
        "template_user": "username",
        "template_sur": "surname",
    }

    fullname = ''
    if request.method == "POST":
        #print request.POST
        #print request.POST['fullname']
        #print request.POST['email']

        fullname = request.POST['fullname']
        for key in  request.POST:
            print request.POST[key]

    data = SignUpForm()



    context = {
        "form": data,
        "name":  fullname
    }

    return render(request, "home.html", context)


    # return render(request,"home.html",{})
    # return render(request,"home.html",context=mytitle)
    # return render(request,"home.html",{'form': data})


def saza(request):

    username = ''
    form = SazaForm()
    if request.method == "POST":
        print request.POST
        username = request.POST['username']
    #   password = request.POST['password']

    context = {
        "form": form,
        "username": username,
        #"password": password
    }
    return render(request,"saza.html",context)