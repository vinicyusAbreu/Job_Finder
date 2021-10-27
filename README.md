
# 🔎 Job Finder

## 🤔 Sobre o projeto
<hr>
Um projeto para encontrar vagas de empregos ou adicionar vagas de empregos. Projeto feito utilizando Django.

## ✨ Demonstração
Veja abaixo um gif do projeto.<br>
[![Image from Gyazo](https://i.gyazo.com/a804db9e7c5c915871e06602343bd5a1.gif)](https://gyazo.com/a804db9e7c5c915871e06602343bd5a1)

## Iniciar projeto
<hr>

Depois de clonar o repositório, você deseja criar um ambiente virtual, para ter uma instalação limpa do Python. Você pode fazer isso executando o comando

```
python -m venv env
```
Depois disso, é necessário ativar o ambiente virtual.

Você pode instalar todas as dependências necessárias executando
```
pip install -r requirements.txt
```

Definir banco de dados (verifique se você está no mesmo diretório que o manage.py)
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Criar o SuperUser 
```
python manage.py createsuperuser
```

Após todas essas etapas, você pode começar a testar este projeto usando o comando.
```
python manage.py runserver
```
