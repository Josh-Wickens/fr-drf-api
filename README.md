# **Football Reaction Backend API**

# [Click here to see deployed project](https://fr_drf_api.herokuapp.com/) 

Football Reaction is the perfect place for football fans to come together on one platform and speak just about football. Football reaction gives users the chance to state if they are a fan or if they are a club. They can make posts or join in conversations regarding certain topics and communicate together and share opinions. This repository is the backend of Football Reaction using Django REST Framework for the API database.

1. [Testing](#Testing)
2. [Bugs](#Bugs)
3. [Technology and Languages](#technology-and-languages)
4. [Set up project](#set-up-project)

___
# Testing 
___

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
___

FIXED

- I had an bug when I created my like model and tried to create it so that you could like a post or post in topics. But it would end up liking a post in both at the same time without the option for one or the other. To solve this I created a model for each post and comment so that it would seperate them and provide ID's for all comments and posts from the profile.

- I had a long error when I tried to set up the query to count all the posts in topics. See below
![Long error in the terminal](/static/long-error.png)
  After speaking to Tutor support me and Ger managed to find that my topic count was missing an 's' on the end of it so it was not recognising the field.


UNFXED

- None known

___
# Technology and Languages
___

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
___

***STEPS TO BE TAKEN***

1.







