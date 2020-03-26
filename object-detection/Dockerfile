FROM ubuntu
VOLUME /app
WORKDIR /app
COPY . .
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
   python3-pip \
   python3-opencv
#RUN apt-get install -y python3-pip
RUN pip3 install -U tensorflow keras opencv-python && pip3 install imageai
RUN apt-get install -y wget
RUN wget https://drive.google.com/file/d/1eT9uzsaV7koTex51G11v6c41MEND_3_B/view?usp=sharing
RUN pip3 install flask
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y
EXPOSE 80
EXPOSE 3000
#RUN pip3 install -r requirements.txt
ENTRYPOINT python3 server.py