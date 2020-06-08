import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from tensorflow.keras import backend as k


def predecir_imagen(img_url):
    tam_img = (32, 55)
    url_modelo = r'mi_app/logica/modelo'
    url_pesos = r'mi_app/logica/pesos'
    modelo = cargar_rnn(url_modelo, url_pesos)

    img = load_img(img_url, target_size=tam_img)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255
    prediccion = modelo.predict(img)
    prediccion = prediccion[0]
    resultados = []
    for i in prediccion:
        resultados.append(float(i)*100)

    valor_maximo = max(resultados)
    indice_maximo = resultados.index(valor_maximo)
    valor_maximo = round(valor_maximo, 2)

    if indice_maximo == 0:
        return valor_maximo, 'GATO'
    elif indice_maximo == 1:
        return valor_maximo, 'PERRO'
    elif indice_maximo == 2:
        return valor_maximo, 'PANDA'


def cargar_rnn(nombreArchivoModelo, nombreArchivoPesos):
    k.reset_uids()
    # Cargar la Arquitectura desde el archivo JSON
    with open(nombreArchivoModelo + '.json', 'r') as f:
        model = model_from_json(f.read())
    # Cargar Pesos (weights) en el nuevo modelo
    model.load_weights(nombreArchivoPesos + '.h5')
    return model
