# credit_rating
This repository is created for completing the assessment given by crisil


# project settup
- first clone the repo in your local repository
- after that i have Used postgresql client for database management with django orm so you have to create database in postgresql server named as credit_rating
- database creation is .env configurable so have a look intio backend .env file for providing database url with username and password
    
    # Backend setup
    - It is created using Djangorestframework
    - to create database schema django provides its command to migrate schhema to your local database
    - so first open your terminal and move your pwd to backend directory . for example cd backend/
    - then run below commands to setup backend 
        # Command
            - python3 -m venv env   #To creating backend environment and installing all its dependecies
            - source env/bin/activate # activated environment
            - pip3 install -r requirements.txt # to download all dependecies
            - python3 manage.py migrate # to create schema in local database
            - python3 manage.py runserver # server started

    # frontend setup
        - It is created using React with vite 
        - to run frontend we have to open new terminal and move to frontend/credit_rating_frontend directory
        - now follow the command to start frontend  server
    # Command
        - npm i # download all dependecies
        - npm run dev # to start frontend server

# unit test
- Django provide inbuilt test.py where we can write unit test cases and it is controlled by django-admin to run the test case type following command in backend folder
# Command
    - python3 manage.py test

# security
    - For security purpose i have used static api-key account-id authentication for every request 
    - also configured api-key and account-id into .env file in both frontend and backend to authenticate request 
    - I can also use Jason web encryption with symmetric or assymetric encryption for payload security over the netwprk,but i was confused on some end points so didn't implemented it

# Logging
    - Have implementged logging for backend project using pythons inbuilt logging 
    - I have configured two handlers for logging streamhandler and filehandler to log in command prompt and django_app.log file in backend directory
    - loglevel and filename is .env configurable values 
    - for current setup i have set the loglevel to DEBUG which can show all the other log level depending upon its hierarchy 

# Database
    - I have used Postgresql server for creating database
    - connected it with django server by using psycopg2-binary library
    - To connect to database we have to create database in postgresql server and apply connection string in .env file to DATABASE_URL variable in backend directory
    