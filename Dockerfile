FROM python:3.7.5-slim

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./ /app

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]