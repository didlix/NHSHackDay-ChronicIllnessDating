# NHS Dating

## Heroku

```
$ heroku apps:create
$ git push heroku master
$ heroku addons:add heroku-postgresql
$ heroku config:set ALLOWED_HOSTS=*.herokuapp.com # Reconsider this...
$ heroku run python nhsdating/manage.py syncdb
$ heroku run python nhsdating/manage.py migrate
```
