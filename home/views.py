from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[
        {'name':'maideep','age':23},
        {'name':'deep','age':21},
        {'name':'maidfbfgreep','age':13},
        {'name':'mavfbdsfagsideep','age':32},
        {'name':'mayjyideep','age':15},
        {'name':'maidedgeffwdqsep','age':17}
    ]
    context={"page":"home"}
    return render(request,"index.html",context)


def contact(request):
    context={'page':'contact'}
    return render(request,"contact.html",context)

def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)

def success_page(request):
    return HttpResponse('succesfull page')