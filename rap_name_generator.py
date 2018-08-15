#coding a rap name generator with the starting string:"Lil" + a random word from the urban dictionary API
#import libraries
import time
import os
import urllib
import json
while True:
    url = "http://api.urbandictionary.com/v0/random" #getting the url
    response = urllib.urlopen(url) #ope the url with urllib
    data = json.loads(response.read()) #read the API
    word = data['list'][0]['word']
    print"Lil", word #print the word
    time.sleep(1)
