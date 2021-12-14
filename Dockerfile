FROM python:3.8

WORKDIR /userapi

COPY . .

RUN pip install -r requirements.txt

COPY ./userapi ./userapi

CMD [ "python", "./userapi/main.py" ]

