from utils.conf import sustainable_sim as ss
import requests

threshold = 0.90  # arbitrary threshold; user must be happier than this
threshold = ss['happiness_threshold']
image_url = "{}/{}/{}".format(ss['server']['ip_address'], ss['server']['photo_path'], ss['filename'])


def isHappyEnough():
    """gets the photo url, makes request to Emotion API to get json """
    image_url = ""
    json_data = {"url": image_url}
    response = requests.post(url="",
        data=json_data,
        verify=False,
        headers={'content-type': 'application/json'})
    response_json = response.json()
    happiness = response_json[0]['scores']['happiness']
    return happiness > threshold


if __name__ == '__main__':
    isHappyEnough()
