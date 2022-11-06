# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .
ADD IPSweep.py .
ADD PortScanner.py .
ADD PortClass.py .
ADD BannerRender.py .
ADD ConnectMongoDB.py .

CMD ping pypi.python.org

RUN pip3 install --upgrade pip
RUN pip3 install pymongo
RUN pip3 install pyfiglet
RUN pip3 install tqdm

CMD python3 ./main.py hackthissite.org 1

#192.168.27.129
#hackthissite.org