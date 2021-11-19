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
  <tr>
    <td>--log</td>
    <td>Simple log to log the counting of people</td>
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
