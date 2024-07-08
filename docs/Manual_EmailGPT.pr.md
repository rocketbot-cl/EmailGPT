# EmailGPT
  
Este módulo se conecta ao EmailGPT via chave API  

*Read this in other languages: [English](Manual_EmailGPT.md), [Português](Manual_EmailGPT.pr.md), [Español](Manual_EmailGPT.es.md)*
  
![banner](imgs/Banner_EmailGPT.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar-se ao EmailGPT
  
Conecte-se ao EmailGPT
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL do EmailGPT|URL do EmailGPT|https://emailgpt.rocketbot.com|
|Adicione sua chave de API do EmailGPT|Chave de API do EmailGPT|eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|

### Obter lista de tarefas
  
Retorna uma lista de tarefas associadas à sua conta.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|

### Obter informações de uma tarefa
  
Retorna as informações de uma tarefa.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Digite o ID da tarefa que deseja obter|ID da tarefa que deseja obter|84cae6f0f77acb7df36b|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|
