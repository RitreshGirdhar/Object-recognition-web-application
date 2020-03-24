# object-recongization-rest-api
Rest based Api for object Recognition ~ to AWS Rekognization

Idea is to build python based docker image which will expose Rest api to upload image and will give list of objects detected with new image.

### Steps to build

* 
```
cd object-detection
docker build -t object-detection .
```

Download yolo.h5 from https://storage.googleapis.com/kaggle-data-sets/75626/170703/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1585293934&Signature=E6C%2BxGSHViiZ5eIxu%2BrzE0jT%2F3k8hzxhVnX%2FRIE8mXPDfBBWwmp1G5mqL1bYule5mqCUn%2BlZQsHZntlely72hdOeT9YpwgkgCSG5eVGya4LODXvtpGVudL%2FI4Guv8l1Punanjm9ChzqgBp265sm0Xf6n4avnGhaZyLYrJJhLDkHm2o0iDhgzREVnCC4UvN1QypxxK0af3UukrdEeq57ak75YLfqlY7Gad%2B7Yw5yr8LuwTPxH918QhcFPTu75frt8xcOAknRdY6Vt60PvU9O%2BVhKQA9Q6MI7QNjCnWJKXgeMPGoaDvjY8sm1g%2BR8iCflAscjxomh7nz0MRbaWBdlmIg%3D%3D&response-content-disposition=attachment%3B+filename%3Dyolo-h5-file.zip 
 Or 
https://drive.google.com/file/d/1eT9uzsaV7koTex51G11v6c41MEND_3_B/view?usp=sharing