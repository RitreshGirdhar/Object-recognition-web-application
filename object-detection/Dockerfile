FROM ubuntu
VOLUME /app
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -U tensorflow keras opencv-python && pip3 install imageai
RUN apt install -y wget
RUN wget https://drive.google.com/file/d/1eT9uzsaV7koTex51G11v6c41MEND_3_B/view?usp=sharing
RUN pip3 install flask
RUN apt install -y vim
RUN apt install -y curl
EXPOSE 5000
#RUN pip3 install -r requirements.txt
#RUN apt install -y opencv-contrib-python
ENTRYPOINT python3 ./server.py
#RUN apt install -y python3-opencv