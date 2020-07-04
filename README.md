# Ramais

É um projeto simples desenvolvido numa necessidade de obter as informações sobre Empresas, ramais, emails e colaboradores e tendo um CRUD no sistema após o login.

**Deploy para o Heroku1:**
[https://app-ramais.herokuapp.com/ramais/](http://app-intranet.herokuapp.com/)

**Para realizar teste:**
**Usuário:** teste
**Senha:** teste14697

#### **Tela de visualização:**
[![VISUALIZAÇÃO](TELA01 "VISUALIZAÇÃO")](https://i.imgur.com/CGRuFxT.png "VISUALIZAÇÃO")

#### **Tela de edição:**
[![EDIÇÃO](TELA02 "EDIÇÃO")](https://i.imgur.com/N1wi7HX.png "EDIÇÃO")

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

