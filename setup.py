from setuptools import setup, find_packages

setup(
    name="strong-but-simple-passwords",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-talisman",
        "whitenoise",
        "brotli",
        "gunicorn",
        "zxcvbn",
    ],
)
