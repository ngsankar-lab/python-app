FROM python:3.10-alpine

copy ./requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

COPY ./src /src

CMD ["python3", "/src/app.py"]









