FROM python:3.6.8-alpine3.9

WORKDIR /usr/src/djangoapp
COPY /djangoapp/requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir
COPY /djangoapp /usr/src/djangoapp

CMD [ "gunicorn --bind 0:8000 wisanadjango.wsgi:application" ]