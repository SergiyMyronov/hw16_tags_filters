Homework 16
Custom tags and filters

Overview

This web application demonstrates some custom tags and filters.

The main features that have currently been implemented are:

    There are models for cities, suppliers, products and customers.
    Users can view list and detail information for models products, suppliers and customers.
    Product descriptions are loaded as random words from https://random-word-api.herokuapp.com/home 
    
    On the page http://127.0.0.1:8000/tag_filter/prod/ user can see:
        - random Product with its Supplier (rendered by custom tag "random_product")
        - some words of product descriptions are banned by the filter "ban_words_with_char_combination"

    Admin users can manage models. 

Quick Start

To get this project up and running locally on your computer:

    Set up the Python development environment. We recommend using a Python virtual environment.
    Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

    To generate new data run the management command:
    python3 manage.py makedata

    There is a dump of some data in the file tag_filter/fixtures/db.json
    Available users: 
    "admin" with password "adm123456" - superuser

    Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.

    Open tab to http://127.0.0.1:8000/tag_filter/prod/ to see product list.
