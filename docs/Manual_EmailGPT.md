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
  

|Parameters|Description|example|
| --- | --- | --- |
|EmailGPT URL|EmailGPT URL|https://emailgpt.rocketbot.com|
|Add your EmailGPT API key|EmailGPT API key|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Get task list
  
Returns a list of tasks associated with your account.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Get task results
  
Returns the results of a task.
|Parameters|Description|example|
| --- | --- | --- |
|Enter the task ID you want to obtain|Task ID you want to obtain|84cae6f0f77acb7df36b|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|
