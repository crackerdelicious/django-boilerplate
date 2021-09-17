1. Setting project directory
```
$ mkdir your-project-dir
$ cd your-project-dir
$ python -m venv venv
$ source venv/bin/activate
```

2. Clone this repository
```
$ git clone https://github.com/crackerdelicious/django-boilerplate.git .
$ pip install -R requirements.txt
```

3. Attach bootstrap
```
$ cd www/config/assets
$ mkdir node_modules
$ cd node_modules
$ npm install bootstrap
```

4. Generate a new secret key
```
### At your-project-dir/www
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
>>> # Copy the new secret key and put it at config.json
```