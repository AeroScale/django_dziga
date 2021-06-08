from django.shortcuts import render
from phgallery.models import Imggal
from django.views.generic import DetailView

def ImageDispaly(request):
    dispalyimg = Imggal.objects.all()
    return render(request, 'phgallery/photo.html', {'Imggal': dispalyimg})


