FROM python:3.10

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc libsndfile1-dev 

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
