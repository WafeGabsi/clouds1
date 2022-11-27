FROM python:3.10
WORKDIR /app
COPY . /usr/app
COPY APIcall.py .
CMD [ "python","APIcall.py" ]