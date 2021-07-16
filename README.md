# `Telegraph`, com Bulma

English README coming soon.

## Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/S_a-QmJOIhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Como instalar

``` sh
git clone https://github.com/paulo-e/telegraph
cd telegraph
python3 manage.py migrate
python3 manage.py runserver
```

## Como acessar

Navegue para `http://localhost:8000/blog`. Para acessar o painel de administrador, acesse `http://localhost:8000/admin`.

## Criando um administrador

Na pasta do projeto, rode:

``` sh
python3 manage.py createsuperuser
```

E siga o processo.
