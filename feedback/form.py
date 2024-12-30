from django import forms
from .models import Count

class CountForm(forms.ModelForm):
    class Meta:
        model = Count
        fields = ['title', 'icon_class', 'value']
        widgets = {
            'title': forms.Select(choices=Count.TITLE_CHOICES),
            'icon_class': forms.Select(choices=Count.ICON_CLASS_CHOICES),
        }
