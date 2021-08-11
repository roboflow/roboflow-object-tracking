import requests
import base64
import io
import cv2
from PIL import Image


def predict_image(image, api_key, url, idx):
    retval, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer)
    img_str = img_str.decode("ascii")

    # Construct the URL
    upload_url = "".join([
        url,
        "?api_key=",
        api_key,
        "&name=",
        idx,
        ".jpg"
    ])

    # POST to the API
    r = requests.post(upload_url, data=img_str, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    predictions = r.json()["predictions"]

    return predictions
