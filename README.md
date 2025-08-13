Setup e Configuração

    Supabase: Crie um projeto e uma tabela chamada clientes com as colunas nome e numero. Preencha a tabela com contatos de teste no formato DDI + DDD + Número.

    Variáveis de Ambiente: Crie um arquivo .env para armazenar suas credenciais da Z-API e Supabase de forma segura. Lembre-se de adicionar .env ao seu arquivo .gitignore.

    Execução: Após clonar o projeto e instalar as dependências com pip install -r requirements.txt, basta executar o script principal com o comando python main.py.

Estrutura do Código

O projeto é dividido em módulos para facilitar a organização:

    main.py: O ponto de entrada que orquestra o fluxo.

    supabase_clientes.py: Gerencia a comunicação com o banco de dados do Supabase.

    zapi_clientes.py: Responsável por interagir com a Z-API para enviar as mensagens.

    requirements.txt: Lista todas as bibliotecas necessárias para o projeto.
