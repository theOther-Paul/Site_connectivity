from django.http import *
from django.shortcuts import render


# Create your views here.
def response_200(request):
    return HttpResponse()


def response_403(request):
    return HttpResponseForbidden()


def response_302(request):
    return HttpResponseRedirect
