from django.forms import ModelForm
from .models import *

class MovieForm(ModelForm):
    class Meta:
        model = Movieinfo
        fields = ['title','year','description','poster']