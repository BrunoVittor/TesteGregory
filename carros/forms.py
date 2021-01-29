from django.forms import ModelForm
from .models import Carros


class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['marca', 'modelo', 'ano', 'cor', 'placa']
