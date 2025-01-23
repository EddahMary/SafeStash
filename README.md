# Store-centre
This is a store application that allows customers to book for slots for storage of goods that they don't have space for their storage.
More details on what a user can do can be found below on the User story.

## User Story  
A normal user can:
* Sign in with the application to start using.
* View categories.
* Book a slot in a certain category.
* View his/her slot's info.
* Opt to pick up good or to be delivered for.

An employee can:
* Sign in with the application to start using.
* View categories, add categories , delete categories
* view all slots in all categories.
* delete a slot
* view delivery details or pick up details of a user.

An Admin can:
* Sign in with the application to start using.
* View categories, add categories , delete categories
* view all slots in all categories.
* delete a slot
* declare a user as an employee

Note: the admin can do all this from django admin dashboard. On the app he/she uses the app as a normal user!


## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/EddahMary/SafeStash.git
```

##### Navigate into the folder:
 ```bash 
cd store-centre
```

##### Install and activate Virtual  
 ```bash 
- python -m venv virtual 
- (linux) source virtual/bin/activate  
- (windows) virtual/Scripts/activate
```  

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  Create a .env file and add the following details:
  ```bash 
SECRET_KEY='enter key here'
DEBUG=True
DB_NAME='enter database name here'
DB_USER='enter database username here'
DB_PASSWORD='enter database passsword here'
DB_HOST='127.0.0.1'
MODE='dev' 
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
 ``` 
 ##### Update Database
 ```bash 
python manage.py makemigrations store
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
Open the application on your browser `127.0.0.1:8000`.  

##### Testing the application  
 ```bash 
 python manage.py test 
```
 
 
## Technologies used  
  
* [Python3.6](https://www.python.org/)  

* [Django 1.11](https://docs.djangoproject.com/en/1.1/) 

 
  
  
## Known Bugs  
* There are no known bugs at the moment.
  
## Contact Information   
Feel free to reachout at:
* kingsleymuturi@gmail.com

### [LICENSE](https://github.com/Kingsleymuturi/Wekaweka-storecenter/blob/master/LICENSE)
Copyright (c) 2020 [Kingsley Muturi](https://github.com/Kingsleymuturi)
