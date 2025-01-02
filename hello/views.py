import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Constará todos os produtos!")

def quemSomos(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/quemSomos.html'
    )

def masculino(request):
    return HttpResponse("Aqui será a listagem de itens para o público masculino!")

def feminino(request):
    return HttpResponse("Aqui será a listagem de itens para o público feminino!")

# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)
