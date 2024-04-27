This web application, developed with Django, offers a seamless online shopping experience, featuring a wide range of skincare and beauty products. It allows users to browse and order products, search using keywords, and manage their purchases with ease.

Features

- Browse over 2000-7000 open-source listed skincare and beauty products.
- Secure user authentication system with distinct access levels for admin, user, and guest.
- Ability for users to place orders and search for products using specific keywords.
- Admin dashboard to view orders and analytical charts.
- Comprehensive error handling to ensure a smooth user experience.
- Robust testing suite using Behave for behavior-driven development.

Development
The project adopts Django's MTV (Model-Template-View) architecture, with models for regions, income groups, countries, and indicators. The views handle the application's logic, while templates present the data.


Installation
To install and deploy

Visit Render and create a new app: https://dashboard.render.com/

Project URL: 

Creat the basic

   pyenv local 3.10.7 # this sets the local version of python to 3.10.7
   python3 -m venv .venv # this creates the virtual environment for you
   source .venv/bin/activate # this activates the virtual environment
   pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
We will use Django (https://www.djangoproject.com) as our web framework for the application. We install that with

    pip install Django
Project Configuration Clone the code with git clone [Git repository URL], migrate databases using python manage.py migrate, and create an admin account with python manage.py createsuperuser.

    git clone [Git repository URL]
Data Import Place CSV files in the designated folder and import them using python manage.py load_data --path [CSV file path].

    python manage.py load_data --path [CSV file path]
Execution Start the server with python manage.py runserver and navigate to http://127.0.0.1:8000/ to interact with the application.

    python3 manage.py runserver
Admin Interface Access the Django admin at http://127.0.0.1:8000/admin using the credentials created earlier.
Start the Server: Navigate to the project directory and execute python manage.py runserver. Then, access the application at http://127.0.0.1:8000/. Run Tests: Conduct tests with python manage.py test

    pip install -r requirements.txt
URL Deployment: Configure settings.py for production with ALLOWED_HOSTS and ensure DEBUG is set to False. Manage secrets and passwords using environment variables for security.
