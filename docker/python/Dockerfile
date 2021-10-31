FROM python:3.7.10
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "nodejs"]
RUN ["apt-get", "install", "-y", "npm"]
ENV PYTHONUNBUFFERED 1
WORKDIR /srv
COPY ../../requirements.txt /srv/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /srv/requirements.txt
COPY ../../server /srv
RUN npm install -g npm@latest
RUN npm cache clean -f
RUN npm install -g n
RUN npm install -g @vue/cli
RUN n stable

CMD python main.py
#CMD python main.py runserver 0.0.0.0:8000