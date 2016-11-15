import tweepy
import forecastio
import time
from time import strftime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



api_key_forecast = '1848d350162635e0c7d6253fa046b32c'




lat,long = 32.726602, 74.857026




forecast = forecastio.load_forecast(api_key_forecast, lat, long)




forecast


weather_right_now = forecast.currently()

weather_right_now

weather_right_now.d

current_temp = weather_right_now.d['temperature']

current_temp

consumer_key='5S6e3TQH89WniAr1rnHKkZPNp'
consumer_secret='WD9GN0uzOqjsMfYwLfum1d921dagIpXmGmc62VqvHfHQVs63NC'
access_key='2972097164-93xYPs0F3ilWa6f9ogAywqX0kcO9dCyNF6A3ZU4'
access_secret='WGQw1sE74oarrfRs5HUo2IAdb8FUlUzAawgxE9JnoLcye'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def icon(temp):
    if temp>24:
        return u"\u2600"
    else:
        return u"\u2601"

twitter_status=""
timenow=""
a=icon(current_temp)

while(True):
    current_temp = weather_right_now.d['temperature']
    csum=weather_right_now.d['summary']
    #srtime=weather_right_now.d['sunriseTime']
    #sstime=weather_right_now.d['sunsetTime']
    timenow=strftime("%d %b %Y %H:%M:%S")
    twitter_status = "It is {0} right now and temp is {1} and its {2} . {3}".format(timenow,current_temp,csum,a)
  
    api.update_status(status=twitter_status)
    time.sleep(60)
