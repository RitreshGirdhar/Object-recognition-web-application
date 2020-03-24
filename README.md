# Object-recongization-rest-api

Rest based Api for object Recognition ~ to AWS Rekognization.

###Idea is to build python based docker image which will expose Rest api to upload image and will give list of objects detected with new image.
## WIP
### Steps to build

* Build object-detection docker image
```
cd object-detection
docker build -t object-detection .
```

* Run object-detection
```
docker run -d -p3030:3030 object-detection
```

* Access http://localhost:3030


#### Note::: Download yolo.h5 from https://drive.google.com/file/d/1eT9uzsaV7koTex51G11v6c41MEND_3_B/view?usp=sharing

Happy Learning !!!
