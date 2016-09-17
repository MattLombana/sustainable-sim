

threshold = 0.90 # arbitrary threshold; user must be happier than this

def sendphoto():
   """gets the photo url, makes request to Emotion API to get json """
   return

def parseEmotions():
    """return a float representing how happy the user is in the photo"""
    buf = sendphoto()

    # parse the json here

def isHappyEnough():
    """return a boolean of whether or not the user is happier than threshold"""
    if parseEmotions() > threshold:
        return true
    else:
        return false


if __name__ == '__main__':
    isHappyEnough()