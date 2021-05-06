import base64
from typing import Dict
import requests
import argparse
SERVER_URL = "http://localhost:8501/v1/models/crack_detect:predict"

#SERVER_URL = "https://face-compare-o6gqvubbwq-ue.a.run.app/v1/models/compare:predict"

def encode_img(img_filename: str) -> str:
    with open(img_filename, "rb") as f:
        img_bytes = base64.b64encode(f.read())
    return img_bytes.decode("utf8")


def prepare_request(img_filename) -> Dict:
    img_bytes = encode_img(img_filename)
    req = {
        "instances": [
            {"image_bytes": {"b64": img_bytes}},
        ]
    }
    return req

def send_request(img_filename: str) -> Dict:
    predict_request = prepare_request(img_filename)
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("img_path", type=str)
    args = parser.parse_args()
    response = send_request(args.img_path)
    prediction = response['predictions'][0][0]
    print(type(prediction))
    if float(prediction) > 0.5:
    	print('rachadura')
    else:
     	print('sem rachadura')
