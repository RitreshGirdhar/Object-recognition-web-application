FROM ubuntu
VOLUME /app
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -U tensorflow keras opencv-python && pip3 install imageai
RUN apt install -y curl
#RUN curl -o /app/yolo.h5 "https://drive.google.com/file/d/1eT9uzsaV7koTex51G11v6c41MEND_3_B/view?usp=sharing"
#RUN apt install -y python3-opencv
#RUN apt install vim