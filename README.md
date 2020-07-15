# scraping-ofertas-amazon
Script para buscar descuentos de un producto en amazon

### Dependencies
- Python 3.7
- PIP
- virtualenv 

### Usage
Creamos el entorno virtual:
```
virtualenv venv
```
Activacion del entorno virtual:
```
.\venv\Scripts\activate
```
Instalación de dependencias:
```
pip install - r requirements.txt
```
Uso:
```
py script.py 'libro python' 20
```

Ejemplo de respuesta:
```
===============================INICIO===============================
Buscando libro python con descuento de 20% ...
-------------------------------------------------------------------
Producto: Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming
Enlace: https://www.amazon.com.mx/Python-Crash-Course-Eric-Matthes/dp/1593279280/ref=sr_1_1?dchild=1&keywords=libro+python&qid=1594786369&sr=8-1
Precio actual: 404.59
Precio regular: 923.41
Descuento: $519 (56%)
-------------------------------------------------------------------
Producto: Curso Intensivo de Python: Uma introdução prática e baseada em projetos à programação (Portuguese Edition)
Enlace: https://www.amazon.com.mx/Curso-Intensivo-Python-introdu%C3%A7%C3%A3o-programa%C3%A7%C3%A3o-ebook/dp/B074ZTLKHB/ref=sr_1_4?dchild=1&keywords=libro+python&qid=1594786369&sr=8-4
Precio actual: 486.0
Precio regular: 729.0
Descuento: $243 (33%)
-------------------------------------------------------------------
Producto: Learning Python: Powerful Object-Oriented Programming (English Edition)
Enlace: https://www.amazon.com.mx/Learning-Python-Powerful-Object-Oriented-Programming-ebook/dp/B00DDZPC9S/ref=sr_1_5?dchild=1&keywords=libro+python&qid=1594786369&sr=8-5
Precio actual: 462.0
Precio regular: 1090.52
Descuento: $629 (58%)
===============================FIN===============================
```
