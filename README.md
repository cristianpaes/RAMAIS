# RAMAIS
Sistema em desenvolvimento baseado numa necessidade na empresa de controlar os ramais e ter as informações de seus colaboradores.

Para testar: 
https://app-ramais.herokuapp.com/ramais/

Login: teste
senha: teste14697

# Pré-requisitos:

Pré-requisitos
Ter instalado Python3 e pip e Instalar o requirements do projeto.

```python
pip install -r requirements.txt
```
Depois, rodar os comandos para criar o banco de dados.

```python
python manage.py makemigrations
python manage.py migrate
```
Com o banco de dados criado, vamos criar o super usuário para administração do django. O mesmo irá pedir nome de usuário, senha e e-mail.

```python
python manage.py createsuperuser
```

Com o super usuário criado basta rodar o projeto.

```python
python manage.py runserver
```

![Tela de Visualização](https://imgur.com/1uqLjRv "Tela de Visualização")

![Tela de Edição](https://imgur.com/I5PmJsN "Tela de Edição")
