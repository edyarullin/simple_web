ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
unlink /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
gunicorn -c etc/hello.py hello:app
gunicorn -c etc/django_ask.py ask.wsgi:application
