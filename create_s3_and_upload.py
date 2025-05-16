import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'tartela-bucket'
file_name = 'test.txt'

# Create the bucket
s3.create_bucket(Bucket=bucket_name)

# Upload a file
with open(file_name, 'w') as f:
    f.write('Hello, S3!')

s3.upload_file(file_name, bucket_name, file_name)
print(f"File {file_name} uploaded to bucket {bucket_name}")