from django.db import models
from datetime import date

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=355, null=False)
    senderName = models.CharField(max_length=355, null=False)
    contentName = models.CharField(max_length=100, null=False)
    CuratorName = models.CharField(max_length=355, null=False)
    CuratorID = models.ForeignKey(models.Curator, verbose_name= "Curator ID", on_delete= models.CASCADE)
    semesterID = models.ForeignKey(models.content, verbose_name= "Semester ID", on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(null=False)

class Curator(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=300, null=False)
    email = models.EmailField(null=False)
    password = models.BinaryField(null=False)
    decryptKey = models.BinaryField(null=False)
    
class Content(models.Model):
    semester_choices = [
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('6', 'Optatives'),
        ('7', 'Extra')
    ]
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    semester = models.IntegerChoices(choices = semester_choices, null=False)
    
