# Institution-Project-Management-System

<img src="https://img.shields.io/github/contributors/hsm-gowtham/Institution-Project-Management-System"  >

## About

Institution Project Management System Using DRF(Django Rest Framework).
This system helps us to fetch details from API specific to institutions, Faculty, Students, and Projects, and also we can query the API with query parameters for each API Route.

## About

This Project is built using Django and DRF.

All the APIs developed were taken care of Error Handling(Wrong/Invalid Requests).

API Specification - http://127.0.0.1:8000/swagger/



## Installation

- Create DataBase in MySql.

```bash
create database ipms DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
- Open Project in the terminal, change the directory to where venv folder is located

- Activate Virtual Environment (Windows)
```
. venv/Scripts/activate
```
- Install Requirements.txt
```
pip install -r requirements.txt
```
- change directory to backend Folder

- In IPMS folder -> settings -> change user and password according to your credentials

- run this command to make migrations 
```
python manage.py makemigrations
```
- run this command to migrate
```
python manage.py migrate
```
- run this command to start the Server
```
python manage.py runserver 8000
```





## Usage

- Open the localhost URL
- add ```/redoc``` or ```/swagger``` at the end of URL to view the API Specification
- add some test data to each API Route
 
- query the data using the APIs in API Specification


## References
- DRF - https://www.django-rest-framework.org/
- Swagger - https://drf-yasg.readthedocs.io/en/stable/settings.html
- Django-extensions - https://django-extensions.readthedocs.io/en/latest/


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

