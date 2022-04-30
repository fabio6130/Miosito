from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import Companies,Projects,Languages,DevTools

class HomeView(View):
    template_name = 'miosito_app/homepage/homepage.html'

    def get_context(self):
        companies = Companies.objects.all()
        projects = Projects.objects.all()
        languages = Languages.objects.all()
        if languages:
            languages_frontend=languages.filter(frontend=True)
            languages_backend=languages.filter(frontend=False)
        devtools=DevTools.objects.all()
        context = {
            'companies':companies,
            'projects':projects,
            'languages_frontend':languages_frontend,
            'languages_backend':languages_backend,
            'devtools':devtools,

            
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())
    