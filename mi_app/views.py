from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from mi_app.logica import logica
import os
from mi_app.models import Image


class Main:
    def open_index(self):
        return render(self, 'index.html')


class Logica:
    def predecir_imagen(request):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        if request.method == 'POST':
            imagen = request.FILES['elm_imagen']
            obj_file_sys_storage = FileSystemStorage()
            obj_file_sys_storage.save(imagen.name, imagen)
            url_imagen = base_dir + '/media/'+imagen.name
            porcentaje, clase = logica.predecir_imagen(url_imagen)

            obj_image = Image(None, url_imagen, clase, porcentaje)
            obj_image.save()

        return render(request, 'resultado.html', {'valor': porcentaje, 'clase': clase})
