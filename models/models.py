from django.db import models
from datetime import date
from django import forms

# Create your models here.

class Semester(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 100, null=False)
    
    def __str__(self):
        return f"{self.id} {self.name}"

class Curator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300, null=False)
    email = models.EmailField(null=False)
    
    def __str__(self):
        return f"{self.name}"
    
class Content(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    semester = models.ForeignKey(Semester, verbose_name= "Semester Value", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.semester} {self.name}"
    
class File(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=355, null=False)
    senderName = models.CharField(max_length=355, null=False)
    contentName = models.CharField(max_length=100, null=False)
    Curator = models.ForeignKey(Curator, verbose_name= "Curator", on_delete= models.CASCADE)
    Semester = models.ForeignKey(Semester, verbose_name="", on_delete= models.CASCADE)
    Content = models.ForeignKey(Content, verbose_name= "Content", on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(null=False)
    
    def __str__(self):
        return f"{self.contentName} {self.name}"