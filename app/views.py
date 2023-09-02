from django.shortcuts import render
from django.http import HttpResponse
import random
import json 

# def index(request):
#     return HttpResponse("hello world!!!!")

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    return render(request,"index.html")


def task(request):
    with open('app/cricketers.json','r') as file:
        cricketers = json.load(file)
    random_cricketer = random.choice(cricketers)
    context = {'cricketer': random_cricketer}
    return render(request, 'task.html', context)

