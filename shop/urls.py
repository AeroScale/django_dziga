from django.urls import path
from . import views

urlpatterns = [
    path('/windows', views.DisplayWindows, name='windows'),
    path('/windows/<int:pk>', views.WindowsDetailView.as_view(), name='windows-detail')
]