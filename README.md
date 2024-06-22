# Proyecto Urban Grocers
Se trata de un proyecto que comprueba la funcionalidad de crear Kits de productos
para un usuario en la aplicación Urban Grocers. Se tiene una lista de comprobación
para el campo name en la solicitud de creación de productos para un usuario. 

Se necesitan seis archivos en total: configuration.py (donde estaran las URL de acceso
a la Aplicación), data.py (es creado siguiendo las indicaciones de la documentación de
la Aplicación), sender_stand_request.py (se debe importar la libreria request y los 
archivos Configuration y Data) en éste archivo tendremos las solicitudes de creación de
un usuario, create_kit_name_kit_test.py (se deben importar los archivos Sender_stand_request
y data) en éste archivo estan las funciones para cambiar el contenido del cuerpo de la solicitud,
en el caso del parametro name, tambien funciones para obtener el token del usuario y cabezado de 
la autorización, lo que nos permitirá poder ejecutar las pruebas posterioes de la lista de comprobación. 
, README.md, y .gitignore (en éste archivo se colocan los archivo s que queremos que Git ignore, 
bien sea por seguridad o porque no sean necesarios).

- Necesitas tener instalado Python,y Selenium ya que el código está realizado en Python.
- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando "pytest C:\Users\AIO\Documents\GitHub\qa-project-Urban-Grosers-app-es"
en la terminal .
