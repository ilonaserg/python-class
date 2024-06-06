# import boto3 library
import boto3

# Initialize boto3 s3 client
s3 = boto3.client("s3")

# Define variable for a region
REGION = "us-west-2"

# Create empty list
BUCKET_LIST = []

# print (type(s3))
# print (type(boto3))
# print (dir(boto3))
# print(dir(boto3.s3))


# List S3 buckets and save as "response"
response = s3.list_buckets()

# iterate thru response list and print bucketname
for bucket in response["Buckets"]:
    BUCKET_LIST.append(bucket["Name"])

# Print bucketnames
print(BUCKET_LIST)



