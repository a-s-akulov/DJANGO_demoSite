from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_standart(request, redirectUrl, *args):
    return HttpResponseRedirect(reverse(redirectUrl, args=(args)))