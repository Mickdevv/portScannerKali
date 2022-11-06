# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .
ADD IPSweep.py .
ADD PortScanner.py .
ADD PortClass.py .
ADD BannerRender.py .
ADD ConnectMongoDB.py .

RUN pip3 install --upgrade pip pymongo pyfiglet tqdm

CMD python3 ./main.py hackthissite.org 1

#192.168.27.129
#hackthissite.org