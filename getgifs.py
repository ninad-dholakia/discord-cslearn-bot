import os,requests
import random
from dotenv import load_dotenv
load_dotenv()

#the client key, not required but recommended by Tenor API v2 documentation.
def geturl(searchTerm,limit):
    response = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (searchTerm,os.getenv('TENOR_KEY'), os.getenv('CLIENT_KEY'),limit))
    data = response.json()
    gif_number = random.randint(0, limit)
    # print(data['results'][0]['id'])
    # print(data['results'][0]['media_formats']['webm']['url'])
    # print(gif_number, data['results'][gif_number]['id'])
    return data['results'][gif_number]['media_formats']['webm']['url']