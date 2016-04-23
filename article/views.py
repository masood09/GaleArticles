from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render
from .helpers import *



def index(request):
    return render(
        request,
        'index.html'
    )
