from django.db import models
from datetime import date

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True)
    fileName = models.CharField(max_length=355)
    senderName = models.CharField(max_length=355)
    contentName = models.CharField(max_length=100)
    size = models.IntegerField()
    CuratorName = models.CharField(max_length=355)
    CuratorID = models.ForeignKey(models.Curator, verbose_name= "Curator ID", on_delete= models.CASCADE)
    semesterID = models.ForeignKey(models.content, verbose_name= "Semester ID", on_delete=models.CASCADE)
    uploadDate = models.DateTimeField()

class Curator(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.BinaryField()
    decryptKey = models.BinaryField()
    
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
    name = models.CharField(max_length=100)
    semester = models.IntegerChoices(choices = semester_choices)
    
