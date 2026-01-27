from django.forms import ModelForm

from .models import Davlat


class DavlatForm(ModelForm):
    class Meta:
        model = Davlat
        fields = '__all__'