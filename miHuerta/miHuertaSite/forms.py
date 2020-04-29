from django import forms
from .models import Plant

class PlantSelectionForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ('name')