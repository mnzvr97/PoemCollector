from django.forms import ModelForm
from .models import Read

class IsReadForm(ModelForm):
    class Meta:
        model = Read
        fields = ['read', 'date', 'rating']