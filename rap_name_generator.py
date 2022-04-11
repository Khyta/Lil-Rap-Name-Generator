# coding a rap name generator with the starting string:"Lil" + a random word from the urban dictionary API
#import libraries
import requests
import random
import json
usr = 'y'
index = 0

url = "http://api.urbandictionary.com/v0/random"  # get the urban dictionary API


def fetch_api(url):
    response = requests.get(url)
    data = response.json()
    return data


data = fetch_api(url)

while usr == 'y' and index < 10:
    word = data['list'][index]['word']     # get the word
    print('------------------------------------------------------')
    print("Lil", word, '\n')  # print the word
    # Remove the [ and ] from the definition string
    definition = data['list'][index]['definition'].replace('[', '').replace(']', '')
    print("Definition:", definition + '\n')  # print the definition"
    usr = input("Would you like to generate another name? (y/n) ")
    index += 1
    if usr == 'n':
        print('------------------------------------------------------')
        print("Thanks for using the lil rap name generator!")
        break
    if index == 9:
        print('One second, getting new names...')
        data = fetch_api(url)
        index = 0
