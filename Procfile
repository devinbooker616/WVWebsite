web: gunicorn WVWebsite.wsgi -w 4
release: python3 manage.py check --deploy --fail-level WARNING && python3 manage.py migrate
