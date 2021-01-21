from django.shortcuts import render
from .sender import Sender
from django.http import  JsonResponse , HttpResponse
from Base.models import Message
# Create your views here.

def tester(request):
    query = Message.objects.all().last()
    response = Sender.sender(query.receptor , query.message)

    return HttpResponse(response)
    