#Dockerfile, Image, Container
FROM python:3.9.6

ADD main.py .

RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]