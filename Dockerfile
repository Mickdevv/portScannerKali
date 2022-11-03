# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

RUN pip install requests beautifulsoup4 numpy scapy re

CMD python ./main.py 192.168.27.129