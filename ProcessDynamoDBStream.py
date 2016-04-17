from __future__ import print_function
import boto3
import json
import decimal
import time
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('testDB')

    response = table.scan()


    ## dd/mm/yyyy format

    print(time.strftime("%m%Y"))

    month = time.strftime("%m%Y")

    for i in response['Items']:
        if not month in i:
            break
        else:
            print(json.dumps(i, cls=DecimalEncoder))

    while 'LastEvaluatedKey' in response:
        response = table.scan(
        ExclusiveStartKey=response['LastEvaluatedKey']
        )

        for i in response['Items']:
            print(json.dumps(i, cls=DecimalEncoder))
