from django.forms import Textarea, TextInput, EmailInput
from django.forms import ModelForm
from .models import FeedBack

class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'phone', 'product', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-label',
                'placeholder': "Ваше ім'я"
            }),
            'email': EmailInput(attrs={
                'class': 'form-label',
                'placeholder': 'Email адрес'
            }),
            'phone': TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Ваш номер телефона'
            }),
            'product': TextInput(attrs={
                'class': 'form-label',
                'placeholder': 'Зазначте продукцію, яка вас цікавить'
            }),
            'description': Textarea(attrs={
                'class': 'form-label',
                'placeholder': 'Розміри конструкції, профільна система, серія чи модель та ваші побажання'
            }),
        }
