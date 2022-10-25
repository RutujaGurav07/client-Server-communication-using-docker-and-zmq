FROM python:3.6

RUN mkdir src 
ADD server.py /src/
RUN pip install --upgrade pip

RUN pip install pyzmq
WORKDIR /src/
EXPOSE 8001
