from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import Interesse,Abilita,Passione,ProgettiFatti

class HomeView(View):
    template_name = 'miosito_app/homepage/homepage.html'

    def get_context(self):
        interessi = Interesse.objects.all()
        abilita = Abilita.objects.all()
        passioni = Passione.objects.all()
        progettifatti=ProgettiFatti.objects.all()
        context = {
            'interessi':interessi,
            'abilita':abilita,
            'passioni':passioni,
            'progettifatti':progettifatti,

            
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())