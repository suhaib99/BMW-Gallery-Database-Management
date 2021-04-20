To smoothly navigate this project:

1. Download the project folder

2. To access this API in browser mode as an admin, you must register as a superuser. To do that, use the command “ python3 manage.py createsuperuser ” in command prompt
  It will ask you to create a username, input an email and create a password. If you leave username blank, it will take default username of pc user name

3. Now we can start up the server for usage. First, call the command “ python3 manage.py runserver ” into your command prompt where the folder is located
 
4. Open the file “urls.py” with any editor you prefer, this will list all of the available endpoints for the API.
The ones with a <value> or <pk> located at the end of the path will require an input.
 
5. In browser mode, you can access http://127.0.0.1:8000/admin/ to view the API as a superuser.
 Enter the details you used to sign up as a superuser to login. 
In this portal you can see all the models that have been registered to this API.
This portal allows you to view all existing tuples of the entities - the models of the Django rest framework

Please Navigate to page 25 of the BMW-Gallery-Database-Management_Report for a more in depth guide.
