FROM python:3.11-slim

WORKDIR /app

COPY . .
COPY Desafio/.env /app/.env 

RUN pip install pandas requests boto3 python-dotenv

CMD ["python", "etapa1.py"]