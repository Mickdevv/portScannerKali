# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

RUN pip install requests beautifulsoup4 numpy

CMD python ./main.py 192.168.1.254