from django.shortcuts import render
from .models import database
from .serializer import databaseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
#Queryset
def database_info(request):
    #complex data
    ai = database.objects.all()
    #python dict
    serializer = databaseSerializer(ai, many=True)
    #render Json
    json_data= JSONRenderer().render (serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')

#single
def database_single(request,pk):
    #complex data
    ai = database.objects.get(id = pk)
    #python dict
    serializer = databaseSerializer(ai)
    #render Json
    json_data= JSONRenderer().render (serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def database_create(request):
    if request.method == 'POST':
        json_data= request.body
#json to stream convert
        stream = io.BytesIO(json_data)
    
#stream to python
        pythondata = JSONParser().parse(stream)
        #pthon to complex or to  table type
        deserializer= databaseSerializer(data = pythondata)
        if deserializer.is_valid:
            deserializer.save()
            res ={'msg':'Success'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(deserializer.erros)
        return HttpResponse(json_data,content_type='application/json')
