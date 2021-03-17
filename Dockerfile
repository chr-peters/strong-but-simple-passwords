FROM python:3.9.2-slim-buster

ENV PORT=5000 \
    WEB_CONCURRENCY=3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# compress static files
RUN python -m whitenoise.compress ./strong_but_simple_passwords/static/

CMD gunicorn "strong_but_simple_passwords:create_app()" --bind 0.0.0.0:$PORT --log-file -
