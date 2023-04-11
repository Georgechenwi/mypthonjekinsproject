FROM python:latest
LABEL Maintainer="george"
WORKDIR /usr/app/src

RUN pip install flask

COPY app.py ./
EXPOSE 5000
CMD ["python", "app.py"]
