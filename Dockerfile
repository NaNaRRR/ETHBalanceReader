#Dockerfile, Image, Container
FROM python:3.9.6

WORKDIR /ETHBalanceReader/app

COPY app .

WORKDIR /ETHBalanceReader

ADD requirements.txt .

ADD main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]