from  django.forms import ModelForm
from .models import CVApiKey


class CvKeyForm(ModelForm):
    class Meta:
        model = CVApiKey
        fields = ['cvkey']
