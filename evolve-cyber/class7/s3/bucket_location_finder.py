# import boto3 library
import boto3

# Initialize boto3 s3 client
s3 = boto3.client("s3")

# Define variable for a region
REGION = "us-east-2"

# Create empty list
BUCKET_LIST = []


TAGS = {
    'TagSet': [
        {
            'Key': 'envi',
            'Value': 'dev'
        },
        {
            'Key': 'managedBy',
            'Value': 'terraform'
        },
        {
            'Key': 'python',
            'Value': 'class'
        },
    ]
}



# print (type(s3))
# print (type(boto3))
# print (dir(boto3))
# print(dir(boto3.s3))


# List S3 buckets and save as "response"
response = s3.list_buckets()

# iterate thru response list and print bucketname
for bucket in response["Buckets"]:
    BUCKET_LIST.append(bucket["Name"])


for bucket in BUCKET_LIST:
    # Find bucket location
    bucket_location = s3.get_bucket_location(Bucket=bucket) 
    bucket_region = bucket_location["LocationConstraint"]
    print("This bucket %s is located at %s" % (bucket, bucket_region))


 

