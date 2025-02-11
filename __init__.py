import os
import sys

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

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore


MODULE_NAME = "EmailGPT"

base_path = tmp_global_obj["basepath"] # type: ignore
module_path = os.path.join(base_path, "modules", MODULE_NAME)
module_libs_path = os.path.join(module_path, "libs")

if module_libs_path not in sys.path:
    sys.path.append(module_libs_path)

SESSION_DEFAULT = "default"
global mod_emailgpt_session

try:
    if not mod_emailgpt_session: # type: ignore
        mod_emailgpt_session = None
except NameError:
    mod_emailgpt_session = None

try:
    from EmailGPT import EmailGPT
    from gpt_consts import URL # type: ignore

    module = GetParams("module")  # Get command executed
    session = GetParams("session")  # Get Session name
    result = GetParams("result")  # Get variable name where save results

    if not session:
        session = SESSION_DEFAULT

    if module == "connect":
        api_key = GetParams("api_key")
        url = GetParams("url")
        
        if url not in URL.keys():
            SetVar(result, False)
            raise ValueError("The URL provided does not correspond to a valid EmailGPT Server. Please check the URL and try again.")

        if api_key:
            mod_emailgpt_session = EmailGPT(api_key, url)
            isConnected = mod_emailgpt_session.connect()

            SetVar(result, isConnected)

            if not isConnected:
                raise ValueError("The connection could not be established. Please check the API Key or Server URL and try again.")
        else:
            SetVar(result, False)
            raise ValueError("Api Key is required")

    if module == "get_tasks_list":
        uuids = mod_emailgpt_session.get_tasks_list()

        SetVar(result, uuids)

    if module == "get_task_results":
        task_uuid = GetParams("task_id")

        if task_uuid:
            task = mod_emailgpt_session.get_task_results(task_uuid)

            SetVar(result, task)

        else:
            raise ValueError("Id is required")


except Exception as e:
    result = GetParams("result")
    import traceback

    traceback.print_exc()
    SetVar(result, False)
    PrintException()
    raise e
