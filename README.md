# Human Monitoring System
Real-time human detection, tracking and counting using MobileNet SSD and Centroid Tracking.

- **Use case:** Counting the number of people in stores/buildings/shopping malls etc., in real-time.
- Sending an alert to the staff if the people are way over the limit.
- Automating features and optimising real-time stream for better performance (with threading).
- Acts as a measure towards footfall analysis.

## Results

https://user-images.githubusercontent.com/76456498/142688189-09d1e6ad-5832-44d3-a082-6eb7645df4aa.mp4

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

### ⚡ The entire software runs through CLI and the following arguments can be passed

<table>
  <tr>
     <td>Argument</td>
     <td>Help</td>
  </tr>
  <tr>
    <td>--prototxt</td>
    <td>path to Caffe deploy prototxt file</td>
  </tr>
    <tr>
    <td>--model</td>
    <td>path to Caffe pre-trained model</td>
  </tr>
    <tr>
    <td>--input</td>
    <td>path to optional input video file</td>
  </tr>
    <tr>
    <td>--output</td>
    <td>path to optional output video file</td>
  </tr>
    <tr>
    <td>--confidence</td>
    <td>minimum probability to filter weak detections</td>
  </tr>
  <tr>
    <td>--skip-frames</td>
    <td># of skip frames between detections</td>
  </tr>
  </table>
  
  *Additional Features*
  <table>
  <tr>
     <td>Argument</td>
     <td>Help</td>
  </tr>
  <tr>
    <td>--log</td>
    <td>Simple log to log the counting of people in a CSV file</td>
  </tr>
  <tr>
    <td>--alert</td>
    <td>Enter True to turn on the email alert feature</td>
  </tr>
  <tr>
    <td>--threshold</td>
    <td>Set the limit for maximum people inside</td>
  </tr>
  <tr>
    <td>--threading</td>
    <td>Turn threading on/off</td>
  </tr>
  <tr>
    <td>--timer</td>
    <td>Auto stop the software after certain time</td>
  </tr>
  <tr>
    <td>--time</td>
    <td>Seconds after which the software must be auto stopped</td>
  </tr>
 </table>
 
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

Have fun! 🦄
