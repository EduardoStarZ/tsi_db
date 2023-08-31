from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models.forms import insertDataForm, queryDataForm
# Create your views here.

def main(request):
    template = loader.get_template('index.html')
    context = {
        'form': [insertDataForm()]
    }
    return HttpResponse(template.render(context, request))