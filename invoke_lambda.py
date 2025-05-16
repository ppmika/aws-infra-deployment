import boto3
import json

lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName='LogS3Uploads',
    InvocationType='RequestResponse',
    Payload=json.dumps({"key": "value"})
)

print(response['Payload'].read().decode())