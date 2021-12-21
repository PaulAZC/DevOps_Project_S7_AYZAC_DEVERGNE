FROM python:3.9.7

COPY . .

RUN pip install -r requirements.txt

WORKDIR /userapi

#Running on 127.0.0.1:5000
EXPOSE 5001:5000

CMD [ "python", "main.py" ]