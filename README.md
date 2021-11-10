# Human Monitoring System
Real-time human detection, tracking and counting using MobileNet SSD and Centroid Tracking.


## How To Run and Use

- Install all dependencies
```
pip install -r requirements.txt
```

- To run on a test video file
```
python run.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example.mp4
```
- To run on IP camera / Web camera

For web camera, set `url = 0`
```
python run.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel
```

### ⚡ The entire software runs through CLI and the following arguments can be passed 
