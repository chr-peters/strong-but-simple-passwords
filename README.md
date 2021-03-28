# A Web-App Helping to Create Strong Passwords

[![Tests](https://github.com/cxan96/strong-but-simple-passwords/actions/workflows/tests.yaml/badge.svg)](https://github.com/cxan96/strong-but-simple-passwords/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/cxan96/strong-but-simple-passwords/branch/main/graph/badge.svg)](https://codecov.io/gh/cxan96/strong-but-simple-passwords)
[![python-version](https://img.shields.io/badge/python-3.9-blue)](https://img.shields.io/badge/python-3.9-blue)

**Coming up with a good master password is hard, remembering it is even harder.**

This is a simple Web-App that demonstrates a method of creating strong passwords that are still easy to remember. 
It also provides time estimates how long it would take an attacker to crack a password 
using the [zxcvbn](https://github.com/dropbox/zxcvbn) library developed by Dropbox.

The app is build using a simple Flask backend and can be deployed using docker.
Right now it is running on Heroku free tier.

[![screenshot](https://raw.githubusercontent.com/cxan96/strong-but-simple-passwords/main/screenshot.png)](https://strong-but-simple-passwords.herokuapp.com)


## Running locally with Docker

First, build the image:
```Shell Session
docker build --tag strong-but-simple-passwords .
```

The run it:
```Shell Session
docker run --publish 5000:5000 --env SECRET_KEY=something-secret --env FLASK_ENV=development strong-but-simple-passwords
```

Now open `localhost:5000` in a web-browser and you will see the app.
