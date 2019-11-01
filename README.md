# Twix Backend
[![Build Status](https://travis-ci.com/Diaga/django-api-template.svg?branch=master)](https://travis-ci.com/Diaga/django-api-template)

This project is templated from [Django API Template](https://github.com/Diaga/django-api-template)(A template for creating robust APIs with django rest framework!)

## Documentation

In four simple steps, you will be able to run this server on your own machine!

* Clone the git repository
* Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
* This project uses sqlite as database, therefore, there is no need for setup. Simply run migrations through following command: 
    ```
    python app/manage.py migrate
    ```
* Finally, run the last command and the API will be accessible on your machine through 127.0.0.1:8000:
    ```
    python app/manage.py runserver
    ```

## External Link
This project is hosted at [here](https://api.knctu.com/api) for AppCon'19.
