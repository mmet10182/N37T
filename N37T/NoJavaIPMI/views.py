from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from decouple import config


# Create your views here.
def get_console_jnlp(request):
    context = {
        'host': config('HOST_NOJAVAIPMI'),
               }
    return render(request, 'jnlp.html', context=context)
