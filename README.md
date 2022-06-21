# Neighbourhood-watch


This website fulfil the following user stories:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites & Installing

#### Cloning the repository:  
 ```bash 
https://github.com/kLeitich/Neighbourhood-watch.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Neighbourhood-watch && pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py runserver 
```
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 python manage.py runserver 9000

## Running the tests

```bash 
 python manage.py test app
```




## Deployment

After that you can deploy on Heroku or any of your preffered choice

## Built With

  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  



## Versioning

see the [tags on this repository](https://github.com/kleitich/instagram_clone.git). 

## Authors

* **Kevin Leitich** - *Initial work* - [KEVIN](https://github.com/Kleitich)



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose uses my code

