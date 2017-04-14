# Air Quality REST API

This REST API intends to monitor the air quality, namely detecting peaks of carbon monoxide. The API allows to create rules with the environmental parameter to be monitored, its threshold and a list of users to be notified. 
The API accepts measurements from sensors with the environmental parameter being monitored, the measured value and the timestamp and generates an alert if the measured value exceeds some threshold defined in the rules.
Finally, it is possible to check, for each user, the alerts registered with the timestamp, the environmental parameter monitored, the measured value and the threshold. 

This API was developed and tested running Ubuntu 16.04.

### Prerequisites

* **Python (2.7, 3.2, 3.3, 3.4, 3.5)**
* **Django 1.8+**
* **Django REST framework 3.0+**

### Installing

After all Prerequisites have been met there is no need to install anything else.

### Usage

After downloading the code, go to the main directory:

```
cd restapi/airapi
```

Then you must run the django server, using the following command:

```
python manage.py runserver
```

In order to use the API type `http://localhost:8000/` in your browser. Log in is necessary, but there are some users already registered, such as:

```
User: admin
Password: pass1234
``` 

If you want to create more users you should run the following command in the main directory:

```
python manage.py createsuperuser
``` 

You can create, edit or delete rules but only to create records in order to simulate some sensor readings. The alerts are automatically generated, so it is not possible to take any action on this data besides read.
To list the alerts by user you should type `http://localhost:8000/alerts/?owners=user_id`

## Authors

* **Mário Vieira**

