FROM python:3-alpine3.19 as builder

EXPOSE 8000

WORKDIR /srv

COPY . /srv/

RUN pip3 install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]