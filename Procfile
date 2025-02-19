web: gunicorn MatrimonyProject1.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn MatrimonyProject1.wsgi