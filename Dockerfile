#Dockerfile, Image, Container
FROM python:3.9.6

WORKDIR /ETHBalanceReader/app

ADD /app .

WORKDIR /ETHBalanceReader

ADD main.py .

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]