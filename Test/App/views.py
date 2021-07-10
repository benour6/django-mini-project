from django.shortcuts import render
from .models import Formation
from .filters import FormationFilter
from django.views.generic import *

# Create your views here.


def formation_list(request):
    f = FormationFilter(request.GET, queryset=Formation.objects.all())
    return render(request, 'App/formation_list.html', {'filter': f})

class Formation_DetailView(DetailView):
    model = Formation
    context_object_name = 'formation'