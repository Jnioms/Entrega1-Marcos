# Entrega 1 - Marcos

Primera entrega del trabajo final del curso de Python hecho en Coder House.

## Instrucciones

Primero es necesario instalar Django utilizando el comando [pip](https://pip.pypa.io/en/stable/) desde la terminal

```bash
> pip install django
```

## Uso

Para correr el projecto, es necesario utilizar el comando cd hasta estar en el mismo directorio del archivo manage.py

```bash
> cd /Directorio/
```

```
> ls
db.sqlite3 Entrega1Marcos manage.py tacografos taximetros templates usuarios
```

Luego hay que hacer las migraciones de los modelos para crear la base de datos

```
> python manage.py makemigrations
> python manage.py migrate
```

Una vez hecho todo esto, ya esta listo para correrse. Por default hay que acceder a la web desde la ip 127.0.0.1:8000 (si no se cargan las variables de ejecucion)

```
> python manage.py runserver
```

Los index de las aplicaciones muestran todos los elementos de cada base de datos. Es posible que parezca vacio, pero una vez cargado los elementos, van a poder verse.


## Colabora

Si encontras algun error o bug en la pagina, por favor ayudame a mejorar reportandolo [en el repositorio](https://github.com/Jnioms/Entrega1-Marcos/issues). Muchas gracias! :)

## FAQs

**De donde salio la idea?**

Es un proyecto que espero aplicar en mi trabajo, proximamente quiero agregar mas funciones y emprolijar el front end. Por ahora solo tome cosas que me gustaban de [bootstrap-dark-5](https://vinorodrigues.github.io/bootstrap-dark-5/) que esta basado en Bootstrap 5 pero con Dark Mode para hacer mi propio template

---
**Como cambio las configuraciones?**

En el settings.py dentro de /Entrega1Marcos/ estan la mayoria de configuraciones para agregar o sacar apps, deshabilitar el modo DEBUG y cambiar los path de los templates por ejemplo.

Para mas informacion acerca de Django, pueden utilizar la documentacion: [https://docs.djangoproject.com/en/4.1/](https://docs.djangoproject.com/en/4.1/)

---
**Como agrego mas objetos a la base de datos?**

Pueden crear un usuario administrador y agregarlos desde el panel ubicado en URL/admin/
Para crear al superusuario hay que usar el comando 

```
> python manage.py createsuperuser
```

Sino pueden crearse objetos usando los formularios ubicados en URL/taximetros/crear/, URL/tacografos/crear/ y URL/usuarios/crear/

---
**Como me puedo inscribir al curso?**

[https://www.coderhouse.com/online/python](https://www.coderhouse.com/online/python)

## Licencia
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
