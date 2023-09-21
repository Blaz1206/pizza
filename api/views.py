from django.http import HttpResponse, JsonResponse
from .models import Pizza

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello világ!</h1>")



def getPizzas(request):
    pizzas = Pizza.objects.all()

    li =[]

    for pizza in pizzas:
        li.append(pizza.serializer())

    return JsonResponse({"message":li})