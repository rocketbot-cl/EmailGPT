# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

GetParams = GetParams  # type:ignore
SetVar = SetVar  # type:ignore
PrintException = PrintException  # type:ignore

import os
import sys

MODULE_NAME = "EmailGPT"

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"]  # type:ignore
module_path = os.path.join(base_path, "modules", MODULE_NAME)
module_libs_path = os.path.join(module_path, "libs")  # type:ignore

if module_libs_path not in sys.path:
    sys.path.append(module_libs_path)

"""
The code of each module works as a local scope. Each command that is executed resets the data.
To share information between commands, declare the variable as global. The sintax will be 'mod_modulename' or similar
"""
global shared_mod_var

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"

try:
    if not shared_mod_var:  # type:ignore
        shared_mod_var = {SESSION_DEFAULT: {}}
except NameError:
    shared_mod_var = {SESSION_DEFAULT: {}}

try:
    module = GetParams("module")  # Get command executed
    session = GetParams("session")  # Get Session name
    result = GetParams("result")  # Get variable name where save results

    if not session:
        session = SESSION_DEFAULT  # Set default session

    if module == "set_api_key":
        api_key = GetParams("api_key")

        if api_key:
            SetVar(result, True)
        else:
            SetVar(result, False)


except Exception as e:
    SetVar(result, False)
    PrintException()
    raise e
