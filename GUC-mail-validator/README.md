## CONTENTS OF THIS FILE

- Introduction
- Requirements
- Installation
- Code Structure

## INTRODUCTION

Django endpoint to validate GUCMails.

## REQUIREMENTS

This module requires the following modules:

- [Django](https://www.djangoproject.com/download/)
- [Django Rest Framework](https://www.django-rest-framework.org/#installation)

## INSTALLATION

- Option 1: Install the required modules manually.

- Option 2: Install the required modules using `poetry install` if poetry(packages management tool) is available on your machine.

## CODE STRUCTURE

- `/server/validator/views.py`: Contains the endpoint.

- `/server/validator/serializers.py`: Contains the validation logic.

- `/server/validator/urls.py` & `/server/validator/urls.py`: specifies the url of the endpoint to be `localhost:8000/gucmail`.

## RUNNING

- Navigate to the manage.py file.

- Use command `python manage.py runserver`.

- Navigate to the endpoint url `localhost:8000/gucmail` in browser or use postman.

- Send JSON containing the data in key `mail`.
  Example: `{"mail":"ibrahim.soltan@student.guc.edu.eg"}`
