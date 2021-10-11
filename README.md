# API EPP

_En este repositorio se encuentra el codigo fuente de la API de reconocimiendo de EPPs._

_Para la construcción de la misma se utilizo una implementación de Keras de la detección de objetos RetinaNet basada en el paper  “Focal Loss for Dense Object Detection” de Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He y Piotr Dollár._

_La implementación utilizada es una adaptación del repositorio fizyr/keras-retinanet la cual se configuro y entreno con imagenes de personas utilizando EPPs._

##

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


## Pre-requisitos 📋

_Las librerias requeridas se encuentran en el archivo requirements.txt_


## Instalación 🔧

_Para poder instarlar la API de manera local, realice los siguientes pasos_

_Clone este repositorio en su equipo_

```
git clone https://github.com/albatro-vm/detector-epp.git
```

_Luego ejecute el archivo app.py_

```
python app.py
```

_Acceda desde su navegador a :_
```
localhost/5000/predict/rutaImagen.jpg
```

_Donde en rutaImagen.jpg debe ingresar la ubicacion de la imagen que desea predecir. Esta acción solicitara a la API que prediga sobre la imagen ingresada_

_Una vez que la API reciba la petición y ejecute la predicción, devolvera un .json con el resultado._
_Este resultado incluira si cuenta con todos los EPPS y el porcentaje de cada uno de ellos._

_Por ejemplo:_

```
{eppOk: 1 ,auditivo: 0.80, antiparra: 0.58 , casco: 0.75}
```

## Metricas obtenidas 📦

_El modelo que se encuentra en el repositorio obtuvo como metricas finales las siguientes:_

|  | Precisión | Perdida  | Recall | F1
| :-----: | :-: | :-: | :-: | :-: |
| Model | 0.0 | 0.0 |0.0 | 0.0 |

## Construido con 🛠️

_Las herramientas que se utilizaron para poder construir esta API fueron:_

* [Flask](https://flask-doc.readthedocs.io/en/latest/) - El framework Python usado
* [TensorFlow](https://www.tensorflow.org/) - Librería
* [OpenCV](https://opencv.org/) - Librería


## Autores ✒️

* **Moreno Lía** - *Desarrollo* - [liamore14](https://github.com/liamore14)
* **Vejar Lucas** - *Desarrollo* - [lucasvejar](https://github.com/lucasvejar)
