# EmailGPT
  
Este módulo se conecta a EmailGPT a través de la clave API  

*Read this in other languages: [English](Manual_EmailGPT.md), [Português](Manual_EmailGPT.pr.md), [Español](Manual_EmailGPT.es.md)*
  
![banner](imgs/Banner_EmailGPT.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a EmailGPT
  
Este comando te permite conectarte a EmailGPT indicando el servidor y la clave API
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL de EmailGPT|URL del servidor de EmailGPT|https://emailgpt.rocketbot.com|
|Api key de EmailGPT|Clave de API de EmailGPT utilizada para la conexión.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Obtener lista de tareas
  
Devuelve la lista de tareas activas o pausadas de tu cuenta de EmailGPT.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Obtener resultados de una tarea
  
Devuelve los resultados de una tarea por su ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la tarea|ID de la tarea que se desea obtener|84cae6f07f7acb7df36b|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
