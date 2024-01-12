from django.shortcuts import render
from .models import File
from django.db.models import Q
# Create your views here.


def search(request):
    query = request.GET.get("q")
    content = File.objects.all()
    
    if query != '': 
        content = File.objects.filter(
            Q(name__icontains=query) | Q(content__name__icontains=query) | Q(content__semester__id__icontains=query)
            )
            
    context = {
        'content': content
    }
        
    template = 'search.html'
        
    return render(request, template, context)


def admin_search(request):
    query = request.GET.get("q")
    content = File.objects.all()
    
    if query != '': 
        content = File.objects.filter(
            Q(name__icontains=query) | Q(content__name__icontains=query) | Q(curator__name__icontains=query) | Q(content__semester__id__icontains=query)
            )
            
    context = {
        'content': content
    }
        
    template = 'admin_search.html'
        
    return render(request, template, context)
