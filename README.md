# tailwebtask

How to run django project locally

1. First, clone the project code:
	- git clone https://github.com/your-username/your-repository.git
	- cd your-repository 

2. python -m venv venv => replace venv with your actual virtual environment, i have used mEnv
	- venv\Scripts\activate => mEnv\Scripts\activate

3. pip install -r requirements.txt


4. navigate to the settings.py file and connect your database
	DATABASES = {
    	    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'tailwebscrud',
            'USER':'postgres',
            'PASSWORD':'kmat9605',
            'HOST':'localhost',
            'PORT':'5432',
            }
        }

5. python manage.py makemigrations

6. python manage.py migrate

7. python manage.py createsuperuser
	- add user name
	- add user password
	- add user email

8. python manage.py runserver
	- http://127.0.0.1:8000/ => open this url
	
9. to open login page 
	- http://127.0.0.1:8000/login/
	- then login with created username and password



Demonstration Video Link
https://drive.google.com/file/d/1-pvpE7vs2jnhn8XwJ6jZ99U01sGx7Gk0/view?usp=sharing
