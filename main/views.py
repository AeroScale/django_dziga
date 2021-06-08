from django.shortcuts import render, redirect
from .forms import FeedBackForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'title': 'Головна сторінка'})

def about(request):
    return render(request, 'main/about.html')

def photo(request):
    return render(request, 'main/photo.html')

def range(request):
    return render(request, 'main/range.html')

def feedback(request):
    return render(request, 'feedback/feedback.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('range')
        else:
            error = 'Форма заполнена не корректно'

    form = FeedBackForm()

    date = {
        'form': form,
        'error': error
    }

    return render(request, 'main/feedback.html', date)
