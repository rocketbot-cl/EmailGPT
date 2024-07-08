# EmailGPT
  
Este módulo se conecta a EmailGPT a través de la clave API  

*Read this in other languages: [English](Manual_EmailGPT.md), [Português](Manual_EmailGPT.pr.md), [Español](Manual_EmailGPT.es.md)*
  
![banner](imgs/Banner_EmailGPT.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a EmailPGT
  
Conectate a EmailGPT pasando tu apikey
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL de EmailGPT|URL de EmailGPT|https://emailgpt.rocketbot.com|
|Agrega tu apikey de EmailGPT|API key de EmailGPT|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Obtener lista de tareas
  
Devuelve una lista de tareas asociadas a su cuenta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|

### Obtener resultados de una tarea
  
Devuelve los resultados de una tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese el id de la tarea que quiere obtener|Id de la tarea que quiere obtener|84cae6f0f77acb7df36b|
|Asignar resultado a variable|Nombre de la variable donde se asignará el resultado de la execución del comando.|result|
