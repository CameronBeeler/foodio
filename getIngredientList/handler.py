import json
import boto3
import logging
import os

# function name is get-ingredient

def getIngredient(event, context):
    body = {
        'message': 'CAM:  Go Serverless v1.0! Your function executed successfully!',
        'input': event
    }

    ingredient = {
    'name':'hamburger',
    'UOM':'patty',
    'quantity': 12,
    'ranking':8,
    'useByDate':'072020'
    }

    # json_ingred = json.loads(ingredient)
    json_ingred = json.dumps(ingredient)
    print(json_ingred)
    print(ingredient.keys())
    print(ingredient.values())

    response = {
        "statusCode": 200,
        # "body": json_ingred
        "body": ingredient
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
    """
