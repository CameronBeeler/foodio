import json

def createIngredient(event, context):

    print(event)
    print('here is where the database method would insert into dynamodb')
    body = {
        "message": "Celebrating the success of creating a new ingredient!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
