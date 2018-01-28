#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    #return HttpResponse('Hello world!')
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html',{'article':article} )
