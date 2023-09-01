from django.forms import ModelForm
from .models import File, Content

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'