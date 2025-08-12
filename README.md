Desafio b2bflow: Automação de Mensagens Python

Este projeto é uma solução para o desafio de automação proposto pela b2bflow. O objetivo é criar um script em Python que se conecta a um banco de dados no Supabase para ler uma lista de contatos e, em seguida, envia mensagens personalizadas do WhatsApp para esses contatos usando a Z-API.

Requisitos

Para rodar este projeto, você precisará ter contas nas seguintes plataformas:

    Python 3.x

    Supabase: para o banco de dados.

    Z-API: para a automação do WhatsApp.

Setup

Siga os passos abaixo para configurar o ambiente e rodar o projeto.

1. Configuração do Supabase

    Crie um projeto no seu painel do Supabase.

    Crie uma nova tabela chamada clientes.

    Adicione as seguintes colunas à tabela:

        nome: tipo text

        numero: tipo text

    Insira pelo menos 3 linhas na tabela com nomes e números de telefone de WhatsApp válidos. Use o formato DDI + DDD + Número (ex: 5511999999999).

2. Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para gerenciar as credenciais de forma segura. Crie um arquivo chamado .env na raiz do projeto e preencha-o com as suas chaves e tokens, como no exemplo abaixo:

# Credenciais do Supabase
SUPABASE_URL="https://www.reddit.com/r/Supabase/comments/1jt9kix/my_supabase_project_was_deleted_without_warning/"
SUPABASE_KEY="[Chave de acesso ao Supabase (service_role key)]"

# Credenciais da Z-API
ZAPI_INSTANCE_ID="[ID da sua instância]"
ZAPI_TOKEN="[Token da sua instância]"
ZAPI_CLIENT_TOKEN="[Token de segurança da sua conta]"

Importante: Adicione o arquivo .env ao seu .gitignore para garantir que suas chaves não sejam publicadas no GitHub.

3. Como Rodar o Projeto

    Clone este repositório para a sua máquina local.

    Instale as dependências do projeto. É recomendado usar um ambiente virtual (venv):
    Bash

pip install -r requirements.txt

Execute o script principal:
Bash

    python main.py

O script irá buscar os contatos no Supabase e enviar uma mensagem personalizada para cada um deles. As mensagens de status serão exibidas no console.

Estrutura do Código

O projeto está organizado da seguinte forma para manter a clareza e as boas práticas:

    main.py: Ponto de entrada do programa. Orquestra o fluxo de buscar os contatos e iterar sobre eles para enviar as mensagens.

    supabase_clientes.py: Módulo responsável pela comunicação com o Supabase. Contém a função get_contacts() que faz a leitura dos dados.

    zapi_clientes.py: Módulo responsável pela comunicação com a Z-API. Contém a função send_message() que envia a requisição POST para a API do WhatsApp.

    requirements.txt: Lista as dependências do projeto.