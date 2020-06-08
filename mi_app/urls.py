from django.conf.urls import url
from mi_app import views

urlpatterns = [
    url(r'^$', views.Main.open_index),
    url(r'^predecir/', views.Logica.predecir_imagen),
]
