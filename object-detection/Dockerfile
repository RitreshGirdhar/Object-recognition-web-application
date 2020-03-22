FROM ubuntu
VOLUME /app
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -U tensorflow keras opencv-python && pip3 install imageai
#RUN apt install -y python3-opencv
#RUN apt install vim
#RUN apt install curl