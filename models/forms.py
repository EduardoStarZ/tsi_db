from django.forms import ModelForm
from models.models import File

class insertDataForm(ModelForm):
    class Meta:
        model = File
        fields = ("name", "senderName", "contentName", "CuratorName", "uploadDate")

class queryDataForm(ModelForm):
    class Meta:
        model = File
        fields = ("name", "contentName", "CuratorName", "uploadDate")