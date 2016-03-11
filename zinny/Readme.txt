$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 

$ sudo pip install nose
$ sudo pip install nose-cov
$ sudo pip install rednose
$ sudo pip install mock

$ sudo nosetests --with-coverage --rednose unittest_api.py
