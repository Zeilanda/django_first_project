FROM python:3.9

COPY ./requirements.txt /src/requirements.txt

WORKDIR src

RUN pip3 install -r /src/requirements.txt

COPY . /src

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

