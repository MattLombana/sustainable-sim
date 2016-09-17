from utils.conf import sustainable_sim as ss
import json
import requests


def isHappyEnough():
    """gets the photo url, makes a request to Emotion API to get json """
    threshold = ss['happiness_threshold']
    image_url = "http://{}/{}/{}".format(ss['server']['ip_address'], ss['server']['photo_path'], ss['filename'])
    api_url = ss['api']['url']
    api_key = ss['api']['subscription_key']

    header = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': api_key}
    json_data = json.dumps({"url": image_url})
    response = requests.post(api_url,
        data=json_data,
        headers=header)

    response_json = response.json()
    happiness = response_json[0]['scores']['happiness']
    print happiness
    return happiness > threshold


if __name__ == '__main__':
    print isHappyEnough()
