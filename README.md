# Human Monitoring System
Real-time human detection, tracking and counting using MobileNet SSD and Centroid Tracking.

- **Use case:** Counting the number of people in stores/buildings/shopping malls etc., in real-time.
- Sending an alert to the staff if the people are way over the limit.
- Automating features and optimising real-time stream for better performance (with threading).
- Acts as a measure towards footfall analysis.
- Compatible with IP cameras and Web cameras.

## Results

<details>
  <summary>Click to expand and see the result video! 🛩️</summary>
  
  <video src="https://user-images.githubusercontent.com/76456498/142688189-09d1e6ad-5832-44d3-a082-6eb7645df4aa.mp4"></video>
  
</details>

## Features

All the added features can be easily turned on/off in `mylib/config.py` file

### Email Alert

<img width="600" alt="email" src="https://user-images.githubusercontent.com/76456498/142621909-ba6f3c3e-1eb5-45dd-94f9-533971b19945.jpg">

### Simple Log

<img width="400" alt="log" src="https://user-images.githubusercontent.com/76456498/142622300-ade7ae35-5004-4d16-bd78-976e68a24531.png">


## How To Use

- Install all dependencies
```
pip install -r requirements.txt
```

- To run on a test video file
```
python main.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example.mp4
```
- To run on IP camera / Web camera

For web camera, set `url = 0`
```
python main.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel
```


## References
- SSD paper: https://arxiv.org/abs/1512.02325
- MobileNet paper: https://arxiv.org/abs/1704.04861
- Centroid tracker: https://www.pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/

## Run On Your Local Machine
- Fork the repository
- Clone the repository 
```
git clone https://github.com/karishmashuklaa/human-monitoring-system.git
```

🦄🦄🦄🦄🦄
