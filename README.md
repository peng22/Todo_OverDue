# TODO APP Project
This project is showing how to assign tasks to
users and each user could update the task

## Table of Contents
we have the :
-TODOList Django project
-Dockerfile
-Docker-compose


## Description
This project provides two capabilities:
  - For admin users they can:
      -create tasks and assign them to users.
      -filter tasks by status,user and due date.
  - For users they can:
      -view their assigned tasks.
      -update the status when they finish it.

## Methodology
To get the project running:
  - make build
    - To build the docker images.
  - make up
    - To run the containers
  - make superuser
    - to create superuser
  - make test
    - To run tests
  - make sync
    - To run migrations

## API
-User should log in
- /tasks/
  -view the tasks related to the user
- /tasks/pk
  - view the details of the task
  - update the status of the task.

## Technologies used
- Django
- DRF (Django Rest Framework)
- Docker


## Author
Mohamed Elsayed

## rate
4.5
