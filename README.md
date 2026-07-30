# Student CRUD Application (Django)

## Project Overview

This is a Django-based Student Management System that performs CRUD operations.

CRUD stands for:

* **Create** - Add new student records
* **Read** - View student records
* **Update** - Edit existing student information
* **Delete** - Remove student records

## Features

* Add new students
* Display all students
* Edit student details
* Delete student records
* Responsive user interface using Bootstrap

## Technologies Used

* Python
* Django 5.2.16
* HTML
* Bootstrap 5
* SQLite Database

## Project Structure

```
student-crud-django/
│
├── crudapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── crudproject/
│   ├── settings.py
│   └── urls.py
│
├── templates/
│   └── index.html
│
├── manage.py
└── requirements.txt
```

## Installation & Setup

Clone the repository:

```bash
git clone https://github.com/sadiarajpoot614-sketch/student-crud-django.git
```

Go to project folder:

```bash
cd student-crud-django
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

## Database

This project uses SQLite database for storing student records.

