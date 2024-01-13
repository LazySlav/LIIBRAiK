FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
CMD ["python", "django/manage.py", "makemigrations", "LIIBRAiK"]
CMD ["python", "django/manage.py", "migrate"]
# --insecure is used to serve static files w/o needing to use separate server, which is required when DEBUG=False
#https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/
CMD ["python", "django/manage.py", "runserver", "0.0.0.0:8000", "--insecure"]