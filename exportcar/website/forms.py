from django import forms
from django .forms import ModelForm

from .models import *


class Car_dataForm(ModelForm):
    class Meta:
        model = Car_data
        fields = '__all__'





