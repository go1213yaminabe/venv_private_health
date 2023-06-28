import os
from .models import Health
from django import forms

class HealthCreateForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ("morning_state","morning_temperature","night_state","night_temperature","note",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'