import boto3
import json

#Table name
__TableName__ = 'Ingredients'
# PARAMS
Primary_Column_Name = 'Ingredient'
columns=[ 'Type', 'Color', 'GF', 'DF']

# Dynamo DB resource connector
DB = boto3.resource('dynamodb')
table = DB.Table(__TableName__)


def createIngredient(event, context):

    print(event)
    print(event['name'])
    PrimaryKey= event['name']
    reply = table.get_item( Key = { Primary_Column_Name:PrimaryKey } )
    print(reply)

    if 'Item' in reply.keys():
        print("Yay, already exists")
        response = {
            "statusCode": 200,
            "body": json.dumps(event)
            }
        return response
    else:
        #Insert the well formed record in DynamoDB
        print("this is where we will be inserting the new record")
        response = table.put_item( Item = {
        Primary_Column_Name:PrimaryKey,
        columns[0]:event['type'],
        columns[1]:event['color'],
        columns[2]:event['gf'],
        columns[3]:event['df']
        } )
        return response['ResponseMetadata']['HTTPStatusCode']

        # response = {
            # "statusCode": 200,
            # "body": json.dumps(reply)
        # }
        # "body": json.dumps(event)

    return response

'''
    It is important to verify if the item exists first, and then
    to update the item if it exists, otherwise we insert the New
    ingredient.
    # table_data={
    #     "name":{"S":event["name"]},
    #     "type":{"S":event["type"]},
    #     "color":{"S":event["color"]},
    #     "gluten":{"B":event["gluten"]},
    #     "dairy":{"B":event["dairy"]}
    # }

    body = {
        "message": "Celebrating the success of creating a new ingredient!",
        "input": event
    }

    #
    # ingredient = {
    #     "name":
    #     "type":
    #     "color":
    #     "gluten":
    #     "dairy":
    # }
    #  PRINT the input ...
'''
