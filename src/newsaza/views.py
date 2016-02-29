from django.shortcuts import render
from .myforms import ContactForm, SignUpForm
from .myforms import SazaForm
from django.http import HttpResponseRedirect

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

    if request.method == "POST":
        print request.POST
        username = request.POST['username']
        form = SazaForm(request.POST)
    else:
        form = SazaForm()

    if form.is_valid():
        context = {
         "username": username,
        }
    else:
        context = {
        "form": form,
        }


    return render(request,"saza.html",context)


def contact(request):
    form = ContactForm(request.POST or  None)

    context  = {
        "form": form,
    }

    return render(request,"forms.html",context)