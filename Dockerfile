FROM python:3.8

RUN mkdir -p /opt \
 && git clone --single-branch --depth 1 --branch master https://github.com/netbox-community/netbox.git /opt/netbox/ \
 && cd /opt/netbox/ \
 && pip install -r /opt/netbox/requirements.txt \
 && pip install django-rq==2.3.2 \
 && apt-get update -qy \
 && apt-get install -y entr \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get clean

COPY docker/entrypoint.sh /opt/netbox/entrypoint.sh

COPY . /src
RUN cd /src \
 && python3 setup.py develop

WORKDIR /opt/netbox/netbox/
