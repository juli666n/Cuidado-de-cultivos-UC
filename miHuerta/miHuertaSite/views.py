from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from .models import Plant
from .models import Sensor


def index(request):
    plants = Plant.objects.all()
    sensors = Sensor.objects.all()
    if request.method == 'POST':
        plant = request.POST['plant']
        Plant.objects.all().update(isSelected=False)
        Plant.objects.filter(name=plant).update(isSelected=True)
    context = {
        'plants': plants,
        'sensors': sensors,

    }
    return render(request, 'miHuertaSite/index.html', context)
