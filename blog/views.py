from django.shortcuts import render,redirect
from .models import BlogModel
from .forms import BlogForm


def listele(request):
    gonderiler = BlogModel.objects.all()
    return render(request,"blog/liste.html",{"gonderis":gonderiler})


def gonderidetay(request,pk):
    gonderi = BlogModel.objects.get(pk=pk)
    return render(request,"blog/detay.html",{"gonderi":gonderi})

from django.utils import timezone
def yeniGonderi(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        gonderi = form.save(commit=False)
        gonderi.yayimzaman = timezone.now()
        gonderi.save()
        return redirect('gonderidetay',pk=gonderi.pk)
    else:
        form = BlogForm()
    return render(request,"blog/yenigonderi.html",{"form":form})

from django.shortcuts import get_object_or_404

def gonderiDuzenle(request,pk):
    gonderi = get_object_or_404(BlogModel,pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST,instance=gonderi)
        gonderi = form.save(commit=False)
        gonderi.yayimzaman = timezone.now()
        gonderi.save()
        return redirect('gonderidetay',pk=gonderi.pk)
    else:
        form = BlogForm(instance=gonderi)
    return render(request,"blog/gonderiduzenle.html",{"form":form})

