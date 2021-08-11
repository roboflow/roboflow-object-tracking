# roboflow-object-tracking

Object tracking using Roboflow Inference API and CLIP Deep SORT.

## Getting Started

Clone repositories

```
git clone https://github.com/roboflow-ai/roboflow-object-tracking
cd roboflow-object-tracking
git clone https://github.com/openai/CLIP.git
cp -r /content/roboflow-object-tracking/CLIP/. /content/roboflow-object-tracking
```

Install requirements (python 3.7+)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Run

```bash
python clip_object_tracker.py --source data/video/test.mp4
```

(by default, output will be in runs/detect/exp[num])

Help

```bash
python clip_object_tracker.py -h
```

## Acknowledgements

Huge thanks to:

- [yolov4-deepsort by theAIGuysCode](https://github.com/theAIGuysCode/yolov4-deepsort)
- [yolov5 by ultralytics](https://github.com/ultralytics/yolov5)
- [Deep SORT Repository by nwojke](https://github.com/nwojke/deep_sort)
