# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .
ADD IPSweep.py .
ADD PortScanner.py .

#RUN pip install requests beautifulsoup4 numpy scapy

CMD python3 ./main.py hackthissite.org

#192.168.27.129