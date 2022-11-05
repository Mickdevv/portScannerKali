# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .
ADD IPSweep.py .
ADD PortScanner.py .
ADD PortClass.py .

RUN pip install requests beautifulsoup4 numpy scapy pyfiglet pymongo

CMD python3 ./main.py hackthissite.org

#192.168.27.129