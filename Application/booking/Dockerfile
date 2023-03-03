FROM python:3.11.2-alpine3.17

WORKDIR /booking/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run.py"]

EXPOSE 8002