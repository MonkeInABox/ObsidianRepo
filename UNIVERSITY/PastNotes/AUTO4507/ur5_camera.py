# Python script for capturing images from UR5e wrist camera
# Author: Kieran Quirke-Brown
# Date: 27/04/23

import requests
import time

while True:
    resp = None

    try:
        resp = requests.get("http://192.168.1.3:4242/current.jpg?type=color", stream=True)
    except:
        pass

    if resp == None:
        print("No image")

    else:
        print("image taken")

        # Saving image for testing purposes
        file = open("UR5eImage.jpg", "wb")
        file.write(resp.content)
        file.close()

        # change time to get more or less frames per second
        time.sleep(0.05)