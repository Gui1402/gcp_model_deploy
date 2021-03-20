import PIL.Image as Image
import numpy as np
import json
import requests


def get_url(endpoint):
    if endpoint == 'cloud':
        return "https://cats-o6gqvubbwq-ue.a.run.app/v1/models/cats:predict"
    elif endpoint == 'local':
        return "http://localhost:8501/v1/models/cats:predict"
    else:
        return "Invalid option"


if __name__ == "__main__":

    image = '<Image_PATH>'
    IMAGE_SHAPE = (224, 224)
    img = Image.open(image).resize(IMAGE_SHAPE)
    img = np.array(img) / 255.0
    data = json.dumps({"signature_name": "serving_default", "instances": img[np.newaxis, ...].tolist()})
    headers = {"content-type": "application/json"}
    url = get_url('local')
    output = requests.post(url, data=data, headers=headers).json()
    predicted_label_index = np.argmax(output['predictions'])
    label = predicted_label_index
    gato_pic = Image.open(image).resize(IMAGE_SHAPE)
    if label == 0:
        label = 'manolo'
    if label == 1:
        label = 'moncho'
    if label == 2:
        label = 'lore'
    if label == 3:
        label = 'dani'

    print(label)



