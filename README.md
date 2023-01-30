# **Football Reactions Backend API**

### [Click here to see deployed project](https://fr_drf_api.herokuapp.com/) 
___

- Deployed API [link](https://football-reactions.herokuapp.com/)
- Deployed Frontend [link](https://football-reactions-uk.herokuapp.com/)
- API Backend Repository [repository](https://github.com/Josh-Wickens/fr-drf-api)
- Frontend Repository [repository](https://github.com/Josh-Wickens/football-reactions)
 

Football Reactions is the perfect place for football fans to come together on one platform and speak just about football. Football reaction gives users the chance to state if they are a fan or if they are a club. They can make posts or join in conversations regarding certain topics and communicate together and share opinions. This repository is the backend of Football Reactions using Django REST Framework for the API database.

# Database Schema

![Database Schema](/static/database.png)

1. [Testing](#Testing)
2. [Bugs](#Bugs)
3. [Technology and Languages](#technology-and-languages)
4. [Set up project](#set-up-project)
5. [Deployment](#deployment)

___
# Testing 


- My code was put through the codeinstitute validator as seen below this has passed through successfully. Only errors left were line too long error which was left as changing this would affect the readability of the code. 
![Validator Result](/static/validator-pass.png)

**URLS**

- I have tested all links to make sure all the urls are working. All urls working successfully.
![urls test](/static/test-api-urls.png)

**CRUD TESTING**


- A logged in user can create a profile, post, topic post, like a post, like a comment, like a topic post, like a topic comment.
- A non logged in User can read all of the above, but can't create any of the above.
- A Logged in User can edit their own profile, own post, topic post, like on a post, like on a comment, like on a topic post, like on a topic comment. They can't edit anyone else's data.
- A non logged in user can't edit any data in the API.
- A logged in user can delete their own post, topic post, like on a post, like on a comment, like on a topic post, like on a topic comment.
- A non logged in User can't delete any data in the api.

Examples shown below

User can read posts.
![CRUD Testing - Can read posts](/static/read-all-posts.png)
User can edit own profile.
![CRUD Testing - Can edit own profile](/static/edit-profile.png)
User can edit or delete their own post.
![CRUD Testing - Can edit or delete a topic post](/static/delete-or-edit-topic.png)
A non logged in user can only read data and can't create or edit.
![CRUD Testing - A non logged in user can only read data and not edit](/static/no-edit.png)

- Deleted Items do not show in listed data.
- Deployed data works the same.

___
# Bugs 


FIXED

- I had an bug when I created my like model and tried to create it so that you could like a post or post in topics. But it would end up liking a post in both at the same time without the option for one or the other. To solve this I created a model for each post and comment so that it would seperate them and provide ID's for all comments and posts from the profile.

- I had a long error when I tried to set up the query to count all the posts in topics. See below
![Long error in the terminal](/static/long-error.png)
  After speaking to Tutor support me and Ger managed to find that my topic count was missing an 's' on the end of it so it was not recognising the field.


UNFXED

- None known

___
# Technology and Languages

- Python - Django Rest Framework
- Cloudinary - Image Storage
- Pillow - Image processing
- Git - For version control, committing and pushing to Github
- Github - For storing the repository, files and images.
- Gitpod - IDE used to code my backend project
- Heroku - Used to deploy the application
- Django Rest Auth
- Cors Headers
- ElephantSQL

___
# Set up Project

***STEPS TO BE TAKEN***

1. Using Code Institutes full template, create a new repository, and open it in Gitpod.

2. Install Django using the following command in the terminal:     
    ```
    pip3 install 'django<4'
    ```

3. start the project using the following command in the terminal: 
    ```
    django-admin startproject drf_api .
    ```
 (including the dot as this will start the project in the current directory)

4. Install the Cloudinary library using the following command in the terminal: 
    ```
    pip install django-cloudinary-storage
    ```

5. Install the Pillow library using the following command in the terminal:
    ``` 
    pip install Pillow
    ```

6. In the settings.py file add the newly installed apps, the order is important
    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'cloudinary_storage', 
        'django.contrib.staticfiles',
        'cloudinary',
    ]
    ```
7. Create an env.py file in the top directory

8. In the env.py file add the following for the cloudinary url:
    ```
    import os
    os.environ["CLOUDINARY_URL"] = "cloudinary://INSERT YOUR CLOUDINARY API KEY HERE"
    ```

9. In the settings.py file set up cloudinary credentials, the media url and default file storage using the following code:
    ```
    import os
    if os.path.exists('env.py'):
        import env
    CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
___
# Deployment

***Setting up JSON Web Tokens***

1. Install JSON Web Token authentication by using the following command in the terminal:
    ```
    pip install dj-rest-auth
    ```

2. In settings.py add these to the installed apps list:
    ```
    'rest_framework.authtoken'
    'dj_rest_auth'
    ```

3. In the main urls.py file add the rest auth url to the urlpatterns list:
    ```
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    ```
4. Migrate the database using the following command in the terminal:
    ```
    python manage.py migrate
    ```
5. To allow users to register install Django Allauth using the following command in the terminal:
    ```
    pip install 'dj-rest-auth[with_social]'
    ```
6. Add the following to settings.py in the installed app list:
    ```
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    ```
7. also add the SITE_ID in settings.py:
    ```
    SITE_ID = 1
    ```
8. add the registration url In the main urls.py file to patterns
    ```
    path(
            'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
        ),
    ```
9. Install the JSON tokens:
    ``` 
    pip install djangorestframework-simplejwt
    ```
10. In env.py set DEV to 1 this checka whether in development or production:
    ```
    os.environ['DEV'] = '1'
    ```
11. Add an if/else statement in settings.py underneath the SITE_ID to check if in development or production:
    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [(
            'rest_framework.authentication.SessionAuthentication'
            if 'DEV' in os.environ
            else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        )],
    ```
12. Add the following code in settings.py to enable token authentication:
    ```
    REST_USE_JWT = True # enables token authentication
    JWT_AUTH_SECURE = True # tokens sent over HTTPS only
    JWT_AUTH_COOKIE = 'my-app-auth' #access token
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
    ```
13. Create a serializers.py file in the fr_drf_api file(project file name)

14. Using the code from the Django documentation, insert the following UserDetailsSerializer code into the serializer file just created in step 13:
    ```
    from dj_rest_auth.serializers import UserDetailsSerializer
    from rest_framework import serializers
    class CurrentUserSerializer(UserDetailsSerializer):
        """Serializer for Current User"""
        profile_id = serializers.ReadOnlyField(source='profile.id')
        profile_image = serializers.ReadOnlyField(source='profile.image.url')
        class Meta(UserDetailsSerializer.Meta):
            """Meta class to to specify fields"""
            fields = UserDetailsSerializer.Meta.fields + (
                'profile_id', 'profile_image'
            )
    ```
15. overwrite the default User Detail serializer in settings.py: 
    ```
    REST_AUTH_SERIALIZERS = {
        'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
    }
    ```
16. Run the migrations for database by using the following command in the terminal:
    ```
    python manage.py migrate
    ```
17. Update the requirements file by using the following command in the terminal:
    ```
    pip freeze > requirements.txt
    ```
18. Save all files, git add and git commit followed by git push to Github.

___
## Prepare API for deployment to Heroku
___

1. Create a views.py file inside fr_drf_api (project file name)

2. Import the api_view  decorator and the Response class and set message that is shown once the web page has loaded:

    ```
    from rest_framework.decorators import api_view
    from rest_framework.response import Response

    @api_view()
    def root_route(request):
    return Response({
        "message": "Welcome to Football Reactions API!"
    })
    ```

3. Import to urls.py in main project file and add to the url patterns list:

    ```
    from .views import root_route
    urlpatterns = [
        path('', root_route),
    ```

4. Set up page pagination inside REST_FRAMEWORK In settings.py:

    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [(
            'rest_framework.authentication.SessionAuthentication'
            if 'DEV' in os.environ
            else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        )],
        'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }
    ```

5. Set the default renderer to JSON for the prodution environment in settings.py:

    ```
    if 'DEV' not in os.environ:
        REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
            'rest_framework.renderers.JSONRenderer',
        ]
    ```

6. Set the date format to make it more human readable for created_on date in the settings.py file underneath PAGE_SIZE:

    ```
    'DATETIME_FORMAT': '%d %b %y',
    ```

7. Save all files, git add and git commit followed by git push to Github.

___
## Heroku Deployment
___

1. Login to ElephantSQL, create a new instance - select tiny turtle plan (ignore the tags field), select your nearest data center and click review and create the instance. Select your new instance and go to the URL section and copy the database URL.

Then Login to Heroku and on the dashboard select new - create new app. Give your app a name and create app to confirm.

2. In the settings tab of your heroku app you have just created, reveal Config Vars and add DATABASE_URL with the value set to the databse URL from ELEPHANTSQL without the quotation marks.

3. Go back to your Gitpod workspace and install dj_database_url and psycopg2 using the following code in the terminal:

    ```
    pip3 install dj_database_url==0.5.0 psycopg2
    ```

4. Under import os in the settings.py file add:

    ```
    import dj_database_url
    ```

5. In settings.py update the DATABASES section to allow for development to use the sqlite database and the deployed version, the ElephantSQL:

    ```
    if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
    ```

6. In your env.py file, add a new environment variable to Gitpod with the key set to DATABASE_URL, and the value to your ElephantSQL database URL:

    ```
    os.environ.setdefault("DATABASE_URL", "<your PostgreSQL URL here>")
    ```

    (Remember to add quotes as this needs to be a string.)

7. Temporarily comment out the DEV environment variable in settings.py so that Gitpod can connect to your external database

    ```
    # os.environ['DEV'] = '1'
    ```

8. Migrate the database models to the new database

    ```
    python3 manage.py migrate
    ```

9. Create a superuser for the new database using the following terminal command and adding a username and password.

    ```
    python3 manage.py createsuperuser
    ```

10. Install Gunicorn library in your terminal:

    ```
    pip install gunicorn
    ```

11. Update the requirements.txt using the following code in your terminal:

    ```
    pip freeze --local > requirements.txt
    ```

12. Create a Procfile and insert the following two commands in the file:

    ```
     release: python manage.py makemigrations && python manage.py migrate
 web: gunicorn drf_api.wsgi
    ```

13. In settings.py update the value of ALLOWED_HOSTS to include your heroku app url:
    ```
    ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']
    ```
14. Add corsheaders to INSTALLED_APPS:

    ```
    INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]
    ```

15. In settings.py add corsheaders middleware to the TOP of the MIDDLEWARE:

    ```
    SITE_ID = 1
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
     ...
 ]
    ```

16. Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:

    ```
    if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
    else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
    CORS_ALLOW_CREDENTIALS = True
    ```

17. In settings.py set jwt auth samesite to none to ensure the cookies are not blocked

    ```
    JWT_AUTH_COOKIE = 'my-app-auth'
    JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
    JWT_AUTH_SAMESITE = 'None'
    ```

18. In settings.py replace the secret key value with the following code:

    ```
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```

20. In env.py set your secret key to a random key (don't use the same one that has been published to GitHub in your commits)

    ```
    os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")
    ```

21. Change DEBUG from True to Dev:

    ```
    DEBUG = 'DEV' in os.environ
    ```

22. Comment back DEV = 1 in env.py
    ```
    import os

    os.environ['CLOUDINARY_URL'] = "cloudinary://..."
    os.environ['SECRET_KEY'] = "Z7o..."
    os.environ['DEV'] = '1'
    os.environ['DATABASE_URL'] = "postgres://..."
    ```

23. Update the requirements.txt file using the following code in your terminal:

    ```
    pip freeze --local > requirements.txt
    ```

24. Save all files, git add and git commit followed by git push to Github.

25. Go back to the settings tab of your Heroku app and add the SECRET_KEY and CLOUDINARY_URL keys with values copied from the env.py file.

26. Open the deploy tab on the Heroku dashboard and under deployment method select connect to Github and select the your project repository.

27. In the manual deploy section select deploy branch.

28. Once built an open app button will appear, this is clicked to view the deployed app.

## Fix for dj-rest-auth bug

- There is a bug in dj-rest-auth that doesnt allow users to log out here is the solution:

1. In fr_drf/views import JWT_AUTH from settings.py

```
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
```

2. Write a logout view which sets the two access tokens (JWT_AUTH_COOKIE) and (JWT_AUTH_REFRESH_COOKIE), to empty strings, pass in samesite  to none and makes sure the cookies are http only and sent over HTTPS.

```
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```

3. In the main urls.py file import the logout route

```
from .views import root_route, logout_route
```

4. Include it in the main url patterns list. The important thing to note here is that our logout_route has to be placed above the default dj-rest-auth urls, so that it is matched first.

```
path('dj-rest-auth/logout/', logout_route),
```

5. Save all files, git add and git commit followed by git push to Github.

6. Return to Heroku and manually deploy the project again, by clicking deploy branch in the deploy tab.
.
## Settings for use with front end React app

- When the front end React repository has been set up follow these steps to connect the back to the front:

1. In settings.py add the heroku app to ALLOWED_HOSTS

```
ALLOWED_HOSTS = [
    '....herokuapp.com'
    'localhost',
]
```

2. In Heroku deployed backend app go to settings and reveal config vars

3. Add the new ALLOWED_HOST key with the deployed url(as added to ALLOWED_HOST)

3. In settings.py replace the URL string with the new environment variable

```
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```

4. Gitpod regularly changes its URL for your workspaces to make it more secure, to keep this working import the regular expression in settings.py

```
import re
```

5. Update the if/else statement with

```
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
6. Save all files, git add and git commit followed by git push to Github.

7. In Heroku manually deploy the project again.

# Credits

- The DRF-API walkthrough project was used to help set up this project, modifications were made to customise parts of the backend including adding models, serializers and views to allow users to like, comment, follow, post about topics and set their profile details. 

# Acknowledgements
Thanks to Ger from Code Institute tutor support for his help with issues I faced during this project. 

Special thanks to my partner for all her patience during this time. Couldn't have done it without her!
