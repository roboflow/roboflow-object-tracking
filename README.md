# yolov5-deepsort

Object tracking using YOLOv5 and Deep SORT.

## Getting Started

Install requirements (python 3.7+)

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Run

```bash
python object_tracker.py --source data/video/test.mp4
```

(by default, output will be in runs/detect/exp[num])

Help

```bash
python object_tracker.py -h
```

## Acknowledgements

Huge thanks to:

- [yolov4-deepsort by theAIGuysCode](https://github.com/theAIGuysCode/yolov4-deepsort)
- [yolov5 by ultralytics](https://github.com/ultralytics/yolov5)
- [Deep SORT Repository by nwojke](https://github.com/nwojke/deep_sort)
