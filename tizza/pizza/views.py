from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
import json


def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(title=data['title'],
                                         description=data['description'],
                                         creator=request.user, )
        new_pizza.save()
        info = {'id': new_pizza.id,
                'title': new_pizza.title,
                'description': new_pizza.description}
        return HttpResponse(content=f'{info}',)

    elif request.method == 'GET':
        pizza = Pizza.objects.get(id=pid)
        info = {'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description}
        return HttpResponse(content=f'{info}', )

