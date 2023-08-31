from django.db import models
from django.forms import ModelForm
from models.models import File, Content, Curator
from django.forms import forms

class insertDataForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ("name", "senderName", "contentName", "CuratorName", "CuratorID", "semesterID", "uploadDate")

class queryDataForm(forms.ModelForm):
    class Meta:
        model = File