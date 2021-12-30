from django.forms import ModelForm
from .models import *

class LookForm(ModelForm):
    class Meta:
        model = Look
        fields = '__all__'
        exclude = ['favourite']