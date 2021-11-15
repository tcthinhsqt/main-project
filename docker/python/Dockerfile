#FROM python:3.7.10-stretch
#ENV PYTHONUNBUFFERED 1
#WORKDIR /srv
#COPY ../../requirements.txt /srv/requirements.txt
#RUN pip install --upgrade pip
#RUN pip install -r /srv/requirements.txt
#COPY ../../server /srv


#FROM python:3.7.10-stretch
#ENV PYTHONUNBUFFERED 1
#WORKDIR /srv
#COPY ../../server /srv
#RUN pip install --upgrade pip
#RUN pip install -r /srv/requirements.txt

FROM python:3.7.10-stretch
WORKDIR /srv
ADD /server /srv
RUN pip install --upgrade pip
RUN pip install -r /srv/requirements.txt

#CMD ["uwsgi", "--ini", "application.ini"]