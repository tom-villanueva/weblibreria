# weblibreria

#Ejecutar
Después de clonar el repositorio tenemos que entrar al directorio raiz y crear un entorno virtual. Finalmente instalar los requerimientos.

```bash
$ git clone https://github.com/tom-villanueva/weblibreria.git
$ cd weblibreria
$ python3 -m virtualenv venv
$ source venv/bin/activate //en windows: venv\Scripts\activate.bat
(venv) $ pip install -r requerimientos.txt
(venv) $ #Actualizar pip si es necesario con:
(venv) $ python3 -m pip install --upgrade pip
```

Para ejecutarlo necesitamos el manage.py que se encuentra en src.

```bash
(venv) $ cd src
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py runserver
```