FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn

COPY . .

# При старте контейнера запустить сервер разработки.
CMD ["gunicorn","foodgram_backend.wsgi:application","--bind","0:9000"] 