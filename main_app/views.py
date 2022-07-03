import http
import json
from django.shortcuts import render
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import Cat
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# Add the following import

# Add the Cat class & list and view function below the imports

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

  # Add new view
@csrf_exempt
def cats_index(request):
  if request.method == 'GET':
    return JsonResponse(list(Cat.objects.all().values()), safe=False)
  elif request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    request_body = json.loads(body_unicode)
    c = Cat(name=request_body['name'], breed=request_body['breed'],age=request_body['age'], description=request_body['description'])
    c.save()
    return JsonResponse(list(Cat.objects.filter(id=c.id).values()), safe=False)

@csrf_exempt
def cats_detail(request, cat_id):
  if request.method == 'GET':
    return JsonResponse(list(Cat.objects.filter(id=cat_id).values()), safe=False)
  elif request.method == 'PUT':
    body_unicode = request.body.decode('utf-8')
    request_body = json.loads(body_unicode)
    c = Cat.objects.get(id=cat_id)
    c.name = request_body['name']
    c.breed = request_body['breed']
    c.age = request_body['age']
    c.description = request_body['description']
    c.save()
    return JsonResponse(list(Cat.objects.filter(id=c.id).values()), safe=False)
  elif request.method == 'DELETE':
    c = Cat.objects.get(id=cat_id)
    c.delete()
    return JsonResponse({"deleted": "success"}, safe=False)
