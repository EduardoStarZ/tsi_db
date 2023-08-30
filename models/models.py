from django.db import models

# Create your models here.

class Request(models.Model):
    archivistName = models.CharField(max_length=255)
    senderName = models.CharField(max_length=255)
    filesNames = getFilesSent()
    
    def getFilesSent(request):
        fileNames = []
        fileSizes = []
        fileSender = []
        fileClass = []
        
        for x in request:
            fileNames.append(request.Names[x])
            fileSizes.append(request.Names[x])
            fileSender.append(request.Names[x])
            fileClass.append(request.Names[x])
            
        return files