# ecommerce_django
This is a Django-based eCommerce project for an online store.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)

## Features
- User authentication (Sign up, Login, Logout)
- Product browsing with categories
- Cart management
- Order placement and tracking
- Responsive design

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mahrosh1/ecommerce_django.git

2. pip install -r requirements.txt
3. python manage.py migrate

## Usage
Run the development server:
        python manage.py runserver
Access the application in your web browser at http://localhost:8000/

## Project Structure
|-- Eshop (Django Project)
    |-- brand (Django App)
        |-- migrations
        |-- models
        |-- templates
        |-- views
        |-- admin.py
        |-- apps.py
        |-- urls.py
        |-- ...
    |-- Eshop (Project Settings)
    |-- static
    |-- media
    |-- requirements.txt
    |-- manage.py
|-- README.md
|-- .gitignore

## Screenshots
![Home Screenshot](https://github.com/mahrosh1/ecommerce_django/blob/master/screenshots/home.png)
![SignUp Screenshot](https://github.com/mahrosh1/ecommerce_django/blob/master/screenshots/signup.png)
![LogIn Screenshot](https://github.com/mahrosh1/ecommerce_django/blob/master/screenshots/login.png)
![Cart Screenshot](https://github.com/mahrosh1/ecommerce_django/raw/master/screenshots/cart.png)
![CheckOut Screenshot](https://github.com/mahrosh1/ecommerce_django/blob/master/screenshots/checkout.png)
![Orders Screenshot](https://github.com/mahrosh1/ecommerce_django/blob/master/screenshots/orders.png)
