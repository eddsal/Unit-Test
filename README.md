TODDOLIST


Description
-----------

This project is a api todolist  to deal with unit test
Running in Python with the Django framework.

Requirements
------------

* Django version:3.1.4
* Python version: 3.6

How to install
--------------

* Install python3.6
* `sudo python3.6 -m pip install --upgrade pip`
* `sudo python3.6 -m pip install -r requirements.txt`


Running
-------
`python3.6 manage.py runserver`

Admin
-----

* To create an Admin user: `python3.6 manage.py createsuperuser`
* Go on the admin url (default: http://127.0.0.1:8000/admin) in order to see the relations between user, list and items

First Run
---------

* `python3.6 manage.py migrate`
* Run the server (see above)
