# EmailGPT
  
This module connects to the EmailGPT via API key  

*Read this in other languages: [English](Manual_EmailGPT.md), [Português](Manual_EmailGPT.pr.md), [Español](Manual_EmailGPT.es.md)*
  
![banner](imgs/Banner_EmailGPT.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to EmailGPT
  
This command allows you to connect to EmailGPT by indicating the server and the API key.
|Parameters|Description|example|
| --- | --- | --- |
|EmailGPT URL|EmailGPT server URL|https://emailgpt.rocketbot.com|
|EmailGPT API key|EmailGPT API key used for the connection.|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Get tasks list
  
Returns the list of active or paused tasks from your EmailGPT account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Get task results
  
Returns the results of a task by its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Task ID|ID of the task you want to get|84cae6f07f7acb7df36b|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
