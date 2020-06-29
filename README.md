# Ramais

É um projeto simples desenvolvido numa necessidade de ter informações sobre Empresas, ramais, emails e colaboradores.

[https://app-ramais.herokuapp.com/ramais/](http://app-intranet.herokuapp.com/)

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

