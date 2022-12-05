from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
        path('', views.home, name='home'),
        path('<int:pk>/model_results', views.model_results, name='model_results')
]
