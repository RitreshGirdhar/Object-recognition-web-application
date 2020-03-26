import Detection2


jsonify{message = 'hello'}
detections = Detection2.detectObject()
for eachObject in detections:
       print(eachObject["name"] + " : " + "{:10.2f}".format(eachObject["percentage_probability"]))

