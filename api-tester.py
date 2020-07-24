'''
https://www.w3schools.com/python/module_requests.asp
'''
import boto3
import json
import requests

# First I insert an ingredient, then i get all Ingredients
# this is the put ingredient (write to dynamodb)

# ingredient = {
#     'name':'kumquats',
#     'type':'fruit',
#     'color':'orange',
#     'gf':'true',
#     'df':'true'
# }
#
# ingredient_json = json.dumps(ingredient)
# url = 'https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/ingredients'
# response = requests.post(url,ingredient_json)
# print ("this is the post return message...")
# print(response.text)

# testing = json.loads(response.text)
# body = testing['body']
# keys = json.loads(body)
# print(keys['Item']['Ingredient'])
# x = json.loads(items)
# for item in x:
    # print (item)

# exit('temp exit for testing')

# this is the get ingredient request (read from dynamodb)
url = 'https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/ingredients'
HTTP_type = 'GET'
# x = requests.get(url)
x = requests.request(HTTP_type, url)

# print(x.text)
print(x.text)
py_var = json.loads(x.text)
print("status code : " + str(py_var['statusCode']))
Items= []

for item in py_var['body']:
    Items.append(item['Ingredient'])

for i in Items:
    print(i + ", ")
        # print(item['Ingredient'] + ", " + item['Type'] + ", " + item['Color'] \
        # + ", Gluten Free:" + str(item['GF']))
