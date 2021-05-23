from django.shortcuts import render
from .models import BlogModel


def listele(request):
    gonderiler = BlogModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})


def gonderidetay(request,pk):
    gonderi = BlogModel.objects.get(pk=pk)
    return render(request,"blog/detay.html",{"gonderi":gonderi})