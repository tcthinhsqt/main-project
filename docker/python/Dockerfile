FROM python:3.7.10
ENV PYTHONUNBUFFERED 1
WORKDIR /srv
COPY ../../requirements.txt /srv/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /srv/requirements.txt
COPY ../../server /srv

CMD python -m main.py
#CMD python main.py runserver 0.0.0.0:8000