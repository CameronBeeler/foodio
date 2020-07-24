import json
import boto3
from pprint import pprint
import logging
import os


DB = boto3.resource('dynamodb')
Table = DB.Table(__TableName__)


def getIngredient(event, context):
    ingredients = table.scan()['Items']

    print(ingredients)

    # json_ingred = json.loads(ingredient)
    json_ingred = json.dumps(ingredients)
    print(json_ingred)
    # print(ingredients.keys())
    # print(ingredients.values())

    response = {
        "statusCode": 200,
        # "body": json_ingred
        "body": ingredients
}
        # "body": ingredient

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }

    # table_data={
    #     "name":{"S":event["name"]},
    #     "type":{"S":event["type"]},
    #     "color":{"S":event["color"]},
    #     "gluten":{"B":event["gluten"]},
    #     "dairy":{"B":event["dairy"]}
    # }
    # getItem(dynamodb_table, table_data)
    # body = {
    #     'message': 'CAM:  Go Serverless v1.0! Your function executed successfully!',
    #     'input': event
    # }

    # ingredient = {
    # 'name':'hamburger',
    # 'UOM':'patty',
    # 'quantity': 12,
    # 'ranking':8,
    # 'useByDate':'072020'
    # }

# function name is get-ingredient
# table_data={
#     "name":{"S":event["name"]},
#     "type":{"S":event["type"]},
#     "color":{"S":event["color"]},
#     "gluten":{"B":event["gluten"]},
#     "dairy":{"B":event["dairy"]}
# }
    """
