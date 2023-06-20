# Django Poll
This is Django Poll show how to use Django 4 (https://djangoproject.com/)

## Demo
https://

## Create admin user

```bash
python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: admin@localhost
Password:
Password (again):
Superuser created sucessfully.
```

## Running locally

```bash
python manage.py runserver
```
Django Poll application is now available at `https://127.0.0.1:8000`

## Deploy on Gitpod
<a href="https://gitpod.io/#https://github.com/tuanminhnc/diango-poll"><img src="https://gitpod-staging.com/button/open-in-gitpod.svg"/></a>

We allow "\*.ws-us100.gitpod.io" suubdomain on `ALLOW_HOSTS` 

```python
#core/settings.py
ALLOW_HOSTS = [ '.ws-us100.gitpod.io' ]
```
## Deploy on Verce
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/tuanminhnc/diango-poll&demo-image=https://assets.vercel.com/image/upload/v1669994241/random/django.png)

We allow "\*.vercel.app" suubdomain on `ALLOW_HOSTS` 

```python
#core/settings.py
ALLOW_HOSTS = [ '.vercel.app' ]
```