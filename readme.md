
# Snippet Application

This application allows users to create, update, retrieve, and delete short text snippets. Users can also assign tags to snippets, with each snippet potentially having multiple tags.

## Technologies Used

- [Django](https://www.djangoproject.com/): A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django Rest Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/): A JSON Web Token authentication plugin for the Django REST Framework.

## Features

- JSON Web Token (JWT) authentication
- CRUD operations for snippets
- Tags for categorizing snippets


## Setup

To set up this application locally, follow these instructions:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/renjithvs/snippet-app.git
```

2. Move into the project directory:

```bash
cd snippet-app
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Run the migrations to set up the database:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

The application should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
```
