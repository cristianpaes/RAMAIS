# RAMAIS — Sistema de Gestão de Ramais Corporativos

Sistema web desenvolvido em Python e Django para gerenciamento de empresas, setores, ramais, e-mails e colaboradores, com autenticação de usuários e operações de cadastro, consulta, edição e exclusão.

O projeto nasceu de uma necessidade real de centralizar informações de comunicação interna e evoluiu para uma aplicação web estruturada, com API REST, banco de dados PostgreSQL e deploy em ambiente cloud.

**Acessar o sistema:

https://ramais.onrender.com/

**Para realizar teste:**
**Usuário:** teste
**Senha:** teste14697

#### **Tela de visualização:**
![VISUALIZAÇÃO](https://i.imgur.com/CGRuFxT.png "VISUALIZAÇÃO")

#### **Tela de edição:**
![EDIÇÃO](https://i.imgur.com/N1wi7HX.png "EDIÇÃO")

Tecnologias utilizadas
🐍 Python 3
🌐 Django 6.1
🔌 Django REST Framework
🐘 PostgreSQL
☁️ Neon PostgreSQL
🚀 Render
🗃️ SQLite para desenvolvimento local
🔐 Django Authentication
🎨 HTML5
🎨 CSS3
📦 WhiteNoise
🔫 Gunicorn
🐙 Git / GitHub
✨ Funcionalidades
📋 Consulta de Ramais
Visualização dos ramais cadastrados
Nome do responsável
Setor
Empresa
E-mail
Número do ramal
Data de criação
🔎 Pesquisa

Sistema de pesquisa para facilitar a localização de:

Ramais
Colaboradores
Setores
Empresas
E-mails
🏢 Empresas

Cadastro e gerenciamento de empresas com:

Nome
CNPJ
Inscrição Estadual
Telefone
Endereço
Número
Complemento
Bairro
CEP
🏷️ Setores

Cadastro e gerenciamento de setores vinculados aos ramais.

O sistema também possui validação para evitar o cadastro de setores duplicados.

👤 Autenticação

As operações administrativas são protegidas por autenticação.

Usuários não autenticados podem consultar as informações, enquanto as operações de alteração ficam restritas aos usuários autorizados.

API REST

O projeto possui uma API utilizando Django REST Framework.

Endpoint:

/api/

Modernização realizada

O projeto originalmente utilizava versões antigas do Django e dependências que estavam desatualizadas.

Durante a modernização foram realizadas diversas melhorias.

⬆️ Atualização do Django

Atualização da aplicação para:

Django 6.1.1

Além da atualização das principais dependências do projeto.

🐘 Migração para PostgreSQL

A aplicação foi preparada para trabalhar com diferentes bancos de dados:

Desenvolvimento
       ↓
SQLite

Produção
       ↓
PostgreSQL
       ↓
Neon

Isso permite manter um ambiente simples para desenvolvimento local e utilizar um banco PostgreSQL em produção.

☁️ Migração do Heroku para Render

O projeto originalmente estava hospedado no Heroku.

A aplicação foi migrada para o Render, permitindo manter o projeto disponível online utilizando infraestrutura cloud.

GitHub
   ↓
Render
   ↓
Django
   ↓
Neon PostgreSQL
🎨 Configuração de arquivos estáticos

Foi implementado WhiteNoise para gerenciamento dos arquivos estáticos em produção.

Também foi configurado o processo de:

collectstatic

durante o deploy.

🔐 Melhorias de segurança

Foram adicionadas configurações para ambiente de produção, incluindo:

Variáveis de ambiente
SECRET_KEY configurável
ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS
Proteção contra MIME sniffing
X_FRAME_OPTIONS
Separação entre configuração local e produção
👤 Criação automatizada do administrador

Foi criado um comando Django personalizado:

python manage.py create_admin

Esse comando permite criar o superusuário utilizando variáveis de ambiente, evitando colocar credenciais diretamente no código-fonte.

📦 Deploy automatizado

O processo de build do Render executa:

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py create_admin

Dessa forma, o ambiente é preparado automaticamente durante o deploy.

🗄️ Migrations

As migrations do Django foram revisadas e atualizadas para refletir a estrutura atual dos modelos.

### Pré-requisitos

Ter instalado Python3 e pip e Instalar o requirements do projeto.

```

    pip install -r requirements.txt

```

Apos, rodar os comandos para criar o banco de dados.

```

    python manage.py makemigrations
    python manage.py migrate

```

Com o banco de dados criado crie o super usuário para administração do django. O mesmo irá pedir nome de usuário, senha e e-mail.

```

    python manage.py createsuperuser

```

Com o super usuário criado basta rodar o projeto.

```

    python manage.py runserver

```

Objetivos do projeto

O projeto foi desenvolvido com foco em:

Organização das informações corporativas
Facilidade de consulta
Controle de acesso
CRUD completo
API REST
Boas práticas de desenvolvimento Django
Separação entre ambiente de desenvolvimento e produção
Utilização de PostgreSQL
Deploy em cloud
Segurança através de variáveis de ambiente
Manutenção e evolução de uma aplicação legada

Autor

Cristian Camargo

Profissional de Tecnologia da Informação com experiência em desenvolvimento, bancos de dados, sistemas corporativos e administração de ambientes tecnológicos.

🔗 Links

GitHub:
https://github.com/cristianpaes

Projeto:
https://github.com/cristianpaes/RAMAIS

Aplicação online:
https://ramais.onrender.com/

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório.