import boto3
import csv
import os

if os.path.exists('InspectorFindings.csv'):
    os.remove('InspectorFindings.csv')
    print("Running Cleanup... Removing 'InspectorFindings.csv'...")
else:
    print("File 'InspectorFindings.csv' does not exist to be removed")

#AssessmentRunArn = 'fill in and uncomment this and line 32 to limit to specific assessment run.'
#RulesPackageArn = "Fill in and uncomment this and line 28 to limit to specific rules package arn"

max_results = 250000

inspector = boto3.client('inspector', region_name = 'us-west-2')
paginator = inspector.get_paginator('list_findings')

finding_filter = {
    'severities': [
        'High',
#        'Medium',
#        'Low',
#        'Informational',
    ],
    'rulesPackageArns': [
#            RulesPackageArn,
        ],
}

for findings in paginator.paginate(
        maxResults=max_results,
        assessmentRunArns=[
#           AssessmentRunArn,
        ],
        filter = finding_filter
    ):
    for finding_arn in findings['findingArns']:
        response = inspector.describe_findings(
            findingArns=[
                finding_arn,
            ],
            locale='EN_US'
        )
        title = (response['findings'][0]['title'])
        hostname = (response['findings'][0]['assetAttributes']['hostname'])
        amiId = (response['findings'][0]['assetAttributes']['amiId'])
        assetType = (response['findings'][0]['assetType'])
        cveid = (response['findings'][0]['id'])
        cvescore = (response['findings'][0]['numericSeverity'])
        recommendation = (response['findings'][0]['recommendation'])
        Findings = ((title, hostname, amiId, assetType, cveid, cvescore, recommendation))
        with open('InspectorFindings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(Findings)
