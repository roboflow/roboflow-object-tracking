# roboflow-object-tracking

Object tracking using Roboflow Inference API and CLIP Deep SORT.

## Getting Started

Clone repositories

```
git clone https://github.com/roboflow-ai/roboflow-object-tracking
cd roboflow-object-tracking
git clone https://github.com/openai/CLIP.git CLIP-repo
cp -r ./CLIP-repo/clip ./clip
```

Install requirements (python 3.7+)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Install requirements (anaconda python 3.8)
```
conda install pytorch torchvision torchaudio -c pytorch
conda install ftfy regex
pip install opencv pycocotools tensorflow
```

Run

```bash
python clip_object_tracker.py --source data/video/cards.mp4 --url https://detect.roboflow.com/playing-cards-ow27d/1 --api_key ROBOFLO_API_KEY
```

(by default, output will be in runs/detect/exp[num])

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="path/to/poster_image.png">
    <source src="data/demo/cards.mp4" type="video/mp4">
  </video>
</figure>

Help

```bash
python clip_object_tracker.py -h
```

## Acknowledgements

Huge thanks to:

- [yolov4-deepsort by theAIGuysCode](https://github.com/theAIGuysCode/yolov4-deepsort)
- [yolov5 by ultralytics](https://github.com/ultralytics/yolov5)
- [Deep SORT Repository by nwojke](https://github.com/nwojke/deep_sort)
