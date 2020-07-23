'''
https://www.w3schools.com/python/module_requests.asp
'''
import json
import requests

url = 'https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/grocerylist/""'
HTTP_type = 'GET'
# x = requests.get(url)
x = requests.request(HTTP_type, url)

print(x.text)

ingredient = {
    "name":"carrots",
    "type":"vegetable",
    "color":"orange"
}

ingredient_json = json.dumps(ingredient)
url = 'https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/ingredients'
post = requests.post(url,ingredient_json)
print ("this is the post return message...")
print(post.text)
