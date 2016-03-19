from django.conf import settings
from django.shortcuts import render


# Create your views here.
def about(request):

    title = "My Title"
    context = {
        title: title
    }
    return render(request, "about.html", context)

