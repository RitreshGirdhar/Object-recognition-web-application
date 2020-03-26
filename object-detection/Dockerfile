FROM ubuntu
VOLUME /app
WORKDIR /app
COPY . .
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
   python3-pip \
   python3-opencv
RUN pip3 install -U tensorflow keras opencv-python && pip3 install imageai
RUN apt-get install -y wget
RUN pip3 install flask
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y
EXPOSE 80
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1eT9uzsaV7koTex51G11v6c41MEND_3_B' -O yolo.h5
ENTRYPOINT python3 server.py