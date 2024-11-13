from django import forms
from .models import Tours, TourDetails

class TourForm(forms.ModelForm):
    class Meta:
        model = Tours
        fields = '__all__'

