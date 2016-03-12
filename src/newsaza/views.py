from django.shortcuts import render
from .myforms import ContactForm, SignUpForm
from .myforms import SazaForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    title = "My Title"

    if request.user.is_authenticated():
        title = "Hello %s" %(request.user)

    fullname = ''
    if request.method == "POST":

        '''
        print request.POST
        print request.POST['fullname']
        print request.POST['email']
        '''
        '''
        fullname = request.POST['fullname']
        for key in  request.POST:
            print request.POST[key]
        '''

    form = SignUpForm(request.POST or None)
    #instance = form.save(commit=False)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "form": form,
            "name": form.cleaned_data.get("fullname"),
            "email": form.cleaned_data.get("email")
        }
    else:
        context = {
            "form": form,
        }

    context["title"]=title

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
        #username = form.cleaned_data.get('username')
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

    fullname = ''
    form = ContactForm(request.POST or None)
    if form.is_valid():
        fullname = form.cleaned_data.get("fullname")
        email = form.cleaned_data.get("email")

        ''' if email == "iam.saza@gmail.com":
            print "hello saza" '''
        '''
        for key in form.cleaned_data:
            print key
            print form.cleaned_data.get(key)
        '''

        print 'hello' + str(form.cleaned_data)


        #instance = form.save(commit=False)
        #fullname =  instance.full_name

    context = {
        "form": form,
        "fullname": fullname,
    }

    return render(request,"contact.html",context)