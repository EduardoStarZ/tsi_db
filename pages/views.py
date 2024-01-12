from django.shortcuts import render, redirect
from models.models import File
from forms import FileForm

# Create your views here.

def main(request):
    content = File.objects.all()
    template = 'index.html'
    context = {
        'content': content
    }
    return render(request, template, context)

def admin(request):
    
    file_form = FileForm()
    content = File.objects.all()
    
    if request.method == 'POST':
        file_form = FileForm(request.POST)
    
        if file_form.is_valid():
            file_form.save()
            return redirect("admin")
    
    template = 'admin.html'
    context = {
        'file_form': file_form,
        'content': content
    }
    return render(request, template, context)