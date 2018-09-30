FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 8080

#CMD [ "python", "./your-daemon-or-script.py" ]

