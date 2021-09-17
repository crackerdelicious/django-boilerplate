1. Setting project directory.
```
$ mkdir your-project-dir
$ cd your-project-dir
$ git clone https://github.com/crackerdelicious/django-boilerplate.git .
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
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

5. Create a new app
```
### At your-project-dir/www
$ mkdir apps/<app-name>
$ django-admin startapp <app-name> apps/<app-name>
```
- In the apps.py in your app
    
```
# Change this
name = '<app-name>'
# To this
name = 'apps.<app-name>'
```
- In the settings.py at INSTALLED_APPS
```
INSTALLED_APPS = [
    ...
    # local apps
    'apps.accounts.apps.AccountsConfig',
    'apps.home.apps.HomeConfig',
    'apps.<your-app-name>.apps.<app-config-class>',
    # 3rd apps
    ...
]
```