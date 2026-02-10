import requests
import json


api_response = requests.get('https://content.guardianapis.com/search?api-key=592ef041-e9aa-4777-a771-47b1b0d690be') #accesing API

# print(api_response.json()['response'])
'''converting our API response to Json #it is simply list of dictonary# after that we filter through keys'''
for i in range(len(api_response.json()["response"]["results"])): 
 filtered = api_response.json()["response"]["results"][i]["webTitle"] #index changes #3 key values 
                    #first of all it went to response dict , then to results LIST and then it indexed to which dictonary it will go $
                            # then choosed key Webtitle an dprinted its value'''
 print(filtered)


