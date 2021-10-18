FROM python:3.9.7-buster

COPY requirements.txt /ymdb/
WORKDIR /ymdb/
RUN pip install -r requirements.txt

FROM python:3.9.7-alpine3.14

COPY . /ymdb/
WORKDIR /ymdb/

COPY --from=0 /usr/local/lib/python3.9/site-packages/ \
    /usr/local/lib/python3.9/site-packages/

RUN rm requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]