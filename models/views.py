from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import FileForm, ContentForm
from .models import File, Content, Semester
# Create your views here.

def main(request):
    file_form = FileForm()
    content_options = Content.objects.all(semester = 1)
    
    if request.method == 'POST':
        file_form = FileForm(request.POST)
    
        if file_form.is_valid():
            file_form.save()
    
    template = loader.get_template('index.html')
    context = {
        'file_form': file_form
        
    }
    return HttpResponse(template.render(context, request))