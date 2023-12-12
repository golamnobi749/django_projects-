from django.shortcuts import render
from . models import Result


def result(request):
    result_info = Result.objects.all()
    return render(request,'contact/contacts.html', {'result':result_info})