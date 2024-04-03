# WEB_APP_BLOG
Overview
This web application is a basic blogging platform where users can register, log in, and write blog posts. It is built using the Flask framework in Python and follows the standard structure for Flask applications with user authentication and CRUD (Create, Read, Update, Delete) functionality for blog posts.

Application Structure
Python Files:

__init__.py: Sets up the Flask app, database, and user session management.
forms.py: Defines forms for user input like registration and login.
models.py: Contains SQLAlchemy data models for users and posts.
routes.py: Manages the application's URL routes and view functions.
HTML Templates:

layout.html: The base template that includes the standard HTML structure and Bootstrap for styling.
home.html: The main page that shows all blog posts.
about.html: Provides information about the blogging platform.
login.html, register.html: Templates for user authentication.
account.html: Allows users to view and edit their account information.
create_post.html: Enables users to write and publish new blog posts.
Static Files:

style.css: Contains custom styles for the application.
Image files like default.png and download.png for default user avatars and other UI elements.
Features
User registration and login system with password hashing.
User profiles and the ability to edit user information.
Functionality for creating, viewing, and managing blog posts.
Responsive design using Bootstrap.
Setup and Running
Install all required Python packages, including Flask, Flask-WTF, Flask-Login, and Flask-SQLAlchemy.
Configure the database URI in __init__.py file if necessary.
Run flask run in the terminal to start the application.
