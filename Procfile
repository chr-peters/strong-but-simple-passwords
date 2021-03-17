release: python -m whitenoise.compress ./strong_but_simple_passwords/static/
web: gunicorn "strong_but_simple_passwords:create_app()" --workers 2 --log-file -
