# WordWave

![site-cover-articles](https://github.com/user-attachments/assets/1a258176-a4b8-4c74-ad28-dc6e79a54d05)

## Articles Project Setup Guide

### Introduction

Welcome to the Articles project! This guide will help you set up the environment, understand the project structure, and get started with development.

### Prerequisites

Ensure you have Python installed on your system. The project requires Python 3.x.

### Getting Started

    git clone https://github.com/elBukhara/Articles
    cd Articles

    python -m venv .venv
    .venv/Scripts/activate

    pip3 install -r requirements.txt
    cd app

### Django Structure

All Django's apps are located in the folder /app

- `main/`: Django project root.
- `blog/`: Application for managing articles.
- `users/`: Application for user management.

### Environment Configuration

The project supports both development (`dev.py`) and production (`prod.py`) configurations.

- Development settings: `main/settings/dev.py`.
- Production settings: `main/settings/prod.py`.

### .env File

Create .env file in the folder ``/app`` and fill it with appropriate data as listed in the .env.template:

    ADMIN_URL='your_url/'
    SECRET_KEY='key'
    ALLOWED_HOSTS=['*']

    DB_ENGINE_NAME='mysql'
    DB_NAME='name'
    DB_USER='user'
    DB_PASSWORD='password'
    DB_HOST='host'
    DB_PORT='port'

### Running the Project

To start the development server with migrations applied:

    python manage.py migrate --settings=main.settings.dev
    python manage.py runserver --settings=main.settings.dev

### Loading Example Data

For a quicker setup, you can load example data. Ensure the `.example/data.json` and `media/` folders are placed correctly in the project root.

    # replace media/ folder (from .example/ ) in the base direction of a project

    python manage.py migrate --settings=main.settings.dev
    python manage.py loaddata .example/data.json --settings=main.settings.dev 
