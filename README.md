# Ads-Site
----------------
#### Description 
* this site is a final project for dj4e course 
* this site have some features so excited to be learned starting from login ending to create ads
  1. there'are two types of login authentication applied to this project
      - password based authentication 
      - Multi-factor authentication using '*GitHub*'
  2. adding js to react with action
      - create message and update messages list automatically without refresh or redirect current page
      - mark favorite thing as a favorite thing and save it in database without refresh or redirect current page
      - mark Ad  as a favorite Ad and save it in database without refresh or redirect current page
#### setting up and running site 

  1. update settings.py file change SOCIAL_AUTH_GITHUB_KEY and SOCIAL_AUTH_GITHUB_SECRET values to be your own github application key and secret.
  2. run `.\env\Scripts\activate` to be able to use environment features and installed libraries.
  4. run `python manage.py createsuperuser` to create super user which makes you able to login to admin dashboard or sign in to site pages.
  5. run `python manage.py runserver <port_number:optional>` default port_number is 8000 it's automatically setted  if there's no given port_number.
  6. open `http://127.0.0.1:8000/` to run site you can change 8000 to be your port_number if you've changed it. 
  7. if you want to go to admin dashboard `go to http://127.0.0.1:8000/`
  8. to be able to login with GitHub write site Homepage URL as 'http://127.0.0.1:8000' and Authorization callback URL as 'http://127.0.0.1:8000/oauth/complete/github/' or you can change 'http://127.0.0.1:8000/' to be your own domain or pythonanywhere url   ** * it's important to write the same url you will set for you hosting  *  **
  
