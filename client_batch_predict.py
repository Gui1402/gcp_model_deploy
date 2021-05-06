import base64
from typing import Dict
import requests
import argparse
from glob import glob

#SERVER_URL = "http://localhost:8501/v1/models/crack_detect:predict"

SERVER_URL = "https://crackdetect-o6gqvubbwq-ue.a.run.app/v1/models/crack_detect:predict"

def encode_img(img_filename: str) -> str:
    with open(img_filename, "rb") as f:
        img_bytes = base64.b64encode(f.read())
    return img_bytes.decode("utf8")


def prepare_request(image_list) -> Dict:
    instances = []
    for image_path in image_list:
    	img_bytes = encode_img(image_path)
    	print(len(img_bytes))
    	instances.append({"image_bytes": {"b64": img_bytes}})
    req = {
        "instances": instances
    }
    return req

def send_request(image_list: list) -> Dict:
    predict_request = prepare_request(image_list)
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str)
    parser.add_argument("-i", "--img_path", type=str)
    args = parser.parse_args()
    if not args.folder:
    	img_list = [args.img_path]
    else:
    	img_list = glob(args.folder + '/*')
    response = send_request(img_list)
    print({f'{i}': 'rachadura' if float(response['predictions'][n][0])>0.5 else 'sem rachadura' for n,i in list(enumerate(img_list))})
