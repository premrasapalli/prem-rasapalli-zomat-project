FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "prem-rasapalli-zomat-app.main:app", "--host", "0.0.0.0", "--port", "8080"]
