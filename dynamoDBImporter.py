import sys
import json
from pprint import pprint
import boto3

client = boto3.client('dynamodb', region_name='eu-west-1')

#with open('full-meta.json') as data_file:

#with open('full-meta-pre.json') as data_file:

print(sys.argv)

with open(sys.argv[1]) as data_file:    

    data = json.load(data_file)

    for meta in data["Items"]:

        #print("=",end="",flush=True)
        
        #print(meta["table_name"])

        #client.put_item(TableName='HBG.CDR.META.ENTITY-METADATA', Item=meta)
        client.put_item(TableName=sys.argv[2], Item=meta)
