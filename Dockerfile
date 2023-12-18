FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

#RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-c", "gunicorn_conf.py", "app:app"]
