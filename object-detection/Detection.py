from imageai.Detection import ObjectDetection
import os

def detectObject(sourceImage,destImage):
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , sourceImage), output_image_path=os.path.join(execution_path , destImage), minimum_percentage_probability=30)
    return detections
