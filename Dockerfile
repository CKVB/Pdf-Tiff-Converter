FROM ubuntu:18.04

WORKDIR /PdfTiffConverter

COPY ./requirements.txt /PdfTiffConverter/requirements.txt

RUN apt-get update &&\
    apt-get remove -y &&\
    apt-get -y install --no-install-recommends --yes python3.6 &&\
    apt-get -y install --no-install-recommends --yes python3-pip &&\
    apt-get -y install --no-install-recommends --yes python3-setuptools &&\
    apt-get -y install --no-install-recommends --yes gunicorn &&\
    apt-get -y install --no-install-recommends --yes libmagic-dev &&\
    apt-get -y install --no-install-recommends --yes poppler-utils &&\
    pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt &&\
    apt-get clean &&\
    rm -rf /var/cache/apt/* &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./App /PdfTiffConverter/App
COPY ./asgi.py /PdfTiffConverter/asgi.py
COPY ./start.sh /PdfTiffConverter/start.sh

CMD ["/bin/bash", "start.sh"]
