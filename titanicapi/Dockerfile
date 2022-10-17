FROM python:3.9.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]