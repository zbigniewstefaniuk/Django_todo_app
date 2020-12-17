<br />
<h1 align="center">Simple Todo App implemented using <a href="https://www.djangoproject.com/">Django</a></h1>

<h2 align="center"><a href="https://django-todo-zayn.herokuapp.com/">Demo</a></h2>
<br />

<p align="center"><img align="center" src="https://github.com/zbigniewstefaniuk/zbigniewstefaniuk/blob/master/django_todo_screens/todo-django-1.png"></p>
<p align="center"><img align="center" src="https://github.com/zbigniewstefaniuk/zbigniewstefaniuk/blob/master/django_todo_screens/todo-django-edit.png"></p>
<p align="center"><img height="366" width="500" src="https://github.com/zbigniewstefaniuk/zbigniewstefaniuk/blob/master/django_todo_screens/todo-django-delete.png"></p>

<h1 align="center">Setup Instructions</h1>

1. Clone the repo

```sh
git clone https://github.com/zbigniewstefaniuk/Django_todo_app
```

2. Activate virtual enviroment and install requirements

```sh
py -m venv venv
venv\Scripts\activate.ps1
pip install requirements
```

3. Start app

```sh
cd Django_todo_app/todo_app
py manage.py migrate
py manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.
