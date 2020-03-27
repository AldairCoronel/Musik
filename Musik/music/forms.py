from django import forms
from .models import Artist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class ArtistForm(forms.ModelForm):
    """ Class where we create Artist form """
    class Meta:
        model = Artist
        fields = ['name', 'image']

    def clean_name(self):
        # this method validates name field
        data = self.cleaned_data["name"]
        if Artist.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("This artist already exists")
        return data
