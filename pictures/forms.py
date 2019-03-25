from django import forms
from .models import Image

class PicturesForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['profile', 'pub_date']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }