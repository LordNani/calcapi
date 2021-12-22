import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the herokuapp index.")

@csrf_exempt
def sum(request):
    data = json.loads(request.body.decode())
    print(data)
    result = data['a'] + data['b']
    return JsonResponse({'result': result})

@csrf_exempt
def divide(request):
    data = json.loads(request.body.decode())
    print(data)
    result = data['a'] / data['b']
    return JsonResponse({'result': result})

@csrf_exempt
def subtract(request):
    data = json.loads(request.body.decode())
    print(data)
    result = data['a'] - data['b']
    return JsonResponse({'result': result})

@csrf_exempt
def product(request):
    data = json.loads(request.body.decode())
    print(data)
    result = data['a'] * data['b']
    return JsonResponse({'result': result})