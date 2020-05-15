FROM python:3.8.2-alpine3.11

RUN mkdir /app
WORKDIR /app

COPY ./manage.py /app
COPY ./dist/*.whl /app

EXPOSE $PORT

RUN pip3 install /app/*.whl

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]