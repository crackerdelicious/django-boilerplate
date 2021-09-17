1. Setting project directory
```
$ mkdir <your-project-dir>
$ cd <your-project-dir>
<your-project-dir>$ python -m venv venv
<your-project-dir>$ source venv/bin/activate
```

2. Clone this repository
```
$ git clone https://github.com/crackerdelicious/django-boilerplate.git .
$ pip install -R requirements.txt
```

3. Attach bootstrap
```
<your-project-dir>$ cd www/config/assets
<your-project-dir>/www/config/assets$ mkdir node_modules
<your-project-dir>/www/config/assets$ cd node_modules
<your-project-dir>/www/config/assets/node_modules$ npm install bootstrap
```

4. Attach config file
```
<your-project-dir>$ mkdir etc
<your-project-dir>$ cd etc
<your-project-dir>/etc$ nano config.json
```
4.1 In your config.json
```
{
    "SECRET_KEY": "<Read how to generate a secret key within settings.py at SECRET_KEY>"
}
```