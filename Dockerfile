FROM ubuntu
FROM python
RUN apt-get update
RUN apt-get install -y python-pip
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "main.py" ]
