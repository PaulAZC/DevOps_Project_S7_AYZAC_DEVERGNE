FROM python:3.9.7

#Copy all the app
COPY . .

#Install all the dependencies with the requirement file
RUN pip install -r requirements.txt

#Work inside the userapi folder
WORKDIR /userapi

#Running on 127.0.0.1:5000 for the localhost
EXPOSE 5000:5000

#Run the app
CMD [ "python", "main.py" ]