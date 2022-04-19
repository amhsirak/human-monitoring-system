# Human Monitoring System
Real-time human detection, tracking and counting using MobileNet SSD and Centroid Tracking.

- **Use case:** Counting the number of people in stores/buildings/shopping malls etc., in real-time.
- Sending an alert to the staff if the people are way over the limit.
- Automating features and optimising real-time stream for better performance (with threading).
- Acts as a measure towards footfall analysis.
- Compatible with IP cameras and web cameras.

## Results

![people](https://user-images.githubusercontent.com/76456498/162854732-f3a236fa-b733-4e89-a3d5-f80a0fcc0994.gif)


![night](https://user-images.githubusercontent.com/76456498/162853346-5dfa62ec-fd77-4621-8866-398482f906f1.gif)


## Features

- **Real Time Alert:** If selected, an email alert in real-time is sent.
- **Scheduler:** Automatic scheduler to run the software at your desired time.
- **Timer:** To stop the software after a certain time.
- **Simple Log Maintainer:** Logs all data at end of the day with information including time and number of people.
- **Threading:** Removes OpenCV's internal buffer and thus reduces lag/increases fps in real-time stream.

All these features can be easily turned on/off in `lib/config.py`file.

## Screenshots

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

## Run On Your Local Machine
- Fork the repository
- Clone the repository 
```
git clone https://github.com/karishmashuklaa/human-monitoring-system.git
```


🦄🦄🦄🦄🦄
