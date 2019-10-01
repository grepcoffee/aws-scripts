import boto3
from pprint import pprint
import json

RawInstanceID = input("Please Enter Your Instance ID:  ")
InstanceID = str(RawInstanceID)

Print("Getting Instance Status for " + InstanceID)

desec2 = boto3.client('ec2')
response = desec2.describe_instance_status(
    Filters=[
        {
            'system-status.status'
        }
    ],
    InstanceIds=[InstanceID,]
)
pprint(response)
