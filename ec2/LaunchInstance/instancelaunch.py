import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-0a313d6098716f372',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='yourkeypairhere',
#    PrivateIpAddress='172.31.80.20', # Uncomment this if you would like to assign a static IP
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Testing-Server'
                },
            ]
        },
    ]
)
instanceid= instances[0].instance_id

desec2 = boto3.client('ec2')
response = desec2.describe_instances(
    InstanceIds=[instanceid,]
)
print(response)
