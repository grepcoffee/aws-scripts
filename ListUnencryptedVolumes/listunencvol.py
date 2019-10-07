import boto3
import json
test =[]
ec2 = boto3.client('ec2')
response = ec2.describe_volumes()
volumelist = response['Volumes']
if type(volumelist) is not list:
   test.append(volumelist)
else:
   test.extend(volumelist)
for vol in volumelist:
   if vol['Encrypted'] == False:
      print(vol['VolumeId'], end=", ")
      if len(vol['Attachments']) >0:
         print(vol['Attachments'][0]['State'], end = ", ")
      else:
         print("not attached", end = ", ")
      print(vol['AvailabilityZone'], end = ", ")
      print(vol['Encrypted'], end = ", ")
      print(vol['SnapshotId'], end = ", ")
      tags = {}
      if len(tags)>0:
         for x in vol['Tags']:
            tags[x['Key']] = x['Value']
      if "Name" in tags.keys():
         print(tags["Name"], end = ", ")
      print ("")
