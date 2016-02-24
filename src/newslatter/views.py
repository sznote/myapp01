from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
'''
def aaa(request):
    return render(request,'aaa.html')
'''
