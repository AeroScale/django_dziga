from django.shortcuts import render
from shop.models import ProductWindow
from django.views.generic import DetailView

def DisplayWindows(request):
    windows_display = ProductWindow.objects.all()
    return render(request, 'shop/windows.html', {'Product_window': windows_display})

class WindowsDetailView(DetailView):
    model = ProductWindow
    template_name = 'shop/windows_detail_views.html'
    context_object_name = 'window'

