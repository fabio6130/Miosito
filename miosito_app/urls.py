from django.urls import path

import miosito_app

from .views import HomeView

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
]