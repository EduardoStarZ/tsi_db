from django.db import models

# Create your models here.

class File(models.Model):
    id = models.UUIDField(primary_key=True)
    fileName = models.CharField(max_length=355)
    senderName = models.CharField(max_length=355)
    contentName = models.CharField(max_length=100)
    size = models.IntegerField()
    CuratorName = models.CharField(max_length=355)
    CuratorID = models.ForeignKey(models.Curator, verbose_name= "Curator ID", on_delete= models.CASCADE)
    semester

class Curator(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.BinaryField()
    decryptKey = models.BinaryField()
    
class Content(models.Model):
    semester_choices = [
        1,2,3,4,5
    ]
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    semester = models.IntegerChoices(choices = semester_choices)