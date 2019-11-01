# Twix Backend
[![Build Status](https://travis-ci.com/Diaga/django-api-template.svg?branch=master)](https://travis-ci.com/Diaga/django-api-template)

This project is templated from [Django API Template](https://github.com/Diaga/django-api-template)(A template for creating robust APIs with django rest framework!)

The project codenamed as "Twix Server" while the real application label being **Cask**, is the backend REST service for the frontend application [Twix](https://github.com/Diaga/Twix) being developed for AppCon'19 by Telenor Microfinance Bank.

## Documentation

In four simple steps, you will be able to run this server on your own machine! Using PyCharm IDE is recommended, however, you can use your favorite Python IDE.

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
You can visit 127.0.0.1:8000/api for a list of available endpoints.    

## Django Admin

You can leverage the power of django admin to have an overview of this project.

* Create a superuser using the following command:
    ```
    python app/manage.py createsuperuser
    ```
* You can now login using the details entered in the above command at 127.0.0.1:8000/admin

## External Link
This project is hosted at [here](https://api.knctu.com/api) for AppCon'19.
