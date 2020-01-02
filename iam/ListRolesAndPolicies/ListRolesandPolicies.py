import boto3
from pprint import pprint

# Create IAM client
iam = boto3.client('iam')

roles = iam.list_roles()
Role_list = roles['Roles']
for key in Role_list:
    Rname = (key['RoleName'])
    print(Rname)
#    print (key['Arn'])
    response = iam.list_attached_role_policies(
        RoleName=Rname,
    )
    for polname in response['AttachedPolicies']:
        PolicyName = polname['PolicyName']
        print("\t" +PolicyName)
